from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Project(models.Model):

    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='project')

    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='project/', null=True)

    created_at = models.DateField(auto_now=True)
