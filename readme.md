# New Year Resolutions API

An API using Django + Django Rest Framework


## Python
[https://www.python.org/]

## python virtual environment
```
python -m venv .venv
source .venv/bin/activate
```
[https://docs.python.org/3/library/venv.html]

## Install Django + Django Rest Framework
```
pip install django djangorestframework
```

## Create dependencies file
```
pip freeze > requirements.txt
```

## Create the Django Project
```
django-admin startproject newyearresolutions .
```

## Create the resolutions app
```
python manage.py startapp resolutions
```

## Add the `rest_framework` module and `resolutions` app to the django project settings.
```
newyearresolutions/settings.py
```
```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'resolutions.apps.ResolutionsConfig',
]
```

## Create the `Resolution` model
```resolutions/models.py```
```
class Resolution(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField()
    category = models.ForeignKey('ResolutionCategory', on_delete=models.CASCADE)

class ResolutionCategory(models.Model):
    title = models.CharField(max_length=100)
```
## Register the Resolution Model to the admin interface
```resolutions/admin.py```
```
from resolutions.models import Resolution, ResolutionCategory

admin.site.register(Resolution)
admin.site.register(ResolutionCategory)
```

## Create and runing first migration
```
python manage.py makemigrations
python manage.py migrate
```

## Create our superuser
```
python manage.py createsuperuser
```

# DRF

## Create Serializer
Create a file ```resolutions/serializers.py```
```
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
```

## Create views
Edit the file ```resolutions/views.py```
```
from django.http import HttpResponse
from resolutions.models import ResolutionCategory, Resolution
from resolutions.serializers import ResolutionSerializer, ResolutionCategorySerializer
from rest_framework import generics

class ResolutionList(generics.ListCreateAPIView):
    queryset = Resolution.objects.all()
    serializer_class = ResolutionSerializer

class ResolutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resolution.objects.all()
    serializer_class = ResolutionSerializer

class ResolutionCategoryList(generics.ListCreateAPIView):
    queryset = ResolutionCategory.objects.all()
    serializer_class = ResolutionCategorySerializer

class ResolutionCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResolutionCategory.objects.all()
    serializer_class = ResolutionCategorySerializer
```

## Configure routes (urls)
Edit the project urls file `newyearresolutions/urls.py`
```
from django.urls import path, include
...
path('api/v1/', include('resolutions.urls')),
```

Create the app urls file `resolutions/urls.py`
```
from django.urls import path
from resolutions import views

urlpatterns = [
    path('resolutions/',  views.ResolutionList.as_view()),
    path('resolutions/<int:pk>',  views.ResolutionDetail.as_view()),
    path('resolution-categories/',  views.ResolutionCategoryList.as_view()),
    path('resolution-categories/<int:pk>',  views.ResolutionCategoryDetail.as_view()),
]
```





