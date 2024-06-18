import torch
from torch.utils.data import DataLoader, Dataset
from transformers import BertForQuestionAnswering, TrainingArguments, Trainer

# Load preprocessed data
encoding = torch.load('../data/encoded_data.pt')

# Define dataset class
class QADataset(Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        return {key: val[idx] for key, val in self.encodings.items()}

    def __len__(self):
        return len(self.encodings['input_ids'])

# Initialize dataset and dataloader
dataset = QADataset(encoding)
dataloader = DataLoader(dataset, batch_size=2, shuffle=True)

# Load pre-trained BERT model
model = BertForQuestionAnswering.from_pretrained('bert-base-uncased')

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=1,
    per_device_train_batch_size=2,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained('./model')
