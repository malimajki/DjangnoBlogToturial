from django.db import models
from django_extensions.db.fields import AutoSlugField

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = AutoSlugField(populate_from="title")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.title)}'
    
    class Meta:
        ordering = ['-created']