from django.db import models
from django.utils import timezone

class Provincia(models.Model):
	codigo = models.IntegerField(primary_key=True)
	provincia = models.CharField(max_length=60)
	
	def __str__(self):
		return str(self.codigo)+' '+self.provincia
