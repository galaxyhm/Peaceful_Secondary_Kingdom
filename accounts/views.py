from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .forms import PaymentInfoForm

# Create your views here.
# accounts/signup
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board:board_index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)
        

@login_required
@require_http_methods(['GET', 'POST'])
def insert_payment_info(request):
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('board:board_index')
    else:
        form = PaymentInfoForm()
    context = {'form' : form}
    return render(request, 'accounts/insert_payment_info.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_login(request, form.get_user())
            return redirect('board:board_index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


@require_safe
def logout(request):
    user_logout(request)
    return redirect('board:board_index')


