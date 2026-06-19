from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Mapping
from .serializers import MappingSerializers

# Create your views here.
class MappingView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        serializer = MappingSerializers(Mapping.objects.all(), many=True)
        return Response(serializer.data, status=200)
    def post(self, request):
        serializer = MappingSerializers(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class MappingDetailView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, mapping_id):
        mapping = get_object_or_404(Mapping, id=mapping_id)
        serializer=MappingSerializers(mapping)
        return Response(serializer.data, status=200)
    
    def delete(self, request, mapping_id):
        mapping = get_object_or_404(Mapping, id=mapping_id)
        mapping.delete()
        return Response({"message":"deleted successfully"}, status=200)

class MappingPatientView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, patient_id):
        mappings=Mapping.objects.filter(patient=patient_id)
        serializer=MappingSerializers(mappings, many=True)
        return Response(serializer.data,status=200)

class MappingDoctorView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, doctor_id):
        mappings=Mapping.objects.filter(doctor=doctor_id)
        serializer=MappingSerializers(mappings, many=True)
        return Response(serializer.data, status=200)