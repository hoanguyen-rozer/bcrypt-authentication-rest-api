"""bcrypt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from products.views import (
    ProductListAPIView, 
    ProductRetrieveAPIView, 
    ProductCreateAPIView
    )

from accounts.views import (
    UserListAPIView,
    UserRetrieveAPIView,
    UserCreateAPIView,
    LoginAPIView,
    ObtainAuthBcryptToken,
    logout
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/products/', ProductListAPIView.as_view(), name='products_api'),
    path('api/v1/products/<int:pk>', ProductRetrieveAPIView.as_view(), name='product_detail_api'),
    path('api/v1/products/create/', ProductCreateAPIView.as_view(), name='product_create_api'),
    path('api/v1/users/', UserListAPIView.as_view(), name='users_api'),
    path('api/v1/users/<int:pk>', UserRetrieveAPIView.as_view(), name='user_detail_api'),
    path('api/v1/users/create/', UserCreateAPIView.as_view(), name='user_create_api'),
    path('api/v1/login/', LoginAPIView.as_view(), name='login'),
    path('api-token-auth/', ObtainAuthBcryptToken.as_view()),
    path('api/v1/logout/', logout, name='logout'),

]
