## Overview
A RAG pipeline built with locally installed Flowise and Ollama to query internal HR policies for the Meridian Athletic Foundation.

## Pipeline Configuration
- LLM: ChatOllama (llama3.2)
- Embedding Model: Ollama Embedding (nomic-embed-text)
- Vector Store: In-Memory Vector Store
- Text Splitter: Recursive Character Text Splitter
  - Chunk Size: 1000
  - Chunk Overlap: 200
- System Prompt and Guardrail:
  Enforces hallucination boundary and outputs "I don't have this information in the HR policy" when information is missing from the document.

## Files Included
- HR-Bot Chatflow.json: flowise export file
- README.md: Submission details