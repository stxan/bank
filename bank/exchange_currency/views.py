from django.shortcuts import render
import json, xml
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import CurrencyRate
import pika
# Create your views here.

@login_required
def currency_page(request):
    usd_currency = CurrencyRate.objects.get(currency_code='USD')
    eur_currency = CurrencyRate.objects.get(currency_code='EUR')
    gbp_currency = CurrencyRate.objects.get(currency_code='GBP')
    gel_currency = CurrencyRate.objects.get(currency_code='GEL')
    aed_currency = CurrencyRate.objects.get(currency_code='AED')
    kzt_currency = CurrencyRate.objects.get(currency_code='KZT')
    kgs_currency = CurrencyRate.objects.get(currency_code='KGS')
    cny_currency = CurrencyRate.objects.get(currency_code='CNY')
    tjs_currency = CurrencyRate.objects.get(currency_code='TJS')
    uzs_currency = CurrencyRate.objects.get(currency_code='UZS')
    jpy_currency = CurrencyRate.objects.get(currency_code='JPY')
    thb_currency = CurrencyRate.objects.get(currency_code='THB')
    primary = [usd_currency, eur_currency, gbp_currency, cny_currency, jpy_currency, gel_currency, aed_currency,
               kzt_currency, kgs_currency, tjs_currency, uzs_currency, thb_currency]
    return render(request, 'exchange_currency.html',
                  {'currencies': primary})
