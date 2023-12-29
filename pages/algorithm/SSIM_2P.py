
import numpy as np
import cv2
from skimage.metrics import structural_similarity as compare_ssim


class SSIM:
    def __init__(self,img1,img2):
        pass
        self.img1=img1
        self.img2=img2
    def calculate_ssim(self):
        # 转换图像为灰度
        gray1 = cv2.cvtColor(np.array(self.img1), cv2.COLOR_RGB2GRAY)
        gray2 = cv2.cvtColor(np.array(self.img2), cv2.COLOR_RGB2GRAY)

        # 计算 SSIM
        score, _ = compare_ssim(gray1, gray2, full=True)
        return score