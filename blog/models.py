from django.db import models
from django_extensions.db.fields import AutoSlugField

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="title")

    class Meta:
        ordering = ("title", )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = AutoSlugField(populate_from="title")
    category = models.ManyToManyField(Category, related_name="posts")
    created = models.DateField()

    def __str__(self):
        return f'{str(self.title)}'
    
    class Meta:
        ordering = ['-created']