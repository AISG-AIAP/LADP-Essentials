# LADP Essentials — Phase 2: Capstone Project

## Overview

In this capstone project, you will build a working LLM application on **Flowise** using either a **RAG (Retrieval Augmented Generation)** pipeline or an **Agentic Workflow** — applying the concepts you learned in Modules 1–4.

Choose **one** of the 7 scenarios below. Each scenario uses a publicly available knowledge base document — download the document you need from the source links below.

> **Important:** Do NOT redistribute these documents. Download them directly from the original sources for your own use in this project.

---

## Knowledge Base Documents

Download the document for your chosen scenario from the original source:

| # | Document | Download Link |
|---|----------|---------------|
| 1 | STF HR Policy | [stf.sg](https://www.stf.sg/wp-content/uploads/2022/08/STF-HR-Policy.pdf) |
| 2 | Singapore Investment Climate Statement (2025) | [state.gov](https://www.state.gov/wp-content/uploads/2025/09/638719_2025-Singapore-Investment-Climate-Statement.pdf) |
| 3 | Contoso Employee Handbook | [developerscantina.com](https://www.developerscantina.com/p/kernel-memory/employee_handbook.pdf) |
| 4 | Sample Purchasing Policy (Town of Middletown, DE) | [evogov.s3.amazonaws.com](https://evogov.s3.amazonaws.com/126/media/167512.pdf) |
| 5 | Singapore's Transformation into a Global Financial Hub | [lkyspp.nus.edu.sg](https://lkyspp.nus.edu.sg/docs/default-source/case-studies/entry-1516-singapores_transformation_into_a_global_financial_hub.pdf?sfvrsn=a8c9960b_2) |
| 6 | Kopi Culture, Consumption, Conservatism | [academia.edu](https://www.academia.edu/79668210/Kopi_culture_consumption_conservatism_and_cosmopolitanism_among_Singapore_s_millennials) |
| 7 | AI/ML Learning Resources (CSV) | [Download from GitHub repo](https://github.com/AISG-AIAP/LADP-Essentials/blob/main/LADPE_Module_2_Workflows/documents_for_rag/aiml-learning-resources.csv) |

---

## How to Share Your Work

You don't have direct write access to this repository, so you'll share your work by submitting a **Pull Request (PR)** from your own GitHub fork. Your contribution will go into the `contributions_from_learners/` folder inside `LADPE_Project_Phase/`.

If you've never submitted a PR before, don't worry — follow the steps below in order.

### Prerequisites

- A free [GitHub account](https://github.com/signup)
- [Git installed](https://git-scm.com/downloads) on your computer
- A terminal (Terminal on macOS/Linux, Git Bash or PowerShell on Windows)
- Tell Git who you are (one-time setup):
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your-email@example.com"
  ```

### Step 1 — Fork the repository

A "fork" is your own personal copy of the repo on GitHub.

1. Go to the repository on GitHub: **https://github.com/AISG-AIAP/LADP-Essentials**
2. Click the **Fork** button in the top-right corner
3. On the next page, leave the defaults and click **Create fork**
4. You'll be redirected to your fork at `https://github.com/<your-github-username>/LADP-Essentials`

### Step 2 — Clone your fork to your computer

1. On your fork's page, click the green **Code** button → **HTTPS** tab → copy the URL
2. In your terminal, navigate to where you want the project to live, then run:
   ```bash
   git clone https://github.com/<your-github-username>/LADP-Essentials.git
   cd LADP-Essentials
   ```
   Replace `<your-github-username>` with your actual GitHub username.

### Step 3 — Create a new branch

Working on a separate branch keeps your changes isolated and is required for a clean PR.

```bash
git checkout -b add-<your_name>-contribution
```

Example: `git checkout -b add-alice-tan-contribution`

### Step 4 — Add your contribution folder

1. Navigate to `LADPE_Project_Phase/contributions_from_learners/`
2. Create a new folder named after yourself, using lowercase with underscores (e.g., `alice_tan/`)
3. Place the following two files inside your folder:

   **a. Exported Flowise Workflow JSON**
   - Export your completed workflow from Flowise (`Chatflow/Agentflow > Settings > Export`)
   - Filename: `<your_name>_scenario_<number>.json`
   - Example: `alice_tan_scenario_3.json`

   **b. A short write-up (`README.md`)**

   A markdown file (1 page max) explaining your workflow, covering:
   - Which scenario you chose and why
   - Your design decisions (e.g., chunking strategy, model choice, prompt design)
   - Any challenges faced and how you resolved them
   - Screenshots of your workflow canvas and at least 3 sample conversations

**Example folder structure:**

```
LADPE_Project_Phase/
└── contributions_from_learners/
    └── alice_tan/
        ├── alice_tan_scenario_3.json
        └── README.md
```

### Step 5 — Commit your changes

Stage and commit only your own folder:

```bash
git add LADPE_Project_Phase/contributions_from_learners/<your_name>/
git commit -m "Add <your_name> capstone contribution (scenario <number>)"
```

Verify your commit:
```bash
git status        # should show "nothing to commit, working tree clean"
git log -1        # should show your commit message
```

### Step 6 — Push your branch to your fork

```bash
git push origin add-<your_name>-contribution
```

If prompted, log in to GitHub (use a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) as the password if HTTPS asks).

### Step 7 — Open the Pull Request

1. Go to your fork on GitHub: `https://github.com/<your-github-username>/LADP-Essentials`
2. You should see a yellow banner saying *"add-<your_name>-contribution had recent pushes"* with a **Compare & pull request** button — click it
   - If you don't see the banner, click the **Pull requests** tab → **New pull request**
3. On the "Open a pull request" page, confirm these settings:
   - **base repository:** `AISG-AIAP/LADP-Essentials`
   - **base:** `main`
   - **head repository:** `<your-github-username>/LADP-Essentials`
   - **compare:** `add-<your_name>-contribution`
4. Set the PR **title**: `Add <your_name> capstone contribution (scenario <number>)`
5. In the PR **description**, include:
   - Your name
   - Which scenario you chose
   - One or two sentences about your approach
6. Click **Create pull request**

### Step 8 — Wait for review

Your instructor will review your PR. You may be asked to make changes — if so:

1. Make the requested edits locally on the same branch
2. Commit and push again:
   ```bash
   git add <changed-files>
   git commit -m "Address review feedback"
   git push origin add-<your_name>-contribution
   ```
3. Your PR will update automatically — no need to open a new one

Once approved, your instructor will merge the PR and your contribution will appear in the main repository. 🎉

### Troubleshooting

- **"Permission denied" when pushing** — make sure you cloned *your fork* (under your username), not the original `AISG-AIAP` repo
- **PR shows files you didn't change** — your branch may be behind `main`. Run `git fetch upstream && git rebase upstream/main` (after adding the original repo as `upstream` with `git remote add upstream https://github.com/AISG-AIAP/LADP-Essentials.git`)
- **Forgot to create a branch and committed to `main`** — create a new branch from your current state with `git checkout -b add-<your_name>-contribution`, then push that branch

---

## Scenarios

### Scenario 1 — HR Policy Q&A Assistant (RAG)
**Document:** STF HR Policy — [Download from stf.sg](https://www.stf.sg/wp-content/uploads/2022/08/STF-HR-Policy.pdf)

**Context:** The Singapore Taekwondo Federation (STF) wants to build an internal chatbot so employees can quickly find answers about HR policies — leave entitlements, medical benefits, resignation procedures, recruitment processes, and more.

**Your Task:**
- Build a **RAG Chatflow** that ingests the STF HR Policy PDF
- The chatbot should accurately answer specific factual questions such as:
  - "How many days of annual leave does a Manager get?"
  - "What is the medical subsidy cap per year?"
  - "What is the notice period for an Executive who resigns?"
  - "Who sits on the interview panel for a Coach-level hire?"
  - "Can employees carry forward annual leave? What is the limit?"
- Design an appropriate **system prompt** that instructs the LLM to answer only from the provided context and to say "I don't have this information in the HR policy" when the answer is not in the document
- Choose an appropriate **chunking strategy** and **chunk size** for a policy document with numbered sections

**Evaluation Criteria:**
- Accurate retrieval and factual answers from the HR policy
- The bot should NOT hallucinate information not in the document
- Proper handling of out-of-scope questions

---

### Scenario 2 — Investment Climate Research Agent (Agentic)
**Document:** Singapore Investment Climate Statement (2025) — [Download from state.gov](https://www.state.gov/wp-content/uploads/2025/09/638719_2025-Singapore-Investment-Climate-Statement.pdf)

**Context:** A consulting firm advises foreign companies looking to invest in Singapore. They need an AI agent that can answer complex, multi-faceted questions about Singapore's investment environment by reasoning over a detailed 64-page government report.

**Your Task:**
- Build an **Agentic Workflow (Agentflow)** that:
  1. Takes a user's investment query
  2. Uses a **RAG tool** to retrieve relevant sections from the Investment Climate Statement
  3. Has an **Analyst Agent** that synthesises retrieved information and provides structured analysis
  4. Outputs a well-formatted response with relevant facts, regulations, and recommendations
- The agent should handle complex queries that may require information from multiple sections, such as:
  - "What are the key regulatory requirements for a U.S. fintech company wanting to set up operations in Singapore?"
  - "Compare the Employment Pass and S Pass requirements, including minimum salaries"
  - "What protections exist for foreign investors regarding intellectual property and dispute resolution?"
- Include proper **system prompts** that instruct the agent to cite specific sections/facts from the document

**Evaluation Criteria:**
- Multi-step reasoning across different sections of the document
- Structured, well-organised output
- Proper use of RAG tool within the agentic workflow
- Factual accuracy with citations

---

### Scenario 3 — Employee Onboarding Assistant (RAG)
**Document:** Contoso Employee Handbook — [Download from developerscantina.com](https://www.developerscantina.com/p/kernel-memory/employee_handbook.pdf)

**Context:** Contoso Electronics, a leading aerospace company, wants a chatbot for new hires to quickly find information about company policies, values, safety procedures, and reporting channels during their onboarding.

**Your Task:**
- Build a **RAG Chatflow** that ingests the Contoso Employee Handbook
- The chatbot should accurately answer questions such as:
  - "What are Contoso's core values?"
  - "How do I report a whistleblower concern? What channels are available?"
  - "What is the Compliance Hotline number?"
  - "What does the workplace safety program include?"
  - "What data security requirements must I follow as an employee?"
  - "How often are performance reviews conducted?"
- Design a **friendly, welcoming system prompt** appropriate for onboarding new employees
- The bot should handle follow-up questions in a conversational manner

**Evaluation Criteria:**
- Accurate answers grounded in the handbook
- Conversational and welcoming tone suitable for new hires
- Correct handling of questions about safety, privacy, and whistleblower policies
- Graceful handling of questions not covered in the handbook

---

### Scenario 4 — Procurement Compliance Checker (Agentic)
**Document:** Sample Purchasing Policy (Town of Middletown, DE) — [Download from evogov.s3.amazonaws.com](https://evogov.s3.amazonaws.com/126/media/167512.pdf)

**Context:** The Town of Middletown, Delaware wants to build an AI assistant that helps department supervisors determine the correct procurement process for their purchases — whether they need formal bidding, how many vendor quotes are required, what approval levels are needed, and what exceptions apply.

**Your Task:**
- Build an **Agentic Workflow (Agentflow)** with at least two stages:
  1. **Classification Agent** — determines the type and value of the purchase to classify which procurement path applies
  2. **Advisory Agent** — provides step-by-step guidance on the required process, approvals, and documentation based on the classification
- The system should handle queries such as:
  - "I need to purchase office supplies worth $800. What process do I follow?"
  - "We need a construction project estimated at $75,000. What are the bidding requirements?"
  - "Can I use a purchasing card for a $1,200 transaction?"
  - "Are there any exceptions for emergency purchases?"
  - "What is the retainage policy for construction contracts?"
- Each agent should have clear, focused **system prompts**

**Evaluation Criteria:**
- Correct classification of purchase type and applicable procurement path
- Accurate threshold identification ($10,000 / $50,000 boundaries)
- Clear step-by-step guidance
- Multi-agent coordination

---

### Scenario 5 — Financial History Research & Report Agent (Agentic)
**Document:** Singapore's Transformation into a Global Financial Hub — [Download from lkyspp.nus.edu.sg](https://lkyspp.nus.edu.sg/docs/default-source/case-studies/entry-1516-singapores_transformation_into_a_global_financial_hub.pdf?sfvrsn=a8c9960b_2)

**Context:** The Lee Kuan Yew School of Public Policy wants a research assistant that helps students and researchers explore Singapore's financial history. The agent should be able to answer research questions and generate mini-reports on specific topics.

**Your Task:**
- Build an **Agentic Workflow (Agentflow)** with a multi-agent pipeline:
  1. **Research Agent** — retrieves relevant information from the case study using RAG
  2. **Writer Agent** — synthesises the research into a well-structured mini-report
  3. Include a **Human-in-the-Loop** step where the user can approve or request revisions to the report
- The system should handle research queries such as:
  - "Write a brief report on the establishment and role of the Monetary Authority of Singapore"
  - "Summarise Singapore's key value propositions as a financial centre"
  - "Explain the significance of the Asian Dollar Market in Singapore's development"
  - "What challenges does Singapore face in maintaining its position as a financial hub?"
- The Writer Agent should produce output with: **Summary**, **Key Findings**, and **Conclusion** sections

**Evaluation Criteria:**
- Multi-agent pipeline with clear separation of concerns
- Human-in-the-Loop implementation
- Report quality (structure, accuracy, grounded in the document)
- Proper use of loop/feedback mechanism

---

### Scenario 6 — Cultural Research Q&A Bot (RAG)
**Document:** Kopi Culture, Consumption, Conservatism and Cosmopolitanism among Singapore's Millennials — [Download from academia.edu](https://www.academia.edu/79668210/Kopi_culture_consumption_conservatism_and_cosmopolitanism_among_Singapore_s_millennials)

**Context:** The National Heritage Board of Singapore wants a chatbot that helps visitors and students learn about Singapore's unique kopi culture through an accessible Q&A interface based on an academic research paper.

**Your Task:**
- Build a **RAG Chatflow** that ingests the academic paper on kopi culture
- The chatbot should make academic content accessible to a general audience by answering questions such as:
  - "What is the difference between traditional kopi and third-wave specialty coffee?"
  - "What is a kopitiam and where does the word come from?"
  - "Why is kopi considered an important part of Singapore's cultural identity?"
  - "How do Singaporean millennials view traditional kopi vs. modern cafe culture?"
  - "What research method did the authors use for this study?"
- Design a system prompt that translates academic language into **accessible, engaging responses** for a general audience
- The bot should be able to explain that its knowledge comes from a specific academic study

**Evaluation Criteria:**
- Accurate retrieval from an academic paper (which is harder to chunk than structured policy documents)
- Ability to make academic content accessible without losing accuracy
- Proper attribution to the source study
- Handling of questions outside the paper's scope

---

### Scenario 7 — AI/ML Learning Pathway Recommender (Agentic)
**Document:** AI/ML Learning Resources (CSV) — [Download from GitHub repo](https://github.com/AISG-AIAP/LADP-Essentials/blob/main/LADPE_Module_2_Workflows/documents_for_rag/aiml-learning-resources.csv)

**Context:** AI Singapore wants an intelligent learning advisor that recommends personalised AI/ML learning resources to users based on their experience level, interests, and learning goals.

**Your Task:**
- Build an **Agentic Workflow (Agentflow)** with at least two stages:
  1. **Assessment Agent** — asks the user about their background (programming experience, ML knowledge, learning goals) and classifies their level (beginner / intermediate / advanced)
  2. **Recommendation Agent** — uses RAG over the CSV of learning resources to recommend a personalised learning pathway of 3–5 resources with explanations for why each resource is relevant
- The system should handle interactions such as:
  - "I'm a complete beginner with no programming experience. Where should I start?"
  - "I know Python well but have never done ML. What should I learn next?"
  - "I want to learn about AI ethics and governance. What resources do you have?"
  - "I'm interested in deep learning. What's the best learning path?"
- The Recommendation Agent should output a **structured learning pathway** (ordered list with resource name, type, link, and a short explanation of why it's recommended)

**Evaluation Criteria:**
- Effective user assessment and level classification
- Personalised recommendations (not one-size-fits-all)
- Recommendations grounded in the actual CSV data (correct titles, links, descriptions)
- Clear, structured output format

---

## General Requirements (All Scenarios)

1. **Model**: Use any LLM available in Flowise (e.g., OpenAI GPT-4o-mini, Azure OpenAI, etc.)
2. **Embeddings**: Use an appropriate embedding model for RAG scenarios
3. **Vector Store**: Use any vector store supported by Flowise (e.g., In-Memory, Chroma, Pinecone, etc.)
4. **System Prompt**: Every LLM/Agent node must have a well-crafted system prompt
5. **Testing**: Test your workflow with at least 5 different queries before submission
6. **Export**: Place the exported JSON file from Flowise into your folder under `contributions_from_learners/` (see "How to Share Your Work" above)

## Grading Rubric

| Criteria | Weight | Description |
|----------|--------|-------------|
| **Workflow Structure** | 25% | Correct node types, proper connections, complete pipeline |
| **Prompt Design** | 25% | Clear system prompts, proper instructions, role definition |
| **Retrieval Quality** | 25% | Appropriate chunking, relevant document retrieval, grounded answers |
| **Functional Correctness** | 25% | The workflow produces accurate, relevant answers to test queries |

---

## Document Sources & Attribution

The knowledge base documents used in this project are sourced from publicly available materials. They are used here strictly for **non-commercial educational purposes** as part of the LADP Essentials programme. Documents are not redistributed — learners download them directly from the original sources.

| # | Document | Author / Publisher | Year | Notes |
|---|----------|--------------------|------|-------|
| 1 | STF HR Policy (Version 6) | Singapore Taekwondo Federation (STF) | 2022 | Publicly available on [stf.sg](https://www.stf.sg) |
| 2 | Singapore Investment Climate Statement | U.S. Department of State | 2025 | U.S. federal government work — public domain under [17 U.S.C. §105](https://www.law.cornell.edu/uscode/text/17/105) |
| 3 | Contoso Electronics Employee Handbook | Microsoft Corporation | 2023 | Fictitious demo document created using Azure OpenAI for demonstration purposes |
| 4 | Sample Purchasing Policy (Policy 1.3.1) | Town of Middletown, Delaware | 2009 | Municipal government public record |
| 5 | Singapore's Transformation into a Global Financial Hub | Woo Jun Jie, Lee Kuan Yew School of Public Policy, NUS | 2017 | Academic case study, accessed via [lkyspp.nus.edu.sg](https://lkyspp.nus.edu.sg) |
| 6 | Kopi Culture, Consumption, Conservatism and Cosmopolitanism among Singapore's Millennials | Cheryl Chang & Ian McGonigle, *Asian Anthropology* (Routledge / Taylor & Francis) | 2020 | Peer-reviewed journal article, accessed via the authors' [Academia.edu page](https://www.academia.edu/79668210/) |
| 7 | AI/ML Learning Resources | Curated for LADP Essentials | 2025 | Links to publicly available courses, tutorials, and ebooks |

If you use any of these documents beyond this course, please cite the original authors and publishers appropriately.
