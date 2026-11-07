# Barbenheimer Q&A — n8n + Docker + Cloud Run

A tiny web app that sends your question to an **n8n AI agent** (which searches a
Barbie and an Oppenheimer vector store) and shows the answer plus the source text it used.

```
 Browser (static/index.html)  ──►  Flask server (app.py)  ──►  n8n webhook  ──►  Vector stores
            ◄──────────────── answer + source chunks ◄────────────────
```

## What's in the folder

| File | What it does |
|---|---|
| `app.py` | The Python server. **This is where you paste your webhook URL.** |
| `static/index.html` | The web page (design + the JavaScript that calls `/api/ask`). |
| `requirements.txt` | The Python libraries we need. |
| `Dockerfile` | Recipe to package the app into a container. |
| `.dockerignore` / `.gcloudignore` | Files to leave out of the container / upload. |

> **Why a Python server and not just an HTML page?** Browsers block web pages from calling
> other websites directly (this is called **CORS**). Our little server calls n8n *for* the
> page, so there are no CORS errors and the webhook URL isn't visible in the page source.

---

## Step 0 — Install the tools (one time)

You need 3 tools:

| Tool | What it's for | Check it's installed |
|---|---|---|
| **Python 3.10+** | Runs the app on your laptop (Step 2) | `python3 --version` (Windows: `python --version`) |
| **Docker Desktop** | Packages the app into a container (Step 3) | `docker --version` |
| **Google Cloud CLI** | Deploys to Cloud Run (Step 4) | `gcloud --version` |

- Python → https://www.python.org/downloads/ (Windows: on the first installer screen, **tick "Add python.exe to PATH"**)
- Google Cloud CLI → https://cloud.google.com/sdk/docs/install
- Docker Desktop → follow the guide below

### Installing Docker Desktop (first time using Docker? start here)

**What is Docker?** Think of a container as a **lunchbox**: it holds your app *plus* everything it
needs (Python, libraries, settings). A lunchbox packed on your laptop opens the same way on Google's
servers, so "it works on my machine" becomes "it works everywhere".
**Docker Desktop** is the free app that builds and runs these lunchboxes on your computer.

> Docker Desktop is free for personal use, education, and small businesses
> (under 250 employees and under US$10M revenue). Larger companies need a paid plan.

---

#### Mac

**1. Find out which chip your Mac has**
Click the  **Apple menu** (top-left) → **About This Mac**. Look at the **Chip** (or **Processor**) line:
- Says **Apple M1 / M2 / M3 / M4…** → you need **Apple Silicon**
- Says **Intel** → you need **Intel chip**

**2. Download**
Go to https://www.docker.com/products/docker-desktop/ → click **Download Docker Desktop** →
choose **Mac – Apple Silicon** or **Mac – Intel chip** to match step 1.

