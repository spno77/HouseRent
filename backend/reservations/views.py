from django.shortcuts import render

from rest_framework import generics,filters

from .models import Reservation
from .serializers import ReservationSerializer

from houses.models import House


class ReservationList(generics.ListCreateAPIView):
	queryset = Reservation.objects.all()
	serializer_class = ReservationSerializer
	
	def perform_create(self, serializer):
		pk = self.request.data['house']
		house = House.objects.get(pk=pk)
		serializer.save(tenant=self.request.user,house=house)


class ReservationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Reservation.objects.all()
	serializer_class = ReservationSerializer
