from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Product


def index(request):
    items = Product.objects.all()
    context = {
        "items": items
    }
    return render(request, "myapp/index.html", context)


def index_item(request, id):
    item = Product.objects.get(id=id)
    context = {
        "item": item
    }
    return render(request, "myapp/detail.html", context)
