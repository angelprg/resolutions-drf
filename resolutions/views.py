from django.http import HttpResponse
from resolutions.models import ResolutionCategory, Resolution
from resolutions.serializers import ResolutionSerializer, ResolutionCategorySerializer
from rest_framework import generics, permissions

class ResolutionList(generics.ListCreateAPIView):
    queryset = Resolution.objects.all()
    serializer_class = ResolutionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ResolutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resolution.objects.all()
    serializer_class = ResolutionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ResolutionCategoryList(generics.ListCreateAPIView):
    queryset = ResolutionCategory.objects.all()
    serializer_class = ResolutionCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ResolutionCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResolutionCategory.objects.all()
    serializer_class = ResolutionCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def homepage(request):
    return HttpResponse('Hello World!')