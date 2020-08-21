from django.shortcuts import render

from rest_framework import generics,filters

from .models import House
from .serializers import HouseSerializer

from django_filters.rest_framework import DjangoFilterBackend

class HouseList(generics.ListCreateAPIView):
	queryset = House.objects.all()
	serializer_class = HouseSerializer
	filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
	#search_fields = ['title','description']
	filterset_fields = ['country', 'cost']
	ordering_fields = ['cost']

	def perform_create(self, serializer):
		serializer.save(host=self.request.user)

	def perform_update(self,serializer):
		serializer.save(host=self.request.user)


class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = House.objects.all()
	serializer_class = HouseSerializer
