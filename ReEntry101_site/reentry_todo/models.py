from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length = 255)
    
class Comment(models.Model):
    body = models.TextField()
    # created_at = models.DateTimeField(auto_now_add = True)
