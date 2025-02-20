"""
URL configuration for IMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import ProductTypeView, ProductView, PurchaseView, VendorView, SellView, DepartmentView, RegisterView, LoginView, GroupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view({"post":"create"})),
    path('login/', LoginView.as_view({"post":"create"})),
    path('group/', GroupView.as_view({"get":"list"})),
    path('product/', ProductView.as_view({'get': 'list', 'post': 'create'})),
    path('product/<int:pk>/', ProductView.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
    path('product-type/', ProductTypeView.as_view({'get': 'list', 'post': 'create'})),
    path('product-type/<int:pk>/', ProductTypeView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'
    })),
    path('purchase/', PurchaseView.as_view({'get':'list', 'post':'create'})),
    path('vendor/', VendorView.as_view({'get':'list', 'post':'create'})),
    path('sell/', SellView.as_view({'get':'list', 'post':'create'})),
    path('department/', DepartmentView.as_view({'get':'list', 'post':'create'}))

]

