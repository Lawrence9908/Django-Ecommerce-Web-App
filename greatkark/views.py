from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def home(request):
    products  = Product.objects.all().filter(is_available=True)
    products_count = products.count()
    return render(request, 'home.html', {
        'products': products,
        'product_count':products_count,

    } )
