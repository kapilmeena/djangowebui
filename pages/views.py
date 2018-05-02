from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the page index.")


def products(request):
    return render(request, "pages/products.html")


def price(request):
    return render(request, "pages/pricing.html")
