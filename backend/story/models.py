from django.db import models

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
