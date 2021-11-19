from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=200)
    def __str__(self):
            return self.country_name



class Cases(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    confirmed= models.IntegerField(null=True,blank=True)
    deaths = models.IntegerField(null=True,blank=True)
    recovered= models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f"{self.country} {self.confirmed} {self.deaths} {self.recovered}"

