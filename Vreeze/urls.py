"""
URL configuration for ioBro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView, TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from . import views

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
urlpatterns = [
    path('admin', admin.site.urls),
    path("api/v1/user/", include("user.urls")),
    path("api/v1/voice/", include("voice.urls")),
    path("api/v1/payment/", include("payment.urls")),
    path("api/v1/present/", include("present.urls")),
]+ [
    path("api/login/", CustomTokenObtainPairView.as_view()),
    path("api/logout/", TokenBlacklistView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path('auth/', include('social_django.urls', namespace='social')),
    path('api/v1/s3/url/', views.S3APIView.as_view()),
]
