from .models import Product, Photo, Comment
from django.forms import ModelForm


class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'content', 'transaction_code', 'price']


class ImageForm(ModelForm):

    class Meta:
        model: Photo
        fields = ['image', ]
