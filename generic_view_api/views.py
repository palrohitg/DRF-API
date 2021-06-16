from .models import Blog
from .serializers import BlogSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class BlogListAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_filed = "id"
