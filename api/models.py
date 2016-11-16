from django.db import models

# Automatically initiates an ID.
class Stock(models.Model):
    """Contains the symbol and the full name for a stock in the database"""
    symbol = models.CharField(max_length=5)
    full_name = models.CharField(max_length=150)
    description = models.CharField(max_length=15000, default="")
    favourite = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.symbol)
    def __str__(self):
        return str(self.symbol)


class PriceData(models.Model):
    stock = models.ForeignKey(Stock, related_name="prices", on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    price_high = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['date']
        
    def __unicode__(self):
        return "{}: {}".format(self.date, self.price_high)
    def __str__(self):
        return "{}: {}".format(self.date, self.price_high)
    def __repr__(self):
        return "{}: {}".format(self.date, self.price_high)


class FundamentalData(models.Model):
    stock = models.ForeignKey(Stock, related_name="fundamentals", on_delete=models.CASCADE)
    symbol = models.CharField(max_length=100, blank=True)
    date = models.CharField(max_length=100, blank=True)
    end_date = models.CharField(max_length=100, blank=True)
    amend = models.CharField(max_length=100, blank=True)
    period_focus = models.CharField(max_length=100, blank=True)
    fiscal_year = models.CharField(max_length=100, blank=True)
    doc_type = models.CharField(max_length=100, blank=True)
    revenues = models.CharField(max_length=100, blank=True)
    op_income = models.CharField(max_length=100, blank=True)
    net_income = models.CharField(max_length=100, blank=True)
    eps_basic = models.CharField(max_length=100, blank=True)
    eps_diluted = models.CharField(max_length=100, blank=True)
    dividend = models.CharField(max_length=100, blank=True)
    assets = models.CharField(max_length=100, blank=True)
    cur_assets = models.CharField(max_length=100, blank=True)
    cur_liab = models.CharField(max_length=100, blank=True)
    cash = models.CharField(max_length=100, blank=True)
    equity = models.CharField(max_length=100, blank=True)
    cash_flow_op = models.CharField(max_length=100, blank=True)
    cash_flow_inv = models.CharField(max_length=100, blank=True)
    cash_flow_fin = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['date']
        
    def __unicode__(self):
        return "{}: {}".format(self.end_date, self.symbol)
    def __str__(self):
        return "{}: {}".format(self.end_date, self.symbol)
    def __repr__(self):
        return "{}: {}".format(self.end_date, self.symbol)
