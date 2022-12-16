from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    user = models.OneToOneField(User,null=True, on_delete=models.SET_NULL,related_name ="customers")

    def __str__(self) -> str:
        return f'{self.first_name} ,{self.last_name}'


class Administrator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_id = models.OneToOneField(User , unique=True , on_delete=models.CASCADE , related_name='administrators')

    def __str__(self) -> str:
        return f'{self.first_name} ,{self.last_name}'
