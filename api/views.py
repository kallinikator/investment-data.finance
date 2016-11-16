from django.shortcuts import render
from django.http import Http404
from .models import Stock, PriceData


def list_view(request):
    head = Stock.objects.filter(favourite=False).order_by('symbol')[0:100]
    favs = Stock.objects.filter(favourite=True).order_by('symbol')[0:100]
    context = {"head" :  head, "favs" : favs}
    return render(request, 'frontend/entry.html', context)

def detail_view(request, symbol):
    try:
        stock = Stock.objects.get(symbol=symbol)
        price_data = stock.prices.order_by("date").iterator()
        fundamental_data = stock.fundamentals.order_by("end_date").all()
        context = {"stock" :  stock, "price_data" :  price_data, "fundamental_data" :  fundamental_data}
    except:
        raise Http404("This Symbol does not belong to any stock in our database! Did you type it right?")
    return render(request, 'frontend/chart.html', context)

"""def favourite(request, symbol):
    try:
        stock = Stock.objects.get(symbol=symbol)
    except:
        head = Stock.objects.filter(favourite=False).order_by('symbol')[0:100]
        favs = Stock.objects.filter(favourite=True).order_by('symbol')[0:100]
        context = {"head" :  head, "favs" : favs, "error_message" : "You didn´t select a valid stock!"}
        return render(request, 'frontend/entry.html', context)
    else:
        stock.favourite = True
        stock.save()
        head = Stock.objects.filter(favourite=False).order_by('symbol')[0:100]
        favs = Stock.objects.filter(favourite=True).order_by('symbol')[0:100]
        context = {"head" :  head, "favs" : favs}
        return render(request, 'frontend/entry.html', context)
    

def unfavourite(request, symbol):
    try:
        stock = Stock.objects.get(symbol=symbol)
        stock.favourite = False
        stock.save()
    except:
        head = Stock.objects.filter(favourite=False).order_by('symbol')[0:100]
        favs = Stock.objects.filter(favourite=True).order_by('symbol')[0:100]
        context = {"head" :  head, "favs" : favs, "error_message" : "You didn´t select a valid stock!"}
        return render(request, 'frontend/entry.html', context)
    else:
        stock.favourite = False
        stock.save()
        head = Stock.objects.filter(favourite=False).order_by('symbol')[0:100]
        favs = Stock.objects.filter(favourite=True).order_by('symbol')[0:100]
        context = {"head" :  head, "favs" : favs}
        return render(request, 'frontend/entry.html', context)"""