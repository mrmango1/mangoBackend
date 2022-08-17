from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Manga(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    images = models.ImageField(upload_to='api/images/manga')
