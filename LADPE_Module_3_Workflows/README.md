# Module 3: Agentic Workflows

Reference materials for Module 3 — covering AI agents, tool integration, multi-agent architectures, and orchestration, plus the demo workflow files. The n8n demos are the main track; the Flowise demos are optional.

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

## 3.1.1 Demo: Building Agentic Workflows (n8n)

### Overview: Agentic Workflows in n8n
The n8n demos build agents with the **AI Agent** node, connected to chat models, memory, tools and structured output parsers.

### Demo 1: Building a Triage Agent
- [`Triaging Agent.json`](n8n_workflows/Triaging%20Agent.json) — A **Text Classifier** routes each question to a specialised agent (AI/ML learning resources, the Barbie movie, or general questions). The specialised agents use Pinecone vector stores and tools to answer
- [n8n — Text Classifier Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier/) — Routing inputs to different branches

### Demo 2: Building a Report Writing Agent
- [`Report Writing Agent.json`](n8n_workflows/Report%20Writing%20Agent.json) — A multi-agent pipeline (Research Agent > Analyst Agent > Report Writing Agent) that uses MCP tools for search and arXiv papers, writes the report to Google Docs, and asks you to approve or request changes in the chat (human-in-the-loop)
- [n8n — Chat Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat/) — Sending a message and waiting for the user's reply

### Demo 3: Connecting the Report Writing Agent to an AI Assistant
- [`Claude Report Writing Agent.json`](n8n_workflows/Claude%20Report%20Writing%20Agent.json) — The report writing agent as a sub-workflow that another workflow can call
- [`Claude MCP Server Trigger for Report Writing Agent.json`](n8n_workflows/Claude%20MCP%20Server%20Trigger%20for%20Report%20Writing%20Agent.json) — Exposes the agent as an MCP server with the **MCP Server Trigger** node, so an AI assistant such as Claude or ChatGPT can use it as a tool

#### Connecting a Custom MCP Server to Claude and ChatGPT
You can expose your own workflow as a remote MCP server (e.g., with n8n's **MCP Server Trigger** node, as in this demo) and then add it to Claude or ChatGPT. Both need a public **HTTPS** URL (a server running only on localhost won't work), and only connect servers you trust.

- **Claude (custom connector):** Customize > Connectors > **+ Add** > add custom connector > enter a name and the remote MCP server URL > set up authentication (OAuth, or an API key in request headers) > **Add**. In a chat, click **+** > Connectors to turn it on. Available on all plans (Free is limited to one custom connector); on Team/Enterprise an Owner adds it in Organization settings > Connectors first.
- **ChatGPT (custom MCP plugin):** add a custom MCP server from the **Plugins** page and acknowledge the risk warning (developer mode is no longer required). Full read/write MCP is for Business and Enterprise/Edu on ChatGPT web; Pro can connect custom servers with read/fetch permissions only.

> Menu names change often, so check the guides below for the latest steps.

- [Claude — Get Started with Custom Connectors Using Remote MCP](https://support.claude.com/en/articles/11175166) — Official steps for adding a remote MCP server to Claude
- [OpenAI — Connecting Custom MCP Servers in ChatGPT](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt-beta) — Official steps and plan availability for ChatGPT
- [n8n — MCP Server Trigger Node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/) — Expose n8n tools as an MCP server URL

### Further Reading (n8n)
- [Advanced AI in n8n](https://docs.n8n.io/advanced-ai/) — Overview of the AI Agent, chat models, memory, and tools
- [n8n — AI Agent Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/) — Node reference for building agents in n8n

---

## 3.1.2 Demo: Building an Agentic Workflow (Flowise, optional)

Optional. For learners following the Flowise track. The Flowise demos are built with Agentflow V2.

- [`LADPE_Module_3.1_demo_1 - my_triaging_agent Agents.json`](flowise_workflows/LADPE_Module_3.1_demo_1%20-%20my_triaging_agent%20Agents.json) — Triaging agent
- [`LADPE_Module_3.1_demo_2- report_writing_agent Agents.json`](flowise_workflows/LADPE_Module_3.1_demo_2-%20report_writing_agent%20Agents.json) — Report writing agent

### Further Reading (Flowise)
- [Flowise Documentation](https://docs.flowiseai.com/) — Official docs for chatflows and agentflows
- [Flowise GitHub Repository](https://github.com/FlowiseAI/Flowise) — Archived source code
- [Leon van Zyl - Flowise v3 Complete Tutorial - Build AI Agents WITHOUT Coding](https://www.youtube.com/watch?v=SLVVDUIbIBE) — Supplementary walkthrough for building agents in Flowise
- [Flowise Agentflow V2](https://docs.flowiseai.com/using-flowise/agentflowv2) — Documentation for advanced workflow orchestration in Flowise
