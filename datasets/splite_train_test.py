import random
import os
import shutil

# 划分训练集测试集
def split_dataset(data_dir, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1):
    # 检查比例之和是否为 1
    assert train_ratio + val_ratio + test_ratio == 1, "The sum of ratios must be 1"
    image_dir = os.path.join(data_dir, 'images')
    label_dir = os.path.join(data_dir, 'labels')
    train_image_dir = os.path.join(data_dir, 'images/train')
    val_image_dir = os.path.join(data_dir, 'images/val')
    test_image_dir = os.path.join(data_dir, 'images/test')
    train_label_dir = os.path.join(data_dir, 'labels/train')
    val_label_dir = os.path.join(data_dir, 'labels/val')
    test_label_dir = os.path.join(data_dir, 'labels/test')

    # 创建目录
    os.makedirs(train_image_dir, exist_ok=True)
    os.makedirs(val_image_dir, exist_ok=True)
    os.makedirs(test_image_dir, exist_ok=True)
    os.makedirs(train_label_dir, exist_ok=True)
    os.makedirs(val_label_dir, exist_ok=True)
    os.makedirs(test_label_dir, exist_ok=True)

    image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    random.shuffle(image_files)

    num_images = len(image_files)
    num_train = int(num_images * train_ratio)
    num_val = int(num_images * val_ratio)
    num_test = num_images - num_train - num_val

    train_files = image_files[:num_train]
    val_files = image_files[num_train:num_train + num_val]
    test_files = image_files[num_train + num_val:]

    def copy_files(files, src_image_dir, src_label_dir, dst_image_dir, dst_label_dir):
        for file in files:
            base_name = os.path.splitext(file)[0]
            image_file = base_name + '.jpg'
            label_file = base_name + '.txt'
            shutil.copy(os.path.join(src_image_dir, image_file), os.path.join(dst_image_dir, image_file))
            shutil.copy(os.path.join(src_label_dir, label_file), os.path.join(dst_label_dir, label_file))

    copy_files(train_files, image_dir, label_dir, train_image_dir, train_label_dir)
    copy_files(val_files, image_dir, label_dir, val_image_dir, val_label_dir)
    copy_files(test_files, image_dir, label_dir, test_image_dir, test_label_dir)


if __name__ == "__main__":
    # 请将此目录修改为你的数据所在目录
    data_dir = r'D:\PythonProject\DataSets\invoice'
    split_dataset(data_dir)