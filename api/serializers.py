from rest_framework.serializers import ModelSerializer
from api.models import Country
from api.models import City

class CountrySerializer(ModelSerializer):
    
    class Meta:
        model = Country
        fields = ['id', 'name','population', 'capital']

class CountryDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Country
        fields = ['id', 'name', 'population', 'capital', 'gdp', 'pop_density', 'Iso2']
        
class CitySerializer(ModelSerializer):
    
    class Meta:
        model = City
        fields = fields = ['id', 'name', 'population']
        
