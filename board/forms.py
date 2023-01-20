from .models import Product, Photo, Comment
from django import forms


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'content', 'transaction_code', 'price')


class ImageForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ('image', )
