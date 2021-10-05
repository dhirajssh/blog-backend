from django.shortcuts import render
from .models import Blog
from users.models import NewUser
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

class BlogList(APIView):

  permission_classes = [IsAuthenticated]
  parser_classes = [MultiPartParser, FormParser]

  def get(self, request):
    user = request.user
    blogs = Blog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, format=None):
    user = request.user
    serializer = BlogSerializer(data=request.data)
    if serializer.is_valid():
      blog = serializer.save()
      blog.user = user
      blog.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserBlogs(APIView):

  permission_classes = [IsAuthenticated]
  parser_classes = [MultiPartParser, FormParser]

  def get(self, request):
    user = request.user
    blog = Blog.objects.filter(user=user)
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class BlogDetail(APIView):

  permission_classes = [IsAuthenticated]

  def get_object(self, pk):
    try:
      return Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

  def put(self, request, pk):
    blog = self.get_object(pk)
    serializer = BlogSerializer(blog, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)

  def delete(self, request, pk):
    blog = self.get_object(pk)
    blog.delete()
    return Response({
      "data": "deleted",
      "id": pk,
      "status": "204",
    }, status=status.HTTP_204_NO_CONTENT)
