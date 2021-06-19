from django.urls import path
from . import views

app_name = 'yolo'

urlpatterns = [
    path('', views.livefe, name='livefe'),
    path('start_real_time', views.start_real_time, name='start_real_time')
]
