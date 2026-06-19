from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Patient
from .serializers import PatientSerializer

# Create your views here.

class PatientView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        patients = Patient.objects.all()
        # serialize the data python object to json
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PatientDetailView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk):
        patient = get_object_or_404(Patient, id=pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data, status = 200)

    def put(self, request, pk):
        patient = get_object_or_404(Patient, id=pk)
        serializer = PatientSerializer(patient, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        patient=get_object_or_404(Patient, id=pk)
        patient.delete()
        return Response({"message":"deleted successfully"}, status=200)
