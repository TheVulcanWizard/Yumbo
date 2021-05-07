
from django.urls import path
from . import views

urlpatterns = [
    path('calendar/', views.schedule, name='calendar'),
    path('calendar/<int:year>/<int:week>/<int:day>/', views.add_meal, name='add-meal'),
]