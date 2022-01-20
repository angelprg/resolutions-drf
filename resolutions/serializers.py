from rest_framework import serializers
from resolutions.models import Resolution, ResolutionCategory

class ResolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resolution
        fields = ['id', 'title', 'description', 'done', 'category']

class ResolutionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolutionCategory
        fields = ['title']
