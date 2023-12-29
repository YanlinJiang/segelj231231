import streamlit as st
from PIL import Image
import numpy as np
from skimage.metrics import mean_squared_error

def calculate_psnr(image1, image2):
    mse = mean_squared_error(image1, image2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

st.title('PSNR Calculator')

# Upload images
# image1 = st.file_uploader("Choose an image...", type="jpg")
# image2 = st.file_uploader("Choose another image...", type="jpg")

image11 = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
image22 = st.file_uploader("Choose another image...", type=["png", "jpg", "jpeg"])

if image11 and image22:
    image1 = Image.open(image11)
    image2 = Image.open(image22)

    # Convert images to numpy arrays
    image1_array = np.array(image1)
    image2_array = np.array(image2)

    # Calculate and display PSNR
    psnr_value = calculate_psnr(image1_array, image2_array)
    st.write('PSNR Value:', psnr_value)