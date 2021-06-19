

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
#keras-yolo에서 image처리를 주요 PIL로 수행. 



LOCAL_PACKAGE_DIR = os.path.abspath("./keras-yolo3")
sys.path.append(LOCAL_PACKAGE_DIR)
default_yolo_dir = '/content/DLCV/Detection/yolo'
config_dict = {}
yolo = YOLO(model_path='./model_data/yolo.h5',  
            anchors_path='./model_data/yolo_anchors.txt',
            classes_path='./model_data/coco_classes.txt')


img = Image.open(os.path.join('../../../data/image/beatles01.jpg'))
detected_img = yolo.detect_image(img)

plt.figure(figsize=(12, 12))
plt.imshow(detected_img)
#plt.show()



def detect_video_yolo(model, input_path, output_path=""):
    
    start = time.time()
    cap = cv2.VideoCapture(input_path)
    
    #codec = cv2.VideoWriter_fourcc(*'DIVX')
    codec = cv2.VideoWriter_fourcc(*'XVID')
    vid_fps = cap.get(cv2.CAP_PROP_FPS)
    vid_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    vid_writer = cv2.VideoWriter(output_path, codec, vid_fps, vid_size)
    
    frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print('총 Frame 갯수:', frame_cnt, '원본 영상 FPS:',vid_fps)
    index = 0
    while True:
        hasFrame, image_frame = cap.read()
        if not hasFrame:
            print('프레임이 없거나 종료 되었습니다.')
            break
        start = time.time()
        image = Image.fromarray(image_frame)
        detected_image = model.detect_image(image)
        result = np.asarray(detected_image)
        index +=1
        print('#### frame:{0} 이미지 처리시간:{1}'.format(index, round(time.time()-start,3)))
        
        vid_writer.write(result)
    
    vid_writer.release()
    cap.release()
    print('### Video Detect 총 수행시간:', round(time.time()-start, 5))

detect_video_yolo(yolo, '../../../data/video/test02.mp4', '../../../data/output/test02.avi')



# wget https://pjreddie.com/media/files/yolov3-tiny.weights
#!python convert.py yolov3-tiny.cfg ./model_data/yolov3-tiny.weights model_data/yolo-tiny.h5



# tiny_yolo = YOLO(model_path='./model_data/yolo-tiny.h5',
#             anchors_path='./model_data/tiny_yolo_anchors.txt',
#             classes_path='./model_data/coco_classes.txt')


# img = Image.open(os.path.join('../../../data/image/beatles01.jpg'))
# detected_img = tiny_yolo.detect_image(img)

# plt.figure(figsize=(12, 12))
# plt.imshow(detected_img)



# detect_video_yolo(tiny_yolo, '../../../data/video/secretlife_pet.mp4', '../../../data/output/secretlife_pet_yolo01.avi')

