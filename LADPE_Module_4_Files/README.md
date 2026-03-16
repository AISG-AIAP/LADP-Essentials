# Module 4: Evaluations, Deployment, and Responsible AI

Reference materials for Module 4 — covering RAG evaluation, deployment strategies, security, bias, and responsible AI practices.

---

## 4.1 Evaluations

### Key Concepts
- **RAG Triad** (by TruEra): Context Relevance, Groundedness (Faithfulness), Answer Relevance
- **LLM-as-a-Judge** — using one LLM to evaluate another LLM's outputs with scoring rubrics
- **Statistical Metrics**: BLEU (n-gram precision), ROUGE (recall-oriented), CHRF (character n-gram F-score)
- **Hybrid Metrics**: BERTScore (contextual embedding similarity)
- **Evaluation Frameworks**: RAGAS, DeepEval, LangSmith, Langfuse, TruLens, OpenAI Evals

### Links from Slides
- [TruLens — RAG Triad](https://www.trulens.org/getting_started/core_concepts/rag_triad/) — Explanation of the RAG evaluation triad
- [BERTScore GitHub Repository](https://github.com/Tiiiger/bert_score) — Implementation and documentation
- [Confident AI — LLM Evaluation Metrics Guide](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation) — Comprehensive overview of evaluation metrics

### Further Reading
- [RAGAS Documentation](https://docs.ragas.io/) — Open-source framework for RAG evaluation
- [DeepEval Documentation](https://docs.confident-ai.com/) — LLM evaluation framework with built-in metrics
- [Langfuse](https://langfuse.com/) — Open-source LLM observability and evaluation platform
- [LangSmith](https://docs.smith.langchain.com/) — LangChain's platform for tracing, testing, and evaluating LLM apps
- [Zheng et al. — Judging LLM-as-a-Judge (2023)](https://arxiv.org/abs/2306.05685) — Research paper on using LLMs as evaluators
- [Papineni et al. — BLEU: A Method for Automatic Evaluation (2002)](https://aclanthology.org/P02-1040/) — The original BLEU paper
- [Ketan Doshi - Foundations of NLP Explained – Bleu Score and WER Metrics](https://towardsdatascience.com/foundations-of-nlp-explained-bleu-score-and-wer-metrics-1a5ba06d812b/) - Explanation of Bleu Score and WER Metrics

---

## 4.2 & 4.3 Deployment

### Key Concepts
- **Local development** — Flowise runs on localhost, accessible only to local users
- **Network tunnelling** — services that create public URLs to expose local applications (used in demos with Google Colab)
- **Cloud deployment** — both the client-facing app and backend (e.g., Flowise) need public endpoints for production use

### Further Reading
- [Flowise — Deployment Guide](https://docs.flowiseai.com/configuration/deployment) — Options for deploying Flowise to various cloud platforms
- [Google Cloud Run](https://cloud.google.com/run/docs) — Serverless container deployment
- [Railway](https://railway.app/) — Simple cloud platform for deploying apps (supports Flowise)
- [Render](https://render.com/) — Cloud platform with free tier for deploying web services
- [Localtunnel GitHub](https://github.com/localtunnel/localtunnel) - GitHub repo for localtunnel
- [Pinggy - Localtunnel - Easiest way to create a local tunnel](https://pinggy.io/blog/local_tunnel/) - Blog on localtunnel
- [Streamlit Documentation](https://docs.streamlit.io/) - Guide on Streamlit Documentation
- [Docker Desktop Manuals](https://docs.docker.com/desktop/) - Guide on Docker Desktop Installation

---

## 4.4 Security, Bias & Responsible AI

### Key Concepts

#### Security
- **LLM Risk Categories**: Control Risk, Data Risk, Action Risk
- **Prompt Injection** — direct (user crafts malicious input) and indirect (injected via retrieved content)
- **Jailbreaking Techniques**: DAN method, character roleplay, grandmother exploit, few-shot jailbreaking, token smuggling, translation transitions, style injection
- **Data Leakage** — unintended exposure of PII, API keys, or proprietary data
- **Mitigations**: input filtering, system prompt hardening, output filtering, separation of concerns, tool permissions, memory isolation, adversarial testing/red-teaming

#### Bias & Fairness
- **Sources of Bias**: training data historical bias, representation gaps, feedback loop amplification
- **Bias Types**: gender, racial/ethnic, age, socioeconomic, ability/disability, language/dialect
- **Fairness Definitions**: Demographic Parity, Equalised Odds, Equal Opportunity
- **Testing**: diverse test prompts across dimensions, evaluation rubrics, scorecards

#### Responsible Deployment
- **Human oversight levels**: Human-in-the-Loop, Human-on-the-Loop, Human-out-of-the-Loop
- **ISO Standards**: ISO 42001, ISO 23894, ISO 25059, ISO 5259-1, ISO 22989, ISO/TR 29119-11

### Links from Slides

**Data Privacy Policies:**
- [OpenAI Enterprise Privacy](https://openai.com/enterprise-privacy/)
- [OpenAI Privacy Policy](https://openai.com/en-GB/policies/privacy-policy/)
- [OpenAI — How Your Data Is Used](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)
- [OpenAI ChatGPT Enterprise](https://chatgpt.com/en-GB/business/enterprise?openaicom_referred=true)
- [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy)
- [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms)
- [Microsoft Azure — OpenAI Data Privacy](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/data-privacy?tabs=azure-portal)

**ISO Standards:**
- [ISO 42001 — AI Management System](https://www.iso.org/standard/42001)
- [ISO 23894 — AI Risk Management](https://www.iso.org/standard/77304.html)
- [ISO 25059 — AI System Quality](https://www.iso.org/standard/80655.html)
- [ISO 5259-1 — Data Quality for AI](https://www.iso.org/standard/81088.html)
- [ISO 22989 — AI Concepts and Terminology](https://www.iso.org/standard/74296.html)
- [ISO/TR 29119-11 — AI Testing](https://www.iso.org/obp/ui/en/#iso:std:iso-iec:tr:29119:-11:ed-1:v1:en)

**Governance & Ethics:**
- [Singapore Launches Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai) — Press release on Launch of Singapore's framework for agentic AI governance
- [IMDA — Model AI Governance Framework for Agentic AI](https://www.imda.gov.sg/about-imda/emerging-technologies-and-research/artificial-intelligence#Model-AI-Governance-Framework-for-Agentic-AI) — Singapore's framework for agentic AI governance
- [AI Singapore — AI Ethics & Governance Course](https://learn.aisingapore.org/courses/ai-ethics-governance/) — Free course on AI ethics
- [Ayo O Agbeja - Human-in, on, and out-of-the-Loop (Medium)](https://medium.com/@Ayo.ore/human-in-on-and-out-of-the-loop-designing-the-right-role-for-people-in-ai-systems-ce2f51e675fc) - Write up on the three roles of humans in AI Systems

### Further Reading
- [OWASP — Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) — Industry-standard LLM security risks and mitigations
- [Simon Willison — Prompt Injection Explained](https://simonwillison.net/2023/Apr/14/worst-that-can-happen/) — Accessible overview of prompt injection attacks
- [Ken Huang - Key differences between prompt injection and jailbreaking](https://kenhuangus.medium.com/key-differences-between-prompt-injection-and-jailbreaking-d397cffbe812) - Differences between prompt injection and jailbreaking
- [United States Cybersecurity Institute - What are LLM Security Risks and Mitigation Plan for 2026](https://www.uscsinstitute.org/cybersecurity-insights/blog/what-are-llm-security-risks-and-mitigation-plan-for-2026) - Overview of LLM Security Risks and Mitigation Plan
- [Claude's Constitution](https://www.anthropic.com/constitution) — A detailed description of Anthropic's vision for Claude's values and behavior
- [Google — Responsible AI Practices](https://ai.google/responsibility/responsible-ai-practices/) — Google's guidelines for responsible AI development
- [AI Verify Foundation](https://aiverifyfoundation.sg/) — Singapore's AI governance testing framework and toolkit