from django.shortcuts import render

from rest_framework import generics,filters

from .models import House
from .serializers import HouseSerializer

from django_filters.rest_framework import DjangoFilterBackend
from url_filter.integrations.drf import DjangoFilterBackend

class HouseList(generics.ListCreateAPIView):
	queryset = House.objects.all()
	serializer_class = HouseSerializer
	filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
	#search_fields = ['title','description']
	#filterset_fields = ['country', 'cost']
	filter_fields = ['av_from','av_to','city','country','people_num']
	ordering_fields = ['cost']

	def perform_create(self, serializer):
		serializer.save(host=self.request.user)

	def perform_update(self,serializer):
		serializer.save(host=self.request.user)

	def get_queryset(self):
		queryset = House.objects.all()
		book_from = self.request.query_params.get('book_from', None)
		book_to   = self.request.query_params.get('book_to', None)
		if book_from is not None:
			queryset = queryset.filter(av_from__lte=book_from,av_to__gte=book_to).exclude(
				reservations__reserve_in__lte=book_to,reservations__reserve_out__gte=book_from)
		return queryset


class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = House.objects.all()
	serializer_class = HouseSerializer


class HostHouseList(generics.ListCreateAPIView):
	serializer_class = HouseSerializer
	filter_backends = [filters.OrderingFilter,]

	ordering_fields = ['cost']

	def get_queryset(self):
		host = self.request.user
		return House.objects.filter(host=host)


'''
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
'''