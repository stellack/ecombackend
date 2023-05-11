from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from json import JSONDecodeError
from rest_framework import views, status
from rest_framework.response import Response

from api.models import Product, Contact
from .serializers import ProductSerializer, ContactSerializer

from django.core.files.storage import default_storage

# Create your views here.
class ContactAPIView(views.APIView):
    serializer_class = ContactSerializer

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format':self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = ContactSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result":"error","message":""})


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
