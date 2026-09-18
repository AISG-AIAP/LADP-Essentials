# Procurement Compliance Checker

**Learner:** Terence Goh  
**Scenario:** 4 - Sample Purchasing Policy (Town of Middletown, DE)  
**Build:** Flowise Agentflow (multi-agent) with RAG  
**Workflow file:** `terence_goh_scenario_4.json`

## Scenario chosen and why

I chose **Scenario 4** because it maps closely to work I already do. My organisation handles a lot of project management and procurement policy, and staff often need a quick, reliable way to check which process applies before they acquire something.

The Middletown purchasing policy is a good test case for that kind of assistant. The correct path depends on **what** is being bought before **how much** it costs, so the same dollar amount can map to a different process depending on the purchase category. The scenario also requires a two-stage Agentflow (classify, then advise), which matches how I would want a real staff-facing tool to behave: decide the procurement path first, then return clear operational steps.

Building this gave me a concrete pattern for an internal helper that points people at the right policy checks instead of leaving them to skim long documents on their own.

## Architecture

```
User Procurement Request
  -> Resolve Conversation Context (memory on)
  -> Purchasing Policy Retriever
  -> Classification Agent (structured output)
  -> Is Classification Complete?
       yes -> Advisory Agent -> Return Procurement Guidance
       no  -> User Information Missing?
               yes -> Request Missing Information
               no  -> Policy Information Not Found
```

The flow separates context resolution, retrieval, classification, and advice so each node has one job. Memory is enabled only on **Resolve Conversation Context**, which rewrites the latest user turn into a standalone request. That matters for follow-ups where the user only supplies a missing fact (for example an amount) without repeating the original purchase.

The retriever stores `policy_context` in flow state. Classification and Advisory run with memory off and read from that state. Advisory also receives the classification result so it can explain the path without re-doing classification.

Incomplete classification is handled explicitly: ask the user for missing facts, or stop cleanly when the retrieved policy context is not enough.

## Design decisions

### Model

Anthropic `claude-haiku-4-5` at temperature `0.1` on the resolver, classifier, and advisor. A smaller, faster model is enough for this multi-node flow, and low temperature keeps threshold language and must/may wording more consistent from run to run.

### Chunking

The PDF loader was unreliable, so the policy was converted to Markdown and loaded with a plain text document loader. After the Markdown text splitter proved unreliable, I used a Recursive Character Text Splitter with:

- chunk size `5000`
- overlap `100`
- separators `["\n## "]`

Larger section-aware chunks help keep rules from the Town of Middletown Purchasing Policy with their headings, especially neighbouring sections such as Section IV (materials, supplies, vehicles, and capital equipment) and Section V (construction and professional services). That reduces cases where a similar subheader from the wrong part of the document contaminates the retrieved context.

### Embeddings and vector store

Anthropic does not provide an embedding model, and I only had an Anthropic API key for the chat nodes. For embeddings I used the Hugging Face API with `BAAI/bge-base-en-v1.5`. Vectors are stored in Pinecone using the Nvidia-hosted `llama-text-embed-v2` configuration at **768** dimensions so the index size matches the BGE embedding output.

### Prompt design

- **Resolver:** rewrites follow-ups into a complete standalone request using conversation history only when needed, with a few short examples in the system prompt.
- **Classification:** classifies only from retrieved excerpts. It returns structured fields (category, value, path, threshold, authority, section, confidence) and a status of `CLASSIFIED`, `NEEDS_USER_INFORMATION`, or `INSUFFICIENT_POLICY_CONTEXT`.
- **Advisory:** gives step-by-step staff guidance grounded in the policy context. It is instructed to preserve obligation and boundary wording, and to end with a Policy basis line so answers stay citeable.

## Challenges and how they were resolved

### PDF ingestion

PDF loading failed in practice, which blocked the knowledge base. Converting the document to Markdown and switching to the plain text loader resolved it.

### Section bleed during chunking

In the sample purchasing policy, similar subheaders across Section IV and Section V mixed rules under the wrong path during early tests. Switching to recursive splitting with `\n## ` separators and larger chunks kept those document headings attached to the right rules.

### Memory between agents

Shared agent memory made multi-turn clarification hard to reason about, because each agent could see different parts of the chat history. Memory now stays on the resolver only. Agents receive `resolved_request` and `policy_context` through flow state, so classification and advice work from a single resolved request.

## Screenshots

- [Workflow canvas](conversations/1-workflow-canvas.png)
- [Sample 1 - Construction process by value band](conversations/2-convo-1.png)
- [Sample 2 - Purchasing card at $1,200](conversations/3-convo-2.png): card limit exceeded; routes to purchase order (Sections IV.A / VIII)
- [Sample 3 - Construction bidding at $75,000](conversations/4-convo-3.png): Section V.B sealed-bid path; off-topic / system-prompt probes refused
