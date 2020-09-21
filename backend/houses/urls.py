# houses/urls.py

from django.urls import path,include
from . import views
from .views import HouseList,HouseDetail,HostHouseList
#HouseImageList,HouseImageDetail

urlpatterns = [
	path('houses/',views.HouseList.as_view()),
	path('houses/<int:pk>/',views.HouseDetail.as_view()),
	path('host/houses/',views.HostHouseList.as_view()),
	#path('houses/search/',views.HouseSearch.as_view()),
	#path('houses/images',views.HouseImageList.as_view()),
	#path('houses/<int:pk>/images',views.HouseImageDetail.as_view()),
]
