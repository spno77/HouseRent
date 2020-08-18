from rest_framework import serializers

from .models import Review
from django.contrib.auth import get_user_model
from reservations.models import Reservation

from reservations.serializers import ReservationSerializer
from houses.models import House


class ReviewSerializer(serializers.ModelSerializer):
	
	reservation = serializers.PrimaryKeyRelatedField(source='reservation.id',queryset=Reservation.objects.all())
	reviewer = 	serializers.PrimaryKeyRelatedField(source='reviewer.username',queryset=get_user_model().objects.all())
	house = serializers.PrimaryKeyRelatedField(source='house.title',queryset=House.objects.all())

	class Meta:
		model = Review
		fields = ['id','content','date_created','rating','reservation','reviewer','house']