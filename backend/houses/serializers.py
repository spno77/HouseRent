from rest_framework import serializers

from .models import House
from django.contrib.auth import get_user_model

class HouseSerializer(serializers.ModelSerializer):
	
	host = serializers.PrimaryKeyRelatedField(source='host.username',queryset=get_user_model().objects.all())

	class Meta:
		model = House
		fields = ['id','title','description','cost','rooms','garage',
		'wifi','aircondition','image','host']
