from django.db import models
from russian_fields import INNBusinessField, KPPField, OGRNField


class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Client(models.Model):
    city = models.ForeignKey('City', models.PROTECT, related_name='clients')
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    inn = INNBusinessField()
    kpp = KPPField()
    ogrn = OGRNField()
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=16)
    site_url = models.CharField(max_length=64)

