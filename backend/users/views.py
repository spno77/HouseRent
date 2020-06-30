from django.shortcuts import render

from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer 
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