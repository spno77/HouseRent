from rest_framework import serializers

from .models import House
from django.contrib.auth import get_user_model
from reviews.serializers import ReviewSerializer


'''class HouseImageSerializer(serializers.ModelSerializer):

	house = serializers.PrimaryKeyRelatedField(source='house.id',queryset=House.objects.all())

	class Meta:
		model = HouseImage
		fields = ['house','image']
'''

class HouseSerializer(serializers.ModelSerializer):
	
	host    =    serializers.PrimaryKeyRelatedField(source='host.username',queryset=get_user_model().objects.all())
	reviews =    ReviewSerializer(many=True,read_only=True)
	#house_img  = HouseImageSerializer(many=True,read_only=True)

	class Meta:
		model = House
		fields = ['id','title','description','cost','rooms','garage',
		'wifi','aircondition','city','country','image','lon','lat','host','reviews',]

	def update(self,instance,validated_data):
		instance.id           = validated_data.get('id', instance.id)
		instance.title        = validated_data.get('title', instance.title)
		instance.description  = validated_data.get('description', instance.description)
		instance.cost         = validated_data.get('cost', instance.cost)
		instance.rooms        = validated_data.get('rooms', instance.rooms)
		instance.garage       = validated_data.get('garage', instance.garage)
		instance.wifi         = validated_data.get('wifi', instance.wifi)
		instance.aircondition = validated_data.get('aircondition', instance.aircondition)
		instance.city         = validated_data.get('city', instance.city)
		instance.country      = validated_data.get('country', instance.country)
		instance.image        = validated_data.get('image', instance.image)
		instance.lon          = validated_data.get('lon', instance.lon)
		instance.lat          = validated_data.get('lat', instance.lat)
		instance.host         = validated_data.get('host.username',instance.host)
		instance.save()
		return instance
		