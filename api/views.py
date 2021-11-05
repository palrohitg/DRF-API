from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BlogSerializer
from .models import Blog
from rest_framework import status
from django.http import Http404
from django.core.mail import send_mail


@api_view(['GET'])
def apiOverview(request):
    """
        adding the decorators before
        writing the view functions
    """
    api_urls = {
        'List': 'api/blog-list/',
        'Detail View': 'api/blog-details/<str: pk>/',
        'Create': 'api/blog-create/',
        'Update': 'api/blog-update/<str:pk>',
        'Delete': 'api/blog-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def blogList(request):
    blog = Blog.objects.all()
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)


def get_objects(pk):
    try:
        return Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        raise Http404


@api_view(['GET'])
def blogDetails(request, pk):
    blog = get_objects(pk)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)


@api_view(['PUT'])
def blogUpdate(request, pk):
    blog = get_objects(pk)
    serializer = BlogSerializer(instance=blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', ])
def blogCreate(request):
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def blogDelete(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
