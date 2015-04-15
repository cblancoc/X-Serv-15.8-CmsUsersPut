from django.db import models

# Create your models here.


class Table(models.Model):
    blog = models.CharField(max_length=32)
    url = models.TextField()
