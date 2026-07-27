# LADP Essentials — Frequently Asked Questions

A central place for common questions and fixes across the course — Flowise installation, setup, and general course questions.

If your problem isn't covered here, please [open an issue](https://github.com/AISG-AIAP/LADP-Essentials/issues) or contact the LADP team.



---



## Contents

- [Installation and Setup](#installation-and-setup)
  1. [Which version of Flowise should I install?](#1-which-version-of-flowise-should-i-install)
  2. [The install keeps looping /](#2-the-install-keeps-looping--modulenotfounderror-no-module-named-distutils) `ModuleNotFoundError: No module named 'distutils'`
  3. [A dependency expects Node 22, or my Node version is EOL](#3-a-dependency-expects-node-22-or-my-node-version-is-eol)
  4. `flowise start` [fails with](#4-flowise-start-fails-with-cannot-find-module-turndown-or-another-module) `Cannot find module 'turndown'` [(or another module)](#4-flowise-start-fails-with-cannot-find-module-turndown-or-another-module)
  5. [How do I switch to a clean Docker setup (e.g. after a broken local install)?](#5-how-do-i-switch-to-a-clean-docker-setup-eg-after-a-broken-local-install)
- [General Course Questions](#general-course-questions)
  1. [Do I need coding experience to take this course?](#6-do-i-need-coding-experience-to-take-this-course)
  2. [Do I have to install Flowise locally? Can I use the hosted version?](#7-do-i-have-to-install-flowise-locally-can-i-use-the-hosted-version)
  3. [Which LLM provider / API key do I need?](#8-which-llm-provider--api-key-do-i-need)
  4. [Do I have to use Flowise? What about other tools?](#9-do-i-have-to-use-flowise-what-about-other-tools)
  5. [How do I submit my capstone project?](#10-how-do-i-submit-my-capstone-project)

---



## Installation and Setup

For step-by-step installation instructions, see **[Module 0](LADPE_Module_0_Files/README.md)**. Most local installation problems come down to your **Node.js version**, your **Python build tools**, or a known **Flowise packaging bug** — *not* the Flowise version you picked. Installing an older Flowise version usually won't help, so work through the issues below instead.

> **Tip:** If you get stuck, the fastest path to a working setup is the **Docker method** (everything is pre-installed, no local build step) or **Flowise Cloud** (nothing to install at all). Both are described in [Module 0](LADPE_Module_0_Files/README.md). The fixes below are for those who want the local npm install.



### 1. Which version of Flowise should I install?

The course videos use **Flowise 3.1.0** on a **Node.js / npm environment version 20.20.1**. By the time you watch this, there will likely be a newer release. You have a few options:

- **Match the videos exactly** — follow the installation steps shown in the video but pin the Flowise version: `npm install -g flowise@3.1.0` (on Node 20.20.1).
- **Use the latest version** — follow the [official Flowise documentation](https://docs.flowiseai.com/getting-started) to install the current release. Newer versions may require a newer Node.js (see [question 3](#3-a-dependency-expects-node-22-or-my-node-version-is-eol) below).
- **Use Docker (simplest)** — skip the Node.js/npm setup entirely. The Docker image comes with everything pre-installed, so you avoid the version and build issues below (see [question 5](#5-how-do-i-switch-to-a-clean-docker-setup-eg-after-a-broken-local-install)).



### 2. The install keeps looping / `ModuleNotFoundError: No module named 'distutils'`

**Symptom:** The installation keeps looping or asking you to reinstall, and you see `ModuleNotFoundError: No module named 'distutils'`.

**Cause:** During install, Flowise compiles a small native component using `node-gyp`, which relies on a Python module called `distutils`. Recent macOS versions (including Tahoe) ship **Python 3.12**, where `distutils` was removed. The build fails, the install never completes, and the terminal keeps re-prompting — that's the loop.

**Fix (macOS):**

```bash
# 1. Ensure Xcode command line build tools are present (safe if already installed)
xcode-select --install

# 2. Restore the missing distutils module
pip3 install setuptools --break-system-packages

# 3. Clear the half-finished install and reinstall cleanly
npm uninstall -g flowise
npm cache clean --force
npm install -g flowise
```



### 3. A dependency expects Node 22, or my Node version is EOL

**Symptom:** You see a warning that a dependency expects Node 22, or that your Node version is end-of-life (e.g. `v20.20.2 EOL`).

**Cause:** A Flowise dependency requires **Node.js 22 or newer**. Older versions such as Node 20 are now end-of-life (EOL) and will trigger warnings or failures. *(Note: a message like* `v20.20.2 EOL` *refers to your **Node** version, not npm.)*

**Fix (using [nvm](https://github.com/nvm-sh/nvm)):**

```bash
nvm install 22
nvm use 22
nvm alias default 22
node -v          # should now show v22.x
```

Then reinstall Flowise (see step 3 of [question 2](#2-the-install-keeps-looping--modulenotfounderror-no-module-named-distutils) above). On Node 22 the current version normally installs cleanly. If you want to match the course videos exactly, you can pin the version with `npm install -g flowise@3.1.0`.

### 4. `flowise start` fails with `Cannot find module 'turndown'` (or another module)

**Symptom:** The install finished, but `flowise start` fails with `Cannot find module 'turndown'` (or a similarly named module).

**Cause:** This is a known Flowise packaging bug ([FlowiseAI/Flowise#5251](https://github.com/FlowiseAI/Flowise/issues/5251)), **not** a problem with your machine. The installer omits a few of its own runtime modules, so Flowise can't find them at startup. Reaching this error is actually good news — it means Node, the build tools, and the install itself are all working.

**Fix:** Install the commonly-missing modules in one go, then start again:

```bash
npm install -g turndown @opentelemetry/exporter-trace-otlp-proto @opentelemetry/exporter-trace-otlp-grpc @opentelemetry/sdk-trace-node langchainhub

flowise start
```

Then open [http://localhost:3000](http://localhost:3000) in your browser.

> If you later see another `Cannot find module 'xxxx'` message, the fix follows the same pattern: `npm install -g xxxx`, then `flowise start` again. If these keep appearing one by one, stop fighting the local install and switch to a clean Docker setup ([question 5](#5-how-do-i-switch-to-a-clean-docker-setup-eg-after-a-broken-local-install)), which ships with everything pre-installed.



### 5. How do I switch to a clean Docker setup (e.g. after a broken local install)?

If the local (npm) install keeps failing, the most reliable fix is to remove it and switch to **Docker**, which comes with everything pre-installed. The steps below are for **macOS (Apple Silicon)**.

**Step 1 — Remove the local install** and the helper packages you may have added along the way:

```bash
npm uninstall -g flowise
npm uninstall -g turndown @opentelemetry/exporter-trace-otlp-proto @opentelemetry/exporter-trace-otlp-grpc @opentelemetry/sdk-trace-node langchainhub winston-daily-rotate-file
```

(If any of those report *"not installed"*, that's fine — just ignore it.)

*Optional — for a completely clean slate*, remove Flowise's local data folder (safe if the local install never finished starting up):

```bash
rm -rf ~/.flowise
```

**Step 2 — Install [Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)** and open it once so it's running in the background (you'll see a whale icon in the top menu bar).

**Step 3 — Start Flowise in Docker:**

```bash
docker run -d --name flowise -p 3000:3000 -v flowise_data:/root/.flowise flowiseai/flowise
```

**Step 4 — Give it about a minute** (the first run downloads the image), then open [http://localhost:3000](http://localhost:3000) in your browser.

> **Port already in use?** If the command reports that port 3000 is taken, switch the **left-hand** number to 3001:
>
> ```bash
> docker run -d --name flowise -p 3001:3000 -v flowise_data:/root/.flowise flowiseai/flowise
> ```
>
> Then open [http://localhost:3001](http://localhost:3001) instead. (To re-run the command, first clear the old container with `docker rm -f flowise`.)

That's the whole setup. **Open Docker Desktop each time** you want to start Flowise. Everything in the course works exactly the same once Flowise is open in the browser — only the way you start it up changes.

Handy commands for later:

```bash
docker stop flowise      # stop it
docker start flowise     # start it again
docker logs -f flowise   # view logs
```

**Why the** `-v flowise_data:/root/.flowise` **part?** It saves your work. Flowise keeps its database, your saved chatflows, and an encryption key in `/root/.flowise`. Without the volume, that folder lives *inside* the container: it survives `docker stop` / `docker start`, but it is **lost the moment the container is removed or recreated** — which happens on upgrades, on the port-conflict fix above (`docker rm -f flowise`), and during most "let me start over" troubleshooting. The `-v flowise_data:/root/.flowise` flag moves that folder to a **named volume on the host**, independent of the container, so you can remove, recreate, or upgrade the container as often as you like and your chatflows persist. It also preserves the encryption key, so previously-saved credentials (API keys, etc.) stay decryptable. One extra flag, no silent data loss — worth it for coursework you want to keep.

---



## General Course Questions



### 6. Do I need coding experience to take this course?

No. LADP Essentials is a **no-code / low-code** course. You build everything visually in Flowise, so you can focus on the concepts (prompt engineering, RAG, agents, evaluation, deployment) rather than writing application code. A few later exercises (e.g. Module 4 evaluations) involve running a provided notebook, but no prior coding is required.

### 7. Do I have to install Flowise locally? Can I use the hosted version?

You have options. You can install Flowise locally (via npm or Docker) **or** use **[Flowise Cloud](https://cloud.flowiseai.com/)**, a managed hosted version that needs no local installation (just create an account and sign in). See [Module 0](LADPE_Module_0_Files/README.md) for all three approaches.

> ⚠️ **The free Flowise Cloud tier is limited.** At the time of writing, it allows only **2 flows/assistants, 100 predictions per month, and 5 MB storage**, with community-only support. That's enough to try out some of the course demos, but you may hit these limits as you build. See the [current Flowise Cloud pricing](https://flowiseai.com/#pricing) for the latest limits and paid tiers. A **local install (npm or Docker) has no such caps** and is free.



### 8. Which LLM provider / API key do I need?

The course videos guide you through **OpenAI** and **Anthropic (Claude)** — you only need one of these to follow along. Step-by-step instructions for obtaining and connecting their API keys are in [Module 0](LADPE_Module_0_Files/README.md). *(Module 0 also includes reference links for Azure OpenAI and Google Gemini if you prefer those, but the video walkthroughs cover OpenAI and Anthropic.)*

### 9. Do I have to use Flowise? What about other tools?

Flowise is the vehicle we use to teach the concepts in an accessible, visual way — but the concepts transfer. Once you understand prompt engineering, RAG, agentic workflows, evaluation, deployment, and responsible AI, you can apply them on other no-code/low-code tools (Langflow, Dify, n8n) or coding frameworks (LangChain, LangGraph, CrewAI).

### 10. How do I submit my capstone project?

Submit a **Pull Request** to this repository, adding your work to a new folder under `LADPE_Project_Phase/contributions_from_learners/`. Full scenario briefs and step-by-step PR instructions (fork → branch → commit → push → open PR) are in **[LADPE_Project_Phase/README.md](LADPE_Project_Phase/README.md)**.

---

*LADP Essentials — AI Singapore*