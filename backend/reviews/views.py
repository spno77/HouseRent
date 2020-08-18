from django.shortcuts import render

from rest_framework import generics,filters

from .models import Review
from .serializers import ReviewSerializer

from reservations.models import Reservation
from houses.models import House


class ReviewList(generics.ListCreateAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	
	def perform_create(self, serializer):
		pk1 = self.request.data['reservation']
		reservation = Reservation.objects.get(pk=pk1)
		
		pk2 = self.request.data['house']
		house = House.objects.get(pk=pk2)
		serializer.save(reviewer=self.request.user,reservation=reservation,house=house)

class HouseReviewList(generics.ListCreateAPIView):
	serializer_class = ReviewSerializer

	def get_queryset(self):
		pk = self.request.data['house']
		house = House.objects.get(pk=pk)
		return Review.objects.filter(house=house)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer