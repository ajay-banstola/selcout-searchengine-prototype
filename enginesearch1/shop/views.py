from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.db.models import Q
from django.contrib.auth.models import User
from .config import pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpRequest, HttpResponseRedirect
from django.db.models import Count


app_name = 'shop'

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all().order_by("-rating")
    products = Product.objects.all().order_by("-number")
    users = User.objects.exclude(id=request.user.id)
    query = request.GET.get('q')
    if query=='':
        return HttpResponseRedirect('/')
    if query:
        categories = Category.objects.filter(Q(slug__icontains=query)| Q(url__icontains=query)).order_by("-rating")
    
    
    #if query:     
        products = Product.objects.filter(Q(slug__icontains=query) | Q(name__icontains=query) | Q(description__icontains=query)).order_by("number")
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    categories_counter = products.annotate(Count('id'))
    categories_count = len(categories_counter)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
		'categories_count':categories_count,
		'query':query,
        'users':users,
    }
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)




