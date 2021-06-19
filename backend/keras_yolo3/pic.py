

import tensorflow as tf
import keras

import os
import sys
import random
import math
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse 
from PIL import Image
from keras_yolo3.yolo import YOLO
import argparse
import cv2
import logging
#keras-yolo에서 image처리를 주요 PIL로 수행. 
import ssl
import easyocr

# def createFolder(directory):
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     except OSError:
#         print ('Error: Creating directory. ' +  directory)

def detection(target_path):
    ssl._create_default_https_context = ssl._create_unverified_context
    # https 뚫어야함 뼤엑

    #이전생성파일 삭제
    if os.path.isfile("./result/좌표.txt"):
        os.remove("./result/좌표.txt")

    if os.path.isfile("./result/번호판.txt"):
        os.remove("./result/번호판.txt")




    HOME_DIR='keras_yolo3/'



    plate_yolo = YOLO(model_path=os.path.join(HOME_DIR,'snapshots/000/plate_model.h5'),
                classes_path=os.path.join(HOME_DIR, 'model_data/plate_class.txt'),
                anchors_path=os.path.join(HOME_DIR,'model_data/yolo_anchors.txt'))

    print('target_path' + target_path)
    img = Image.open(target_path)
    print('이미지 오픈!!!!!!')
    plt.figure(figsize=(12, 12))
    # plt.imshow(img)

    print('디텍트 이미지 시작')
    detected_img = plate_yolo.detect_image(img)
    print('디텍트 이미지 성공')

    # plt.figure(figsize=(12, 12))


    plt.imshow(detected_img)
    plt.axis('off')
    # # 돌린 번호판인식된거 사진저장
    plt.savefig(target_path)

    # 좌표불러오기
    print('좌표 불러오기 시작')
    with open('keras_yolo3/result/좌표.txt', 'r') as file:
        point_files = file.readlines()
    print('좌표 불러오기 성공')

    i = point_files[0]
    split_points = i.split(' ')
    
    left = split_points[0]
    top = split_points[1]
    right = split_points[2]
    bottom = split_points[3]


    i_left = int(left)
    i_top = int(top)
    i_right = int(right) + 1
    i_bottom = int(bottom) + 1
    # print(i_bottom)
    # for line in point_files : # 파일 배열로 자르기
    #      split_points = line.split(' ')
    #      split_points[-1] = split_points[-1][:-1]

    #     print(split_points[0])

    #춉춉 하기~ >< 
    
    croppedImage=detected_img.crop((i_left,i_top,i_right,i_bottom))
    # croppedImage.show()
    plt.imshow(croppedImage)
    plt.axis('off')
    
    # plate path 지정
    plate_path = target_path.replace('.jpg', 'plate.jpg')
    plt.savefig(target_path.replace('.jpg', 'plate.jpg'))
    # plt.show()
    plt.close()
    print('yolo 끗')
    result = {
        'detect' : "http://localhost:8000/" + target_path,
        'plate' : "http://localhost:8000/" + plate_path,
        'status' : True
    }
    return result

def start_ocr(plate_path):
    reader = easyocr.Reader(['ko']) # need to run only once to load model into memory
    result = reader.readtext(plate_path)
    print(result)
    
    return result



# ## 흐으으윽 백 컨투어 구상좀 해야함 
# img_ori = cv2.imread('detected.jpg')

# height, width, channel = img_ori.shape


# plt.figure(figsize=(12, 10))
# # plt.imshow(img_ori, cmap='gray')

# gray = cv2.cvtColor(img_ori, cv2.COLOR_BGR2GRAY)

# plt.figure(figsize=(12, 10))
# # plt.imshow(gray, cmap='gray')

# img_blurred = cv2.GaussianBlur(gray, ksize=(5, 5), sigmaX=0)

# img_thresh = cv2.adaptiveThreshold(
#     img_blurred, 
#     maxValue=255.0, 
#     adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
#     thresholdType=cv2.THRESH_BINARY_INV, 
#     blockSize=19, 
#     C=9
# )

# plt.figure(figsize=(12, 10))
# plt.imshow(img_thresh, cmap='gray')
# plt.axis('off')
# plt.savefig('thresh_detected.jpg')
