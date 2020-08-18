#reviews/urls.py

from django.urls import path,include
from . import views
from .views import ReviewList,ReviewDetail

urlpatterns = [
	path('reviews/',views.ReviewList.as_view()),
	path('reviews/<int:pk>/',views.ReviewDetail.as_view()),
	path('house/reviews/',views.HouseReviewList.as_view()),
]