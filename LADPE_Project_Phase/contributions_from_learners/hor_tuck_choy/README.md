# Employee Onboarding Assistant (RAG Chatbot)

## Overview

This project is a Retrieval-Augmented Generation (RAG) chatbot built using Flowise as part of the AIAP LADP Capstone Project.

The chatbot serves as an Employee Onboarding Assistant for new hires at Contoso Electronics. It provides reliable and conversational answers about company policies, values, safety procedures, reporting channels, compliance requirements, and employee responsibilities by retrieving information directly from the employee handbook.

The solution combines semantic search with a Large Language Model (LLM) to ensure responses are grounded in the company's knowledge base while maintaining a friendly onboarding experience.

## Problem Statement

New employees often need quick access to information such as:

- Company values and culture
- Workplace safety requirements
- Data privacy and security policies
- Reporting and compliance procedures
- Whistleblower channels
- Performance review processes

Instead of manually searching through lengthy documentation, employees can interact with a conversational assistant that retrieves and explains relevant information from the employee handbook.

## Solution Architecture

```text
User Question
       │
       ▼
Flowise Chatflow
       │
       ▼
Retriever Node
       │
       ▼
Pinecone Vector Store
       │
       ▼
Relevant Handbook Chunks
       │
       ▼
GPT-4o-mini
       │
       ▼
Grounded Response
```

## Technology Stack

### LLM
- OpenAI GPT-4o-mini

### Embedding Model
- OpenAI text-embedding-3-large

### Vector Store
- Pinecone

### Record Manager
- SQLite Record Manager

### Framework
- Flowise

### Retrieval Strategy
- Retrieval-Augmented Generation (RAG)

## Knowledge Base

The chatbot uses the following document as its knowledge source:

**Contoso Employee Handbook**

### Topics Covered

- Company values
- Workplace safety
- Compliance policies
- Information security
- Data privacy
- Employee conduct
- Whistleblower reporting
- Performance management
- Employee benefits
- Reporting channels

## Features

### Conversational Employee Onboarding

The assistant provides a welcoming onboarding experience and helps new employees navigate company policies and procedures.

### Retrieval-Augmented Generation (RAG)

Responses are generated using information retrieved from the employee handbook instead of relying solely on the LLM's general knowledge.

### Conversation Memory

The chatbot maintains conversational context and supports follow-up questions.

### Hallucination Protection

Guardrails were implemented to:

- Use only retrieved context
- Avoid speculation
- Avoid legal interpretation
- Prevent fabricated answers
- Return fallback responses when information is unavailable

### Policy-Aware Responses

Special handling is included for:

- Workplace Safety
- Incident Reporting
- Data Privacy
- Information Security
- Code of Conduct
- Ethics Violations
- Fraud Reporting
- Whistleblower Procedures
- Regulatory Compliance

### Welcome Experience

The chatbot provides a friendly onboarding greeting and guides new employees towards supported topics and questions.

## System Prompt Design

The chatbot is configured with a custom onboarding-focused system prompt that:

- Welcomes new employees
- Restricts responses to retrieved handbook content
- Handles follow-up questions conversationally
- Presents clear fallback responses when information is unavailable
- Applies additional safeguards for compliance and whistleblower-related questions
- Prevents hallucinations by refusing to answer unsupported questions

### Example Welcome Message

> 👋 Welcome to the Employee Onboarding Assistant!
>
> You can ask about:
>
> • Workplace Safety  
> • Data Privacy  
> • Compliance Policies  
> • Information Security  
> • Whistleblower Procedures  
> • Employee Benefits
>
> How may I assist you today?

### Example Fallback Response

> I am sorry that I don't have this information.

## Sample Questions

The chatbot can answer questions such as:

- What are Contoso's core values?
- What does the workplace safety program include?
- How do I report a whistleblower concern?
- What channels are available for reporting misconduct?
- What data security requirements must employees follow?
- How often are performance reviews conducted?
- What is the compliance hotline number?
- What employee benefits are available?

## Testing

The chatbot was tested using the following scenarios.

| Test Case | Screenshot |
|-----------|------------|
| What are Contoso's core values? | test1.png |
| How do I report a whistleblower concern? What channels are available? | test2.png |
| What is the Compliance Hotline number? | test3.png |
| What does the workplace safety program include? | test4.png |
| How do I report a whistleblower concern? | test5.png |
| What data security requirements must I follow? | test6.png |
| What are the employee benefits? | test7.png |

## Test Results Summary

✅ Successful retrieval of company values  
✅ Successful retrieval of compliance reporting information  
✅ Successful retrieval of compliance hotline information  
✅ Successful retrieval of workplace safety policies  
✅ Successful retrieval of whistleblower procedures  
✅ Successful retrieval of data security requirements  
✅ Successful retrieval of employee benefits information  
✅ Maintained context across multiple interactions  
✅ Gracefully handled unsupported queries

## Evaluation Criteria Addressed

### Accurate Answers
Responses are grounded in retrieved handbook content.

### Conversational Onboarding Experience
Provides a welcoming and user-friendly onboarding experience.

### Safety and Compliance Handling
Correctly handles workplace safety and compliance-related questions.

### Privacy and Whistleblower Policies
Properly answers questions regarding privacy, ethics, and whistleblower reporting channels.

### Graceful Fallback Behaviour
Provides clear fallback responses when requested information is unavailable.

### Follow-Up Question Support
Uses conversation memory to support contextual follow-up interactions.

## Flowise Workflow

### Main Components

1. Start Node
2. Retriever Node
3. Pinecone Vector Store
4. GPT-4o-mini LLM Node
5. Conversation Memory
6. Custom Onboarding System Prompt

### Workflow Diagram

```text
Start
  │
  ▼
Retriever
  │
  ▼
Knowledge Base
(Pinecone)
  │
  ▼
GPT-4o-mini
  │
  ▼
Response
```

The exported Flowise workflow is included in this repository:

`my_rag_onboarding_bot Agents.json`

## Repository Structure

```text
.
├── README.md
├── my_rag_onboarding_bot Agents.json
├── screenshots/
│   ├── architecture.png
│   ├── test1.png
│   ├── test2.png
│   ├── test3.png
│   ├── test4.png
│   ├── test5.png
│   ├── test6.png
│   └── test7.png
└── docs/
    └── Employee_Handbook.pdf
```

## Screenshots

### Chatflow Architecture

`screenshots/architecture.png`

### Testing Evidence

| Test | Screenshot |
|------|------------|
| Test 1 | screenshots/test1.png |
| Test 2 | screenshots/test2.png |
| Test 3 | screenshots/test3.png |
| Test 4 | screenshots/test4.png |
| Test 5 | screenshots/test5.png |
| Test 6 | screenshots/test6.png |
| Test 7 | screenshots/test7.png |


## Author

**Hor Tuck Choy**

AIAP LADP Capstone Project

## Licence

This project is created for educational and learning purposes as part of the AIAP LADP programme.

