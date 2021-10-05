from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
  user_name = serializers.CharField(source="user.first_name", read_only=True)
  class Meta:
    model = Blog
    fields = ('title', 'description', 'image', 'id', 'user_name')
    