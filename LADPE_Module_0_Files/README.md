# Module 0: Setup and Prerequisites

Reference materials for getting started — installing Flowise, accessing Flowise Cloud, and provisioning LLM API credentials.

---

## Flowise Installation

### Local Installation (via npm)
Flowise requires [Node.js](https://nodejs.org/) version 18.15.0 or above.

```bash
npm install -g flowise
npx flowise start
```

### Local Installation (via Docker)
```bash
docker pull flowiseai/flowise
docker run -d --name flowise -p 3000:3000 flowiseai/flowise
```

### References
- [Flowise — Getting Started](https://docs.flowiseai.com/getting-started) — Official installation guide (npm, Docker, and Git clone methods)
- [Flowise GitHub Repository](https://github.com/FlowiseAI/Flowise) — Source code, releases, and setup instructions
- [Node.js Download](https://nodejs.org/en/download) — Install Node.js (required for npm method)
- [Docker Desktop](https://docs.docker.com/desktop/) — Install Docker (required for Docker method)

### Flowise Cloud
- [Flowise Cloud](https://cloud.flowiseai.com/) — Managed hosted version of Flowise (no local installation needed but requires to setup an account and sign in)

---

## Provisioning LLM API Credentials

### OpenAI
1. Go to [platform.openai.com](https://platform.openai.com/) and sign up or log in
2. Navigate to **API Keys** under your profile settings
3. Click **Create new secret key**, name it, and copy the key immediately (it won't be shown again)
4. Add billing details under **Settings > Billing** to activate API access

- [OpenAI API Keys](https://platform.openai.com/api-keys) — Manage your API keys
- [OpenAI API Quickstart](https://platform.openai.com/docs/quickstart) — Getting started guide
- [OpenAI Pricing](https://platform.openai.com/docs/pricing) — Current model pricing

### Anthropic
1. Go to [console.anthropic.com](https://console.anthropic.com/) and sign up or log in
2. Navigate to **API Keys** in the console sidebar
3. Click **Create Key**, name it, and copy the key immediately
4. Add billing details under **Plans & Billing** to activate API access

- [Anthropic Console](https://console.anthropic.com/) — Manage API keys and billing
- [Anthropic API Quickstart](https://docs.anthropic.com/en/docs/initial-setup) — Getting started guide
- [Anthropic Pricing](https://www.anthropic.com/pricing#anthropic-api) — Current model pricing

### Azure OpenAI
> **Note:** Azure OpenAI is available to **organisations only** — it requires an Azure enterprise subscription and your organisation must apply for and be granted access. It is not available to individual consumer accounts. This is typically used when organisations need enterprise-grade security, compliance, and data residency controls.

1. Your organisation must first [apply for access to Azure OpenAI](https://aka.ms/oai/access)
2. Sign in to the [Azure Portal](https://portal.azure.com/) with your organisation account
3. Create an **Azure OpenAI** resource (search "Azure OpenAI" in the marketplace)
4. Once deployed, go to **Keys and Endpoint** in the resource blade to find your API key and endpoint URL
5. Use [Azure AI Foundry](https://ai.azure.com/) to deploy specific models (e.g., GPT-4.1) before calling them

- [Azure OpenAI — Getting Started](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview) — Overview and setup guide
- [Azure OpenAI — Quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/chatgpt-quickstart) — Step-by-step quickstart
- [Azure OpenAI Pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/) — Current model pricing

### Google (Gemini)
1. Go to [Google AI Studio](https://aistudio.google.com/) and sign in with your Google account
2. Click **Get API Key** in the sidebar
3. Create a key for a new or existing Google Cloud project and copy it

- [Google API Keys](https://aistudio.google.com/api-keys) — Get API keys and test Gemini models
- [Gemini API Quickstart](https://ai.google.dev/gemini-api/docs/quickstart) — Getting started guide
- [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing) — Current model pricing

---

## Connecting Credentials in Flowise

In Flowise, credentials are added via the **Credentials** section in the sidebar. Each LLM node (e.g., ChatOpenAI, ChatAnthropic) will prompt you to select or create a credential where you paste your API key.

- [Leon van Zyl's Flowise Tutorial — Adding AI Models & Credentials](https://www.youtube.com/watch?v=pUnKEKz-Mdg) — How to add API keys and credentials in Flowise
