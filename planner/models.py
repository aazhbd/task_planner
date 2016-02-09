from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=70, blank=False)
    status = models.CharField(max_length=50, default='To Do', blank=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2, blank=False)

    enabled = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        pass
