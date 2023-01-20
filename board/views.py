from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Photo, Comment
from .forms import ProductForm, ImageForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe, require_http_methods, require_POST
# Create your views here.


@require_safe
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'board/index.html', context)


@login_required()
@require_http_methods(['GET','POST'])
def create_product(request):
    if request.method == 'POST':
        form_product = ProductForm(request.POST)
        form_image = ImageForm(request.POST, request.FILES)
        if form_product.is_valid():
            product = form_product.save(commit=False)
            product.user = request.user
            product.save()

            if form_image.is_valid():
                image = form_image.save(commit=False)
                image.product = product
                image.user = request.user
                image.save()
                return redirect('board:board_product', product.id)
    else:
        form_product = ProductForm()
        form_image = ImageForm()
    context = {'form_product': form_product,
               'form_image': form_image,
               }
    return render(request, 'board/product_form.html', context)


@require_safe
def board_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}

    return render(request, 'board/product_detail.html', context)


def board_product_delete(request, product_id):
    pass


def board_product_modify(request, product_id):
    pass


def board_comment_create(request, product_id):
    pass


def board_comment_delete(request, product_id, comment_id):
    pass

