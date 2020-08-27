from django.db import models
from PIL import Image
from django.contrib.auth import get_user_model

class House(models.Model):

	title        = models.CharField(max_length=20)
	description  = models.CharField(max_length=100)
	cost         = models.FloatField()
	rooms        = models.IntegerField()
	garage       = models.BooleanField(default=False)
	wifi         = models.BooleanField(default=False)
	aircondition = models.BooleanField(default=False)
	city         = models.CharField(max_length=30)
	country      = models.CharField(max_length=20)
	image        = models.ImageField(default='default.jpg',upload_to='images',null=True)

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