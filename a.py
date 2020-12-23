

import tensorflow as tf

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


HOME_DIR='/Users/kimbeomchul'
yolo = YOLO(model_path='./model_data/plate_model.h5', 
            anchors_path='./model_data/yolo_anchors.txt',
            classes_path='./model_data/plate_class.txt')


# img = Image.open(os.path.join('../../../data/image/beatles01.jpg'))
# detected_img = yolo.detect_image(img)

# plt.figure(figsize=(12, 12))
# plt.imshow(detected_img)
#plt.show()
        ##OCR
import easyocr
import shutil 

if os.path.isfile("./result/좌표.txt"):
    os.remove("./result/좌표.txt")
  
if os.path.isfile("./result/번호판.txt"):
    os.remove("./result/번호판.txt")
  

# if os.path.isdir("./result"):
#     shutil.rmtree('./result', ignore_errors=True)​


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
createFolder('/Users/kimbeomchul/DLCV/DLCV_Colab_SrcCode_20200905/Detection/keras-yolo3/result')


createFolder('/Users/kimbeomchul/DLCV/DLCV_Colab_SrcCode_20200905/Detection/keras-yolo3/result/frame')




def detect_video_yolo(model, input_path, output_path=""):
    
    start = time.time()
    cap = cv2.VideoCapture(0)
    
    #codec = cv2.VideoWriter_fourcc(*'DIVX')
    codec = cv2.VideoWriter_fourcc(*'XVID')
    vid_fps = cap.get(cv2.CAP_PROP_FPS)
    vid_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    vid_writer = cv2.VideoWriter(output_path, codec, vid_fps, vid_size)  #출력
    


    frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print('총 Frame 갯수:', frame_cnt, '원본 영상 FPS:',vid_fps)
    index = 0
    index2 = 0
    while True:
        hasFrame, image_frame = cap.read()
        if not hasFrame:
            print('프레임이 없거나 종료 되었습니다.')
            break
        start = time.time()
        image = Image.fromarray(image_frame)
        detected_image = model.detect_image(image) 
        
        plt.figure(figsize=(12, 12))



#         plt.imshow(detected_image)
#         plt.axis('off')
# # # 돌린 번호판인식된거 사진저장
#         str_index= str(index)
#         plt.savefig('./result/frame/detected'+str_index+'.jpg')


        if os.path.isfile("./result/좌표.txt"):
            print('REACTED')
            with open('./result/좌표.txt', 'r') as file:
                point_files = file.readlines()

            str_index2 = str(index2)
            for i in point_files :
                split_points = i.split(' ')

                left = split_points[0]
                top = split_points[1]
                right = split_points[2]
                bottom = split_points[3]


            i_left = int(left)
            i_top = int(top)
            i_right = int(right)
            i_bottom = int(bottom)

            croppedImage=detected_image.crop((i_left,i_top,i_right,i_bottom))
# croppedImage.show()
            plt.imshow(croppedImage)
            plt.axis('off')
            plt.savefig('./result/frame/detected'+str_index2+'.jpg')
            index2 +=1
            
        # cv2.imshow("Moon", detected_image)
        result = np.asarray(detected_image)


        # print('detected_img',detected_image)
        # print('img',image)
        

        index +=1
        print('#### frame:{0} 이미지 처리시간:{1}'.format(index, round(time.time()-start,3)))
        vid_writer.write(result)

        cv2.imshow('test', result)
       
        k = cv2.waitKey(1) 
        if k == 97: 
            break

    vid_writer.release()
    cap.release()
    print('### Video Detect 총 수행시간:', round(time.time()-start, 5))


    print('Start OCR License Plate : ')

    reader = easyocr.Reader(['ko'])

    for i in range(index2) : 
        str_i = str(i)
        result = reader.readtext('./result/frame/detected'+str_i+'.jpg', detail = 0)

        str_result = "\n".join(result)
        with open("./result/번호판.txt", "a") as f:
            f.write(str_i)
            f.write(':')
            f.write(str_result)
            f.write('\n')
        
        print(result)
        print(i+1,'is Finished')
        print(i+1,'/',index2)    
        
detect_video_yolo(yolo, '../../../data/video/test02.mp4', '../../../data/output/test02.avi')
