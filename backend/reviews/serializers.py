from rest_framework import serializers

from .models import Review
from django.contrib.auth import get_user_model
from reservations.models import Reservation

from reservations.serializers import ReservationSerializer

class ReviewSerializer(serializers.ModelSerializer):
	
	reservation = serializers.PrimaryKeyRelatedField(source='reservation.id',queryset=Reservation.objects.all())
	reviewer = 	serializers.PrimaryKeyRelatedField(source='reviewer.username',queryset=get_user_model().objects.all())


	class Meta:
		model = Review
		fields = ['id','content','date_created','rating','reservation','reviewer',]