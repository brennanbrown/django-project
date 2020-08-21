from django.db import models

# Create your models here.


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=128,  default='TITLE')
    summary = models.CharField(max_length=256, default='SUMMARY')
    date = models.CharField(max_length=128, default='DATE')
    hyperlink = models.CharField(max_length=256, default='HYPERLINK')
    # repository = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return self.title
