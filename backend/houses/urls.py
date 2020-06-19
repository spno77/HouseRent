# houses/urls.py

from django.urls import path,include
from . import views
from .views import HouseList,HouseDetail

urlpatterns = [
	path('houses/',views.HouseList.as_view()),
	path('houses/<int:pk>/',views.HouseDetail.as_view()),

]
