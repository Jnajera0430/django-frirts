from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    dateCompleted = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"id: {self.id} Project: {self.name}"


class Tasks(models.Model):
    tarea = models.CharField(max_length=200)
    descripcion = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    dateCompleted = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"id: {self.id} - Titulo:{self.tarea}"
