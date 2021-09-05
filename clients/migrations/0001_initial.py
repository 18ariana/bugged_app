# Generated by Django 3.1.4 on 2021-05-18 11:29

from django.db import migrations, models
import django.db.models.deletion
import russian_fields.inn
import russian_fields.kpp
import russian_fields.ogrn


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('inn', russian_fields.inn.INNBusinessField(mode='legal')),
                ('kpp', russian_fields.kpp.KPPField()),
                ('ogrn', russian_fields.ogrn.OGRNField()),
                ('email', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=16)),
                ('site_url', models.CharField(max_length=64)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clients', to='clients.city')),
            ],
        ),
    ]