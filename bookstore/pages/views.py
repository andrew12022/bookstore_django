from django.shortcuts import render


def about(request):
    return render(request, 'pages/about.html')


def promo(request):
    return render(request, 'pages/promo.html')
