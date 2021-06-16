from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.title
