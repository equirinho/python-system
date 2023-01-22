"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from cadastro.api import viewsets as cadastroviewsets
from cadastro.views import LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include





route = routers.DefaultRouter()



route.register(r'cadastro', cadastroviewsets.CadastroViewSet, basename="Cadastro de Usuários")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)), #como eh o diretório principal da aplicação, deixo em branco!
    path('login/', LoginView.as_view(), name='login'),
    path ('token/', TokenObtainPairView.as_view()),
    path ('token/refresh/', TokenRefreshView.as_view()),
]


