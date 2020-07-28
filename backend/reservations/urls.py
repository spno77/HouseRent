
from django.urls import path,include
from . import views
from .views import ReservationList,ReservationDetail

urlpatterns = [
	path('reservations/',views.ReservationList.as_view()),
	path('reservations/<int:pk>/',views.ReservationDetail.as_view()),
]