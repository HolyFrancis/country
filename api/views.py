import requests
import phonenumbers
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from api.models import Country
from api.models import City
from api.models import PhoneNumber
from api.serializers import CountrySerializer
from api.serializers import CountryDetailSerializer
from api.serializers import CitySerializer
from api.serializers import PhoneNumberSerializer

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

    #country details template rendering using API Country
    def country_details(request):
        #country = get_object_or_404(Country)
        api_url = 'https://api.api-ninjas.com/v1/country?name=France'
        response = requests.get(api_url, headers={'X-Api-Key': 'O9J2KXrDyZ+FVpAgQ5oBwQ==rGz0H3cKMZvDuGU6'}).json()
        return render(request, 'api/country_details.html', {'country': response})


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


class PhoneNumberValidationViewset(ModelViewSet):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                return Response({'error': 'Numéro de téléphone invalide.'}, status=400)

            # Récupérez les informations associées au numéro de téléphone
            country = phonenumbers.region_code_for_number(parsed_number)
            

            # Créez une instance de PhoneNumber avec les données associées
            phone_data = {
                'country': country,
                'phone_number': phone_number,
                
            }
            serializer = PhoneNumberSerializer(data=phone_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        except phonenumbers.phonenumberutil.NumberParseException as e:
            return Response({'error': "Erreur lors de l'analyse du numéro de téléphone."}, status=400)