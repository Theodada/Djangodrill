from django.db import models

# Create your models here.
class Todo(models.Model): #table in the database
    title = models.CharField(max_length=200) #columns in table
    description = models.CharField(max_length=200)
    done = models. BooleanField(default=False)
    createAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
