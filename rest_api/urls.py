from django.urls import path
from .views import *


urlpatterns = [
    path('article/',article_list),
    path('detail/<int:pk>/',article_detail),
]