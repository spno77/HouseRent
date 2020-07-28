from rest_framework import serializers

from .models import Reservation
from houses.models import House
from django.contrib.auth import get_user_model

class ReservationSerializer(serializers.ModelSerializer):
	
	tenant = serializers.PrimaryKeyRelatedField(source='tenant.username',queryset=get_user_model().objects.all())
	house = serializers.PrimaryKeyRelatedField(source='house.title',queryset=House.objects.all())


	class Meta:
		model = Reservation
		fields = ['id','cost','days','tenant','house',]