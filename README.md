# LADP-Essentials

This repository contains the workflows and files used in the LADP-Essentials videos and demos. LADP-Essentials is a low-code/no-code course for beginners who want to build LLM applications. Demos are built in Flowise. The course covers LLM basics, prompt engineering, RAG, agents, evaluations, deployment, and more.

## Repository Structure

- `LADPE_Module_1_Workflows/`
  - Intro workflows: first chatbot and first agent
  - Prompt engineering demos: zero-shot, few-shot, chain-of-thought, and prompt chaining
- `LADPE_Module_2_Workflows/`
  - RAG workflow demo
  - `documents_for_rag/` contains sample source docs for ingestion
- `LADPE_Module_3_Workflows/`
  - Agent workflows: triaging agent and report writing agent
- `LADPE_Module_4_Files/`
  - Evaluation materials including a notebook, CSV inputs, and `.env.example`

## How to Use

1. Open Flowise.
2. Import the JSON workflows from the module folders.
3. Follow the corresponding video lessons to configure keys, data sources, and settings.
4. For evaluations (Module 4.2), use the notebook and CSV files in the `LADPE_Module_4_Files` folder and copy `.env.example` to `.env` to add your own values.

## Notes

- The JSON files are Flowise exports and can be imported directly.
- File names align with the demo names shown in the course.
- The `.env` file should not be committed to source control.
