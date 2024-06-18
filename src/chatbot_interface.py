import torch
from transformers import BertTokenizer, BertForQuestionAnswering

# Load fine-tuned model and tokenizer
model = BertForQuestionAnswering.from_pretrained('./model')
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Function to get answer from the model
def get_answer(question, context):
    inputs = tokenizer.encode_plus(question, context, return_tensors='pt')
    input_ids = inputs['input_ids']
    token_type_ids = inputs['token_type_ids']

    start_scores, end_scores = model(input_ids, token_type_ids=token_type_ids)
    all_tokens = tokenizer.convert_ids_to_tokens(input_ids.squeeze().tolist())
    answer = ' '.join(all_tokens[torch.argmax(start_scores): torch.argmax(end_scores)+1])
    
    return answer.replace('[CLS]', '').replace('[SEP]', '').strip()

# Context for the chatbot
context = """
Surgical Site Infections (SSIs) are infections that occur after surgery in the part of the body where the surgery took place.
SSIs are typically caused by bacteria that enter the incision site during surgery or in the days following surgery.
SSIs can be prevented by maintaining proper hygiene, using sterile equipment, and administering antibiotics before surgery.
Symptoms of SSIs include redness and swelling at the incision site, pain or tenderness, and pus or drainage from the wound.
Treatment for SSIs typically involves antibiotics and, in some cases, additional surgery to remove infected tissue.
"""

# Sample questions
questions = [
    "What are Surgical Site Infections (SSIs)?",
    "What are the common causes of SSIs?",
    "How can SSIs be prevented?",
    "What are the symptoms of SSIs?",
    "How are SSIs treated?"
]

# Print questions and their corresponding answers
for question in questions:
    answer = get_answer(question, context)
    print(f"Question: {question}")
    print(f"Answer: {answer}\n")
