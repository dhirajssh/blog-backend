from django.urls import path
from .views import BlogList, UserBlogs, BlogDetail

app_name='blogs'

urlpatterns = [
  path('blogs/', BlogList.as_view()),
  path('user/blogs/', UserBlogs.as_view()),
  path('blogs/detail/<str:pk>/', BlogDetail.as_view()),
]
