from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from .models import Blog 
from .serializers import BlogSerializer

class BlogList(APIView):
	"""
	List all Blogs, or create new blogs 
	"""

	def get(self, request, format=None):
		blog = Blog.objects.all()
		serializer = BlogSerializer(blog, many=True) 
		return Response(serializer.data, status = status.HTTP_200_OK)

	def post(self, request, format=None):
		serializer = BlogSerializer(data = request.data) 
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class BlogDetails(APIView):
	"""
	Retreive, Update and delete by primary keys
	"""

	def get_objects(self, pk):
		try :
			return Blog.objects.get(pk=pk)
		except Blog.DoesNotExist:
			raise Http404


	def get(self, request, pk, format = None):
		blog = self.get_objects(pk) 
		serializer = BlogSerializer(blog)
		return Response(serializer.data) 	


	def put(self, request, pk, format = None):
		blog = self.get_objects(pk)
		serializer = BlogSerializer(blog, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


	def patch(self, request, pk, format = None):
		blog = self.get_objects(pk) 
		serializer = BlogSerializer(blog, data=request.data, partial = True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		blog = self.get_objects(pk)
		transformer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)