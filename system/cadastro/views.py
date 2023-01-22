from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from rest_framework.decorators import authentication_classes, permission_classes

class LoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            # Autenticação bem sucedida
            # Faça algo com o usuário, como criar um token
            return Response({"status": "success"})
        else:
            # Autenticação falhou
            return Response({"status": "error"})



class LoginView(APIView):
    def post(self, request, format=None):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return Response({"status": "success"})
            else:
                return Response({"status": "user is not active"})


class LogoutView(APIView):
    def post(self, request, format=None):
        logout(request)
        return Response({"status": "success"})
# Create your views here.




