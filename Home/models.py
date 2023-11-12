from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    due = models.DateField()
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)

    class Meta:
        ordering = ['due']

    def __str__(self):
        return self.title