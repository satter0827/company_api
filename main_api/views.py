from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters
from .models import Company
from .serializer import CompanySerializer

def index(request):
  return render(request, 'main_api/index.html')

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    