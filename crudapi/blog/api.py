from rest_framework import generics
from rest_framework.response import Response
from .models import Blog
from .serializer import BlogSerializer

class CreateBlogApi(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class ListBlogApi(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class UpdateBlogApi(generics.RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class DeleteBlogApi(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer