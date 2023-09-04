"""
URL configuration for APICountry project.

"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from api.views import CountryViewset
from api.views import CityViewset

router = routers.SimpleRouter()

router.register('country', CountryViewset, basename='country')
router.register('city',CityViewset, basename='city')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
