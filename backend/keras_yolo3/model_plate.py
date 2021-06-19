import os
import keras
import tensorflow as tf 
from pathlib import Path
import glob
import xml.etree.ElementTree as ET
import numpy as np
import keras.backend as K
from keras.layers import Input, Lambda
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import TensorBoard, ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import sys
from train import get_classes, get_anchors
from train import create_model, data_generator, data_generator_wrapper
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt


default_dir = '/Users/kimbeomchul'
default_yolo_dir = os.path.join(default_dir, '/DLCV/DLCV_Colab_SrcCode_20200905/Detection/yolo')

LOCAL_PACKAGE_DIR = os.path.abspath(os.path.join(default_yolo_dir,'keras-yolo3'))
#print(LOCAL_PACKAGE_DIR)
sys.path.append(LOCAL_PACKAGE_DIR)

from yolo3.model import preprocess_true_boxes, yolo_body, tiny_yolo_body, yolo_loss
from yolo3.utils import get_random_data

HOME_DIR = '/Users/kimbeomchul'

ANNO_DIR = os.path.join(HOME_DIR, 'DLCV/data/plate/annotations')
IMAGE_DIR = os.path.join(HOME_DIR, 'DLCV/data/plate/images')
print(ANNO_DIR)

files = os.listdir(ANNO_DIR)

# 라벨링한 파일 변환 
def xml_to_csv(path, output_filename):
    xml_list = [] 
    with open(output_filename, "w") as train_csv_file:
        for xml_file in glob.glob(path + '/*.xml'):
            tree = ET.parse(xml_file)
            root = tree.getroot()
            full_image_name = os.path.join(IMAGE_DIR, root.find('filename').text)
            value_str_list = ' '
            for obj in root.findall('object'):
                
                xmlbox = obj.find('bndbox')
                x1 = int(xmlbox.find('xmin').text)
                y1 = int(xmlbox.find('ymin').text)
                x2 = int(xmlbox.find('xmax').text)
                y2 = int(xmlbox.find('ymax').text)
                class_id = 0
                value_str = ('{0},{1},{2},{3},{4}').format(x1, y1, x2, y2, class_id)
                value_str_list = value_str_list+value_str+' ' 
            train_csv_file.write(full_image_name+' '+ value_str_list+'\n')

xml_to_csv(ANNO_DIR, os.path.join(ANNO_DIR,'plate_anno.csv'))
#print(os.path.join(ANNO_DIR,'raccoon_anno.csv'))

BASE_DIR = os.path.join(HOME_DIR, 'DLCV/DLCV_Colab_SrcCode_20200905/Detection/yolo/keras-yolo3')
classes_path = os.path.join(BASE_DIR, 'model_data/plate_class.txt') # 클랙스 입력 
with open(classes_path, "w") as f:
    f.write("plate") # 클래스입력 


annotation_path = os.path.join(ANNO_DIR, 'plate_anno.csv')
log_dir = os.path.join(BASE_DIR, 'snapshots/000/')
classes_path = os.path.join(BASE_DIR, 'model_data/plate_class.txt')
anchors_path = os.path.join(BASE_DIR,'model_data/yolo_anchors.txt')

class_names = get_classes(classes_path)
num_classes = len(class_names)
anchors = get_anchors(anchors_path)

model_weights_path = os.path.join(BASE_DIR, 'model_data/yolo.h5' ) # 가중치 설정 

input_shape = (416,416) # multiple of 32, hw

is_tiny_version = len(anchors)==6 #디폴트 
if is_tiny_version:
    model = create_tiny_model(input_shape, anchors, num_classes,
        freeze_body=2, weights_path=model_weights_path)
else:
    model = create_model(input_shape, anchors, num_classes,
        freeze_body=2, weights_path=model_weights_path) 

logging = TensorBoard(log_dir=log_dir)
checkpoint = ModelCheckpoint(log_dir + 'ep{epoch:03d}-loss{loss:.3f}-val_loss{val_loss:.3f}.h5',
    monitor='val_loss', save_weights_only=True, save_best_only=True, period=3)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, verbose=1)
early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, patience=10, verbose=1)

val_split = 0.1

with open(annotation_path) as f:
    lines = f.readlines()

np.random.seed(10101)
np.random.shuffle(lines)
np.random.seed(None)
num_val = int(len(lines)*val_split)
num_train = len(lines) - num_val

if True:
    model.compile(optimizer=Adam(lr=1e-3), loss={

        'yolo_loss': lambda y_true, y_pred: y_pred})

    batch_size = 4
    print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
    model.fit_generator(data_generator_wrapper(lines[:num_train], batch_size, input_shape, anchors, num_classes),
            steps_per_epoch=max(1, num_train//batch_size),
            validation_data=data_generator_wrapper(lines[num_train:], batch_size, input_shape, anchors, num_classes),
            validation_steps=max(1, num_val//batch_size),
            epochs=50,
            initial_epoch=0,
            callbacks=[logging, checkpoint])
    model.save_weights(log_dir + 'plate_model.h5')

if True:
    for i in range(len(model.layers)):
        model.layers[i].trainable = True
    model.compile(optimizer=Adam(lr=1e-4), loss={'yolo_loss': lambda y_true, y_pred: y_pred}) 
    print('Unfreeze all of the layers.')

    batch_size = 4  # 배치사이즈 
    print('Train on {} samples, val on {} samples, with batch size {}.'.format(num_train, num_val, batch_size))
    model.fit_generator(data_generator_wrapper(lines[:num_train], batch_size, input_shape, anchors, num_classes),
        steps_per_epoch=max(1, num_train//batch_size),
        validation_data=data_generator_wrapper(lines[num_train:], batch_size, input_shape, anchors, num_classes),
        validation_steps=max(1, num_val//batch_size),
        epochs=100,
        initial_epoch=50,
        callbacks=[logging, checkpoint, reduce_lr, early_stopping])
    model.save_weights(log_dir + 'plate_model.h5')
