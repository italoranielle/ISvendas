from rest_framework import viewsets

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import  Product, Purchase, Stock
from .serializers import ProductSerializer ,PurchaseSerializer, StockSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes





class ProductAPIView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@permission_classes((permissions.AllowAny,))
class ProductView(APIView):
    def get(self, request, format=None):
        name = request.GET.get('name','')
        products = Product.objects.get(name__contains = name )
        serializer = ProductSerializer(products, many=False)
        return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class ProductList(APIView):

    def get(self, request, format=None):
        description = request.GET.get('description','')
        products = Product.objects.filter(description__contains = description )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class PurchaseView(APIView):

    def get(self, request, format=None):
        #description = request.GET.get('description','')
        purchase = Purchase.objects.all()
        serializer = ProductSerializer(purchase, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PurchaseSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class StockList(APIView):
    def get(self, request, format=None):
        name = request.GET.get('name','')
        products = Stock.objects.filter(product__name__contains = name )
        serializer = StockSerializer(products, many=True)
        return Response(serializer.data)