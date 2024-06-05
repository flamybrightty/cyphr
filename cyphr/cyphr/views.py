from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def info(request):
    return render(request, 'main/info.html')


def ctf(request):
    return render(request, 'main/ctf.html')


def products(request):
    return render(request, 'main/products.html')
