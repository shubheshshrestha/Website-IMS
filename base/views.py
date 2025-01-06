from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet #Generic:Most Logics written by ourselves
from .models import ProductType, Product, Purchase
from .serializers import ProductTypeSerializer, ProductSerializer, PurchaseSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ProductTypeView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductView(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        product_objs = self.get_queryset()
        serializer = self.get_serializer(product_objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #Important: status (for frontend devs)
        
class PurchaseView(GenericViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
 
    def list(self, request):
        product_objs = self.get_queryset()
        serializer = self.get_serializer(product_objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        pass
    





    


