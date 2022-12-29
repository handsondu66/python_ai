# opencv包
import numpy as np
import cv2
# # 加载本地图像
# img = cv2.imread("./1.jpg")
# # print(img, type(img), img.shape)
# # 把彩图转化成灰度图
# img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# # 更改图片的大小
# img_resize = cv2.resize(img_gray, dsize=(200, 200))
# # 显示图像
# cv2.imshow("src", img)
# cv2.imshow("gray", img_gray)
# cv2.imshow("resize", img_resize)
# # 等待任意按键
# cv2.waitKey(0)
# # 销毁所有窗口
# cv2.destroyAllWindows()

# 打开本地摄像头
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("摄像头打开失败")
    exit(0)
while True:
    # 读取一帧图像
    ret, frame = cap.read()
    if not ret:
        print("读取图像失败")
        break
    # 显示图像
    cv2.imshow("IMG", frame)
    # 暂停并获取按键
    key = cv2.waitKey(30) & 0xff
    if 27 == key:    # 判断按键是否是esc键
        break

# 释放摄像头
cap.release()
cv2.destroyAllWindows()