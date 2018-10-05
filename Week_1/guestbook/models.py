from django.db import models
from django.conf import settings
# Create your models here.

class Vocabulary(models.Model):
	"""docstring for Vocabulary"""
	vocab = models.CharField(max_length=20)
	meaning = models.CharField(max_length=50)
	def __str__(self):
		return self.vocab + " " + self.meaning
		