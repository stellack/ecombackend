from rest_framework import serializers
from api.models import Product

class ProductSerializer(serializers.ModelSerializer):
    ProductImages = serializers.ListField(
        child=serializers.ImageField(), allow_empty=True
    )
    class Meta:
        model = Product
        fields = ('ProductId','ProductName','ProductCategory','ProductPrice','ProductImages')

    def create(self, validated_data):
        images_data = validated_data.pop('ProductImages', [])
        product = super().create(validated_data)
        for image_data in images_data:
            product.productimages_set.create(image=image_data)
        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('ProductImages', [])
        product = super().update(instance, validated_data)
        for image_data in images_data:
            product.productimages_set.create(image=image_data)
        return product