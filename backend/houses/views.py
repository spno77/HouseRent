from django.shortcuts import render

from rest_framework import generics,filters

from .models import House,HouseImage
from .serializers import HouseSerializer,HouseImageSerializer

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


class HouseImageList(generics.ListCreateAPIView):
	queryset = HouseImage.objects.all()
	serializer_class = HouseImageSerializer
	
	#def get_queryset(self):
	#	house = self.request.data['house']
	#	return HouseImage.objects.filter(house=house)


	def perform_create(self, serializer):
		pk = self.request.data['house']
		house = House.objects.get(pk=pk)
		serializer.save(house=house)	

	
class HouseImageDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = HouseImage.objects.all()
	serializer_class = HouseImageSerializer