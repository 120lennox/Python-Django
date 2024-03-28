from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#tasks created by user stored here
class TasksFields(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    text_tasks = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.text_tasks