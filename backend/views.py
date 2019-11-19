from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPI(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateAPI(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteAPI(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer