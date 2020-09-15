from rest_framework           import serializers

from .models                  import House
from django.contrib.auth      import get_user_model
from reviews.serializers      import ReviewSerializer
from reservations.serializers import ReservationSerializer
from users.serializers        import UserSerializer

'''class HouseImageSerializer(serializers.ModelSerializer):

	house = serializers.PrimaryKeyRelatedField(source='house.id',queryset=House.objects.all())

	class Meta:
		model = HouseImage
		fields = ['house','image']
'''

class HouseSerializer(serializers.ModelSerializer):
	
	#host    =    serializers.PrimaryKeyRelatedField(source='host.username',queryset=get_user_model().objects.all())
	host =       UserSerializer(read_only=True)
	reviews =    ReviewSerializer(many=True,read_only=True)
	#house_img  = HouseImageSerializer(many=True,read_only=True)
	reservations = ReservationSerializer(many=True,read_only=True)

	class Meta:
		model = House
		fields = ['id','title','description','cost','garage',
		'wifi','aircondition','city','country','image','lon','lat',
		'av_from','av_to','host','reviews','reservations',
		'heat','area','beds','bedrooms','bathrooms','transport_desc',
		'house_type','people_num','people_max','rules','plus_cost']

	def update(self,instance,validated_data):
		instance.id             = validated_data.get('id', instance.id)
		instance.title          = validated_data.get('title', instance.title)
		instance.description    = validated_data.get('description', instance.description)
		instance.cost           = validated_data.get('cost', instance.cost)
		#instance.rooms          = validated_data.get('rooms', instance.rooms)
		instance.garage         = validated_data.get('garage', instance.garage)
		instance.wifi           = validated_data.get('wifi', instance.wifi)
		instance.aircondition   = validated_data.get('aircondition', instance.aircondition)
		instance.city           = validated_data.get('city', instance.city)
		instance.country        = validated_data.get('country', instance.country)
		instance.image          = validated_data.get('image', instance.image)
		instance.lon            = validated_data.get('lon', instance.lon)
		instance.lat            = validated_data.get('lat', instance.lat)
		#instance.host           = validated_data.get('host.username',instance.host)
		#new fields
		instance.heat           = validated_data.get('heat',instance.heat)
		instance.area           = validated_data.get('area',instance.area)
		instance.beds           = validated_data.get('beds',instance.beds)
		instance.bedrooms       = validated_data.get('bedrooms',instance.bedrooms)
		instance.bathrooms      = validated_data.get('bathrooms',instance.bathrooms)
		instance.transport_desc = validated_data.get('transport_desc',instance.transport_desc)
		instance.house_type     = validated_data.get('house_type',instance.house_type)

		instance.people_num     = validated_data.get('people_num',instance.people_num)
		instance.people_max     = validated_data.get('people_max',instance.people_max)
		instance.rules          = validated_data.get('rules',instance.rules)
		instance.plus_cost      = validated_data.get('plus_cost',instance.plus_cost)

		instance.av_from        = validated_data.get('av_from',instance.av_from)
		instance.av_to          = validated_data.get('av_to',instance.av_to)

		instance.save()
		return instance
		