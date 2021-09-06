from django.db import models
from russian_fields import INNBusinessField, KPPField, OGRNField
from phonenumber_field.modelfields import PhoneNumberField

class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class INNBusinessField2(INNBusinessField):
    def from_db_value(self, value, expression, connection, context=None):
        return self.to_python(value)

class KPPField2(KPPField):
    def from_db_value(self, value, expression, connection, context=None):
        return self.to_python(value)

class OGRNField2(OGRNField):
    def from_db_value(self, value, expression, connection, context=None):
        return self.to_python(value)


class Client(models.Model):
    city = models.ForeignKey('City', models.PROTECT, related_name='clients')
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    inn = INNBusinessField2()
    kpp = KPPField2()
    ogrn = OGRNField2()
    email = models.EmailField()
    phone_number = PhoneNumberField()
    site_url = models.URLField()

