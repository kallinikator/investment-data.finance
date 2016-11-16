from django.contrib import admin
from .models import Stock, PriceData, FundamentalData

admin.site.register(Stock)
admin.site.register(PriceData)
admin.site.register(FundamentalData)