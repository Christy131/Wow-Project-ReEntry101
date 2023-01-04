from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length = 255)
    
class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField (default=timezone.now())
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)
