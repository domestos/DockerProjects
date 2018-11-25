"""   URLS INVENTORY """
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import *

# це список і порядок правил має значення
# This is a list and the order of the rules matters
urlpatterns = [
    path('', main_point, name='inventory_url'),

]
