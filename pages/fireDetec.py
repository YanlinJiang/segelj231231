import streamlit as st
import cv2
import numpy as np
from PIL import Image

def detect_flame(image):
    # 转换到HSV色彩空间
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义火焰颜色的HSV范围
    lower_flame = np.array([18, 50, 50])
    upper_flame = np.array([35, 255, 255])

    # 创建一个颜色掩码
    mask = cv2.inRange(hsv, lower_flame, upper_flame)

    # 寻找火焰区域
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 对找到的轮廓按面积大小排序，选择最大的两个
    if contours:
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]

        # 在原始图像上用矩形标记最大的两个火焰区域
        for contour in sorted_contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return image

# Streamlit 页面布局
st.title("Fire Detecting Service")

# 文件上传
uploaded_file = st.file_uploader("choose an image...", type=["jpg", "jpeg", "png"])
ex = st.button("Execute")
if ex:
    if uploaded_file is not None:
        # 将上传的文件转换为OpenCV图像格式
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        # 进行火焰检测
        result_image = detect_flame(opencv_image)

        # 将结果图像转换为PIL格式以显示在Streamlit上
        result_image_pil = Image.fromarray(result_image)
        col1, padding, col2 = st.columns((10, 2, 10))
        with col1:
            image1 = Image.open(uploaded_file)
            st.image(image1, use_column_width=True)
        with col2:
            st.image(result_image_pil, use_column_width=True)
        st.success("finished")
    else:
        st.error("Please input an image first!")
