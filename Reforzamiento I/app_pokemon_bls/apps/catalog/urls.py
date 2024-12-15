from django.urls import path
from . import views

urlpatterns = [
    path('catalog_message/', views.catalog_message, name='catalog_message'),
]
