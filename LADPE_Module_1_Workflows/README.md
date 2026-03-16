# Module 1: Foundations of LLM Applications

Reference materials for Module 1 — covering tokenization, LLM communication basics, and prompt engineering.

---

## 1.1 Foundations and Tokenization

### Key Concepts
- **Tokenization** — the process of breaking text into smaller units (tokens) that LLMs can process
- **Subword tokenization** (e.g., Byte Pair Encoding) is the standard approach used by modern LLMs, balancing vocabulary size with handling of rare words
- **Vocab sizes**: GPT-2 (50,257), GPT-4 (100,256), GPT-4o (199,997)

### Links from Slides
- [Tiktokenizer — Interactive BPE Tokenizer Demo](https://tiktokenizer.vercel.app/?model=o200k_base) — Try tokenization live in your browser

### Further Reading
- [OpenAI Tokenizer Tool](https://platform.openai.com/tokenizer) — Official OpenAI tokenizer playground
- [Hugging Face — Summary of Tokenizers](https://huggingface.co/docs/transformers/tokenizer_summary) — Covers BPE, WordPiece, SentencePiece, and Unigram
- [tiktoken GitHub Repository](https://github.com/openai/tiktoken) — OpenAI's open-source BPE tokenizer library (Python)
- [Andrej Karpathy — Let's Build the GPT Tokenizer (Video)](https://www.youtube.com/watch?v=zduSFxRajkE) — Deep walkthrough of BPE tokenizer implementation
- [Sebastian Raschka - Implementing A Byte Pair Encoding (BPE) Tokenizer From Scratch](https://sebastianraschka.com/blog/2025/bpe-from-scratch.html) - A standalone notebook implementing the popular byte pair encoding (BPE) tokenization algorithm from scratch
- [The Unicode Standard](https://home.unicode.org/) — Background on Unicode and UTF-8 encoding referenced in BPE

---

## 1.2 LLM Communication Basics

### Key Concepts
- **Message types**: User Message, System Message, Assistant Message
- **System Message** — the most important prompt; it shapes the LLM's behaviour for your application
- **Context Window** — the maximum number of tokens an LLM can process at once
- **Lost-in-the-Middle** — LLMs tend to pay less attention to information in the middle of long contexts
- **Context management strategies**: Full History, Selective History, Compressed History, Hybrid/Progressive Summarization

### Further Reading
- [Hugging Face — Messages and Special Tokens](https://huggingface.co/learn/agents-course/en/unit1/messages-and-special-tokens) — Part of Hugging Face's agents course that covers message roles
- [PromptHub - The Difference Between System Messages and User Messages in Prompt Engineering](https://www.prompthub.us/blog/the-difference-between-system-messages-and-user-messages-in-prompt-engineering) — Covers the difference between system messages and user messages in Prompt Engineering
- [Liu et al. — Lost in the Middle (2023)](https://arxiv.org/abs/2307.03172) — The research paper behind the Lost-in-the-Middle finding
- [Agenta — Top techniques to Manage Context Lengths in LLMs](https://agenta.ai/blog/top-6-techniques-to-manage-context-length-in-llms) — Cover several techniques to overcome LLM token limits

---

## 1.3 Prompt Engineering

### Key Concepts
- **Zero-Shot Prompting** — task instructions only, no examples
- **Few-Shot Prompting** — providing input-output examples to guide the model
- **Chain-of-Thought (CoT)** — breaking problems into reasoning steps to improve accuracy
- **Prompt Chaining** — connecting multiple prompts sequentially (output of one becomes input of next)
- **Structured Outputs** — getting LLMs to return data in formats like JSON for integration with other systems
- **JSON Validation** — schema, type, value, and business logic validation of structured outputs

### Further Reading
- [Anthropic — Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — Comprehensive guide covering all major techniques
- [OpenAI — Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering) — Practical tips with examples
- [OpenAI — Best practices for prompt engineering with the OpenAI API](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api) - How to give clear and effective instructions to OpenAI models
- [Google — Prompt Engineering Guide](https://ai.google.dev/gemini-api/docs/prompting-strategies) — Gemini-focused but broadly applicable techniques
- [Wei et al. — Chain-of-Thought Prompting (2022)](https://arxiv.org/abs/2201.11903) — Original CoT research paper
- [OpenAI — Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs) — Guide to getting reliable JSON from LLMs
- [Anthropic — Tool Use for Structured Output](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#json-mode) — Using tool definitions to enforce output schemas
- [Humanloop - Structured Outputs: Everything You Should Know](https://humanloop.com/blog/structured-outputs) - Guide on structured outputs
