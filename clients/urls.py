from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientListView.as_view()),
    path('<int:pk>/', views.ClientView.as_view()),
]
