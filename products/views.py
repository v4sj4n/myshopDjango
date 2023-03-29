from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "products/home.html")


def product_cat(request, product):
    if product in ["suits", "dresses", "shirts", "shoes"]:
        return HttpResponse(f"Here is our {product}")
    else:
        return HttpResponse(f"{product} not found")


def signup(request):
    return render(request, "products/signup.html")
