# LADP Essentials — Frequently Asked Questions

A central place for common questions and fixes across the course — Flowise installation, setup, and general course questions.

If your problem isn't covered here, please [open an issue](https://github.com/AISG-AIAP/LADP-Essentials/issues) or contact the LADP team.

<!--
──────────────────────────────────────────────────────────────────────
MAINTAINER GUIDE — HOW TO ADD TO THIS FAQ
This page is organised by TOPIC. Each "## Heading" is a topic section,
and each "### N. Heading" under it is a single, numbered question.
Adding content is meant to be a copy-paste job — follow the patterns below.

▸ Questions are numbered SEQUENTIALLY across the whole FAQ (1, 2, 3, ...).
  Append new questions at the end of a section and continue the numbering.
  Only renumber the following questions if you must insert in the middle.

▸ To add a QUESTION to an existing topic:
    1. Under the right "## topic", add a "### N. question" heading (next
       number in the sequence), phrased the way a learner would ask it.
    2a. For an error / problem, use the ISSUE template:
            ### N. <short description of the symptom>
            **Symptom:** what the learner sees.
            **Cause:** why it happens.
            **Fix:** what to do (add a ```bash code block``` if useful).
    2b. For a general question, just write a short, direct answer.
    3. Add a matching entry to the "## Contents" list. Contents uses plain
       bullets with the number written into the link text (e.g.
       "- [7. My question](#7-my-question)") — NOT an auto-numbered "1."
       list, so code formatters don't renumber it. Avoid inline `code`
       in Contents link text (formatters split it); use plain words.

▸ To add a NEW TOPIC (e.g. "Module 2: RAG", "Deployment",
  "Credentials & API Keys", "Evaluation"):
    1. Add a new "## Topic Name" section (place install/setup near the
       top; keep "General Course Questions" last as the catch-all).
    2. Add its questions beneath it, continuing the number sequence.
    3. Add the topic (and its questions, nested) to "## Contents".

▸ Keep every entry self-contained so topics can be reordered freely.
▸ This Markdown file is the single source of truth for the FAQ (it is
  linked from the READMEs). There is no separate rendered HTML page.
──────────────────────────────────────────────────────────────────────
-->

---

## Contents

