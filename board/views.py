from django.shortcuts import render, redirect
from .models import Product, Photo, Comment
from .forms import ProductForm, ImageForm
# Create your views here.


def index(request):
    products = Product.objects.all()
    context = {'Products': products}
    return render(request, 'board/index.html', context)


def create_product(request):
    if request.method == 'POST':
        form_product = ProductForm(request.POST)
        form_image = ImageForm(request.FILES)
        if form_product.is_valid():
            product = form_product.save(commit=False)
            # 합치면 주석을 풀것
            # product.user = request.user
            product.save()
            if form_image.is_valid():
                image = form_image.save(commit=False)
                image.product = product.id
                image.save()
                redirect('')
    else:
        form_product = ProductForm()
        form_image = ImageForm()
    context = {'form_product': form_product,
               'form_image': form_image,
               }
    return render(request, 'board/product_form.html', context)


def board_product(request, product_id):
    pass


def board_product_delete(request, product_id):
    pass


def board_product_modify(request, product_id):
    pass


def board_comment_create(request, product_id):
    pass


def board_comment_delete(request, product_id, comment_id):
    pass

