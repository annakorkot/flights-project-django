from django.db import models
from django_countries.fields import CountryField
from accounts.models import Customer , User


class Country(models.Model):

    name = models.CharField(max_length=100)
    country = CountryField()

    def __str__(self) -> str:
        return self.name

class AirlineCompany(models.Model):
    name =models.CharField(max_length=100 , unique=True)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="airline_companies")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE , related_name="airline_companies")

    def __str__(self) -> str:
        return self.name + " " + self.user_id.email

class Flight(models.Model):
    airline_company = models.ForeignKey(AirlineCompany , on_delete=models.CASCADE ,related_name="flights")
    origin_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="flights_as_origin")
    destination_country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name="flights_as_destination")
    departure_time = models.DateTimeField()
    landing_time = models.DateTimeField()
    remaning_tickets= models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'airline company: {self.airline_company.name} ,from: {self.origin_country.name} , to: {self.destination_country.name} ,departure: {self.departure_time} , landing: {self.landing_time}'

class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE , related_name="tickets")
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="tickets")

    def __str__(self) -> str:
        return f'{self.customer.first_name} {self.customer.last_name} ,from: {self.flight.origin_country.name} to: {self.flight.destination_country.name} departure_time: {self.flight.departure_time}'