from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PaymentInfo

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
    )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name',
            'email',
            'birthday',
            'address',
        )


class PaymentInfoForm(forms.ModelForm):

    class Meta:
        model = PaymentInfo
        fields = '__all__'


class CustomPaymentChangeForm(UserChangeForm):

    class Meta:
        model = PaymentInfo
        fields = '__all__'