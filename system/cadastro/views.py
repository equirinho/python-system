from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.decorators import action



class LoginView(APIView):
    @action(detail=False)
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response({"status": "Missing credentials"})
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({"status": "success"})
            else:
                return Response({"status": "Account is not active"})
        else:
            return Response({"status": "Invalid credentials"})
    
    def get(self, request, format=None):
        # your get logic here
        return Response({"status": "success", "message":"Seja Bem Vindo!"})



class LogoutView(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response({"status": "success"})

    def get(self, request, format=None):
        # your get logic here
        return Response({"status": "success", "message":"Você deslogou do sistema"})

# Create your views here.




