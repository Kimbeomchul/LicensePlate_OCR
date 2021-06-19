import tensorflow as tf
import keras
import os
import sys
import random
import math
import time
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import argparse 
from PIL import Image
from yolo import YOLO ,detect_video
import argparse
import cv2
# import pytesseract 


img = cv2.imread('detected.jpg')
# img = cv2.imread('./pic/card2.jpg')
orig_img = img.copy()
height, width, channel = img.shape
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.figure(figsize=(12,8))
plt.subplot(121),plt.imshow(img[:,:,::-1],'gray')
plt.subplot(122),plt.imshow(imgray,'gray')
plt.axis('off')
plt.savefig("Start")
# plt.show()

# Edge를 뚜렷하게 하기 위해 가우시안 블러 적용
blur = cv2.GaussianBlur(imgray,(5,5),0)

# Adaptive Threshold 적용
thr = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
plt.figure(figsize=(20,20))

# dilation - erode with / without blur 
kernel = np.ones((3,3),np.uint8)
dil = cv2.dilate(blur,kernel,iterations=1)
ero = cv2.erode(blur,kernel,iterations=1)
morph = dil - ero

kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

topHat = cv2.morphologyEx(imgray, cv2.MORPH_TOPHAT, kernel2)
blackHat = cv2.morphologyEx(imgray, cv2.MORPH_BLACKHAT, kernel2)

imgGrayscalePlusTopHat = cv2.add(imgray, topHat)
subtract = cv2.subtract(imgGrayscalePlusTopHat, blackHat)
thr2 = cv2.adaptiveThreshold(subtract,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY,11,2)
plt.figure(figsize=(12,8))
plt.subplot(221), plt.imshow(blur,'gray')
plt.title("blurred")
plt.subplot(222), plt.imshow(thr,'gray')
plt.title("after Adaptive Threshold")
plt.subplot(223), plt.imshow(morph,'gray')
plt.title("Dilation - Erode (with blur)")
plt.subplot(224), plt.imshow(thr2,'gray')
plt.title("top-black AT")
plt.savefig("Preprocess")

