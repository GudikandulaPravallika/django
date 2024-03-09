# chatbot/models.py
from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField()