- **Installation and Setup**
  - [1. Which version of Flowise should I install?](#1-which-version-of-flowise-should-i-install)
  - [2. The install keeps looping / distutils error](#2-the-install-keeps-looping--modulenotfounderror-no-module-named-distutils)
  - [3. A dependency expects Node 22, or my Node version is EOL](#3-a-dependency-expects-node-22-or-my-node-version-is-eol)
  - [4. flowise start fails with a missing module (e.g. turndown)](#4-flowise-start-fails-with-cannot-find-module-turndown-or-another-module)
  - [5. How do I switch to a clean Docker setup (e.g. after a broken local install)?](#5-how-do-i-switch-to-a-clean-docker-setup-eg-after-a-broken-local-install)
- **General Course Questions**
  - [6. Flowise is being discontinued. Is the course still worth taking?](#6-flowise-is-being-discontinued-is-the-course-still-worth-taking)
  - [7. Do I need coding experience to take this course?](#7-do-i-need-coding-experience-to-take-this-course)
  - [8. Do I have to install Flowise locally? Can I use the hosted version?](#8-do-i-have-to-install-flowise-locally-can-i-use-the-hosted-version)
  - [9. Which LLM provider / API key do I need?](#9-which-llm-provider--api-key-do-i-need)
  - [10. Do I have to use Flowise? What about other tools?](#10-do-i-have-to-use-flowise-what-about-other-tools)
  - [11. How do I submit my capstone project?](#11-how-do-i-submit-my-capstone-project)

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

If the local (npm) install keeps failing, the most reliable fix is to remove it and switch to **Docker**, which comes with everything pre-installed. This works on **both macOS and Windows** — the Docker commands are identical; only the OS-specific setup steps are called out below. Run the commands in **Terminal** (macOS) or **PowerShell** (Windows).

**Step 1 — Remove the local install** and the helper packages you may have added along the way:

```bash
npm uninstall -g flowise
npm uninstall -g turndown @opentelemetry/exporter-trace-otlp-proto @opentelemetry/exporter-trace-otlp-grpc @opentelemetry/sdk-trace-node langchainhub winston-daily-rotate-file
```

(If any of those report *"not installed"*, that's fine — just ignore it.)

*Optional — for a completely clean slate*, remove Flowise's local data folder (safe if the local install never finished starting up):

- **macOS** (Terminal):

  ```bash
  rm -rf ~/.flowise
  ```

- **Windows** (PowerShell):

  ```powershell
  Remove-Item -Recurse -Force $env:USERPROFILE\.flowise
  ```

**Step 2 — Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)** and open it once so it's running in the background:

- **macOS:** you'll see a whale icon in the top menu bar.
- **Windows:** Docker Desktop uses the **WSL 2** backend — if prompted, accept its one-time installation of WSL 2 (it may ask you to restart). Once it's running, you'll see a whale icon in the system tray (bottom-right corner).

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

**Why the `-v flowise_data:/root/.flowise` part?** It saves your work. Flowise keeps its database, your saved chatflows, and an encryption key in `/root/.flowise`. Without the volume, that folder lives *inside* the container: it survives `docker stop` / `docker start`, but it is **lost the moment the container is removed or recreated** — which happens on upgrades, on the port-conflict fix above (`docker rm -f flowise`), and during most "let me start over" troubleshooting. The `-v flowise_data:/root/.flowise` flag moves that folder to a **named volume on the host**, independent of the container, so you can remove, recreate, or upgrade the container as often as you like and your chatflows persist. It also preserves the encryption key, so previously-saved credentials (API keys, etc.) stay decryptable. One extra flag, no silent data loss — worth it for coursework you want to keep.

---

## General Course Questions

### 6. Flowise is being discontinued. Is the course still worth taking?

**Programme Update:** We want to make learners aware of a recent announcement regarding Flowise, the visual AI platform used in portions of LADP. We understand some of you may have questions about what this means for the programme. The good news is that there is **no change to the learning outcomes or the value of the course**, and we've answered the most common questions below.

<ins>**Update: Flowise is being discontinued. Is the course still worth taking?**</ins> <br>
**Yes—absolutely**. Flowise has been the platform we use to demonstrate concepts, but it has never been the end goal of the programme. The core skills you develop in LADP—prompt engineering, Retrieval-Augmented Generation (RAG), agentic workflows, evaluation, deployment, and responsible AI—are applicable across AI platforms and frameworks. These are the capabilities that remain valuable regardless of which tools are popular in the future.

**What has changed?**<br>
**In July 2026**, the Flowise team announced that they will be winding down active development of the project. Their published timeline is:
- **29 July 2026** – Feature development stops (code freeze); no new pull requests will be accepted.
- **10 August 2026** – The GitHub repository will be archived, and npm packages and Docker images will be marked as deprecated.
- **31 August 2026** – Official support through Discord and GitHub ends.

While active development and official support are ending, **Flowise itself will continue to be available as open-source software under the Apache 2.0 licence**. The source code, Docker images, and npm packages remain accessible, allowing learners to continue installing and using the platform to complete the programme's hands-on exercises.

**What does this mean for our LADP learners?**<br>
_Your learning outcomes remain unchanged._

From the beginning of the programme, our focus has been on teaching the principles behind building AI applications—not on mastering a single tool. Flowise has served as a visual, low-code environment that makes it easier to understand how prompts, retrieval, agents, memory, and evaluation work together before introducing more advanced implementation approaches.

These concepts transfer directly to other platforms and frameworks, including Langflow, Dify, n8n, LangChain, LangGraph, CrewAI, and coding agents such as Claude Code and Codex. As the AI ecosystem continues to evolve, the ability to understand these underlying concepts becomes even more valuable than familiarity with any individual platform.

**Why we're continuing with Flowise**<br>
We will continue using Flowise because it remains an effective learning platform for illustrating the concepts taught throughout LADP. Learners will still be able to complete the practical exercises and gain the intended skills and knowledge.

The industry will continue to introduce new tools and retire others. Our objective is to equip you with the understanding and practical experience to adapt confidently, regardless of which platform you use in the future.

A useful way to think about it is this: learning with Flowise is like learning to drive in a particular model of car. Even if that model is eventually discontinued, the driving skills you develop stay with you and transfer to any other vehicle. In the same way, the platform may evolve, but the knowledge and skills you gain through LADP remain relevant.

### 7. Do I need coding experience to take this course?

No. LADP Essentials is a **no-code / low-code** course. You build everything visually in Flowise, so you can focus on the concepts (prompt engineering, RAG, agents, evaluation, deployment) rather than writing application code. A few later exercises (e.g. Module 4 evaluations) involve running a provided notebook, but no prior coding is required.

### 8. Do I have to install Flowise locally? Can I use the hosted version?

You have options. You can install Flowise locally (via npm or Docker) **or** use **[Flowise Cloud](https://cloud.flowiseai.com/)**, a managed hosted version that needs no local installation (just create an account and sign in). See [Module 0](LADPE_Module_0_Files/README.md) for all three approaches.

> ⚠️ **The free Flowise Cloud tier is limited.** At the time of writing, it allows only **2 flows/assistants, 100 predictions per month, and 5 MB storage**, with community-only support. That's enough to try out some of the course demos, but you may hit these limits as you build. See the [current Flowise Cloud pricing](https://flowiseai.com/#pricing) for the latest limits and paid tiers. A **local install (npm or Docker) has no such caps** and is free.

> ⚠️ **Heads-up on the 2026 wind-down.** Flowise is being discontinued (see [question 6](#6-flowise-is-being-discontinued-is-the-course-still-worth-taking)), and the future of the hosted Flowise Cloud service is uncertain. For coursework you want to keep, a **local install (npm or Docker) is the safer choice** — the open-source images remain usable after the sunset, whereas a hosted service could change or close.

### 9. Which LLM provider / API key do I need?

The course videos guide you through **OpenAI** and **Anthropic (Claude)** — you only need one of these to follow along. Step-by-step instructions for obtaining and connecting their API keys are in [Module 0](LADPE_Module_0_Files/README.md). *(Module 0 also includes reference links for Azure OpenAI and Google Gemini if you prefer those, but the video walkthroughs cover OpenAI and Anthropic.)*

### 10. Do I have to use Flowise? What about other tools?

Flowise is the vehicle we use to teach the concepts in an accessible, visual way — but the concepts transfer. Once you understand prompt engineering, RAG, agentic workflows, evaluation, deployment, and responsible AI, you can apply them on other no-code/low-code tools (Langflow, Dify, n8n) or coding frameworks (LangChain, LangGraph, CrewAI).

### 11. How do I submit my capstone project?

Submit a **Pull Request** to this repository, adding your work to a new folder under `LADPE_Project_Phase/contributions_from_learners/`. Full scenario briefs and step-by-step PR instructions (fork → branch → commit → push → open PR) are in **[LADPE_Project_Phase/README.md](LADPE_Project_Phase/README.md)**.

---

*LADP Essentials — AI Singapore*
