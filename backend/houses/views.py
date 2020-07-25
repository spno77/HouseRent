from django.shortcuts import render

from rest_framework import generics,filters

from .models import House
from .serializers import HouseSerializer


class HouseList(generics.ListCreateAPIView):
	queryset = House.objects.all()
	serializer_class = HouseSerializer
	filter_backends = [filters.SearchFilter,filters.OrderingFilter]
	search_fields = ['title','description']
	ordering_fields = ['cost']

	def perform_create(self, serializer):
		serializer.save(host=self.request.user)

	

class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = House.objects.all()
	serializer_class = HouseSerializer
