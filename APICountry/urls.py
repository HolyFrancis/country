"""
URL configuration for APICountry project.

"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from api.views import CountryViewset
from api.views import CityViewset
from api.views import PhoneNumberValidationViewset

router = routers.SimpleRouter()

router.register('country', CountryViewset, basename='country')
router.register('city',CityViewset, basename='city')
#router.register('validate',PhoneNumberValidationViewset, basename='validate')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/validate/', PhoneNumberValidationViewset.as_view(), name='phone_validation'),
    # API externe
    path('country/',CountryViewset.country_list, name='country'),
    path('country_details/<str:country>/',CountryViewset.country_details, name='country_details'),
    path('country_details/cities/<str:country_iso>/',CountryViewset.cities_of_country, name='country_cities'),
    # Local API
    path('countries/',CountryViewset.countries_list, name='countries'),
    path('countries_details/<int:pk>',CountryViewset.countries_details, name='countries_details'),
    
    path('countries/cities/<int:pk>',CountryViewset.country_cities, name='city_details'),
]
