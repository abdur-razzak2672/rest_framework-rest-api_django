from django.urls import path
from .views import *


urlpatterns = [
    #path('article/',article_list), funtion view api
    #path('article/',ArticleAPIView.as_view()), class view api
    #path('detail/<int:pk>/',article_detail),funtion view api
    path('detail/<int:id>/',articleDetails.as_view()),

    path('generic/article/<int:id>',GenericAPIView.as_view()),
]