from django.shortcuts import render
import cv2
import threading
from django.http import StreamingHttpResponse

import keras_yolo3.a as a

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        # threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        grabbed, frame = self.video.read()
        image = frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()



cam = VideoCamera()


def gen(camera):
    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def livefe(request):
    return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")


def start_real_time(request):
    return StreamingHttpResponse(a.start_real_time(), content_type="multipart/x-mixed-replace;boundary=frame")

  

