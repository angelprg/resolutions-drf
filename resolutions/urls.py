from django.urls import path
from resolutions import views


urlpatterns = [
    path('resolutions/',  views.ResolutionList.as_view()),
    path('resolutions/<int:pk>',  views.ResolutionDetail.as_view()),
    path('resolution-categories/',  views.ResolutionCategoryList.as_view()),
    path('resolution-categories/<int:pk>',  views.ResolutionCategoryDetail.as_view()),
]