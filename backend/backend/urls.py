#Project level urls

from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/',include('houses.urls')),
    path('api/v1/',include('users.urls')),

    #JWT endpoints
    path('api-token-auth/', obtain_jwt_token),
	path('api-token-refresh/', refresh_jwt_token),

	#rest-auth endpoints
	path('api/v1/rest-auth/', include('rest_auth.urls')),

	#all-auth endpoints
	path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)