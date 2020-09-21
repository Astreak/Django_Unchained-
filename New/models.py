from django.db import models
from django.contrib.auth.models import User
import datetime
class Todo(models.Model):
    text=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.datetime.now())
    def __str__(self):
        return f"{self.text}";



