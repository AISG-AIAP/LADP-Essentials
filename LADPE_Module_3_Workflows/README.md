# Module 3: Agentic Workflows

Reference materials for Module 3 — covering AI agents, tool integration, multi-agent architectures, and orchestration.

---

## 3.1 Agentic Workflows

### Key Concepts
- **AI Agents** — LLM-powered systems that autonomously plan, reason, and take actions to achieve goals
- **ReAct Framework** — combining Reasoning and Acting in an iterative loop (Goal > Observe > Think > Act > Reflect)
- **Tool Integration** — giving agents access to external tools (information retrieval, computation, action execution)
- **Model Context Protocol (MCP)** — Anthropic's standard for connecting LLMs to external tools and data sources
- **Multi-Agent Patterns**: Manager (centralised), Decentralised (peer handoff)
- **Orchestration**: centralised, decentralised, or hybrid coordination of multiple agents

### Links from Slides
- [Andrew Ng — What's Next for AI Agentic Workflows (Video)](https://www.youtube.com/watch?v=sal78ACtGTc) — Influential talk on the agentic AI paradigm
- [Yao et al. — ReAct: Synergizing Reasoning and Acting in Language Models (2022)](https://arxiv.org/pdf/2210.03629) — The foundational ReAct paper
- [OpenAI — A Practical Guide to Building Agents (PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) — Comprehensive guide on agent design and multi-agent patterns
- [OneReach — What is AI Agent Orchestration?](https://onereach.ai/blog/what-is-ai-agent-orchestration/) — Overview of orchestration concepts

### Further Reading
- [Anthropic — Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — Official MCP documentation and specification
- [Model Context Protocol servers - GitHub Repo](https://github.com/modelcontextprotocol/servers) - GitHub repository comprising a collection of reference implementations for the Model Context Protocol (MCP)
- [Anthropic — Tool Use with Claude](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) — How to give Claude access to tools
- [OpenAI — Function Calling](https://platform.openai.com/docs/guides/function-calling) — OpenAI's approach to tool integration
- [LangChain — Agents](https://python.langchain.com/docs/concepts/agents/) — Building agents with LangChain
- [LangGraph](https://langchain-ai.github.io/langgraph/) — Framework for building stateful, multi-agent applications
- [CrewAI](https://www.crewai.com/) — Framework for orchestrating multi-agent workflows
- [AutoGen (Microsoft)](https://github.com/microsoft/autogen) — Multi-agent conversation framework

---

## 3.2 Agentic Workflows Demo

### Key Concepts
- **Flowise** — a low-code/no-code tool for building LLM applications with a drag-and-drop interface
- **Demo 1**: Routing agent directing queries to specialised sub-agents (Course Agent, Movie Agent)
- **Demo 2**: Multi-agent report writing pipeline (Research > Analyst > Report Writer) with Human-in-the-Loop review

### Further Reading
- [Flowise Documentation](https://docs.flowiseai.com/) — Official Flowise docs for building chatflows and agentflows
- [Flowise GitHub Repository](https://github.com/FlowiseAI/Flowise) — Source code and setup instructions
- [Leon van Zyl - Flowise v3 Complete Tutorial - Build AI Agents WITHOUT Coding](https://www.youtube.com/watch?v=SLVVDUIbIBE) - Supplementary Youtube Tutorial to build AI Agents on Flowise
- [Flowise Agentflow V2](https://docs.flowiseai.com/using-flowise/agentflowv2) - Documentation for Flowise Agentflow V2
