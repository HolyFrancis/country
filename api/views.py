import requests
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from api.models import Country
from api.models import City
from api.serializers import CountrySerializer
from api.serializers import CountryDetailSerializer
from api.serializers import CitySerializer

# Create your views here.
class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        
        # if the action is 'retrieve' then  we return the detail serializer
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()

class CountryViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    
    serializer_class = CountrySerializer
    
    detail_serializer_class = CountryDetailSerializer
    
    def get_queryset(self):
        return Country.objects.all()
    
    #country template rendering using API Country
    def country_list(request):
        api_url = 'https://api.api-ninjas.com/v1/country?name=France'
        response = requests.get(api_url, headers={'X-Api-Key': 'O9J2KXrDyZ+FVpAgQ5oBwQ==rGz0H3cKMZvDuGU6'}).json()
        return render(request, 'api/country.html',{'countries':response})
    
    #country template rendering using local API 
    def country_list(request):
        countries = Country.objects.all()
        return render(request, 'api/country.html',{'countries':countries})

    #country details template rendering using API Country
    def country_details(request):
        #country = get_object_or_404(Country)
        api_url = 'https://api.api-ninjas.com/v1/country?name=France'
        response = requests.get(api_url, headers={'X-Api-Key': 'O9J2KXrDyZ+FVpAgQ5oBwQ==rGz0H3cKMZvDuGU6'}).json()
        return render(request, 'api/country_details.html', {'country': response})
    
    #country details template rendering using local API Country
    def country_details(request, pk):
        country = get_object_or_404(Country, pk=pk)	
        return render(request, 'api/country_details.html', {'country': country})

class CityViewset(MultipleSerializerMixin, ModelViewSet):
    
    serializer_class = CitySerializer
    
    def get_queryset(self):
        query_set = City.objects.all()
        country = self.request.GET.get('country')
        if country is not None:
            return query_set.filter(country=country)
        return query_set
    
    def city_details(self, request, pk):
        city = get_object_or_404(City, pk=pk)
        return render(request, 'city_details.html', {'cities': city})
