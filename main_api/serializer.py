from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'name_english', 'url', 'business_information', 'error', 'pdf_etc' 
        ,'company_num', 'prefacture', 'city', 'town', 'address_etc', 'location', 'head_office_address'
        ,'year_of_establishment', 'month_of_establishment', 'date_of_establishment', 'capital'
        , 'full_time_employees', 'net_sales', 'operating_income', 'offering_period', 'listed_market_name'
        , 'technology_code', 'technology_field', 'service_supply_code', 'service_supply')