from django.urls import path
from . import views


app_name = 'img'

urlpatterns = [
    path('', views.save_img, name='save_img'),
    path('recognition/<target_name>', views.recognition, name='recognition'),
    path('ocr/<plate>', views.ocr, name='ocr')
]
