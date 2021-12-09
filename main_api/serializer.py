from rest_framework import serializers
from .models import Company

import pandas as pd

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'name_english', 'url', 'business_information', 'error', 'pdf_etc' 
        ,'company_num', 'prefacture', 'city', 'address_etc', 'location', 'head_office_address'
        ,'year_of_establishment', 'month_of_establishment', 'date_of_establishment', 'capital'
        , 'full_time_employees', 'net_sales', 'operating_income', 'offering_period', 'listed_market_name'
        , 'technology_code', 'technology_field', 'service_supply_code', 'service_supply')

    def save_csv(csv_data):
        df = pd.read_csv(csv_data, header=0, sep=",", encoding="cp932")

        df['法人番号'] = df['法人番号'].fillna(0)
        df['設立年'] = df['設立年'].fillna(0)
        df['設立月'] = df['設立月'].fillna(0)
        df['設立年月'] = df['設立年月'].fillna(0)
        df['資本金_現在'] = df['資本金_現在'].fillna(0)
        df['正社員数_現在'] = df['正社員数_現在'].fillna(0)
        df['売上高_直近'] = df['売上高_直近'].fillna(0)
        df['営業利益_直近'] = df['営業利益_直近'].fillna(0)
        df['株式公開 公開時期'] = df['株式公開 公開時期'].fillna(0)
        df['株式公開 公開時期'] = df['株式公開 公開時期'].fillna(0)
        df['主力製品サービス関連技術分野コード'] = df['主力製品サービス関連技術分野コード'].fillna(0)
        df['主力製品サービス供給形態コード'] = df['主力製品サービス供給形態コード'].fillna(0)
        df = df.fillna("")

        company_list = []
        Company.objects.all().delete()
        for _, row in df.iterrows():
            company =  Company()

            company.name = row[0]
            company.name_english = row[1]
            company.url = row[2]
            company.business_information = row[3]
            company.error = row[4]
            company.pdf_etc = row[5]
            company.company_num = row[6]
            company.prefacture = row[7]
            company.city = row[8]
            company.address_etc = row[9]
            company.location = row[10]
            company.head_office_address = row[11]
            company.year_of_establishment = row[12]
            company.month_of_establishment = row[13]
            company.date_of_establishment = row[14]
            company.capital = row[15]
            company.full_time_employees = row[16]
            company.net_sales = row[17]
            company.operating_income = row[18]
            company.offering_period = row[19]
            company.listed_market_name = row[20]
            company.technology_code = row[21]
            company.technology_field = row[22]
            company.service_supply_code = row[23]
            company.service_supply = row[24]

            company_list.append(company)

            company.save()

        #Company.objects.all().delete()
        #Company.objects.bulk_create(company_list)
