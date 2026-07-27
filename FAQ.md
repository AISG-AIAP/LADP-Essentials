# LADP Essentials — Frequently Asked Questions

A central place for common questions and fixes across the course — Flowise installation, setup, and general course questions.

If your problem isn't covered here, please [open an issue](https://github.com/AISG-AIAP/LADP-Essentials/issues) or contact the LADP team.

<!--
──────────────────────────────────────────────────────────────────────
MAINTAINER GUIDE — HOW TO ADD TO THIS FAQ
This page is organised by TOPIC. Each "## Heading" is a topic section,
and each "### Heading" under it is a single question. Adding content is
meant to be a copy-paste job — follow the patterns below.

▸ To add a QUESTION to an existing topic:
    1. Under the right "## topic", add a "### question" heading, phrased
       the way a learner would ask it.
    2a. For an error / problem, use the ISSUE template:
            ### <short description of the symptom>
            **Symptom:** what the learner sees.
            **Cause:** why it happens.
            **Fix:** what to do (add a ```bash code block``` if useful).
    2b. For a general question, just write a short, direct answer.
    3. Add a matching bullet to the "## Contents" list.

▸ To add a NEW TOPIC (e.g. "Module 2: RAG", "Deployment",
  "Credentials & API Keys", "Evaluation"):
    1. Add a new "## Topic Name" section (place install/setup near the
       top; keep "General Course Questions" last as the catch-all).
    2. Add its questions beneath it using the templates above.
    3. Add the topic (and its questions, nested) to "## Contents".

▸ Keep every entry self-contained so topics can be reordered freely.
▸ There is no build step — if you edit this file, mirror the change in
  FAQ.html so the rendered page stays in sync.
──────────────────────────────────────────────────────────────────────
-->

---

## Contents

