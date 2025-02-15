from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, related_name="tasks", null=True)

    def __str__(self):
        return self.title
