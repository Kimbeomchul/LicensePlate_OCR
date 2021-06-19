import cv2
import time
import numpy as np
import sys
import argparse
import os
from yolo import YOLO, detect_video
from PIL import Image


HOME_DIR='/Users/kimbeomchul'
raccoon_yolo = YOLO(model_path=os.path.join(HOME_DIR,'./DLCV/DLCV_Colab_SrcCode_20200905/Detection/keras-yolo3/snapshots/000/plate_model.h5'), # MODEL
            classes_path=os.path.join(HOME_DIR, './DLCV/DLCV_Colab_SrcCode_20200905/Detection/keras-yolo3/model_data/plate_class.txt'),
            anchors_path=os.path.join(HOME_DIR,'./DLCV/DLCV_Colab_SrcCode_20200905/Detection/keras-yolo3/model_data/yolo_anchors.txt'))





def detect_video_yolo(model, input_path, output_path=""):
    
    start = time.time()
    cap = cv2.VideoCapture(0)
 ##    
    #codec = cv2.VideoWriter_fourcc(*'DIVX')
    codec = cv2.VideoWriter_fourcc(*'XVID')
    vid_fps = cap.get(cv2.CAP_PROP_FPS)
    vid_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    vid_writer = cv2.VideoWriter(output_path, codec, vid_fps, vid_size)
    
    frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print('총 Frame 갯수:', frame_cnt, '원본 영상 FPS:',vid_fps, '원본 Frame 크기:', vid_size)
    index = 0
    while True:
        hasFrame, image_frame = cap.read()
        if not hasFrame:
            print('프레임이 없거나 종료 되었습니다.')
            break
        start = time.time()
        image = Image.fromarray(image_frame)
        detected_image = model.detect_image(image)
        if detected_image is null :
            print('nonon')


        result = np.asarray(detected_image)
        index +=1
        print('#### frame:{0} 이미지 처리시간:{1}'.format(index, round(time.time()-start,3)))
        
        vid_writer.write(result)

        # # RealTime 
        # cv2.imshow('라쿠우우우우우우운', result)
        # k = cv2.waitKey(1) 
        # if k == 'q': 
        #     break



    vid_writer.release()
    cap.release()
    print('### Video Detect 총 수행시간:', round(time.time()-start, 5))

# default_dir = '/Users/kimbeomchul/DLCV'
# detect_video_yolo(raccoon_yolo, os.path.join(default_dir, './data/video/vid.mp4'), os.path.join(default_dir, './data/output/vid.avi'))