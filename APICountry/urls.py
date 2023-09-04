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
    path('api/', include(router.urls)),
    path('countries/',CountryViewset.country_list, name='countries'),
    path('countries/<int:pk>',CountryViewset.country_details, name='country_details'),
    path('cities/',CityViewset.as_view({'get': 'list'}), name='cities'),
    path('cities/<int:pk>',CityViewset.city_details, name='city_details')
]
