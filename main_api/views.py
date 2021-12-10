from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.response import Response
from .models import Company, Result
from .serializer import CompanySerializer, ResultSerializer
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated

import csv

class CompanyViewSet(viewsets.ModelViewSet):
  class META:
    lookup_field = 'company_id'

  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  permission_classes = [IsAuthenticated]

class CompanyCsvView(views.APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=CompanysData_info.csv'

    writer = csv.writer(response)

    writer.writerow(Company.COMPANY_COLUMN_LIST)
    
    for company in Company.objects.all():
        writer.writerow(company.get_list())

    return response

  def post(self, request):
    Company.save_csv(request.data['csv_file'])

    return Response("OK")

class ResultViewSet(viewsets.ModelViewSet):
  class META:
    lookup_field = 'result_id'

  queryset = Result.objects.all()
  serializer_class = ResultSerializer
  permission_classes = [IsAuthenticated]

class ResultCsvView(views.APIView):
  permission_classes = [IsAuthenticated]
  
  def get(self, request):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=ResultsData_info.csv'

    writer = csv.writer(response)

    writer.writerow(Result.RESULT_COLUMN_LIST)
    
    for result in Result.objects.all():
        writer.writerow(result.get_list())

    return response

  def post(self, request):
    Result.save_csv(request.data['csv_file'])

    return Response("OK")