from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name = models.CharField(max_length=255)

class Client(models.Model):
    account_number = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField()
    inn = models.CharField(max_length=12)
    responsible_person = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    status = models.CharField(max_length=20, default='Не в работе')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
