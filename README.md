# Chatbot Project

This project involves creating a chatbot that provides information about Surgical Site Infections (SSIs) using a fine-tuned BERT model.

## Project Structure

- `data/`: Contains the dataset.
- `notebook/`: Contains the Jupyter notebook for development.
- `src/`: Contains the Python scripts for data preprocessing, model fine-tuning, and building the chatbot interface.
- `README.md`: Project documentation.
- `requirements.txt`: Project dependencies.

## How to Run

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run the scripts in the `src` directory or follow the notebook in the `notebook` directory.

## Dataset

The dataset (`ssi_qa_pairs.csv`) contains question-answer pairs related to SSIs.

## Notebook

The Jupyter notebook (`chatbot_notebook.ipynb`) demonstrates the entire process from data preprocessing to building the chatbot interface.

## Scripts

- `data_preprocessing.py`: Preprocesses the dataset.
- `fine_tune_model.py`: Fine-tunes the BERT model.
- `chatbot_interface.py`: Builds the chatbot interface.
