import streamlit as st
from skimage.metrics import structural_similarity as compare_ssim
import cv2
from PIL import Image
import numpy as np

def calculate_ssim(image1, image2):
    # 转换图像为灰度
    gray1 = cv2.cvtColor(np.array(image1), cv2.COLOR_RGB2GRAY)
    gray2 = cv2.cvtColor(np.array(image2), cv2.COLOR_RGB2GRAY)

    # 计算 SSIM
    score, _ = compare_ssim(gray1, gray2, full=True)
    return score

def main():
    st.title("图像结构相似性指数 (SSIM) 计算器")

    # 上传图像
    image1 = st.file_uploader("上传第一幅图像", type=["png", "jpg", "jpeg"])
    image2 = st.file_uploader("上传第二幅图像", type=["png", "jpg", "jpeg"])

    if image1 and image2:
        image1 = Image.open(image1)
        image2 = Image.open(image2)

        # 显示图像
        st.image(image1, caption="图像 1", use_column_width=True)
        st.image(image2, caption="图像 2", use_column_width=True)

        # 计算 SSIM
        ssim_score = calculate_ssim(image1, image2)
        st.write("SSIM:", ssim_score)

if __name__ == "__main__":
    main()
