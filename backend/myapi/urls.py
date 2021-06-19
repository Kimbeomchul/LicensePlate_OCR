
from django.contrib import admin
from django.urls import path
from img import views
from rest_framework import routers
from django.conf.urls import url , include
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'images', views.ImagesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('img/', include('img.urls')),
    path('yolo/', include('my_yolo.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
