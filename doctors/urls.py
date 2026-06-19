from django.urls import path
from .views import DoctorView, DoctorDetailView

urlpatterns = [
    path('', DoctorView.as_view(), name='doctor-list'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail')
]