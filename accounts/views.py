from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as user_login, logout as user_logout
from django.contrib.auth.decorators import login_required
from .forms import (CustomUserCreationForm, PaymentInfoForm, CustomUserChangeForm, CustomPaymentChangeForm)
from .models import User, PaymentInfo
from django.http import HttpResponseForbidden


# Create your views here.
# accounts/signup
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form_user = CustomUserCreationForm(request.POST)
        if form_user.is_valid():
            user=form_user.save()
            form_payment = PaymentInfo.objects.create(user=user)
            form_payment.save()
            return redirect('board:board_index')
    else:
        form_user = CustomUserCreationForm()
    context = {
        'form_user' : form_user,
    }
    return render(request, 'accounts/signup.html', context)
        

@login_required
def add_payment_method(request):
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:my_page')
    else:
        form = PaymentInfoForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/add_payment_method.html', context)


@login_required
def modify_payment_method(request, payment_pk):
    payment = get_object_or_404(PaymentInfo, pk=payment_pk)
    if request.method == 'POST':
        form = PaymentInfoForm(request.POST, instance=payment)
        if form.is_valid():
            payment = form.save()
            return redirect('accounts:my_page')
    else:
        form = PaymentInfoForm()
    context = {'form' : form}
    return render(request, 'accounts/modify_user_info.html', context)



@login_required
def my_page(request, accounts_pk, payment_pk):
    user = get_object_or_404(User, pk=accounts_pk)
    if request.user != user:
        return HttpResponseForbidden()
    form_user = CustomUserChangeForm(request, request.POST)
    form_payment = CustomPaymentChangeForm(request, request.POST)
    context = {
        'form_user' : form_user,
        'form_payment' : form_payment,
    }
    return render(request, 'accounts/my_page.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def modify_user_info(request, accounts_pk):
    user_obj1 = get_object_or_404(User, pk=accounts_pk)
    if request.user != user_obj1.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user_obj1)
        if form.is_valid():
            user = form.save()
            return redirect('board:board_index')
    else: 
        user = CustomUserChangeForm(instance=user_obj1)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/modify_user_info.html', context)


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


