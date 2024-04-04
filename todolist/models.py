from django.db import models
from django.contrib.auth.models import User # new
from datetime import datetime  


class TodoItem(models.Model):
    title = models.CharField(max_length=100)
    created_at= models.DateTimeField(default=datetime.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    
    def __str__(self):
        return f'({self.id}) {self.title}'

# Create your models here.
