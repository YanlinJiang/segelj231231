import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import cv2
import io
from pages.algorithm.SSIM_2P import SSIM
from pages.algorithm.PSNR_2P import PSNR
from pages.algorithm.NRSS2 import NRSSzwei
from skimage.metrics import structural_similarity as compare_ssim

def refreshButton():
    step4Button = st.button('re-start')
    if step4Button:
        st.experimental_rerun()

st.header("""Multiple Modules Image Processing""")
st.caption("-You can choose what function you like and processing image here.")


#第一步，选择FR/RR/NR
step1Button = st.selectbox('Step-1, Choose an type for image processing:',
             ('Full Reference(FR)','Reduce Reference(RR)','None Reference(NR)','Click to select'),index=3)
if step1Button=='Full Reference(FR)':
    # 第二步，选择算法
    step2Button = st.selectbox('Step-2, Choose an type for image processing:',
                               ( 'Click to select','SSIM', 'PSNR'),
                               index=0)
    if step2Button == 'SSIM':
        # 上传图像
        image11 = st.file_uploader("上传第一幅图像", type=["png", "jpg", "jpeg"])
        image22 = st.file_uploader("上传第二幅图像", type=["png", "jpg", "jpeg"])
        step3Button = st.button("Execute")
        if step3Button:
            if image11 and image22:
                image1 = Image.open(image11)
                image2 = Image.open(image22)
                temp = SSIM(image1, image2)
                ssim_score = temp.calculate_ssim()
                st.write("SSIM score:", ssim_score)
                st.success("finished")
                col1, padding, col2 = st.columns((10, 2, 10))
                with col1:
                    st.image(image1, use_column_width=True)
                    image_details = {"file_name": image11.name,
                                     "file_type": image11.type,
                                     "file_size": image11.size}
                    st.write(image_details)
                with col2:
                    st.image(image2, use_column_width=True)
                    image_details = {"file_name": image22.name,
                                     "file_type": image22.type,
                                     "file_size": image22.size}
                    st.write(image_details)
                refreshButton()
            else:
                st.error("Please input two images first")
    elif step2Button == 'PSNR':
        image11 = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
        image22 = st.file_uploader("Choose another image...", type=["png", "jpg", "jpeg"])
        step3Button = st.button("Execute")
        if step3Button:
            if image11 and image22:
                image1 = Image.open(image11)
                image2 = Image.open(image22)

                # Convert images to numpy arrays
                image1_array = np.array(image1)
                image2_array = np.array(image2)
                temp = PSNR(image1_array, image2_array)
                # Calculate and display PSNR
                psnr_value = temp.calculate_psnr()
                st.write('PSNR Value:', psnr_value)
                st.success("finished")
                col1, padding, col2 = st.columns((10, 2, 10))
                with col1:
                    st.image(image1, use_column_width=True)
                    image_details = {"file_name": image11.name,
                                     "file_type": image11.type,
                                     "file_size": image11.size}
                    st.write(image_details)
                with col2:
                    st.image(image2, use_column_width=True)
                    image_details = {"file_name": image22.name,
                                     "file_type": image22.type,
                                     "file_size": image22.size}
                    st.write(image_details)
                refreshButton()
            else:
                st.error("Please input two images first")

elif step1Button=='Reduce Reference(RR)':
    # 第二步，选择算法
    step2Button = st.selectbox('Step-2, Choose an type for image processing:',
                               ('Click to select','尚未完成'),
                               index=0)
    #buttonEx = st.button("Execute")
elif step1Button=='None Reference(NR)':
    # 第二步，选择算法
    step2Button = st.selectbox('Step-2, Choose an type for image processing:',
                               ('Click to select', 'NRSS'),
                               index=0)
    if step2Button=='NRSS':
        # st.error("还在debug，还没做完")
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
        step3Button = st.button("Execute")
        if step3Button:
            if uploaded_file:
                image1 = Image.open(uploaded_file)
                # 将图像转换为灰度
                image1_gray = image1.convert('L')
                # 将 PIL 图像转换为 NumPy 数组
                image1_np = np.array(image1_gray)
                temp = NRSSzwei(image1_np)
                result = temp.NRSS()
                st.write('NRSS Result:', result)
                st.success("finished")
                col1, col2 = st.columns((10, 12))
                with col1:
                    st.image(uploaded_file, use_column_width=True)
                    image_details = {"file_name": uploaded_file.name,
                                     "file_type": uploaded_file.type,
                                     "file_size": uploaded_file.size}
                    st.write(image_details)
                refreshButton()
            else:
                st.error("Please input an image first")






# def calculate_ssim(image1, image2):
#     # 转换图像为灰度
#     gray1 = cv2.cvtColor(np.array(image1), cv2.COLOR_RGB2GRAY)
#     gray2 = cv2.cvtColor(np.array(image2), cv2.COLOR_RGB2GRAY)
#
#     # 计算 SSIM
#     score, _ = compare_ssim(gray1, gray2, full=True)
#     return score