from rest_framework.serializers import ModelSerializer
from api.models import Country
from api.models import City
from api.models import PhoneNumber


class CitySerializer(ModelSerializer):
    
    class Meta:
        model = City
        fields = fields = ['id', 'name', 'population']

class CountrySerializer(ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['id', 'name','population', 'capital','cities']

class CountryDetailSerializer(ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['id', 'name', 'population', 'capital', 'gdp', 'pop_density', 'Iso2', 'cities']
        
class PhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = '__all__'     
