from rest_framework import serializers
from .models import Company, Result

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company_id', 'name', 'name_english', 'url', 'business_information', 'error', 'pdf_etc' 
        ,'company_num', 'prefacture', 'city', 'address_etc', 'location', 'head_office_address'
        ,'year_of_establishment', 'month_of_establishment', 'date_of_establishment', 'capital'
        , 'full_time_employees', 'net_sales', 'operating_income', 'offering_period', 'listed_market_name'
        , 'technology_code', 'technology_field', 'service_supply_code', 'service_supply')

class ResultSerializer(serializers.ModelSerializer):
    target = CompanySerializer()
    suggest_1 = CompanySerializer()
    suggest_2 = CompanySerializer()
    suggest_3 = CompanySerializer()

    class Meta:
        model = Result
        fields = ('result_id', 'target', 'suggest_1', 'suggest_2', 'suggest_3')