**3. Install**
- Open the downloaded **`Docker.dmg`** file (it's in your **Downloads** folder).
- In the window that appears, **drag the whale icon into the Applications folder**.

**4. Open Docker for the first time**
- Open **Applications** → double-click **Docker**.
- If macOS asks *"Docker is an app downloaded from the internet. Are you sure?"* → click **Open**.
- Click **Accept** on the service agreement.
- Choose **Use recommended settings** → click **Finish**. Enter your Mac password if asked.
- If it asks you to **sign in or create an account** → you can click **Skip** / **Continue without signing in**.

**5. Wait for it to be ready**
Look for the **whale icon in the menu bar** (top-right of your screen). When the Docker
Desktop window says **"Engine running"** (green, bottom-left), you're ready.

Jump to **"Test that Docker works"** below.

---

#### Windows

**1. Check your Windows version**
Press **Windows key + R**, type `winver`, press Enter. You need **Windows 10 (version 22H2 or newer)
or Windows 11**, 64-bit.

**2. Install WSL 2 (the engine Docker uses on Windows)**
WSL lets Windows run Linux, which Docker needs.
- Click **Start**, type **PowerShell**, then **right-click → Run as administrator** → click **Yes**.
- Paste this and press Enter:
  ```powershell
  wsl --install
  ```
- When it finishes, **restart your computer**.
- (If it says WSL is already installed, run `wsl --update` instead.)

**3. Download**
Go to https://www.docker.com/products/docker-desktop/ → click **Download Docker Desktop** →
choose **Windows – AMD64** (almost all PCs).
Only pick **Windows – ARM64** if you have an ARM laptop (e.g. Surface with Snapdragon). Not sure?
**Settings → System → About → System type** tells you "x64" (→ AMD64) or "ARM" (→ ARM64).

**4. Install**
- Double-click **`Docker Desktop Installer.exe`** (in your **Downloads** folder). Click **Yes** if Windows asks for permission.
- On the configuration screen, make sure **"Use WSL 2 instead of Hyper-V"** is **ticked**.
- Click **OK** and wait. When it says **Installation succeeded**, click **Close and restart** (or restart yourself).

**5. Open Docker for the first time**
- Click **Start** → open **Docker Desktop**.
- Click **Accept** on the service agreement.
- If it asks you to **sign in or create an account** → you can click **Skip** / **Continue without signing in**.
- Wait until the window says **"Engine running"** (green, bottom-left). You'll also see the
  whale icon in the system tray (bottom-right, you may need to click the **^** arrow).

> **Windows users, everywhere in this guide:** use `python` instead of `python3`, and activate the
> Python environment with `.venv\Scripts\activate` instead of `source .venv/bin/activate`.
> If PowerShell says *"running scripts is disabled on this system"*, run this once, then try again:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (type **Y** if asked).

---

#### Test that Docker works (Mac & Windows)

Open a **new** terminal (Mac: **Terminal** app · Windows: **PowerShell**) and run:

```bash
docker --version
```
You should see something like `Docker version 28.x.x`.

Then run Docker's built-in test:
```bash
docker run hello-world
```
You should see **"Hello from Docker!"** This means Docker downloaded a tiny test container and ran it.

> **Remember:** Docker Desktop must be **open and running** whenever you use `docker` commands.
> If you restart your computer, open Docker Desktop again first.

#### Docker install problems?

| Problem | Fix |
|---|---|
| `docker: command not found` / `'docker' is not recognized` | Close the terminal and open a **new** one. Still failing? Restart your computer. |
| `Cannot connect to the Docker daemon` / `error during connect` | Docker Desktop isn't running. Open it and wait for **"Engine running"**. |
| Windows: *"WSL 2 installation is incomplete"* or *"WSL needs updating"* | Open PowerShell **as administrator**, run `wsl --update`, then restart. |
| Windows: *"Virtualization support not detected"* | Virtualization is switched off in your PC's BIOS. Search "enable virtualization" + your laptop brand, or ask your IT team. |
| Mac: *"Docker.app can't be opened"* | Open **System Settings → Privacy & Security**, scroll down, click **Open Anyway**. |
| Work laptop blocks the install | You may need admin rights. Ask your IT team to install Docker Desktop. |

---

When all 3 tools pass their checks, open a terminal **in this project folder** for every step below.

> **How to open a terminal in this folder:**
> - **Mac:** open **Terminal**, type `cd ` (with a space), drag the project folder into the window, press Enter.
> - **Windows:** open the project folder in File Explorer, click the address bar, type `powershell`, press Enter.
> - **VS Code (both):** **File → Open Folder…** → pick this folder → **Terminal → New Terminal**.

---

## Step 1 — Paste your n8n webhook URL

1. In n8n, open your workflow → click the **Webhook** node → choose the **Production URL** tab → copy it.
2. Make sure the workflow is **Active** (toggle at the top right). Production URLs only work when it is.
3. Open `app.py` and paste the URL between the quotes:

```python
WEBHOOK_URL = os.environ.get(
    "N8N_WEBHOOK_URL",
    "https://YOUR-N8N.app.n8n.cloud/webhook/xxxxxxxx",   # paste here
)
```

> Your webhook must accept a POST with `{"question": "..."}` and return
> `{"answer": "...", "chunks": [{"store": "...", "content": "...", "lines": "..."}]}`.

**Quick check that the webhook works** (optional):

**Mac (Terminal):**
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"question":"Who directed Oppenheimer?"}' \
  https://YOUR-N8N.app.n8n.cloud/webhook/xxxxxxxx
