from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response

from .models import Company
from .serializer import CompanySerializer
from .consts import *
from django.http import HttpResponse
import csv

class CompanyViewSet(viewsets.ModelViewSet):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer

class CompanyCsvView(views.APIView):
  def get(self, request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=CompanysData_info.csv'

    writer = csv.writer(response)

    writer.writerow(CSV_COLUMN_LIST)
    
    for company in Company.objects.all():
        writer.writerow(company.get_list())

    return response

  def post(self, request):
    CompanySerializer.save_csv(request.data['csv_file'])

    return Response("OK")