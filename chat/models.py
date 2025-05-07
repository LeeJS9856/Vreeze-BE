from django.db import models
from django.contrib.auth.models import User


class UserQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    session_id = models.CharField(max_length=100)