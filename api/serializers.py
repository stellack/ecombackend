from rest_framework import serializers
from .models import Product, Contact
from rest_framework.fields import CharField, EmailField

class ContactSerializer(serializers.ModelSerializer):
    name = CharField(source="title", required=True)
    message = CharField(source="description", required=True)
    email = EmailField(required=True)

    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message'
        )

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