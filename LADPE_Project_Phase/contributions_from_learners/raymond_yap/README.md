# Raymond Yap — LADP Capstone Project (Scenario 4)

**Contributor:** Raymond Yap  
**Workflow export:** `raymond_yap_scenario_4.json`  
**Platform:** Flowise Agentflows

-----------------------------------------------------

## Scenario Choice

I choose Scenario 4 because this scenario is partially related to my working industry.

## Design Decision
### Agent Flow Design

User Input => Classification Agent => Advisory Agents

Classification Agent: It helps to classify 5 major types of purchasing policy sections as shown below:

1) Purchasing authority and guidelines for Materials, Supplies, Vehicles, and Capital Equipment section with purchase amount equal or less than $10,000

2) Purchasing authority and guidelines for Materials, Supplies, Vehicles, and Capital Equipment section with purchase amount more than $10,000

3) Purchasing authority and guidelines for Construction and Professional Services Contracts section with purchase amount equal or less than $50,000

4) Purchasing authority and guidelines for Construction and Professional Services Contracts section with purchase amount more than $50,000

5) Other General Policy Info

Advisory Agents: It helps to answer questions according to 5 different categories above.
Those questions out of these 5 categories will not answer. 

### Chunking Strategy
Using one page per chunk for PDF and store at Pinecone Vector DB as the lesson taught.

### Prompt Design
Using Few-shots prompting method for this case. Provide very details example is not needed. Add filtering prompt to let agent only answer question related to purchasing policy only. 

## Screenshots
There are some screenshots in the screenshots folder.
One of them is the Agent Workflow screenshots. 
The rest of them are some input examples. 
