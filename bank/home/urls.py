import exchange_currency.views
from . import views
from .views import home_page, deposit_button, profile_page, deposit_page, transactions_view
from django.urls import path
urlpatterns = [
    path('', home_page),
    path('deposit/', deposit_button, name='deposit_button'),
    path('profile/', profile_page),
    path('deposit/', deposit_page),
    path('transactions_new/', views.transactions_view, name='transactions_new'),
    path('exchange_currency/', exchange_currency.views.currency_page),
]