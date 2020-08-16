from django.db import models
from PIL import Image
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

from reservations.models import Reservation

class Review(models.Model):
	content      = models.CharField(max_length=100)
	date_created = models.DateField(auto_now=True)
	rating		 = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])

	reservation  = models.ForeignKey('reservations.Reservation',on_delete=models.CASCADE,related_name='reservation') 
	reviewer     = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='reviewer')

	def __str__(self):
		return self.content
