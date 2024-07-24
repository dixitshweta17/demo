from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)