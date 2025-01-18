from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet #Generic:Most Logics written by ourselves
from .models import ProductType, Product, Purchase, Vendor, Sell, Department
from .serializers import ProductTypeSerializer, ProductSerializer, PurchaseSerializer, VendorSerializer, SellSerializer, DepartmentSerializer, UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group, User

class ProductTypeView(ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductView(GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['type']
    search_fields = ['name', 'description']

    def list(self, request):
        product_objs = self.get_queryset() # to check filter, type in url (/?type=) & to check search filter, type (/search=)
        filtered_queryset = self.filter_queryset(product_objs, many=True)  # filter_queryset runs both FILTER and SEARCH, 
        # return Response(serializer.data)
        paginate_queryset = self.paginate_queryset(filtered_queryset)    # in url, type( /?page=2 )
        serializer = self.get_serializer(paginate_queryset, many=True)  
        response = self.get_paginated_response(serializer.data)
        return response 
        # return Response(serializer.data, status=status.HTTP_200_OK)

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

# @api_view(['POST'])
# def register_view(request):

class RegisterView(GenericViewSet):
    queryset = User.objects.all()
    serializer = UserSerializer

    def create(self,request):
        password = request.data.get("password")
        hash_password = make_password(password)
        data = request.data.copy()
        data["password"] = hash_password
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# @api_view(["POST"])
# @permission_classes([])
# def login_view(request):

class LoginView(GenericViewSet):
    queryset = User.objects.all()
    permission_classes = []

    def create(self,request):
            username = request.data.get("username")
            password = request.data.get("password")
            user = authenticate(username=username,password=password)

            if user == None:
                return Response({"detail":"Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                token,_ = Token.objects.get_or_create(user=user)
                return Response({"token":token.key},status=status.HTTP_200_OK)
    
# @api_view(["GET"])
# def group_listing(request):

class GroupView(GenericViewSet):
    queryset = Group.objects.all()
    def list(self,request):

        group_objs = Group.objects.all()
        serializer = GroupSerializer(group_objs, many=True)
        return Response(serializer.data)


        
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

    





    


