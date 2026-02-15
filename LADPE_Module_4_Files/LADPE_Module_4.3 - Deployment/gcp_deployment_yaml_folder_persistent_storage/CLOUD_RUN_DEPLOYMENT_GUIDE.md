# Deploying to Google Cloud Run

This guide walks you through deploying the **Streamlit App** and the **HTML App** to Google Cloud Run using Artifact Registry.

Cloud Run is a fully managed serverless platform that automatically scales your containerized applications. Unlike GKE (Google Kubernetes Engine), Cloud Run does not require you to manage clusters, nodes, or Kubernetes YAML files — making it ideal for simple web app deployments.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Key Concepts](#2-key-concepts)
3. [Part A — Deploy the HTML App](#3-part-a--deploy-the-html-app)
4. [Part B — Deploy the Streamlit App](#4-part-b--deploy-the-streamlit-app)
5. [Managing Your Deployments](#5-managing-your-deployments)
6. [Troubleshooting](#6-troubleshooting)
7. [Cost Management](#7-cost-management)

---

## 1. Prerequisites

Before you begin, make sure you have:

- A **Google Cloud Platform (GCP) account** with billing enabled
- The **gcloud CLI** installed ([Install Guide](https://cloud.google.com/sdk/docs/install))
- **Docker Desktop** installed and running
- A **GCP project** created
- Both apps already built locally with `docker-compose up -d` (so the images exist on your machine)

### Initial Setup

```bash
# Log in to Google Cloud
gcloud auth login

# Set your project (replace with your actual project ID)
gcloud config set project YOUR_PROJECT_ID

# Enable the required APIs
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com

# Set your preferred region
gcloud config set run/region us-central1
```

### Create an Artifact Registry Repository

Artifact Registry is where your Docker images will be stored. If you haven't created one yet:

```bash
gcloud artifacts repositories create YOUR_REPO_NAME \
  --repository-format=docker \
  --location=us-central1 \
  --description="LADP Essentials app images"
```

> Replace `YOUR_REPO_NAME` with a name of your choice (e.g. `flowise-app`, `ladp-apps`, etc.)

### Authenticate Docker with Artifact Registry

```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```

> Replace `us-central1` with your region if different.

---

## 2. Key Concepts

### Container Port Configuration

Each app listens on a different port inside its container:
- **HTML App (nginx)** — listens on port **80**
- **Streamlit App** — listens on port **8501**

Cloud Run defaults to sending traffic to port `8080`, but you can override this with the `--port` flag during deployment. This guide uses `--port` to match each app's container port, so **no Dockerfile changes are needed**.

### Cloud Run vs GKE

| Feature | Cloud Run | GKE |
|---------|-----------|-----|
| Infrastructure | Fully managed (serverless) | You manage clusters & nodes |
| Scaling | Scales to zero automatically | Minimum 1 node always running |
| Pricing | Pay per request | Pay for running nodes |
| Best for | Stateless web apps & APIs | Complex, stateful workloads |
| Setup complexity | Low | High |

---

## 3. Part A — Deploy the HTML App

The HTML app is an nginx container serving a static Flowise chat interface.

### Step 1: Build the Image Locally

If you haven't already, build the image using docker-compose:

```bash
cd LADPE_Module_4_Files/LADPE_Module_4.3\ -\ Deployment/html_deployment
docker-compose up -d
```

This creates a local image named `html_deployment-flowise-web`.

### Step 2: Tag the Image for Artifact Registry

```bash
docker tag html_deployment-flowise-web \
  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/html-app:dev
```

### Step 3: Push the Image to Artifact Registry

```bash
docker push us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/html-app:dev
```

### Step 4: Deploy to Cloud Run

```bash
gcloud run deploy flowise-html-app \
  --image us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/html-app:dev \
  --platform managed \
  --region us-central1 \
  --port 80 \
  --allow-unauthenticated
```

> **Note:** `--port 80` tells Cloud Run to send traffic to port 80, which is the port nginx listens on inside the container.

Cloud Run will output a URL like:
```
https://flowise-html-app-xxxxx-uc.a.run.app
```

Open this URL in your browser to verify the deployment.

### Important: Update flowise.html Before Deploying

Make sure the `apiHost` in `flowise.html` points to your deployed Flowise instance (not `localhost`):

```html
<script type="module">
    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
    Chatbot.initFull({
        chatflowid: "YOUR_CHATFLOW_ID",
        apiHost: "https://YOUR_FLOWISE_URL",
    })
</script>
```

If you update this file after the initial deployment, you will need to rebuild, re-tag, push, and redeploy (see [Section 5 — Update a Deployment](#update-a-deployment-after-code-changes)).

---

## 4. Part B — Deploy the Streamlit App

The Streamlit app is a Python application that generates business reports.

### Step 1: Build the Image Locally

If you haven't already, build the image using docker-compose:

```bash
cd LADPE_Module_4_Files/LADPE_Module_4.3\ -\ Deployment/streamlit_deployment
docker-compose up -d
```

This creates a local image named `streamlit_deployment-streamlit-app`.

### Step 2: Tag the Image for Artifact Registry

```bash
docker tag streamlit_deployment-streamlit-app \
  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/streamlit-app:dev
```

### Step 3: Push the Image to Artifact Registry

```bash
docker push us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/streamlit-app:dev
```

### Step 4: Deploy to Cloud Run

```bash
gcloud run deploy streamlit-report-app \
  --image us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/streamlit-app:dev \
  --platform managed \
  --region us-central1 \
  --port 8501 \
  --allow-unauthenticated \
  --memory 512Mi \
  --timeout 300
```

**Flags explained:**
- `--port 8501` — Tells Cloud Run to send traffic to port 8501, which is the port Streamlit listens on inside the container
- `--memory 512Mi` — Streamlit needs more memory than a static HTML page
- `--timeout 300` — Allows up to 5 minutes for report generation requests (default is 60s, which may not be enough for AI-generated reports)

Cloud Run will output a URL like:
```
https://streamlit-report-app-xxxxx-uc.a.run.app
```

### Important: Update the API URL Before Deploying

The `API_URL` in `streamlit_app.py` must point to your deployed Flowise instance (not `localhost`):

```python
API_URL = "https://YOUR_FLOWISE_URL/api/v1/prediction/YOUR_CHATFLOW_ID"
```

If you update this file after the initial deployment, you will need to rebuild, re-tag, push, and redeploy (see [Section 5 — Update a Deployment](#update-a-deployment-after-code-changes)).

---

## 5. Managing Your Deployments

### View Running Services

```bash
gcloud run services list
```

### View Logs

```bash
# HTML app logs
gcloud run services logs read flowise-html-app --region us-central1

# Streamlit app logs
gcloud run services logs read streamlit-report-app --region us-central1
```

### Update a Deployment (After Code Changes)

When you update your application code, repeat the build-tag-push-deploy cycle:

```bash
# 1. Rebuild the image (from the app's directory)
docker-compose up -d --build

# 2. Re-tag with a new version
docker tag IMAGE_NAME \
  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/APP_NAME:v2

# 3. Push the new image
docker push us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/APP_NAME:v2

# 4. Redeploy to Cloud Run
gcloud run deploy SERVICE_NAME \
  --image us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/APP_NAME:v2 \
  --region us-central1
```

> **Tip:** Increment the tag (`:dev` → `:v2` → `:v3`) so you can roll back to a previous version if needed.

### Delete a Service (Stop Incurring Costs)

```bash
gcloud run services delete flowise-html-app --region us-central1
gcloud run services delete streamlit-report-app --region us-central1
```

---

## 6. Troubleshooting

### "Container failed to start and listen on the port"

**Cause:** Cloud Run is sending traffic to a port your app isn't listening on.

**Fix:** Make sure the `--port` flag in your `gcloud run deploy` command matches the port your app actually listens on:
- HTML app (nginx): `--port 80`
- Streamlit app: `--port 8501`

### "Container failed to become healthy. Startup probes timed out"

**Cause:** The app took too long to start.

**Fix:**
```bash
gcloud run deploy SERVICE_NAME \
  --image YOUR_IMAGE \
  --startup-cpu-boost \
  --timeout 300
```
- `--startup-cpu-boost` temporarily allocates more CPU during container startup
- `--timeout 300` extends the request timeout to 5 minutes

### Platform Mismatch Warning

If you see: `The requested image's platform (linux/amd64) does not match the detected host platform (linux/arm64/v8)`

**Cause:** You're building on an Apple Silicon Mac (ARM) but Cloud Run runs on x86 (amd64).

**This is expected.** The `FROM --platform=linux/amd64` in both Dockerfiles ensures the image is built for the correct architecture. The warning only appears when running locally and does not affect Cloud Run deployment.

### App Works Locally but Not on Cloud Run

Common causes:
- **`localhost` URLs in your code** — Replace `localhost` references in `flowise.html` and `streamlit_app.py` with the actual deployed URLs of your services
- **Missing environment variables** — Set them with `--set-env-vars`:
  ```bash
  gcloud run deploy SERVICE_NAME --set-env-vars KEY1=VALUE1,KEY2=VALUE2
  ```
- **Insufficient memory** — Increase with `--memory 1Gi`

---

## 7. Cost Management

Cloud Run charges based on CPU/memory usage and number of requests. To minimize costs:

- **Scale to zero:** Cloud Run scales to 0 instances when there's no traffic (this is the default). You only pay when your app is handling requests
- **Set max instances:** Limit how many instances can run simultaneously:
  ```bash
  gcloud run deploy SERVICE_NAME --max-instances 3
  ```
- **Delete unused services:** If you're done testing, delete the service to avoid any charges:
  ```bash
  gcloud run services delete SERVICE_NAME --region us-central1
  ```
- **Free tier:** Cloud Run offers a generous free tier — 2 million requests/month, 360,000 vCPU-seconds, and 180,000 GiB-seconds of memory per month

---

## Quick Reference — Full Command Sequence

```bash
# ============================================================
# ONE-TIME SETUP
# ============================================================
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud services enable run.googleapis.com artifactregistry.googleapis.com
gcloud artifacts repositories create YOUR_REPO_NAME \
  --repository-format=docker --location=us-central1
gcloud auth configure-docker us-central1-docker.pkg.dev

# ============================================================
# DEPLOY HTML APP
# ============================================================
cd html_deployment
docker-compose up -d
docker tag html_deployment-flowise-web \
  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/html-app:dev
docker push \
  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/html-app:dev
gcloud run deploy flowise-html-app \
  --image us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/html-app:dev \
  --platform managed --region us-central1 --port 80 --allow-unauthenticated

# ============================================================
# DEPLOY STREAMLIT APP
# ============================================================
cd streamlit_deployment
docker-compose up -d
docker tag streamlit_deployment-streamlit-app \
  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/streamlit-app:dev
docker push \
  us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/streamlit-app:dev
gcloud run deploy streamlit-report-app \
  --image us-central1-docker.pkg.dev/YOUR_PROJECT_ID/YOUR_REPO_NAME/streamlit-app:dev \
  --platform managed --region us-central1 --port 8501 \
  --allow-unauthenticated --memory 512Mi --timeout 300
```

> **Remember:** Replace `YOUR_PROJECT_ID` and `YOUR_REPO_NAME` with your actual GCP project ID and Artifact Registry repository name in all commands above.
