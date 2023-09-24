from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from home.forms import TransferForm
from home.models import Transfer
from exchange_currency import currency_consumer


@login_required
def home_page(request):
    #print((Transfer.objects.filter(receiver_username=request.user.username)).order_by('-timestamp')[:20])
    #incomes = {}
    #for elem in Transfer.objects.filter(receiver_username=request.user.username):
        #print(elem.timestamp)
    #print(incomes)
    #dramatiq_process.process()

    return render(request, 'home.html',
                  {'outcomes': (Transfer.objects.filter(sender_id=request.user.id)).order_by('-timestamp')[:20],
                'incomes_data':
                    (Transfer.objects.filter(receiver_username=request.user.username)).order_by('-timestamp')[:20]})


@login_required
def profile_page(request):
    profile_info = Profile.objects.all()
    for prf in profile_info:
        if prf.user_id == request.user.id:
            return render(request, 'profile_new.html', {'data': prf})
    return render(request, 'profile_new.html')


def deposit_page(request):
    return render(request, 'deposit.html')


@login_required
def deposit_button(request):
    if request.method == 'POST':
        # Получаем значение из формы
        profile_info = Profile.objects.all()
        amount = int(request.POST.get('amount'))
        for prf in profile_info:
            if prf.user_id == request.user.id:
                prf.value += amount
                prf.save()
        return render(request, 'deposit.html', {'data': amount})
    else:
        return render(request, 'deposit.html')


@login_required
def transactions_view(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            receiver_username = form.cleaned_data['receiver_username']
            amount = form.cleaned_data['amount']
            profile_info = Profile.objects.all()
            profile_balance = 0
            for prf in profile_info:
                if prf.user_id == request.user.id:
                    profile_balance = prf.value
                    if prf.value < amount:
                        return render(request, 'transactions_new.html',
                                      {'form': form, 'error_message': 'Недостаточно средств!',
                                       'success': False,
                                       'current_balance': profile_balance})

                    # Проверьте, существует ли пользователь с указанным логином
                    try:
                        receiver_user = User.objects.get(username=receiver_username)
                    except User.DoesNotExist:
                        return render(request, 'transactions_new.html',
                                      {'form': form, 'success': False,
                                       'error_message': 'Нет пользователя с таким логином',
                                       'current_balance': profile_balance})

                    # Создайте запись о переводе
                    for receive_profile in profile_info:
                        if receive_profile.user_id == receiver_user.id:
                            transfer = Transfer(sender=request.user, receiver_username=receiver_username, amount=amount)
                            transfer.save()

                            # Обновите балансы отправителя и получателя (псевдокод)
                            prf.value -= amount
                            receive_profile.value += amount
                            prf.save()
                            receive_profile.save()
                            messages.success(request, 'Перевод успешно выполнен!')
                            return render(request, 'transactions_new.html', {'success': True,
                                                                             'current_balance': prf.value,
                                                                             'data': amount,
                                                                             'receiver': receive_profile})
    else:
        form = TransferForm()
        profile_info = Profile.objects.all()
        for prf in profile_info:
            if prf.user_id == request.user.id:
                return render(request, 'transactions_new.html', {'form': form, 'current_balance': prf.value})
