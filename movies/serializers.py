from rest_framework import serializers
from .models import MovieData

class MovieSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(max_length=None , use_url = True)
    image = serializers.ImageField(max_length=None, use_url=True, required=False, allow_null=True, default='Images/download.png')

    class Meta:
        model = MovieData
        fields = ['id' , 'name', 'duration', 'rating' , 'typ', 'image']