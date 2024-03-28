from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    grade = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.name}, {self.grade}'
    
