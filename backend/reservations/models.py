from django.db import models
from django.contrib.auth import get_user_model

from houses.models import House

class Reservation(models.Model):

	tenant      = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='tenant')
	house       = models.ForeignKey('houses.House',on_delete=models.CASCADE,related_name='house')

	cost        = models.FloatField()
	
	reserve_in  = models.DateField()
	reserve_out = models.DateField()


	def __str__(self):
		return f"User {self.tenant} reserved {self.house}"