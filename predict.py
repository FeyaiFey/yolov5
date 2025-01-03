import torch
import cv2
from datasets.image_process import resize_image,cv_show

def detect_invoice(img_path, model_path='runs/train/exp10/weights/best.pt', save_output=False):
    img = cv2.imread(img_path)
    # 加载自定义训练的模型
    model = torch.hub.load(r'D:/PythonProject/yolov5', 'custom', path=model_path, force_reload=True,source='local')

    # 预测
    results = model(img_path)

    for pred in results.pred[0]:
        x1, y1, x2, y2, conf, cls = pred  # 提取边界框坐标和置信度
        # 绘制边界框，但不显示类别标签
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
    img = resize_image(img,width=800)

    cv_show('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 显示检测结果
    # results.show()

    # 保存检测结果
    if save_output:
        results.save()  # 保存预测后的图像到 runs/detect/exp 目录

    # 打印检测框信息
    print(results.pandas().xyxy[0])  # 输出检测框坐标、类别和置信度
    return results.pandas().xyxy[0]


if __name__ == '__main__':
    # 测试一张发票
    detect_invoice(r'C:\Users\admin\Desktop\b.jpg')
