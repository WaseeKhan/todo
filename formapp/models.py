from django.db import models

# Create your models here.

class FormModel(models.Model):
	name = models.CharField(max_length=20)
	mob = models.CharField(max_length=10)
	std = models.CharField(max_length=10)