- [Installation and Setup](#installation-and-setup)
  - [Which version of Flowise should I install?](#which-version-of-flowise-should-i-install)
  - [The install keeps looping / `ModuleNotFoundError: No module named 'distutils'`](#the-install-keeps-looping--modulenotfounderror-no-module-named-distutils)
  - [A dependency expects Node 22, or my Node version is EOL](#a-dependency-expects-node-22-or-my-node-version-is-eol)
  - [`flowise start` fails with `Cannot find module 'turndown'` (or another module)](#flowise-start-fails-with-cannot-find-module-turndown-or-another-module)
- [General Course Questions](#general-course-questions)

---

## Installation and Setup

For step-by-step installation instructions, see **[Module 0](LADPE_Module_0_Files/README.md)**. Most local installation problems come down to your **Node.js version**, your **Python build tools**, or a known **Flowise packaging bug** — *not* the Flowise version you picked. Installing an older Flowise version usually won't help, so work through the issues below instead.

> **Tip:** If you get stuck, the fastest path to a working setup is the **Docker method** (everything is pre-installed, no local build step) or **Flowise Cloud** (nothing to install at all). Both are described in [Module 0](LADPE_Module_0_Files/README.md). The fixes below are for those who want the local npm install.

### Which version of Flowise should I install?

The course videos use **Flowise 3.1.0** on a **Node.js / npm environment version 20.20.1**. By the time you watch this, there will likely be a newer release. You have a few options:

- **Match the videos exactly** — follow the installation steps shown in the video but pin the Flowise version: `npm install -g flowise@3.1.0` (on Node 20.20.1).
- **Use the latest version** — follow the [official Flowise documentation](https://docs.flowiseai.com/getting-started) to install the current release. Newer versions may require a newer Node.js (see the [Node version question](#a-dependency-expects-node-22-or-my-node-version-is-eol) below).
- **Use Docker (simplest)** — skip the Node.js/npm setup entirely. The Docker image comes with everything pre-installed, so you avoid the version and build issues below.

### The install keeps looping / `ModuleNotFoundError: No module named 'distutils'`

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

### A dependency expects Node 22, or my Node version is EOL

**Symptom:** You see a warning that a dependency expects Node 22, or that your Node version is end-of-life (e.g. `v20.20.2 EOL`).

**Cause:** A Flowise dependency requires **Node.js 22 or newer**. Older versions such as Node 20 are now end-of-life (EOL) and will trigger warnings or failures. *(Note: a message like `v20.20.2 EOL` refers to your **Node** version, not npm.)*

**Fix (using [nvm](https://github.com/nvm-sh/nvm)):**

```bash
nvm install 22
nvm use 22
nvm alias default 22
node -v          # should now show v22.x
```

Then reinstall Flowise (see step 3 of the [distutils fix](#the-install-keeps-looping--modulenotfounderror-no-module-named-distutils) above). On Node 22 the current version normally installs cleanly. If you want to match the course videos exactly, you can pin the version with `npm install -g flowise@3.1.0`.

### `flowise start` fails with `Cannot find module 'turndown'` (or another module)

**Symptom:** The install finished, but `flowise start` fails with `Cannot find module 'turndown'` (or a similarly named module).

**Cause:** This is a known Flowise packaging bug ([FlowiseAI/Flowise#5251](https://github.com/FlowiseAI/Flowise/issues/5251)), **not** a problem with your machine. The installer omits a few of its own runtime modules, so Flowise can't find them at startup. Reaching this error is actually good news — it means Node, the build tools, and the install itself are all working.

**Fix:** Install the commonly-missing modules in one go, then start again:

```bash
npm install -g turndown @opentelemetry/exporter-trace-otlp-proto @opentelemetry/exporter-trace-otlp-grpc @opentelemetry/sdk-trace-node langchainhub

flowise start
```

Then open [http://localhost:3000](http://localhost:3000) in your browser.

> If you later see another `Cannot find module 'xxxx'` message, the fix follows the same pattern: `npm install -g xxxx`, then `flowise start` again. If these keep appearing one by one, switch to the Docker method (see [Module 0](LADPE_Module_0_Files/README.md)), which ships with everything pre-installed.

---

## General Course Questions

### Do I need coding experience to take this course?

No. LADP Essentials is a **no-code / low-code** course. You build everything visually in Flowise, so you can focus on the concepts (prompt engineering, RAG, agents, evaluation, deployment) rather than writing application code. A few later exercises (e.g. Module 4 evaluations) involve running a provided notebook, but no prior coding is required.

### Do I have to install Flowise locally? Can I use the hosted version?

You have options. You can install Flowise locally (via npm or Docker) **or** use **[Flowise Cloud](https://cloud.flowiseai.com/)**, a managed hosted version that needs no local installation (just create an account and sign in). See [Module 0](LADPE_Module_0_Files/README.md) for all three approaches.

### Which LLM provider / API key do I need?

The course works with several providers — **OpenAI**, **Anthropic (Claude)**, **Azure OpenAI**, and **Google (Gemini)**. You only need one to follow along. Step-by-step instructions for obtaining and connecting API keys for each provider are in [Module 0](LADPE_Module_0_Files/README.md).

### Do I have to use Flowise? What about other tools?

Flowise is the vehicle we use to teach the concepts in an accessible, visual way — but the concepts transfer. Once you understand prompt engineering, RAG, agentic workflows, evaluation, deployment, and responsible AI, you can apply them on other no-code/low-code tools (Langflow, Dify, n8n) or coding frameworks (LangChain, LangGraph, CrewAI).

### How do I submit my capstone project?

Submit a **Pull Request** to this repository, adding your work to a new folder under `LADPE_Project_Phase/contributions_from_learners/`. Full scenario briefs and step-by-step PR instructions (fork → branch → commit → push → open PR) are in **[LADPE_Project_Phase/README.md](LADPE_Project_Phase/README.md)**.

---

*LADP Essentials — AI Singapore*
