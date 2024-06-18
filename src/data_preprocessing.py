import pandas as pd
import torch
from transformers import BertTokenizer

# Load dataset
data = pd.read_csv('../data/ssi_qa_pairs.csv')

# Initialize tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = ''.join(c for c in text if c not in ('!', '.', ':', ','))
    return text

# Preprocess dataset
data['Question'] = data['Question'].apply(preprocess_text)
data['Answer'] = data['Answer'].apply(preprocess_text)

# Tokenize dataset
questions = data['Question'].tolist()
answers = data['Answer'].tolist()
encoding = tokenizer(questions, answers, padding=True, truncation=True, return_tensors="pt")

# Save preprocessed data
torch.save(encoding, '../data/encoded_data.pt')
