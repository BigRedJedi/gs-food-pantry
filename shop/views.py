from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

# Create your views here.

# Added per Cart (see page 229)

from django.contrib.auth.decorators import login_required
from .forms import *


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                        'shop/product/list.html',
                        {'category': category,
                            'categories': categories,
                                'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                    id=id,
                                    slug=slug,
                                    available=True)
    print("test")
    return render(request,
                        'shop/product/detail.html',
                        {'product': product})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


# Test Employee Product CRUD Methods

'''

@login_required
def product_list(request):
    items = Item.objects.filter(expired_date__lte=timezone.now())
    return render(request, 'shop/product_list.html', {'items': items})
'''


'''
@login_required
def product_new(request):
   if request.method == "POST":
       form = ItemForm(request.POST)
       if form.is_valid():
           item = form.save(commit=False)
           item.created_date = timezone.now()
           item.save()
           items = Item.objects.filter(expired_date__lte=timezone.now())
           return render(request, 'shop/product_list.html',
                         {'items': items})
   else:
       form = ItemForm()
       # print("Else")
   return render(request, 'shop/emp_product_new.html', {'form': form})


@login_required
def product_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
       form = ItemForm(request.POST, instance=item)
       if form.is_valid():
           item = form.save()
           # investment.customer = investment.id
           item.updated_date = timezone.now()
           item.save()
           items = Item.objects.filter(expired_date__lte=timezone.now())
           return render(request, 'shop/emp_product_list.html',
                         {'items': items})
    else:
       # print("else")
       form = ItemForm(instance=item)
       return render(request, 'shop/emp_product_edit.html', {'form': form})


@login_required
def product_delete(request,pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    items = Item.objects.filter(expired_date__lte=timezone.now())
    return render(request, 'shop/emp_product_list.html', {'items': items})
'''
