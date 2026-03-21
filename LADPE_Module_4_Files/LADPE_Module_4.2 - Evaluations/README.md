# Module 4.2 - Evaluations

This folder contains the evaluation assets used in the LADP-Essentials Module 4.2 demos. It includes a notebook for running evaluations and CSV files that provide inputs and reference answers.

## Contents

- `LADPE - Module 4.2.ipynb`  
  Notebook that walks through setting up and running an evaluation workflow.
- `Movies_Evaluation_input.csv`  
  Sample inputs used for evaluation runs.
- `Movies_Evaluation_input_n_reference.csv`  
  Inputs paired with reference outputs for comparison.
- `.env.example`  
  Template for environment variables required by the notebook.

## How to Use

1. Copy `.env.example` to `.env` and fill in your own keys and settings.
2. Open the notebook in your preferred environment. For the easiest setup, use Google Colab [![open the notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1bb5qjSoVWxkEp0ovl0U3CDoD0qVgCQZG), but a local notebook in Jupyter or VS Code works too.
3. Run the cells in order to load data, execute the evaluation, and review results.
4. Replace the CSV files with your own dataset as needed.

## Notes

- Keep your `.env` file local and do not commit it.
- The CSV headers are expected by the notebook. If you edit them, update the notebook accordingly.
- Use small datasets first to validate your setup before scaling up.
