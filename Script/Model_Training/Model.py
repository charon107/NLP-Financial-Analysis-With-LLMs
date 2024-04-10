import os
import torch
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer, LongT5ForConditionalGeneration
from torch.optim import AdamW
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch.cuda.amp import GradScaler, autocast
from tqdm.auto import tqdm
from torch.nn.utils import clip_grad_norm_


os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



model_name = 'google/long-t5-local-base'

tokenizer = AutoTokenizer.from_pretrained(model_name)

model = LongT5ForConditionalGeneration.from_pretrained(model_name).to(device)


class TextDataset(Dataset):
    def __init__(self, tokenizer, data_dir, labels_dir, max_length=2048, split_text=True, num_splits=8, limit=None):
        self.tokenizer = tokenizer
        self.data_dir = data_dir
        self.labels_dir = labels_dir
        self.max_length = max_length
        self.inputs = []
        self.targets = []
        self.split_text = split_text
        self.num_splits = num_splits
        
        filenames = os.listdir(data_dir)
        if limit:
            filenames = filenames[:limit]

        for filename in filenames:
            if filename.endswith('.txt'):
                file_path = os.path.join(data_dir, filename)
                labels_path = os.path.join(labels_dir, filename.replace('.txt', '_converted.txt'))
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read().strip()
                with open(labels_path, 'r', encoding='utf-8') as f:
                    label = f.read().strip()

                if self.split_text:
                    split_length = len(text) // self.num_splits
                    for i in range(self.num_splits):
                        start_idx = i * split_length
                        if i == self.num_splits - 1:  # Last split takes the remaining part of the text
                            end_idx = len(text)
                        else:
                            end_idx = (i + 1) * split_length
                        split_text = text[start_idx:end_idx]
                        self.inputs.append(split_text)
                        self.targets.append(label)
                else:
                    self.inputs.append(text)
                    self.targets.append(label)

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        input_text = self.inputs[idx]
        target_text = self.targets[idx]
        input_ids = self.tokenizer(input_text, return_tensors="pt", max_length=self.max_length, padding='max_length', truncation=True).input_ids.squeeze()
        target_ids = self.tokenizer(target_text, return_tensors="pt", max_length=self.max_length, padding='max_length', truncation=True).input_ids.squeeze()
        return {"input_ids": input_ids, "labels": target_ids}



train_data_dir = "/users/sgzli54/FYP/Dataset/Train_txt/"
train_labels_dir = "/users/sgzli54/FYP/Dataset/Train_csv_txt/"
test_data_dir = "/users/sgzli54/FYP/Dataset/Val_txt/" 
test_labels_dir = "/users/sgzli54/FYP/Dataset/Val_csv_txt/"  


train_dataset = TextDataset(tokenizer, train_data_dir, train_labels_dir, max_length=2048,limit=50)

test_dataset = TextDataset(tokenizer, test_data_dir, test_labels_dir, max_length=2048)  


train_loader = DataLoader(train_dataset, batch_size=2, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=2)  


#first_batch = next(iter(train_loader))
#
#inputs, labels = first_batch['input_ids'], first_batch['labels']
#
#print(inputs)
#print(labels)


optimizer = AdamW(model.parameters(), lr=5e-6)
scheduler = ReduceLROnPlateau(optimizer, 'min', patience=1, factor=0.5)


scaler = GradScaler() if torch.cuda.is_available() else None
best_val_loss = float('inf')

max_norm = 1.0

for epoch in range(10):
     model.train()
     train_loss = 0
     for batch in tqdm(train_loader, desc=f'Epoch {epoch+1}', leave=True):
         optimizer.zero_grad()
         inputs, labels = batch['input_ids'].to(device), batch['labels'].to(device)
         with autocast(enabled=scaler is not None):
             outputs = model(input_ids=inputs, labels=labels)
             loss = outputs.loss
         if scaler:
             scaler.scale(loss).backward()
         
             if max_norm > 0:
                 scaler.unscale_(optimizer) 
                 clip_grad_norm_(model.parameters(), max_norm)
             scaler.step(optimizer)
             scaler.update()
         else:
             loss.backward()
   
             if max_norm > 0:
                 clip_grad_norm_(model.parameters(), max_norm)
             optimizer.step()
         train_loss += loss.item()
     model.eval()
     test_loss = 0
     with torch.no_grad():
         for batch in test_loader:
             inputs, labels = batch['input_ids'].to(device), batch['labels'].to(device)
             with autocast(enabled=scaler is not None):
                 outputs = model(input_ids=inputs, labels=labels)
                 test_loss += outputs.loss.item()
     test_loss /= len(test_loader)
     if test_loss < best_val_loss:
         best_val_loss = test_loss
         torch.save(model.state_dict(), f'/users/sgzli54/FYP/Model/model_epoch_{epoch+1}.pth')
     print(f'Epoch {epoch+1}, Train Loss: {train_loss / len(train_loader)}, Test Loss: {test_loss}')