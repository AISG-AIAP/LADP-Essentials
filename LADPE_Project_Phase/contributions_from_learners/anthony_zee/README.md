# Anthony Zee — Capstone Contribution (Scenario 7)

**Contributor:** Anthony Zee (`zeekiankok92@gmail.com`)  
**Workflow export:** `anthony_zee_scenario_7.json`  
**Platform:** Flowise Agentflow (Assessment Agent → Document Store Retriever → Recommendation Agent)  
**Scenario:** Scenario 7 — AI/ML Learning Pathway Recommender (AGENTIC / lifelong learning)

## Why this scenario

Chose Scenario 7 because lifelong learning in AI/ML is noisy: the same Coursera playlist is wrong for a complete beginner and for someone who already knows Python. An **agentic** split — assess level first, then RAG over a curated resource CSV — mirrors how a good learning advisor works and matches Capstone’s multi-stage Agentflow requirement (Assessment + Recommendation with RAG).

## Design decisions

- **Architecture:** Start → **Assessment Agent** (LLM) → **AI/ML Learning Resources Retriever** (Document Store RAG) → **Recommendation Agent** (LLM). Assessment classifies beginner / intermediate / advanced and writes a retrieval focus; Recommendation returns a structured pathway of **3–5** resources with Name, Type, Link, Why — grounded only in retrieved CSV rows.
- **Model:** OpenAI `gpt-4o-mini`, **temperature 0** on both LLM nodes (deterministic classification + faithful titles/links). Credentials via Flowise / `OPENAI_API_KEY` — never hardcoded.
- **Embeddings / chunking:** `text-embedding-3-small`; Recursive Character Text Splitter ~**800–1000** / overlap ~**100–150** so each CSV resource (title, type, area, description, link) stays coherent.
- **KB:** `aiml-learning-resources.csv` — course-curated public links (AISG Learn, Coursera, Google, fast.ai, docs.python.org, YouTube, ebooks). Capstone points at GitHub; the live `LADPE_Project_Phase/data/` folder lacked the CSV at packaging time, so the Module 2 `documents_for_rag/` copy is used for local upsert (documented in the package `knowledge_base/SOURCE.txt`). CSV is **not** shipped inside this PR folder.
- **Prompts:** Assessment never invents background and does not recommend courses; Recommendation never invents titles/URLs and must match level + goals.

## Challenges & resolutions

1. **Exported JSON does not include vector index.** After import, upsert the CSV into a Document Store, then point the Retriever at that store (replace `REPLACE_WITH_YOUR_DOCUMENT_STORE_ID:AIML_Learning_Resources_CSV`).
2. **Capstone `data/` path vs Module 2 CSV.** Documented the Module 2 raw GitHub URL and capture-time gap so reviewers know why the file is sourced from `documents_for_rag/`.
3. **One-size-fits-all risk.** Assessment must classify level before retrieval; Recommendation orders prerequisites before deep learning / ethics deep-dives and skips beginner Python when the user already knows Python.
4. **Structured pathway readability.** Used an explicit plain-text pathway template (Name / Type / Link / Why × 3–5) instead of opaque JSON-only output so chat demos stay reviewable.

## Sample conversations (illustrative of expected bot behaviour)

> Samples reflect titles present in the curated CSV. After Document Store upsert, verify wording and links against retrieved chunks. **Live Flowise screenshots pending.**

1. **Q:** I'm a complete beginner with no programming experience. Where should I start?  
   **Expected:** Level **beginner**. Pathway of 3–5 items starting with Python fundamentals and/or AISG **AI4I - Literacy in AI**, then gentle next steps — not fast.ai deep learning first. Each item: Name, Type, Link, Why.

2. **Q:** I know Python well but have never done ML. What should I learn next?  
   **Expected:** Level **intermediate**. Skip absolute-beginner Python playlists; recommend ML Crash Course / StatQuest / ISLP (or similar CSV ML rows) in a sensible order.

3. **Q:** I want to learn about AI ethics and governance. What resources do you have?  
   **Expected:** Grounded on **Practical Data Ethics** (and optionally AI4I Literacy); no invented ethics catalogues.

4. **Q:** I'm interested in deep learning. What's the best learning path?  
   **Expected:** **Practical Deep Learning for Coders** / Google ML&AI deep-learning resources from the CSV; prepend ML/Python bridges only if assessment says they are needed.

5. **Q (extra):** I'm an experienced ML practitioner who wants a short refresh on statistical learning and then ethics for production AI.  
   **Expected:** Higher level classification; prefer statistical-learning ebook(s) + Practical Data Ethics — personalised, not beginner Python.

6. **Out-of-scope:** Recommend a secret internal staff-only syllabus not in the CSV.  
   **Expected:** No invented titles/links; say nothing matching was retrieved; offer only closest public CSV items if any.

## Screenshots

> Capture after local Flowise run (requires `OPENAI_API_KEY` + Document Store upsert) and place under `screenshots/`:
>
> - `screenshots/canvas.png` — Agentflow canvas (Start → Assessment → Retriever → Recommendation)
> - `screenshots/sample_1.png` — beginner / Python-then-ML pathway
> - `screenshots/sample_2.png` — ethics & governance and/or deep learning
> - `screenshots/sample_3.png` — advanced refresh pathway and/or out-of-scope refusal

![Workflow canvas](screenshots/canvas.png)

![Sample conversation 1](screenshots/sample_1.png)

![Sample conversation 2](screenshots/sample_2.png)

![Sample conversation 3](screenshots/sample_3.png)