```

**Windows (PowerShell):**
```powershell
Invoke-RestMethod -Method Post -ContentType "application/json" -Body '{"question":"Who directed Oppenheimer?"}' -Uri "https://YOUR-N8N.app.n8n.cloud/webhook/xxxxxxxx"
```

You should get back an `answer` and some `chunks`.

---

## Step 2 — Run it locally (no Docker yet)

**Mac (Terminal):**
```bash
python3 -m venv .venv                 # create an isolated Python environment
source .venv/bin/activate             # switch it on
pip install -r requirements.txt       # install Flask + requests
python app.py                         # start the app
```

**Windows (PowerShell):**
```powershell
python -m venv .venv                  # create an isolated Python environment
.venv\Scripts\activate                # switch it on
pip install -r requirements.txt       # install Flask + requests
python app.py                         # start the app
```

> When the environment is on, your prompt starts with **`(.venv)`**.
> Windows: if you see *"running scripts is disabled on this system"*, run
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, type **Y**, then activate again.

Open **http://localhost:8080** → click a suggestion or type a question.

Stop the app with **Ctrl + C**.

---

## Step 3 — Run it in Docker

Docker packages the app + Python + libraries into one "container" that runs the same everywhere.
Make sure **Docker Desktop is open** and says **"Engine running"**. Stop the Step 2 app first (**Ctrl + C**)
so port 8080 is free.

These commands are the **same on Mac and Windows**:

```bash
docker build -t barbenheimer .                  # build the image (the "recipe" → "meal")
docker run --rm -p 8080:8080 barbenheimer       # run it
```

Open **http://localhost:8080** again — same app, now running inside a container.
Stop it with **Ctrl + C**.

> `-p 8080:8080` means "connect port 8080 on my laptop to port 8080 in the container".

---

## Step 4 — Deploy to Google Cloud Run

All `gcloud` commands in Steps 4 and 5 are the **same on Mac and Windows** (Terminal or PowerShell).

### 4a. Log in and pick your project (one time)

```bash
gcloud auth login                               # opens a browser to sign in
gcloud projects list                            # find your PROJECT_ID
gcloud config set project YOUR_PROJECT_ID
gcloud config set run/region asia-southeast1    # Singapore
```

### 4b. Turn on the services Cloud Run needs (one time)

```bash
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com
```
> Your project needs **billing enabled**. Cloud Run has a generous free tier.

### 4c. Deploy

```bash
gcloud run deploy barbenheimer --source . --allow-unauthenticated
```

- `--source .` uploads this folder; Google **builds the Docker image for you** using our `Dockerfile`.
- `--allow-unauthenticated` makes the site public so anyone with the link can use it.
- If asked *"create an Artifact Registry repository?"* → type **Y**.

After 2–4 minutes you'll see:

```
Service URL: https://barbenheimer-xxxxxxxx.asia-southeast1.run.app
```

Open that link — your app is live on the internet!

### Updating the app later
Change any file, then run the **same** deploy command again. Cloud Run rolls out the new version.

### (Optional) Change the webhook without editing code
```bash
gcloud run services update barbenheimer --set-env-vars N8N_WEBHOOK_URL=https://YOUR-N8N.app.n8n.cloud/webhook/xxxxxxxx
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `Could not reach n8n: 404` | Workflow isn't **Active**, or you pasted the **Test** URL instead of the **Production** URL. |
| `Could not reach n8n: 500` | The n8n workflow errored. Open n8n → **Executions** to see why. |
| `Address already in use` / `port is already allocated` | Something else uses port 8080 (often the Step 2 app, so stop it with **Ctrl + C**). Or use another port, then open http://localhost:8081:<br>• Python on Mac: `PORT=8081 python app.py`<br>• Python on Windows: `$env:PORT=8081; python app.py`<br>• Docker (both): `docker run --rm -p 8081:8080 barbenheimer` |
| `python3: command not found` (Windows) | On Windows, type `python` instead of `python3`. |
| `'python' is not recognized` (Windows) | Reinstall Python and **tick "Add python.exe to PATH"**, then open a new PowerShell. |
| `Cannot connect to the Docker daemon` | Open Docker Desktop and wait until it says it's running. |
| Cloud Run: `PERMISSION_DENIED` / billing error | Enable billing on the project and re-run step 4b. |
| Cloud Run page says `Forbidden` | You forgot `--allow-unauthenticated`. Re-run the deploy command with it. |

---

## Step 5 — Destroy everything when you're done

Deploying with `--source .` creates **3 things** in Google Cloud. Delete all 3 so nothing is left
behind (Cloud Run itself costs nothing when idle, but stored images and files can add small charges).

| What | Where it came from |
|---|---|
| Cloud Run service `barbenheimer` | The running website |
| Artifact Registry repo `cloud-run-source-deploy` | Where Google stored the Docker image it built |
| Cloud Storage bucket (`run-sources-…` or `…_cloudbuild`) | Where your uploaded source code was kept |

### 5a. Delete the website (Cloud Run service)
```bash
gcloud run services delete barbenheimer --region asia-southeast1
```
Type **Y** to confirm. The Service URL stops working right away.

### 5b. Delete the stored Docker images
```bash
gcloud artifacts repositories delete cloud-run-source-deploy --location asia-southeast1
```
Type **Y** to confirm.
> If you used `--source .` deploys for **other** apps in this region, their images live in this repo too.
> In that case skip this step, or delete only this app's images in the Console
> (**Artifact Registry → cloud-run-source-deploy → barbenheimer → Delete**).

### 5c. Delete the uploaded source code
List your buckets and look for one starting with `run-sources-` or ending in `_cloudbuild`:
```bash
gcloud storage buckets list --format="value(name)"
```
Delete it (replace with the name you found):
```bash
gcloud storage rm --recursive gs://BUCKET_NAME
```
> Only delete the bucket created by the deploy. Leave any other buckets alone.

### 5d. Check everything is gone
```bash
gcloud run services list
gcloud artifacts repositories list
gcloud storage buckets list
```
If `barbenheimer`, `cloud-run-source-deploy` and the source bucket no longer appear, you're done.

### 5e. Clean up your laptop (optional)
**Mac:**
```bash
docker rmi barbenheimer        # delete the local Docker image
deactivate                     # leave the Python environment (if it's active)
rm -rf .venv                   # delete the Python environment folder
```

**Windows (PowerShell):**
```powershell
docker rmi barbenheimer                   # delete the local Docker image
deactivate                                # leave the Python environment (if it's active)
Remove-Item -Recurse -Force .venv         # delete the Python environment folder
```

### The nuclear option: delete the whole project
If you made a Google Cloud project **just for this workshop**, the easiest cleanup is to delete
the whole project. This removes everything inside it and stops all billing for it:
```bash
gcloud projects delete YOUR_PROJECT_ID
```
> This deletes **everything** in the project. Only do this if nothing else lives in it.
> Google keeps it for 30 days in case you change your mind (`gcloud projects undelete YOUR_PROJECT_ID`).
