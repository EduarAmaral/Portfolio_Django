from django.urls import path
from . import views

urlpatterns = [
    path('area_cad/', views.area_cad, name='area_cad')
]