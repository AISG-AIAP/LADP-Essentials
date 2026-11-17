# LADP Essentials

**LLM Application Developer Programme (Essentials)**
*A No-Code / Low-Code Course by AI Singapore*

---

Welcome to LADP Essentials! This course takes you from understanding how Large Language Models (LLMs) communicate, all the way to deploying and securing your own LLM-powered applications — without needing to write much code. You build everything visually in a drag-and-drop workflow tool: the course videos and demos use **n8n**.

This repository contains the workflows and files used in the LADP Essentials videos and demos, for both the n8n track and the optional Flowise track.

> **Course update: the course now uses n8n.** Flowise reached end of life on 31 August 2026, so the hands-on demos have moved to **n8n**, and the n8n demo videos are now the main course videos. New learners should follow the n8n videos and use the n8n workflows (in each module's `n8n_workflows/` folder). The Flowise demos and workflows (in `flowise_workflows/`) are kept as an optional track for learners who started with them, but Flowise no longer receives fixes or updates and may be removed from the course in future. See the [FAQ](FAQ.md) for more details.

---

## Course Overview

The course starts with a course overview and setup module, then four learning modules that each build on the previous one, and ends with a capstone project:

| Module | Title | What You'll Learn |
|--------|-------|-------------------|
| **0** | **Course Overview** | Introduction to NLP and LLMs, how to use the course and its learning tracks, and setting up n8n (hosted or with Docker), an IDE and the course repo, and LLM API keys. |
| **1** | **LLM Foundations & Prompt Engineering** | How LLMs work under the hood (tokens, context windows), how to communicate with them effectively (system/user/AI messages), and advanced prompting techniques (chain-of-thought, few-shot, prompt chaining). |
| **2** | **Retrieval Augmented Generation (RAG)** | How to connect LLMs to your own data — covering document processing, chunking strategies, embeddings, vector databases, similarity search, and building RAG chatbots in n8n. |
| **3** | **Agentic Workflows** | How to build LLM agents that use tools, make decisions, and work together — including multi-agent triage systems, structured outputs, and visual agent builders such as the n8n AI Agent. |
| **4** | **Evaluations, Deployment & Responsible AI** | Everything you need to go from prototype to production — evaluating LLM applications (4.1–4.3), deploying to the cloud (4.4–4.5), and security, bias, and responsible AI (4.6). |
| **5** | **Capstone Project** | Build a working LLM application for one of seven scenarios, in n8n or Flowise, and share it through a Pull Request. |

### Learning Tracks

Each module has three kinds of lessons:

- **Core** — Concept lessons, quizzes and resources for everyone.
- **n8n** — Hands-on demos in n8n. This is the main track, and all new learners should follow it.
- **Flowise (optional)** — The same demos in Flowise, for learners who started with Flowise. Flowise reached end of life and may be removed from the course in future.

Follow the Core lessons plus one demo track. You don't need to do both.

### The Learning Journey

```
Module 1              Module 2          Module 3            Module 4
Prompt Engineering --> RAG           --> Agentic         --> Production
                                        Workflows           Readiness

"How do I talk    "How do I give   "How do I make     "How do I evaluate,
 to an LLM?"      it my data?"     it take action?"    deploy, and secure it?"
```

Each module builds directly on the previous one. RAG uses prompting skills from Module 1. Agents in Module 3 combine prompting and RAG. Module 4 brings it all together for real-world deployment.

### A Note on Tools vs Concepts

We build everything hands-on using **n8n** (with an optional **Flowise** track), but the platform does not matter — the concepts do. Once you understand the fundamentals (prompt engineering, RAG, agentic workflows, evaluation, deployment, and responsible AI), you can apply them on any platform: other no-code/low-code tools like Dify; coding frameworks like LangChain, LangGraph, or CrewAI; or even coding assistants like Claude Code or Codex.

n8n and Flowise are simply the vehicles we use to teach these concepts in an accessible, visual way. Focus on the *why* behind each concept, and you'll transfer that knowledge to whatever tools you choose.

---

## Repository Structure

- **`LADPE_Module_0_Files/`** — Module 0, Course Overview: setting up n8n (n8n Cloud, recommended, or locally with Docker), an IDE and the course repo, LLM API credentials (including free options), and the optional Flowise setup; `n8n_workflows/` has the Getting Started guide and your first n8n workflow
- **`LADPE_Module_1_Workflows/`** — LLM messages and prompt engineering demos (prompt engineering, chain-of-thought, prompt chaining), plus the optional Flowise demos (first chatbot, first agent, zero-shot, few-shot, chain-of-thought, prompt chaining)
- **`LADPE_Module_2_Workflows/`** — RAG workflow demos (Qdrant and Pinecone vector stores in n8n, including creating a Pinecone index) and the optional Flowise RAG demo; `documents_for_rag/` contains sample source docs for ingestion
- **`LADPE_Module_3_Workflows/`** — Agent workflows: triaging agent, report writing agent, and connecting the report writing agent to an AI assistant such as Claude through an MCP server (n8n), plus the optional Flowise agent workflows
- **`LADPE_Module_4_Files/`**
  - `LADPE_Module_4.2 - Evaluations/` — evaluation notebooks (n8n version for 4.2, optional Flowise version for 4.3), CSV inputs, `.env.example`, and the n8n workflow used for evaluation
  - `LADPE_Module_4.3 - Deployment/`
    - `n8n_deployment/` (4.4) — a guide to hosting the n8n backend on Google Cloud Run, and a web app that calls an n8n agent (Docker + Cloud Run)
    - `flowise_deployment/` (4.5, optional) — Streamlit app, static HTML embed, Docker files, Kubernetes configs, and a Cloud Run deployment guide

> The folder names under `LADPE_Module_4_Files/` keep their original numbering. The chapter numbers in brackets above are the ones used in the course.

In Modules 1–3, workflow files are split into **`n8n_workflows/`** and **`flowise_workflows/`** folders.
- **`LADPE_Project_Phase/`** — Module 5, Capstone Project: scenario briefs, submission instructions, and a `contributions_from_learners/` folder for learner submissions via Pull Request

Each module folder contains its own `README.md` with reference materials and additional details.

---

## Getting Started

1. **Set up your tool** — Follow [Module 0](LADPE_Module_0_Files/README.md) to set up **n8n**. We recommend the hosted **n8n Cloud** free trial; running n8n locally with Docker is the alternative. Then get an LLM API key (free options available). Hitting an installation error? See the **[FAQ](FAQ.md)**.
2. **Import workflows** — Import the JSON files from each module's `n8n_workflows/` folder into n8n (via **…** menu → **Import from File**). If you're on the optional Flowise track, the Flowise versions are in `flowise_workflows/`.
3. **Follow the videos** — Each workflow maps to a video lesson. Configure your API keys, data sources, and settings as shown. If you watch both the n8n and Flowise demos, the Flowise-to-n8n table in [Module 0](LADPE_Module_0_Files/README.md) helps you compare the equivalent pieces.
4. **For evaluations (Module 4.2)** — Use the notebook and CSV files provided. Copy `.env.example` to `.env` and add your own values.

> The JSON files are n8n and Flowise exports and can be imported directly. File names align with the demo names shown in the course. Credentials are never included in the exported files, so you'll add your own after importing. The `.env` file should not be committed to source control.

---

## How to Go Through This Course

### For Complete Beginners (Recommended: Two-Pass Approach)

If LLMs, RAG, and agents are all new to you, we recommend watching the course **twice** with different goals each time.

**Pass 1 — Get the Big Picture (Watch Mode)**
- Watch all videos from Module 0 through Module 4 **without stopping to do the hands-on exercises**.
- Don't worry about memorising details or tool configurations.
- Your goal is to understand the *story*: what each concept is, why it matters, and how the pieces fit together.
- Jot down anything that confuses or excites you — you'll revisit it in Pass 2.

**Pass 2 — Go Deep (Build Mode)**
- Go through the course again, module by module.
- **Pause the videos and follow along** with every hands-on exercise in n8n.
- Experiment! Change settings, try different prompts, break things on purpose. This is where real learning happens.
- Use the resources and references in each module folder to go deeper.

> **Why two passes?** LLM application development involves many interconnected concepts. The first pass gives you the mental scaffolding; the second pass fills in the detail.

### For Learners with Some LLM Experience

- **Skim Module 1** — Review tokenisation, context windows, and message roles. The advanced prompting sections may still offer new techniques.
- **Focus on Modules 2 and 3** — RAG and Agentic Workflows are where the real application-building skills live. Go through these carefully with hands-on exercises.
- **Don't skip Module 4** — Evaluation, deployment, and security are critical for real applications and often underserved in beginner courses.

### For Learners with Technical / Coding Backgrounds

- You'll move faster through the conceptual sections, but pay attention to **tool-specific** implementation patterns and trade-offs in n8n.
- **RAG evaluation frameworks** (RAGAS, DeepEval, TruLens) and **bias/fairness definitions** may offer new perspectives.
- Use the hands-on exercises to prototype quickly before writing custom code.

---

## Module-by-Module Tips

### Module 1: LLM Foundations & Prompt Engineering

**Key takeaway:** The quality of your LLM application starts with how you communicate with the model.

- Pay special attention to **system messages** — they are the foundation of every application you'll build later.
- **Tokenisation and context windows** may feel abstract, but understanding these limits will save you debugging time in Modules 2 and 3.
- Try the prompting techniques on your own use cases, not just the examples given.

### Module 2: RAG

**Key takeaway:** RAG lets you build LLM apps that work with *your* data, not just what the model was trained on.

- **Chunking** is where most RAG quality issues begin. Understand the difference between fixed-size, recursive, and semantic chunking.
- The **similarity search** section uses some math, but focus on the *intuition* — you don't need to memorise formulas.
- Start with a small, clean document for your first RAG chatbot. Don't use a 200-page PDF on your first attempt.

### Module 3: Agentic Workflows

**Key takeaway:** Agents add decision-making and tool use to your LLM applications.

- The **multi-agent triage** example is the core pattern — most real-world agent architectures are variations of it.
- Experiment with connecting different tools to your agents. The power of agents comes from what you connect them to.
- **Structured JSON outputs** and **output validation** are essential for building reliable agent workflows.

### Module 4: Evaluations, Deployment & Responsible AI

**Key takeaway:** Building an LLM app is one thing. Making it reliable, deployable, and responsible is another.

- **4.1–4.3 (Evaluation):** The RAG Triad (Context Relevance, Groundedness, Answer Relevance) is your go-to framework for assessing RAG quality.
- **4.4–4.5 (Deployment):** Don't be intimidated by Docker and Cloud Run. Focus on understanding *why* each step exists, not just copying commands.
- **4.6 (Security, Bias & Responsible AI):** Prompt injection, bias testing, and responsible deployment practices are not optional — they separate a demo from a real application.

---

## Tips for Getting the Most Out of This Course

1. **Build something real.** Pick a use case that matters to you — a chatbot for your team, a document Q&A system, an agent that automates a tedious task — and build it alongside the course.
2. **Break things intentionally.** Don't just follow the steps. Change parameters, use different models, feed in unexpected input. Understanding failure modes is as valuable as understanding success.
3. **Take notes on connections.** How does chunking strategy (Module 2) affect RAG evaluation scores (Module 4)? How does system prompt design (Module 1) impact agent reliability (Module 3)?
4. **Use n8n as a playground.** Test ideas quickly before committing to a full implementation.
5. **Revisit earlier modules after finishing.** You'll understand Module 1 much better after completing Module 4.

---

## Quick Reference: Key Concepts by Module

| Module | Key Concepts |
|--------|-------------|
| **1 — LLM Foundations & Prompt Engineering** | Tokens, BPE, context window, system/user/AI messages, chain-of-thought, few-shot prompting, role-based assistants, sliding window, summarisation chains |
| **2 — RAG** | Document processing, chunking (fixed-size, recursive, semantic), embeddings, vector databases (HNSW, LSH), cosine similarity, Euclidean distance, dot product, RAG pipeline |
| **3 — Agentic Workflows** | Agents, tools, n8n AI Agent, multi-agent triage, MCP, structured JSON output, output validation, sequential/parallel workflows |
| **4 — Evaluations, Deployment & Responsible AI** | RAG Triad, LLM-as-a-Judge, BLEU, BERTScore, RAGAS, DeepEval, TruLens, Docker, GKE, Cloud Run, prompt injection, jailbreaking, data leakage, bias & fairness, responsible deployment |

---

## Module 5: Capstone Project

After completing Modules 1–4, you'll apply what you've learned in a hands-on **capstone project**. Choose one of seven scenarios and build a working LLM application using either a **RAG pipeline** or an **Agentic Workflow** — grounded in a real, publicly available document (HR policies, government reports, employee handbooks, academic research, and more). We recommend building it in n8n, but you can also use Flowise or any other framework you prefer.

**How to share your work:** Submit a **Pull Request** to this repository. Your contribution goes into a folder you create under `LADPE_Project_Phase/contributions_from_learners/` containing:

- Your exported workflow file (from n8n, Flowise, or the framework you used)
- A short `README.md` describing your scenario, design decisions, and sample conversations

Full project brief, scenario list, and step-by-step PR instructions (fork → branch → commit → push → open PR) are in **[`LADPE_Project_Phase/README.md`](LADPE_Project_Phase/README.md)**.

---

*LADP Essentials — AI Singapore*
