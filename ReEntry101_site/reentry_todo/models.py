from django.db import models
from django.utils import timezone

# Create your models here.
class Tag(models.Model):
        # Setting `unique=True` on the name attribute below ensures that no two tags
        # will have the same name
    name = models.CharField(max_length=30, unique=True)
        # When we add the `tags` ManyToMany field to the Question model below,
        # Django automatically creates an attribute `task_set` on the Tag Model
        # so that we can use the relationship between Tags and Questions both ways

class Question(models.Model):
    # Create the question box for the user to enter
    question = models.CharField(max_length = 255)
    # Allows the user to tag keywords so that way when we add a search feature it isn't too much
    tags = models.ManyToManyField(Tag)
class Comment(models.Model):
    body = models.TextField()
    # Keeps the comments in order
    created_at = models.DateTimeField (default=timezone.now())
    # Creates the foregin key so the One to Many Relationship is established
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=1)

