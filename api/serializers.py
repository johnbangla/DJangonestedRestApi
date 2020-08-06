from rest_framework import serializers
from .models import Task, Album, IImage, Location


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['latitude', 'longitude']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IImage
        fields = ['url', 'thumbnailUrl']


class AlbumSerializer(serializers.ModelSerializer):
    iimages = ImageSerializer(many=True, read_only=True)
    locations = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['title', 'iimages', 'price',
                  'categoryId', 'userId', 'locations']

    def create(self, validated_data):
        tracks_data = validated_data.pop('iimages')
        tracks_data2 = validated_data.pop('locations')

        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            IImage.objects.create(album=album, **track_data)

        for track_datae in tracks_data2:
            Location.objects.create(album=album, **track_datae)
        return album
