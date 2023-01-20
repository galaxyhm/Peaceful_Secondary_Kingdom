from django import forms
from .models import User, PaymentInfo

class UserForm(forms.ModelForm):

    class meta:
        model = User
        fields = (
            'password',
            'username',
            'firstname', 
            'lastname',
            'email',
            'birthday',
            'address',
    )


class PaymentInfoForm(forms.ModelForm):

    class meta:
        model = PaymentInfo
        fields = '__all__'