from django.db import models
from PIL import Image

class House(models.Model):

	title  = models.CharField(max_length=20)
	description = models.CharField(max_length=100)
	cost = models.FloatField()
	rooms = models.IntegerField()
	garage = models.BooleanField(default=False)
	wifi = models.BooleanField(default=False)
	aircondition = models.BooleanField(default=False)
	image = models.ImageField(default='default.jpg',upload_to='images')

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)


	def __str__(self):
		return self.title