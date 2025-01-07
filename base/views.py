from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet #Generic:Most Logics written by ourselves
from .models import ProductType, Product, Purchase, Vendor, Sell, Department
from .serializers import ProductTypeSerializer, ProductSerializer, PurchaseSerializer, VendorSerializer, SellSerializer, DepartmentSerializer
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
        
    def retrieve(self,request,pk):
        # try:    
        #     product_obj = Product.objects.get(id=pk)
        # except:
        #     return Response("Data not found", status=status.HTTP_404_NOT_FOUND)
        product_obj = self.get_object() 
        serializer = self.get_serializer(product_obj)
        return Response(serializer.data)
    
    def update(self,request,pk):
        product_obj = self.get_object()
        serializer = self.get_serializer(product_obj, data=request.data) # update object through serializer 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk):
        product_obj = self.get_object()
        product_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
class PurchaseView(GenericViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
 
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VendorView(GenericViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class SellView(GenericViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer

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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentView(GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    





    


