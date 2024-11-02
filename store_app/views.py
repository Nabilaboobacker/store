from django.shortcuts import render
from . models import Product

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products.html', context)