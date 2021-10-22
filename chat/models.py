from django.db import models

class Message(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nickname = models.CharField(max_length=20)
    text = models.CharField(max_length=255)
