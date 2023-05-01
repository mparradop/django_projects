from django.db import models
from main import models as core


# Create your models here.

class Todo(models.Model):
    title = models.TextField()
    status = models.ForeignKey(core.Status,on_delete=models.CASCADE)
    responsible =  models.ForeignKey(core.Employee, on_delete=models.CASCADE)
    description = models.CharField("Descriptions",max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
