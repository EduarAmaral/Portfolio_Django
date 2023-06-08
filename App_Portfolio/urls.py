from django.urls import path
from . import views

urlpatterns = [
    path('Portfolio/', views.Portfolio, name='Portfolio')
]