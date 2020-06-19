from django.db import models

class House(models.Model):

	title  = models.CharField(max_length=20)
	description = models.CharField(max_length=100)
	cost = models.FloatField()
	rooms = models.IntegerField()
	garage = models.BooleanField(default=False)
	wifi = models.BooleanField(default=False)
	aircondition = models.BooleanField(default=False)


	def __str__(self):
		return self.title