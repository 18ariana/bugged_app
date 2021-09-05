from rest_framework import generics
from .models import *
from .serializers import *


class ClientListView(generics.ListCreateAPIView):
    queryset = Client.objects.all().order_by('id')
    serializer_class = ClientSerializer
    filterset_fields = [
        'state', 'company_name', 'occupation', 'client_type',
        'inn', 'kpp', 'ogrn', 'email', 'phone_number', 'site_url', 'city'
    ]


class ClientView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

