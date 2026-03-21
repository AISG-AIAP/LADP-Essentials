# LADP Essentials

**LLM Application Developer Programme (Essentials)**
*A No-Code / Low-Code Course by AI Singapore*

---

Welcome to LADP Essentials! This course takes you from understanding how Large Language Models (LLMs) communicate, all the way to deploying and securing your own LLM-powered applications — without needing to write much code. We use **Flowise**, a visual drag-and-drop tool, as our primary platform throughout the course.

This repository contains the workflows and files used in the LADP Essentials videos and demos.

---

## Course Overview

The course is structured in four modules, each building on the last:

| Module | Title | What You'll Learn |
|--------|-------|-------------------|
| **1** | **Prompt Engineering** | How LLMs work under the hood (tokens, context windows), how to communicate with them effectively (system/user/AI messages), and advanced prompting techniques (chain-of-thought, few-shot, role-based assistants). |
| **2** | **Retrieval Augmented Generation (RAG)** | How to connect LLMs to your own data — covering document processing, chunking strategies, embeddings, vector databases, similarity search, and building RAG chatbots in Flowise. |
| **3** | **Agentic Workflows** | How to build LLM agents that use tools, make decisions, and work together — including multi-agent triage systems, prompt chaining, structured outputs, and Flowise AgentFlow V2. |
| **4** | **Production Readiness** | Everything you need to go from prototype to production — quality assessment and RAG evaluation (4.1), cloud deployment with Docker, GKE, and Cloud Run (4.2–4.3), and security, bias, and responsible AI (4.4). |

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

We build everything hands-on using **Flowise**, but the platform does not matter — the concepts do. Once you understand the fundamentals (prompt engineering, RAG, agentic workflows, evaluation, deployment, and responsible AI), you can apply them on any platform: other no-code/low-code tools like Langflow, Dify, or n8n; coding frameworks like LangChain, LangGraph, or CrewAI; or even coding assistants like Claude Code or Codex.

Flowise is simply the vehicle we use to teach these concepts in an accessible, visual way. Focus on the *why* behind each concept, and you'll transfer that knowledge to whatever tools you choose.

---

## Repository Structure

- **`LADPE_Module_0_Files/`** — Intro module: overview of the course, then setup and prerequisites (Flowise installation, LLM API credential provisioning, and connecting credentials in Flowise)
- **`LADPE_Module_1_Workflows/`** — Intro workflows (first chatbot and first agent) and prompt engineering demos (zero-shot, few-shot, chain-of-thought, prompt chaining)
- **`LADPE_Module_2_Workflows/`** — RAG workflow demo; `documents_for_rag/` contains sample source docs for ingestion
- **`LADPE_Module_3_Workflows/`** — Agent workflows: triaging agent and report writing agent
- **`LADPE_Module_4_Files/`**
  - `LADPE_Module_4.2 - Evaluations/` — notebook, CSV inputs, and `.env.example`
  - `LADPE_Module_4.3 - Deployment/` — Streamlit app, static HTML embed, Docker files, Kubernetes configs, and a Cloud Run deployment guide

Each module folder contains its own `README.md` with reference materials and additional details.

---

## Getting Started

1. **Install Flowise** — Follow the setup instructions in `LADPE_Module_0_Files/`.
2. **Import workflows** — Open Flowise and import the JSON files from each module folder.
3. **Follow the videos** — Each workflow maps to a video lesson. Configure your API keys, data sources, and settings as shown.
4. **For evaluations (Module 4.2)** — Use the notebook and CSV files provided. Copy `.env.example` to `.env` and add your own values.

> The JSON files are Flowise exports and can be imported directly. File names align with the demo names shown in the course. The `.env` file should not be committed to source control.

---

## How to Go Through This Course

### For Complete Beginners (Recommended: Two-Pass Approach)

If LLMs, RAG, and agents are all new to you, we recommend watching the course **twice** with different goals each time.

