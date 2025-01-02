import os
from pdf2image import convert_from_path


def convert_pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path,dpi=300)
    if len(images) == 1:
        # 如果只有 1 页，直接返回该页转换的图像
        return images[0]
    else:
        # 如果有多页，返回最后一页转换的图像
        return images[-1]


save_folder = r'D:\PythonProject\DataSets\invoice\images'
pdf_folder = r'D:\PythonProject\DataSets\pdf'


i = 1001  # 根据文件名来判断
for filename in os.listdir(pdf_folder):
    file_path = os.path.join(pdf_folder, filename)
    image = convert_pdf_to_image(file_path)
    image.save(os.path.join(save_folder, f"{str(i)}.jpg"))
    print(f"{filename}处理完成！")
    i += 1
print("处理完毕！")