from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    # title = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)