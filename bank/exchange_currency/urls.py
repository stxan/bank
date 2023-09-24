from django.urls import path
from . import views



url_patterns = [
    path('/exchange_currency/', views.currency_page, name='exchange_currency'),
    ]