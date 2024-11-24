from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ticket(models.Model):
    issue = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=4)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tickets")

    def __str__(self):
        return self.issue
