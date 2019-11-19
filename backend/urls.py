from django.urls import path, include
from rest_framework import routers
from .views import PostListAPI, PostCreateAPI, PostDetailAPI, PostUpdateAPI, PostDeleteAPI

urlpatterns = [
    path('', PostListAPI.as_view()),
    path('create/', PostCreateAPI.as_view()),
    path('detail/<int:pk>', PostDetailAPI.as_view()),
    path('update/<int:pk>', PostUpdateAPI.as_view()),
    path('delete/<int:pk>', PostDeleteAPI.as_view()),
]