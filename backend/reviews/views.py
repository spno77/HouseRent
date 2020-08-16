from django.shortcuts import render

from rest_framework import generics,filters

from .models import Review
from .serializers import ReviewSerializer

from reservations.models import Reservation


class ReviewList(generics.ListCreateAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer
	
	def perform_create(self, serializer):
		pk = self.request.data['reservation']
		reservation = Reservation.objects.get(pk=pk)
		serializer.save(reviewer=self.request.user,reservation=reservation)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Review.objects.all()
	serializer_class = ReviewSerializer