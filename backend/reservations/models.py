from django.db import models
from django.contrib.auth import get_user_model

from houses.models import House

class Reservation(models.Model):

	tenant      = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='tenant')
	house       = models.ForeignKey('houses.House',on_delete=models.CASCADE,related_name='reservations')

	cost        = models.FloatField()
	people		= models.PositiveIntegerField()
	reserve_in  = models.DateField()
	reserve_out = models.DateField()


	def __str__(self):
		return f"Reserved from {self.reserve_in} to {self.reserve_out}"