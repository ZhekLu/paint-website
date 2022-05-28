from rest_framework import serializers

from paintsite.models import PictureBoard


class PictureBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureBoard
        fields = ('id', 'title', 'description', 'created_at')


class PPDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PictureBoard
        fields = ('id', 'title', 'description', 'created_at', 'author', 'image')
