from django.db import models
class quiz(models.Model):
    question=models.CharField(max_length=255)
    choice1=models.CharField(max_length=255)
    choice2=models.CharField(max_length=255)
    choice3=models.CharField(max_length=255)
    choice4=models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
# Create your models here.
