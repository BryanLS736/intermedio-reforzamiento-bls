from django.urls import path
from . import views

urlpatterns = [
    path('category_message/', views.category_message, name='category_message'),
]
