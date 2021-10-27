from django.urls import path
from .views import BlogList, UserBlogs, BlogDetail, PaginatedBlogs

app_name='blogs'

urlpatterns = [
  path('blogs/', BlogList.as_view()),
  path('user/blogs/', UserBlogs.as_view()),
  path('blogs/detail/<str:pk>/', BlogDetail.as_view()),
  path('page/', PaginatedBlogs().as_view()),
]
