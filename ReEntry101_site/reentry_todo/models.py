from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length = 255)
    tags = models.ManyToManyField(Tag)
class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField (default=timezone.now())
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)

class Tag(models.Model):
        # Setting `unique=True` on the name attribute below ensures that no two tags
        # will have the same name
    name = models.CharField(max_length=30, unique=True)
        # When we add the `tags` ManyToMany field to the Task model below,
        # Django automatically creates an attribute `task_set` on the Tag Model
        # so that we can use the relationship between Tags and Tasks both ways
