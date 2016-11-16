from django.http import Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Stock
from rest.serializers import StockSerializer, DetailSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
		
@csrf_exempt
def Stock_list(request):
    """
    List all Stocks, or create a new Stock.
    """
    if request.method == 'GET':
        Stocks = Stock.objects.all()
        serializer = StockSerializer(Stocks, many=True)
        return JSONResponse(serializer.data)

    """elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StockSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)"""

@csrf_exempt
def Stock_detail(request, symbol):
        """
        Retrieve, update or delete a Stock.
        """
        try:
                SingleStock = Stock.objects.get(symbol=symbol)
        except:
                raise Http404("This Symbol does not belong to any stock in our database! Did you type it right?")

        if request.method == 'GET':
                serializer = DetailSerializer(SingleStock)
                return JSONResponse(serializer.data)

        """elif request.method == 'PUT':
                data = JSONParser().parse(request)
                serializer = StockSerializer(Stock, data=data)
                if serializer.is_valid():
                        serializer.save()
                        return JSONResponse(serializer.data)
                return JSONResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
                Stock.delete()
                return HttpResponse(status=204)"""
