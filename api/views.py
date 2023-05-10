from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from api.models import Product
from api.serializers import ProductSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def productApi(request, id=0):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serilizer = ProductSerializer(products, many=True)
        return JsonResponse(products_serilizer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser.parse(request)
        product_serializer = ProductSerializer(data=product_data, files=request.FILES)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added successfully!")
        return JsonResponse("Failed to add product!", safe=False)
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(ProductId=product_data['ProductId'])
        product_serializer = ProductSerializer(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated successfully!", safe=False)
        return JsonResponse("Failed to update!", safe=False)
    elif request.method == 'DELETE':
        product = Product.objects.get(ProductId=id)
        product.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file_name,file)
    
    return JsonResponse(file_name, safe=False)
