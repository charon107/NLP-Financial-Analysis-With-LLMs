import os
import torch
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer, LongT5ForConditionalGeneration
from torch.optim import AdamW
from torch.optim.lr_scheduler import ReduceLROnPlateau
from torch.cuda.amp import GradScaler, autocast
from tqdm.auto import tqdm

# 禁用 transformers 库的并行 tokenization 警告
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# 检测是否有 CUDA 设备可用，并据此设置设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 指定预训练模型名称
model_name = 'google/long-t5-local-base'
# 加载分词器
tokenizer = AutoTokenizer.from_pretrained(model_name)
# 加载预训练模型，并将模型移动到指定的设备上
model = LongT5ForConditionalGeneration.from_pretrained(model_name).to(device)

# 定义一个 Dataset 类，用于处理文本数据
class TextDataset(Dataset):
    def __init__(self, tokenizer, data_dir, labels_dir, max_length=8192):
        self.tokenizer = tokenizer
        self.data_dir = data_dir
        self.labels_dir = labels_dir
        self.max_length = max_length
        self.inputs = []
        self.targets = []

        for filename in os.listdir(data_dir):
            if filename.endswith('.txt'):
                file_path = os.path.join(data_dir, filename)
                labels_path = os.path.join(labels_dir, filename.replace('.txt', '_converted.txt'))
                with open(file_path, 'r', encoding='utf-8') as f, open(labels_path, 'r', encoding='utf-8') as f2:
                    self.inputs.append(f.read().strip())
                    self.targets.append(f2.read().strip())

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        input_text = self.inputs[idx]
        target_text = self.targets[idx]
        input_ids = self.tokenizer(input_text, return_tensors="pt", max_length=self.max_length, padding='max_length', truncation=True).input_ids.squeeze()
        target_ids = self.tokenizer(target_text, return_tensors="pt", max_length=self.max_length, padding='max_length', truncation=True).input_ids.squeeze()
        return {"input_ids": input_ids, "labels": target_ids}

# 定义训练集和测试集的文件路径
train_data_dir = "/users/sgzli54/FYP/Dataset/Train_txt/"
train_labels_dir = "/users/sgzli54/FYP/Dataset/Train_csv_txt/"
test_data_dir = "/users/sgzli54/FYP/Dataset/Val_txt/" 
test_labels_dir = "/users/sgzli54/FYP/Dataset/Val_csv_txt/"  

# 创建训练集和测试集的 Dataset 实例
train_dataset = TextDataset(tokenizer, train_data_dir, train_labels_dir, max_length=8192)
test_dataset = TextDataset(tokenizer, test_data_dir, test_labels_dir, max_length=8192)  

# 使用 DataLoader 加载数据集
train_loader = DataLoader(train_dataset, batch_size=1, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1)  

# 定义优化器和学习率调度器
optimizer = AdamW(model.parameters(), lr=5e-5)
scheduler = ReduceLROnPlateau(optimizer, 'min', patience=1, factor=0.5)

# 如果有 CUDA 设备可用，则启用梯度缩放以支持混合精度训练
scaler = GradScaler() if torch.cuda.is_available() else None
best_val_loss = float('inf')

# 开始训练循环
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
            scaler.step(optimizer)
            scaler.update()
        else:
            loss.backward()
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
