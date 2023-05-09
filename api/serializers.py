from rest_framework import serializers
from api.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('ProductId','ProductName','ProductCategory','ProductPrice','ProductImages')