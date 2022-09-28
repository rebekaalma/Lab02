from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # ketika user di hapus, maka task juga akan terhapus 
    date = models.DateField()
    description = models.TextField()

    is_finished = models.BooleanField(default=False)

