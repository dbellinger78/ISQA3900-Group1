from django.shortcuts import get_object_or_404, render
from .models import Category, Product


def categories(request):
    return {'categories': Category.objects.all}


def product_all(request):
    products = Product.objects.all()
    return render(request, 'estore/home.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'estore/products/detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'estore/products/category.html', {'category': category, 'products': products})
