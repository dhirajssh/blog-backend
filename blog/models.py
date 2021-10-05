from django.db import models
from django.utils import timezone
from users.models import NewUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

def upload_to(instance, filename):
  return 'posts/{filename}'.format(filename=filename)

class Blog(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  user = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='blog_posts', null=True)
  created = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.jpg')

  def __str__(self):
    return self.title
