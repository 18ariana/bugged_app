from .models import Client as my_client
import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from clients.serializers import *
from random import randrange

client = Client()

class GetAllClients(TestCase):

    def get_client(self):
        random_value = randrange(1,my_client.objects.all().count())
        response = client.get(reverse('get_client', kwargs={'pk': random_value}))
        random_client = my_client.objects.get(pk=random_value)
        serializer = ClientSerializer(random_client)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def get_invalid_client(self):
        count = my_client.objects.all().count() + 1
        response = client.get(
            reverse('get_client', kwargs={'pk': count}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def get_all_clients(self):
       response = client.get(reverse('get_all_clients'))
       clients = my_client.objects.all()
       serializer = ClientSerializer(clients, many=True)
       self.assertEqual(response.data, serializer.data)
       self.assertEqual(response.status_code, status.HTTP_200_OK)