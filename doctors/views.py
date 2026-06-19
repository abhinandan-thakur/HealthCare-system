from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Doctor
from .serializer import DoctorSerializer

# Create your views here.
class DoctorView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = DoctorSerializer(Doctor.objects.all(), many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DoctorDetailView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, id=pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data, status=200)
    
    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, id=pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, id=pk)
        doctor.delete()
        return Response("Deleted Successfully", status=201)

