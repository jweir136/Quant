from django.db import models

# Create your models here.
class Contact(models.Model):
	name = models.CharField(max_length=1000)
	email = models.CharField(max_length=1000)
	message = models.CharField(max_length=100000)
	
class Visitor(models.Model):
	ip = models.CharField(max_length=100)
	date = models.CharField(max_length=1000)
	
	def __str__(self):
		return "{}\t{}".format(self.ip, self.date.split('.')[0])