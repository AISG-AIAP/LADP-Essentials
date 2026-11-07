# Host n8n on Google Cloud Run

Run your own n8n instance on the internet so your workflows, webhooks and chat triggers have a **public HTTPS URL**, instead of only working on `localhost:5678`.

This guide follows the **easy mode** from the official n8n guide ([Deploy n8n to Google Cloud Run](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run)), with one change: the service is kept at **1 always-on instance** so it doesn't scale to zero and lose your data as easily.

> **Easy mode is for learning and demos, not production.** n8n stores everything (your account, workflows and credentials) **inside the container**. Keeping 1 instance running reduces data loss, but it is **not foolproof**: your data is still wiped whenever the service is redeployed, updated, or restarted by Google.
>
> **Need it to last?** Use the **durable mode** in the [official n8n guide](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run#durable-mode), which adds a Cloud SQL Postgres database and Secret Manager so your data survives restarts. That is the production-grade setup.

---

## What You Need

| Requirement | Notes |
|---|---|
| **A Google Cloud project with billing enabled** | Create one in the [Google Cloud Console](https://console.cloud.google.com/). Billing must be on, even though Cloud Run has a free tier |
| **Cloud Shell** (recommended) | A terminal in your browser with `gcloud` already installed and logged in. In the Console, click the **terminal icon** (top right) or press **G** then **S**. All commands in this guide are written for Cloud Shell |

> **This setup costs money while it's running.** Because the instance is always on (`--scaling=1` and `--no-cpu-throttling`), you're billed for every hour it runs, not just when it's used. This can add up to **tens of US dollars a month**. Check the [Cloud Run pricing](https://cloud.google.com/run/pricing) page, set a [budget alert](https://cloud.google.com/billing/docs/how-to/budgets), and **follow [Step 6](#step-6--delete-everything-when-youre-done) to delete the service when you're done**.

---

## Step 1 — Open Cloud Shell and Pick Your Project

In Cloud Shell, check which project you're using, and switch if needed:

```bash
gcloud config get-value project                 # shows the current project
gcloud projects list                            # lists your projects
gcloud config set project YOUR_PROJECT_ID       # switch project (if needed)
```

If you're using your own terminal instead of Cloud Shell, log in first with `gcloud auth login`.

---

## Step 2 — Deploy n8n

```bash
gcloud run deploy n8n \
    --image=n8nio/n8n \
    --region=us-west1 \
    --allow-unauthenticated \
    --port=5678 \
    --no-cpu-throttling \
    --memory=2Gi \
    --scaling=1 \
    --set-env-vars="N8N_ENDPOINT_HEALTH=health"
```

If asked to enable the Cloud Run API, type **Y**. Deployment takes 1–3 minutes.

**What each flag does:**

| Flag | What it does |
|---|---|
| `n8n` | The name of your Cloud Run service. The rest of this guide assumes this name |
| `--image=n8nio/n8n` | Runs the official n8n Docker image (latest version) |
| `--region=us-west1` | Where it runs. You can use another region (e.g., `asia-southeast1` for Singapore), but **use the same region in every command** below |
| `--allow-unauthenticated` | Makes the URL public, so webhooks and chat can reach it. n8n's own login still protects the editor |
| `--port=5678` | n8n listens on port 5678 inside the container |
| `--no-cpu-throttling` | Keeps the CPU always allocated, so background work and **Schedule Trigger** nodes keep running between requests |
| `--memory=2Gi` | Gives n8n 2 GB of memory |
| `--scaling=1` | Keeps **exactly 1 instance** running, so it **doesn't scale to zero** (which would wipe your data) |
| `N8N_ENDPOINT_HEALTH=health` | **Required.** Cloud Run reserves `/healthz` for itself, which can break the n8n canvas. This moves n8n's health check to `/health` |

When it finishes you'll see:

```
Service URL: https://n8n-xxxxxxxxxxxx.us-west1.run.app
```

> **Don't create your n8n account yet.** Do Step 3 first. Step 3 restarts the service, and in easy mode a restart wipes everything, including your account.

---

## Step 3 — Set the Public URL (fixes webhooks showing `localhost:5678`)

**Why this is needed:** n8n doesn't know its public URL by itself. If no webhook URL is set, it builds webhook URLs from `N8N_PROTOCOL://N8N_HOST:N8N_PORT`, which default to `http://localhost:5678`. Cloud Run gives you a public HTTPS address, but nothing passes that address to n8n. So your **Webhook** nodes would show `http://localhost:5678/webhook/...` as the Production URL, which nobody outside can reach.

**Fix:** tell n8n its public URL. In Cloud Shell, save your service URL into a variable, check it, then update the service:

```bash
SERVICE_URL=$(gcloud run services describe n8n --region=us-west1 --format='value(status.url)')
echo $SERVICE_URL       # should print https://n8n-....run.app

gcloud run services update n8n \
  --region=us-west1 \
  --update-env-vars="N8N_WEBHOOK_URL=${SERVICE_URL}/,N8N_EDITOR_BASE_URL=${SERVICE_URL}/,N8N_PROXY_HOPS=1"
```

You can also do this in the Cloud Console: **Cloud Run → your service → Edit & deploy new revision → Variables & secrets → add the variables → Deploy**.

**What each variable does:**

| Variable | What it does |
|---|---|
| `N8N_WEBHOOK_URL` | Fixes the **Test URL** and **Production URL** shown in Webhook nodes (and the Chat Trigger's public URL). **Keep the trailing slash** |
| `N8N_EDITOR_BASE_URL` | Fixes links n8n generates to the editor, such as OAuth callback URLs and emails |
| `N8N_PROXY_HOPS=1` | Tells n8n it's running behind Google's proxy, so it reads client IPs and the HTTPS scheme correctly. Without it, rate-limiting warnings can show up in the logs |

> **Older n8n versions (before 2.30):** use `WEBHOOK_URL` instead of `N8N_WEBHOOK_URL`. On current versions `WEBHOOK_URL` still works but logs a deprecation warning.

> **Don't set `N8N_PORT` to 443 or change `N8N_HOST` to make this work.** The container must still listen on 5678, which must match the container port in Cloud Run. `N8N_WEBHOOK_URL` changes the URL n8n *displays* without changing the port it listens on.

---

## Step 4 — Open n8n and Create Your Account

1. Open your **Service URL** in a new browser tab. You may first see *"n8n is starting up. Please wait"*, then the setup screen
2. **Create your owner account straight away**, with a strong password. The URL is public, so whoever opens it first can claim the owner account
3. You can now import workflows (**…** menu → **Import from File**) and add your credentials, the same as on your laptop

---

## Step 5 — Check the Webhook URLs

1. Create a workflow with a **Webhook** node (or import one) and open the node
2. Both URLs should now show your public address:
   - Test URL: `https://n8n-....run.app/webhook-test/...`
   - Production URL: `https://n8n-....run.app/webhook/...`
3. The **Production URL only responds once the workflow is set to Active** (toggle at the top right). The Test URL only responds while you click **Listen for test event**

If the URLs still show `localhost:5678`, reload the editor page. If they still do, check Step 3 ran without errors with:

```bash
gcloud run services describe n8n --region=us-west1 --format='yaml(spec.template.spec.containers[0].env)'
```

---

## Limitations of Easy Mode

| Issue | What happens | What to do |
|---|---|---|
| **Data loss on restart** | There's no database, so n8n keeps everything inside the container. Your account, workflows and credentials **disappear** whenever the service is redeployed, updated (including any env var change), or restarted by Google | **Download your workflows as JSON regularly** (**…** menu → **Download**). For anything you need to keep, use [durable mode](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run#durable-mode) with Cloud SQL Postgres (`DB_TYPE=postgresdb` and related settings) |
| **Always-on cost** | 1 instance with CPU always allocated is billed 24/7 | Delete the service when you're not using it ([Step 6](#step-6--delete-everything-when-youre-done)) |
| **Schedule Trigger nodes** | With Cloud Run's default settings (CPU only during requests, scale to zero), schedules don't fire while the service is idle | Already handled in this guide by `--no-cpu-throttling` and `--scaling=1`. Keep both if you use schedules |

---

## Troubleshooting

| Problem | Fix |
|---|---|
| *"Cannot GET /"* or *"n8n is starting up"* | n8n is still starting. Wait a moment and refresh |
| Webhook node still shows `localhost:5678` | Step 3 wasn't applied. Re-run it, wait for the new revision to deploy, then reload the editor |
| Workflows and account are gone | The service restarted or was updated (see *Limitations*). Create your account again and re-import your exported JSON files |
| Canvas keeps disconnecting / connection lost | Check `N8N_ENDPOINT_HEALTH=health` is set (Step 2) |
| `PERMISSION_DENIED` / billing error | Enable billing on the project, then re-run the command |
| Production webhook returns 404 | The workflow isn't **Active**, or you're calling the Test URL (`/webhook-test/`) instead of the Production URL (`/webhook/`) |

---

## Step 6 — Delete Everything When You're Done

**First, download any workflows you want to keep** (**…** menu → **Download**). Deleting the service deletes all your n8n data.

### 6a. Delete the Cloud Run service

This is the only resource easy mode creates. It stops all charges for n8n.

```bash
gcloud run services delete n8n --region=us-west1
```

Type **Y** to confirm. The Service URL stops working right away.

> Easy mode deploys a ready-made image from Docker Hub (`--image=n8nio/n8n`), so unlike `--source .` deploys, there's no Artifact Registry repository or Cloud Storage bucket to clean up.

### 6b. Check it's gone

```bash
gcloud run services list
```

If `n8n` no longer appears, you're done.

### 6c. If you also tried durable mode

Durable mode creates extra resources that keep costing money (especially the Cloud SQL database) until you delete them. Set your project ID, then delete each one:

```bash
export PROJECT_ID=$(gcloud config get-value project)

gcloud sql instances delete n8n-db                     # the Postgres database
gcloud secrets delete n8n-db-password                  # stored DB password
gcloud secrets delete n8n-encryption-key               # stored encryption key
gcloud projects remove-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/cloudsql.client"                     # remove the project-level role
gcloud iam service-accounts delete \
    n8n-service-account@$PROJECT_ID.iam.gserviceaccount.com   # the service account
```

Then check:

```bash
gcloud sql instances list
gcloud secrets list
gcloud iam service-accounts list
```

### The nuclear option: delete the whole project

If you created a Google Cloud project **just for this**, deleting the project removes everything in it and stops all billing for it:

```bash
gcloud projects delete YOUR_PROJECT_ID
```

>  This deletes **everything** in the project. Only do this if nothing else lives in it. Google keeps it for 30 days in case you change your mind (`gcloud projects undelete YOUR_PROJECT_ID`).

---

## References

- [n8n — Self-Hosting Options](https://docs.n8n.io/deploy/host-n8n) — All the ways to host n8n yourself
- [n8n — Deploy to Google Cloud Run](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider/deploy-to-google-cloud-run) — Official guide, including **durable mode** (Cloud SQL + Secret Manager) and Google Workspace OAuth setup
- [n8n — Configure Webhook URLs with a Reverse Proxy](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-webhook-urls-with-reverse-proxy) — Why and how to set `N8N_WEBHOOK_URL`
- [n8n — Endpoint Environment Variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables/endpoints) — Reference for webhook and endpoint settings
- [Terraform example for durable mode](https://github.com/ryanpei/n8n-hosting/tree/main/google-cloud-run) — Deploys the durable setup as code
- [Cloud Run Pricing](https://cloud.google.com/run/pricing) — How Cloud Run is billed
- [Cloud Run Billing Settings](https://cloud.google.com/run/docs/configuring/billing-settings) — Request-based vs instance-based (always-on) CPU
- [Google Cloud Budgets and Alerts](https://cloud.google.com/billing/docs/how-to/budgets) — Get warned before costs grow
- [Cloud Shell](https://cloud.google.com/shell/docs) — Browser terminal with `gcloud` pre-installed
