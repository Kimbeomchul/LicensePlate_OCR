from .models import Images
from rest_framework import serializers

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"