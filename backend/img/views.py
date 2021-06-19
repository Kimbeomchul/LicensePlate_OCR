from django.shortcuts import render

# models
from .models import Images
from .serializers import ImagesSerializer
# Create your views here.

# forms
from .forms import UploadFileForm

# rest_framework
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# ocr
import keras_yolo3.pic as pic



class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

@api_view(['POST'])
def save_img(request):
    context = {
                'result' : 'False' 
            }
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("form 형식이 올바릅니다.")
            print(request.FILES['image'])
            instance = Images(image=request.FILES['image']) # 감자ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ감쟈ㅑㅑㅑㅑㅑ 대홍단 가암자 ~ 
            instance.save()
            context = {
                'result' : 'True',
                'message' : '파일을 업로드 하였습니다.',
                'path' : instance.image.url,
                'name' : instance.image.url.replace('/media/images/', '')
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            form = UploadFileForm()
    return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def recognition(request, target_name):
    result = pic.detection('media/images/{}'.format(target_name))
    if result['status']:
        context = result
        return Response(context, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def ocr(request, plate):
    plate_path = 'media/images/'+ plate
    ocr_texts = pic.start_ocr(plate_path)
    result1 = ''
    result2 = ''
    for ocr_text in ocr_texts:
        if 47 < ord(ocr_text[1][-1]) < 58:
            result2 = ocr_text[1]
        elif 44032 <= ord(ocr_text[1][-1]) <= 55203:
            result1 = ocr_text[1]
    if result1:
        result = result1 + ' ' + result2
    else:
        result = result2
    print('백앤드 작업 결과 :'+result)
    context = {
        'ocr_text' : result
    }
    return Response(context, status=status.HTTP_200_OK)