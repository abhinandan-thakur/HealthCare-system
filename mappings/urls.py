from django.urls import path
from .views import MappingView, MappingDetailView, MappingDoctorView, MappingPatientView

urlpatterns = [
    path('', MappingView.as_view(), name='mapping-list'),
    path('<int:mapping_id>/', MappingDetailView.as_view(), name='mapping-detail-list'),
    path('patient/<int:patient_id>/', MappingPatientView.as_view(), name='mapping-patient-list'),
    path('doctor/<int:doctor_id>/', MappingDoctorView.as_view(), name='mapping-doctor-list')
]