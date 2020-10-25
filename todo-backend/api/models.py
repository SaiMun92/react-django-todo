from django.db import models


# Create your models here.
class Todo(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    label = models.CharField(max_length=200)
    done = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.label
