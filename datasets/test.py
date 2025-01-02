import os
import torch
torch.cuda.empty_cache()


train_labels_dir = 'D:/PycharmProjects/DataSets/invoice/labels/train'
val_labels_dir = 'D:/PycharmProjects/DataSets/invoice/labels/val'

def check_labels(labels_dir):
    for filename in os.listdir(labels_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(labels_dir, filename), "r") as file:
                lines = file.readlines()
                for line in lines:
                    class_id = int(line.split()[0])
                    if class_id >= 8:  # 检查是否有类别超出范围
                        print(f"Invalid class {class_id} in file {filename}")

# 检查训练集和验证集标签
# check_labels(train_labels_dir)
# check_labels(val_labels_dir)