**Pass 1 — Get the Big Picture (Watch Mode)**
- Watch all videos from Module 1 through Module 4 **without stopping to do the hands-on exercises**.
- Don't worry about memorising details or tool configurations.
- Your goal is to understand the *story*: what each concept is, why it matters, and how the pieces fit together.
- Jot down anything that confuses or excites you — you'll revisit it in Pass 2.

**Pass 2 — Go Deep (Build Mode)**
- Go through the course again, module by module.
- **Pause the videos and follow along** with every hands-on exercise in Flowise.
- Experiment! Change settings, try different prompts, break things on purpose. This is where real learning happens.
- Use the resources and references in each module folder to go deeper.

> **Why two passes?** LLM application development involves many interconnected concepts. The first pass gives you the mental scaffolding; the second pass fills in the detail.

### For Learners with Some LLM Experience

- **Skim Module 1** — Review tokenisation, context windows, and message roles. The advanced prompting sections may still offer new techniques.
- **Focus on Modules 2 and 3** — RAG and Agentic Workflows are where the real application-building skills live. Go through these carefully with hands-on exercises.
- **Don't skip Module 4** — Evaluation, deployment, and security are critical for real applications and often underserved in beginner courses.

### For Learners with Technical / Coding Backgrounds

- You'll move faster through the conceptual sections, but pay attention to **Flowise-specific** implementation patterns and trade-offs.
- **RAG evaluation frameworks** (RAGAS, DeepEval, TruLens) and **bias/fairness definitions** may offer new perspectives.
- Use the hands-on exercises to prototype quickly before writing custom code.

---

## Module-by-Module Tips

### Module 1: Prompt Engineering

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

### Module 4: Production Readiness

**Key takeaway:** Building an LLM app is one thing. Making it reliable, deployable, and responsible is another.

- **4.1–4.2 (Evaluation):** The RAG Triad (Context Relevance, Groundedness, Answer Relevance) is your go-to framework for assessing RAG quality.
- **4.3 (Deployment):** Don't be intimidated by Docker and Kubernetes. Focus on understanding *why* each step exists, not just copying commands.
- **4.4 (Security, Bias & Responsible AI):** Prompt injection, bias testing, and responsible deployment practices are not optional — they separate a demo from a real application.

---

## Tips for Getting the Most Out of This Course

1. **Build something real.** Pick a use case that matters to you — a chatbot for your team, a document Q&A system, an agent that automates a tedious task — and build it alongside the course.
2. **Break things intentionally.** Don't just follow the steps. Change parameters, use different models, feed in unexpected input. Understanding failure modes is as valuable as understanding success.
3. **Take notes on connections.** How does chunking strategy (Module 2) affect RAG evaluation scores (Module 4)? How does system prompt design (Module 1) impact agent reliability (Module 3)?
4. **Use Flowise as playground.** Test ideas quickly before committing to a full implementation.
5. **Revisit earlier modules after finishing.** You'll understand Module 1 much better after completing Module 4.

---

## Quick Reference: Key Concepts by Module

| Module | Key Concepts |
|--------|-------------|
| **1 — Prompt Engineering** | Tokens, BPE, context window, system/user/AI messages, chain-of-thought, few-shot prompting, role-based assistants, sliding window, summarisation chains |
| **2 — RAG** | Document processing, chunking (fixed-size, recursive, semantic), embeddings, vector databases (HNSW, LSH), cosine similarity, Euclidean distance, dot product, RAG pipeline |
| **3 — Agentic Workflows** | Agents, tools, AgentFlow V2, multi-agent triage, prompt chaining, structured JSON output, output validation, sequential/parallel workflows |
| **4 — Production Readiness** | RAG Triad, LLM-as-a-Judge, BLEU, BERTScore, RAGAS, DeepEval, TruLens, Docker, GKE, Cloud Run, prompt injection, jailbreaking, data leakage, bias & fairness, responsible deployment |

---

*LADP Essentials — AI Singapore*
