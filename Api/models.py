from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name=models.CharField(max_length=100,default="none")
    book=models.CharField(max_length=10)
    def __str__(self):
        return f"{self.book} -- by  {self.name}"

    
