from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer

# Define a view function for the registration page
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)