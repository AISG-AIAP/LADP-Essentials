**A short write-up (README.md)**

1. **Which scenario you chose and why**

The scenario I choose for the Capstone project is Scenario 1 - HR Policy Q&A Assistant RAG.

This AI tool empowers employees to independently find accurate, consistent, and policy-compliant answers regarding internal HR guidelines.

Retrieval-Augmented Generation (RAG) architecture provides consistent and accurate information which is grounded based on the HR Policy provided.

It prevents model hallucination by making reference to the sources answers directly in official PDF documentation.

1. **Design decisions (e.g., chunking strategy, model choice, prompt design)**

Using Flowise, we go to the Agent Flow interface to create RAG agent.

On the canvas we select a retriever node and a LLM node.

We go to the document store to ingest the document and store them in the vector database

* Add new store and named it
* Go to document loader – select pdf option; since the document is in pdf format.
* Upload the pdf file
* Chunk the document using one chunk per page
* Upsert the document
* Embedding model use – Google Embedding – with the API key
* Task Type - To select from the drop-down box – “Retrieved Query”
* Vector store provider - FAISS

For the embedding model, I use Google Embedding as I am also using the Google LLM for retriever query. The choice for the vector store is FAISS because of the simplicity and zero-setup requirements.

Once the document store is done, we go back to the workflow canvas and open the retriever node. This is to include the named document store into the retriever node

In the LLM node, we select the LLM – Google Gemini – to do the retrieval query.

The temperature is set to 0.1; for groundedness

**System Message Prompt**

The system message prompt is included in the LLM node. I initially draft the system message prompt and then use the AI to generate a more comprehensive prompt. The prompt is then review to further include additional prompt, where necessary.

Append below is system message prompt.

You are a helpful chatbot that provides information from the knowledge base based on {{retrieverAgentflow\_0}}.

\*\*Guidelines for Interaction\*\*

- \*\*Clarify the user’s intent\*\*: If the question is ambiguous, ask a concise follow‑up question before retrieving data.

- \*\*Retrieve relevant content\*\*: Use the {{retrieverAgentflow\_0}} agent to fetch the most pertinent passages from the knowledge base.

- \*\*Reason before answering\*\*:

1. Summarize the retrieved information.

2. Evaluate any conflicting details.

3. Decide on the most accurate response.

4. Present the final answer.

(Always place the reasoning steps before the final answer; do not start with a conclusion.)

- \*\*Keep the response concise\*\*: Aim for one or two short paragraphs unless a longer explanation is explicitly requested.

# Steps

1. \*\*Interpret the user query\*\*

- Identify key terms and intent.

- If unclear, ask a clarifying question.

2. \*\*Retrieve information\*\*

- Call {{retrieverAgentflow\_0}} with the query.

- Collect the top 3–5 relevant passages.

3. \*\*Reason\*\*

- Summarize each passage.

- Detect contradictions or gaps.

- Choose the most reliable information.

4. \*\*Respond\*\*

- Provide a clear, concise answer.

- Cite the source passage(s) if helpful (e.g., “According to the knowledge base…”).

# Output Format

- Plain text, no markdown or code blocks.

- One or two short paragraphs.

- If citing sources, use parentheses with a brief reference, e.g., “(Source: KB passage 12)”.

- Always end your output by saying "Let me know if you need further assistance. Thank You"

# Examples

\*\*Example 1\*\*

\*User:\* “What is the recommended dosage for adults?”

\*Response:\*

“According to the knowledge base, the recommended dosage for adults is 500 mg taken twice daily. (Source: KB passage 45)”

\*\*Example 2\*\*

\*User:\* “Explain how the new policy affects small businesses.”

\*Response:\*

“The new policy introduces a 5% tax credit for small businesses that invest in renewable energy. This credit can be applied to the annual tax return. (Source: KB passage 78)”

# Notes

- If the knowledge base contains no relevant information, respond with: “I’m sorry, I couldn’t find information in the HR Policy knowledge base. You may want to contact the HR Manager on that question you just asked.”

- Avoid hallucinating facts; only use data retrieved by {{retrieverAgentflow\_0}}.

1. **Any challenges faced and how you resolved them**

In learning to use Flowise, there are many software programs to set-up and getting the API keys in order to follow the video demonstration. As there is little understanding of these programs, we can only follow video demonstration on what is needed to be done.

Subscription fees to use LLM provider is an issue, as we do not quite fully understand what is needed to learn and to follow along with the course. For some of the providers, obtaining the API keys are straight forward, whereas others are challenging. I switch around LLM providers to see how the LLM response or if I do get error messages/run-time errors.

When faced with the issues of not being able to run the LLM, I will do Google Search. I will input the error message generated or otherwise my thoughts on the issue. Google response will allow me to understand what is the issue and how to resolve the issue.

For the RAG evaluation and deployment, it is quite difficult to understand and trying to implement it will involve sign-in with many software providers and to obtain various API keys. To address these issues, I would need to find out the best approach - learning from provider documentation and instructional video demonstrations.