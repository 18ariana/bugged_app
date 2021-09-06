from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientListView.as_view(), name='get_all_clients'),
    path('<int:pk>/', views.ClientView.as_view(), name='get_client'),
]
