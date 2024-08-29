from rest_framework import serializers
from .models import Moviedata

# this class create a serializer (converts its data to JSON format) from the Moviedata model
# This is a method used to create API from a model
class MovieSerializer(serializers.ModelSerializer):
    # serialize the image field
    image = serializers.ImageField(max_length=None, use_url=True)
    # a meta class that contains the models name and fields accessible via the API
    class Meta:
        # specify model to serialize
        model = Moviedata
        # specify fields accessible in the API response 
        # id is a default unique field which is available for every model
        fields = ['id', 'name', 'duration', 'rating', 'typ', 'image']
