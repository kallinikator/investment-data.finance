from rest_framework import serializers
from api.models import Stock, PriceData, FundamentalData

class StockSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stock
		fields = ("full_name", "symbol")

class FundamentalSerializer(serializers.ModelSerializer):
	class Meta:
		model = FundamentalData
		fields = ("end_date", "symbol", "amend", "period_focus", "fiscal_year", "doc_type", "revenues", "op_income", "net_income", "eps_basic", "eps_diluted", "dividend", "assets", "cur_assets", "cur_liab", "cash", "equity", "cash_flow_op", "cash_flow_inv", "cash_flow_fin")

class DetailSerializer(serializers.ModelSerializer):
    prices = serializers.StringRelatedField(many=True, read_only=True)
    fundamentals = FundamentalSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = ("full_name", "symbol", "description", "prices", "fundamentals")

