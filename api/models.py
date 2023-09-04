from django.db import models

# country model.
class Country(models.Model):
    
    name=models.CharField(max_length=250)
    capital=models.CharField(max_length=200)
    Iso2=models.CharField(max_length=20)
    surface_are=models.DecimalField(max_digits=10, decimal_places=2)
    gdp=models.IntegerField()
    population=models.IntegerField()
    pop_density=models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
# city model
class City(models.Model):
    name=models.CharField(max_length=200)
    population=models.IntegerField(default=False)
    is_capital=models.BooleanField(default=False)
    country=models.ForeignKey('api.Country',on_delete=models.CASCADE,related_name='cities')
    
    def __str__(self):
        return self.name
