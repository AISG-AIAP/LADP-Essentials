# Module 0: Setup and Prerequisites

**Module 0** is the introductory module for this course: it gives an overview of the programme and what follows, then moves into practical setup.

Reference materials for getting started — installing Docker, setting up Flowise (used in the current videos) or n8n (coming soon), and provisioning LLM API credentials.

---

## Install Docker Desktop

Docker is the primary way to run both **n8n** and **Flowise** on your own computer. The Docker image comes with everything pre-installed, so you don't need to set up Node.js.

1. Download [Docker Desktop](https://www.docker.com/products/docker-desktop/) for your computer (Mac: pick **Apple Silicon** or **Intel chip**; Windows: install **WSL 2** first with `wsl --install` in an administrator PowerShell, then restart)
2. Install it and open Docker Desktop. Wait until it shows **"Engine running"**
3. Open a terminal (Mac: **Terminal** · Windows: **PowerShell**) and check it works:

```bash
docker --version
docker run hello-world
```

You should see **"Hello from Docker!"**. For detailed, screen-by-screen Mac and Windows steps (and fixes for common install errors), see the [Docker Desktop guide in Module 4](../LADPE_Module_4_Files/LADPE_Module_4.3%20-%20Deployment/n8n_deployment/n8n_app_deployment/README.md).

> Docker Desktop must be **open and running** whenever you use `docker` commands.

---

## n8n Setup

Flowise reached **end of life on 31 August 2026** and no longer receives fixes or updates, so we are moving the course to **n8n**, which will become the primary tool once the n8n demo videos are released. n8n versions of the hands-on demos are already provided as workflow files. The concepts (prompts, chain-of-thought, prompt chaining, RAG, agents, tools) are the same in any tool.

> **n8n demo videos are coming soon.** The demo videos using n8n have not been released yet, so please stay tuned. Until they are released, please **continue to follow the Flowise videos and use the Flowise demo workflows** (see [Flowise Installation](#flowise-installation) below). The n8n workflow files are available if you'd like to try n8n early, and the [Flowise to n8n table](#flowise-to-n8n-what-maps-to-what) below helps you find the equivalent pieces.

### Option A — Run n8n with Docker (free, Community Edition)
Once Docker Desktop is running (see [Install Docker Desktop](#install-docker-desktop) above), run:

```bash
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

- `-d` — runs n8n in the background
- `--name n8n` — names the container so you can stop/start it easily
- `-p 5678:5678` — makes n8n available on port 5678 of your computer
- `-v n8n_data:/home/node/.n8n` — saves your workflows and credentials in a Docker volume called `n8n_data`, so **your work is kept** when the container is stopped, restarted or removed

Then open **http://localhost:5678** and create your local owner account.

### Option B — n8n Cloud (nothing to install)
New users get a **2-week free trial** (at the time of writing). The trial starts when you sign up, so watch the videos first (or wait for the n8n demo videos, which are coming soon) and sign up at [n8n.io](https://n8n.io/) when you're ready to build. Export your workflows as JSON before the trial ends. If you already have an n8n account (e.g., through work), just log in.

### Everyday Docker Commands
These work for both n8n and Flowise; replace `n8n` with `flowise` for the Flowise container.

```bash
docker stop n8n      # stop n8n
docker start n8n     # start it again (your workflows are still there)
docker logs -f n8n   # see what n8n is doing (Ctrl + C to exit)
docker ps            # list running containers
```

> **Don't run the `docker run` command a second time.** It will fail with *"container name already in use"*. Use `docker start n8n` instead. To start completely fresh, run `docker rm -f n8n` and then the `docker run` command again; your data in the `n8n_data` volume is kept.

### Your First n8n Workflow
1. Download [My_first_workflow.json](n8n_workflows/My_first_workflow.json) from this folder
2. In n8n, create a new workflow, open the **…** menu (top right) and choose **Import from File**
3. Open each **Chat Model** node and select or create your own credential (credentials are never included in exported files). This workflow uses an OpenAI chat model with an Anthropic fallback; you can swap in a **Google Gemini** or **OpenRouter** chat model to use a free key (see [Provisioning LLM API Credentials](#provisioning-llm-api-credentials) below)
4. Click **Open chat** at the bottom of the canvas and send a message to test it

### Flowise to n8n: What Maps to What
If you are watching a Flowise video and building in n8n, use this table to find the equivalent piece.

| In Flowise | In n8n |
|---|---|
| Chatflow / Agentflow | Workflow |
| Chat window / Start node | Chat Trigger node (*When chat message received*) |
| Agent / LLM node | AI Agent node |
| ChatOpenAI, ChatAnthropic, and other chat models | OpenAI Chat Model, Anthropic Chat Model, and so on, attached to the AI Agent's **Chat Model** input |
| System message / prompt template | **System Message** option and **Prompt (User Message)** field on the AI Agent |
| Buffer Memory | Simple Memory node, attached to the AI Agent's **Memory** input |
| Structured Output Parser / JSON structured output | Structured Output Parser, enabled with **Require Specific Output Format** |
| Flow state / variables passed between nodes | Expressions such as `{{ $json.output }}` and `{{ $('Node Name').item.json }}` |
| Tools (Calculator, web search, custom tools) | Tool nodes attached to the AI Agent's **Tool** input |
| Credentials (sidebar) | Credentials (Overview page, or created directly from a node) |
| Load / Export Chatflow (JSON) | Import from File / Download (JSON) |

### n8n Troubleshooting

| What you see | What to do |
|---|---|
| Imported workflow shows red warning icons on the Chat Model nodes | Credentials are not included in workflow files. Open each Chat Model node and select or create your own credential |
| The model name in an imported workflow is not available | Pick any current model from the dropdown in the Chat Model node. The demo concepts do not depend on a specific model |
| **Import from File** is greyed out or missing | Make sure you are inside a workflow (create a new one first). You can also copy the JSON and paste it onto the canvas with Ctrl/Cmd + V |
| The Cloud trial has ended and I can no longer edit workflows | Subscribe to a Cloud plan, or [run n8n with Docker](#option-a--run-n8n-with-docker-free-community-edition) and import the JSON files you exported |
| `localhost:5678` does not load after running Docker | Check Docker Desktop is running and that nothing else is using port 5678. Run `docker logs n8n` to look for errors |
| Data passed between nodes looks wrong or shows `undefined` | Check the field is set to **Expression** (not **Fixed**) and the expression points at the right node. See the [n8n Expressions docs](https://docs.n8n.io/code/expressions/) |

### References
- [n8n Docs — Docker Installation](https://docs.n8n.io/hosting/installation/docker/) — Official self-hosting guide
- [n8n Pricing](https://n8n.io/pricing/) — Cloud plans and current trial details
- [n8n Docs — Credentials](https://docs.n8n.io/credentials/) — Adding API keys to n8n

---

## Flowise Installation

The course videos demonstrate the demos in Flowise. If you'd like to follow them in Flowise, **Docker is the primary way to install it**.

### Install via Docker
Once Docker Desktop is running (see [Install Docker Desktop](#install-docker-desktop) above), run:

```bash
docker run -d --name flowise -p 3000:3000 -v flowise_data:/root/.flowise flowiseai/flowise:3.1.3
```

- `-d` — runs Flowise in the background
- `--name flowise` — names the container so you can stop/start it easily
- `-p 3000:3000` — makes Flowise available on port 3000 of your computer
- `-v flowise_data:/root/.flowise` — saves your flows, credentials and settings in a Docker volume called `flowise_data`, so **your work is kept** when the container is stopped, restarted or removed. Flowise 3.1.3 runs as the root user and stores its data in `/root/.flowise`. (From Flowise 3.1.4, the image runs as the `node` user and the path is `/home/node/.flowise` instead, so keep the path matched to the version you run.)
- `flowiseai/flowise:3.1.3` — pins Flowise **3.1.3** (works on Mac Apple Silicon, Mac Intel and Windows). The course videos use 3.1.0; 3.1.3 is a later patch release in the same 3.1 line. As Flowise is end of life, pinning a version keeps your setup stable

The first run downloads the image, which takes a few minutes. Then open **http://localhost:3000** in your browser. Use the [everyday Docker commands](#everyday-docker-commands) above with `flowise` as the container name (e.g., `docker start flowise`).

### Install via npm (as shown in the course videos)
The course videos install Flowise with npm, using **Flowise 3.1.0** on **Node.js 20.20.1**. This requires [Node.js](https://nodejs.org/):

```bash
npm install -g flowise@3.1.0
npx flowise start
```

The npm method stays on **3.1.0** because Flowise **3.1.3 and later require Node.js 24**, while the videos use Node.js 20. The Docker image includes its own Node.js, which is why the Docker method can use the newer 3.1.3. If you run into errors, see the [FAQ](../FAQ.md#3-a-dependency-expects-node-22-or-my-node-version-is-eol).

### References
- [Flowise](https://flowiseai.com/) — Official Flowise website
- [Flowise — Getting Started](https://docs.flowiseai.com/getting-started) — Official installation guide (npm, Docker, and Git clone methods)
- [Flowise GitHub Repository](https://github.com/FlowiseAI/Flowise) — Source code, releases, and setup instructions
- [Flowise on Docker Hub](https://hub.docker.com/r/flowiseai/flowise/tags) — Available Flowise image versions
- [Docker Desktop](https://docs.docker.com/desktop/) — Install Docker
- [Node.js Download](https://nodejs.org/en/download) — Install Node.js (required for the npm method)

### Flowise Cloud
Flowise Cloud, the hosted version of Flowise, has been shut down as part of the Flowise sunset, so it's no longer an option. To use Flowise, install it with Docker or npm as above. If you don't want to install anything, use [n8n Cloud](#option-b--n8n-cloud-nothing-to-install) instead.

---

## Troubleshooting

> ### Having installation issues? See the **[LADP Essentials FAQ](../FAQ.md)**.

---

## Provisioning LLM API Credentials

> **No credit card? Start with a free option.** OpenAI, Anthropic and Azure OpenAI all require billing to be set up. **Google AI Studio** and **OpenRouter** (below) both give free API keys with access to capable models, enough to follow the course demos. Free tiers have low rate limits and the list of free models changes often, so check the linked pages for the latest.
>
> **Keep your keys secret.** Treat an API key like a password: don't paste it into shared files, screenshots, or GitHub. Store it in your tool's credentials (Flowise / n8n) or an environment variable.

### OpenAI
1. Go to [platform.openai.com](https://platform.openai.com/) and sign up or log in
2. Navigate to **API Keys** under your profile settings
3. Click **Create new secret key**, name it, and copy the key immediately (it won't be shown again)
4. Add billing details under **Settings > Billing** to activate API access

- [OpenAI API](https://openai.com/api/) — OpenAI API overview and capabilities
- [OpenAI API Keys](https://platform.openai.com/api-keys) — Manage your API keys
- [OpenAI API Quickstart](https://platform.openai.com/docs/quickstart) — Getting started guide
- [OpenAI Pricing](https://platform.openai.com/docs/pricing) — Current model pricing

### Anthropic
1. Go to [console.anthropic.com](https://console.anthropic.com/) and sign up or log in
2. Navigate to **API Keys** in the console sidebar
3. Click **Create Key**, name it, and copy the key immediately
4. Add billing details under **Plans & Billing** to activate API access

- [Claude Platform](https://platform.claude.com/login) — Claude platform login and dashboard
- [Anthropic Console](https://console.anthropic.com/) — Manage API keys and billing
- [Anthropic API Quickstart](https://docs.anthropic.com/en/docs/initial-setup) — Getting started guide
- [Anthropic Pricing](https://www.anthropic.com/pricing#anthropic-api) — Current model pricing

### Azure OpenAI (Microsoft Foundry)
> **Note:** Azure OpenAI is now part of **Microsoft Foundry** (previously Azure AI Foundry) and is **open to any Azure customer**, including individuals with a pay-as-you-go subscription. You no longer need to apply for access, except for a few models marked as *Limited Access* or if you want to turn off the built-in content filters. The same Foundry endpoint and key also give you access to other models (e.g., Mistral, Llama, Cohere). It's popular with organisations that need enterprise-grade security, compliance, and data residency.
>
> **It is not free.** You're billed per token, and a credit card is required. Free trial and Azure for Students subscriptions often have little or no quota for deploying models, so use a **pay-as-you-go** subscription.

1. Create an [Azure account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account) and set up a **pay-as-you-go** subscription (or use your organisation's subscription)
2. Sign in to [Microsoft Foundry](https://ai.azure.com/) and create a **project** (this creates the Foundry resource for you)
3. Open the **Model catalog**, pick a model (e.g., `gpt-4.1-mini`) and click **Deploy**. Note the **deployment name**, as your tool calls the model by this name
4. Copy the **endpoint URL** and **API key** from your project or deployment page
5. Set a budget alert under **Cost Management** in the [Azure Portal](https://portal.azure.com/) so you don't get surprised by charges

- **In Flowise:** use the **AzureChatOpenAI** node. **In n8n:** use the **Azure OpenAI Chat Model** node. Both ask for your resource/endpoint, API key and deployment name

- [What is Microsoft Foundry?](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry) — Overview of the platform
- [Microsoft Foundry — Quickstart](https://learn.microsoft.com/en-us/azure/foundry/quickstarts/get-started-code) — Create a project, deploy a model and make your first call
- [Limited Access to Azure OpenAI](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/limited-access) — Who needs to register (most users don't)
- [Foundry Models Pricing (Azure OpenAI)](https://azure.microsoft.com/en-us/pricing/details/ai-foundry-models/aoai/) — Current model pricing
- [Azure Budgets and Cost Alerts](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/cost-mgt-alerts-monitor-usage-spending) — Monitor and limit spending
- [Flowise — AzureChatOpenAI](https://docs.flowiseai.com/integrations/langchain/chat-models/azure-chatopenai) — Using Azure OpenAI in Flowise
- [n8n — Azure OpenAI Chat Model Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatazureopenai/) — Using Azure OpenAI in n8n

### Google (Gemini) — free tier available
1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey) and sign in with your Google account
2. Accept the Terms of Service. New users get a default Google Cloud project created automatically
3. Click **Create API key**, then copy the key and store it safely

**Free models** (free tier, as of Nov 2026)
- `gemini-3-flash-preview` — fast, capable general-purpose model, good default for the demos
- `gemini-3.8-flash`, `gemini-3.6-flash` — newer Flash models
- `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite` — lighter and faster, for simple tasks
- `gemini-embedding-001`, `gemini-embedding-2` — free embedding models (useful for RAG in Module 2)
- Gemma 4 open models

**Things to know**
- Free-tier limits are low (requests per minute and per day) and can change without notice. Check your current limits in AI Studio
- On the free tier, Google **uses your prompts and responses to improve its products**, so don't send personal or confidential data
- Pro models (e.g., `gemini-3.1-pro-preview`) are not free via the API, though you can try them in the AI Studio chat
- **In Flowise:** use the **ChatGoogleGenerativeAI** node. **In n8n:** use the **Google Gemini Chat Model** node with a *Google Gemini (PaLM) API* credential

- [Google API Keys](https://aistudio.google.com/api-keys) — Get API keys and test Gemini models
- [Google — Using Gemini API Keys](https://aistudio.google.com/docs/api-key) — Official guide to creating and securing API keys
- [Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart) — Getting started guide
- [Gemini API Pricing](https://aistudio.google.com/docs/pricing) — Current model pricing and which models have a free tier
- [Gemini API Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits) — How free-tier limits work
- [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview) — Model details
- [Flowise — ChatGoogleGenerativeAI](https://docs.flowiseai.com/integrations/langchain/chat-models/google-ai) — Using Gemini in Flowise
- [n8n — Google Gemini Chat Model Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatgooglegemini/) — Using Gemini in n8n

### OpenRouter (many providers, one key) — free models available
1. Sign up at [openrouter.ai](https://openrouter.ai/) (Google / GitHub login works)
2. Go to [Settings > Keys](https://openrouter.ai/settings/keys) and click **Create API Key**. Give it a name, then copy the key (it's only shown once)
3. No credit card is needed to use free models

**Free models** — any model whose ID ends in `:free`. Currently available examples (Nov 2026):
- `nvidia/nemotron-3-ultra-550b-a55b:free` — large, strong reasoning model (1M token context)
- `nvidia/nemotron-3.5-super-vl:free` — supports images as well as text (1M context)
- `google/gemma-4-31b-it:free` — Google's open Gemma 4 model
- `nvidia/nemotron-3.5-lightning:free` — faster, lighter Nemotron model

To see the full, up-to-date list, filter the [model catalogue by price = 0](https://openrouter.ai/models?max_price=0) or browse the [Free Models collection](https://openrouter.ai/collections/free-models).

**Things to know**
- Free models are limited to **20 requests/minute and 50 requests/day**. Buying at least $10 of credits raises this to 1,000/day. Failed requests also count toward the limit
- Popular free models can be slow or temporarily unavailable at peak times; switch to another `:free` model if that happens
- If a free model returns *"No endpoints found"*, check your [privacy settings](https://openrouter.ai/settings/privacy). Some free providers require you to allow prompt logging/training
- OpenRouter is **OpenAI-compatible**: base URL `https://openrouter.ai/api/v1`
- **In Flowise:** use the **ChatOpenRouter** node. **In n8n:** use the **OpenRouter Chat Model** node

- [OpenRouter — Quickstart](https://openrouter.ai/docs/quickstart) — Making your first API call
- [OpenRouter — Pricing](https://openrouter.ai/pricing) — Free-tier limits and credit options
- [n8n — OpenRouter Chat Model Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenrouter/) — Using OpenRouter in n8n

---

## Connecting Credentials in Flowise

In Flowise, credentials are added via the **Credentials** section in the sidebar. Each LLM node (e.g., ChatOpenAI, ChatAnthropic) will prompt you to select or create a credential where you paste your API key.

- [Leon van Zyl's Flowise Tutorial — Adding AI Models & Credentials](https://www.youtube.com/watch?v=pUnKEKz-Mdg) — How to add API keys and credentials in Flowise
- [Leon van Zyl — How to Build a Local AI Agent With Flowise (Ollama, Postgres)](https://www.youtube.com/watch?v=GE9IlksvGiU) — Building a local AI agent using Flowise with Ollama and Postgres
