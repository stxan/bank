from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_registration.backends.one_step.views import RegistrationView
from accounts.models import Profile
from django.contrib.auth.models import User
from django.urls import include
from accounts.models import Profile
from django.core.exceptions import ValidationError

def reg_suc(request):
    users = User.objects.all()
    Profile.objects.create(value=0, user_id=users[len(users) - 1].id)
    return render(request, 'django_registration/registration_successful.html')


