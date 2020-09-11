from django.shortcuts import render

from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView

from .models import User,Message
from .serializers import UserSerializer,MessageSerializer 
from rest_framework.response import Response
from rest_framework import status


class UserList(generics.ListCreateAPIView):
	#permission_classes = [permissions.IsAdminUser,]
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = [IsOwnerOrAdmin,]
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

class MessageList(generics.ListCreateAPIView):
	#permission_classes = [permissions.IsAdminUser,]
	serializer_class = MessageSerializer

	def perform_create(self, serializer):
		serializer.save(sender=self.request.user)
		

	def get_queryset(self):
		receiver = self.request.user
		return Message.objects.filter(receiver=receiver)

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
	#permission_classes = [IsOwnerOrAdmin,]
	queryset = Message.objects.all()
	serializer_class = MessageSerializer