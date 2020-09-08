from django.db import models
from PIL import Image
from django.contrib.auth import get_user_model

from django.utils.translation import ugettext_lazy as _

class House(models.Model):

	ENTIRE_PLACE  = 'entire_place'
	PRIVATE_ROOM  = 'private_room'
	SHARED_ROOM   = 'shared_room'

	HOUSE_TYPES = [
		(ENTIRE_PLACE,_('entire_place')),
		(PRIVATE_ROOM,_('private_room')),
		(SHARED_ROOM,_('shared_room')),
	]	

	title          = models.CharField(max_length=20)
	description    = models.CharField(max_length=150)
	cost           = models.FloatField()
	rooms          = models.IntegerField()
	garage         = models.BooleanField(default=False)
	wifi           = models.BooleanField(default=False)
	aircondition   = models.BooleanField(default=False)
	city           = models.CharField(max_length=30)
	country        = models.CharField(max_length=20)
	image          = models.ImageField(default='default.jpg',upload_to='images')
	lon            = models.FloatField()
	lat            = models.FloatField()
	av_from        = models.DateField()
	av_to          = models.DateField()

	#new fields added
	heat           = models.BooleanField(default=False)
	area           = models.FloatField()
	beds           = models.IntegerField()
	bedrooms       = models.IntegerField()
	bathrooms      = models.IntegerField()
	transport_desc = models.CharField(max_length=150)
	house_type     = models.CharField(max_length=15,choices=HOUSE_TYPES)

	host = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='host')

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

	def __str__(self):
		return self.title

'''class HouseImage(models.Model):


	image        = models.ImageField(default='default.jpg',upload_to='images')
	house        = models.ForeignKey(House,on_delete=models.CASCADE,related_name='house_img')

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

	def __str__(self):
		return self.image
'''