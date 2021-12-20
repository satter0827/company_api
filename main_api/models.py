from django.db import models
from django.db.models.query_utils import check_rel_lookup_compatibility
from django.utils.translation import TranslatorCommentWarning

import pandas as pd
import uuid

class Company(models.Model):
    COMPANY_COLUMN_LIST = ["UUID", "企業名", "企業名（英語）", "ホームページ", "事業情報", "エラー", "pdf等", "法人番号", "都道府県名" 
        , "市区町村名", "市区町村名以下", "所在地", "本店所在地", "設立年", "設立月", "設立年月", "資本金_現在", "正社員数_現在"
        , "売上高_直近", "営業利益_直近", "株式公開 公開時期", "株式公開 上場市場名", "主力製品サービス関連技術分野コード"
        , "主力製品サービス関連技術分野", "主力製品サービス供給形態コード", "サービス供給形態"
        ]

    company_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, db_index=True)
    name = models.CharField(max_length=100000, db_index=True)
    name_english = models.CharField(max_length=100000)
    url = models.URLField()
    business_information = models.CharField(max_length=100000)
    error = models.CharField(max_length=100000)
    pdf_etc = models.CharField(max_length=100000)
    company_num = models.CharField(max_length=100000)
    prefacture = models.CharField(max_length=100000)
    city = models.CharField(max_length=100000)
    address_etc = models.CharField(max_length=100000)
    location = models.CharField(max_length=100000)
    head_office_address = models.CharField(max_length=100000)
    year_of_establishment = models.CharField(max_length=100000)
    month_of_establishment = models.CharField(max_length=100000)
    date_of_establishment = models.CharField(max_length=100000)
    capital = models.CharField(max_length=100000)
    full_time_employees = models.CharField(max_length=100000)
    net_sales = models.CharField(max_length=100000)
    operating_income = models.CharField(max_length=100000)
    offering_period = models.CharField(max_length=100000)
    listed_market_name = models.CharField(max_length=100000)
    technology_code = models.CharField(max_length=100000)
    technology_field = models.CharField(max_length=100000)
    service_supply_code = models.CharField(max_length=100000)
    service_supply = models.CharField(max_length=100000)

    def get_list(self):
        return [self.company_id, self.name, self.name_english, self.url, self.business_information, self.error, self.pdf_etc, self.company_num,self.prefacture,
        self.city, self.address_etc, self.location, self.head_office_address, self.year_of_establishment, self.month_of_establishment,
        self.date_of_establishment, self.capital, self.full_time_employees, self.net_sales, self.operating_income, self.offering_period,
        self.listed_market_name, self.technology_code, self.technology_field, self.service_supply_code, self.service_supply]

    def save_csv(csv_data):
        df = pd.read_csv(csv_data, header=0, sep=",", encoding="cp932")
        df = df.fillna("")

        company_list = []

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

        Company.objects.all().delete()
        Company.objects.bulk_create(company_list)

class Result(models.Model):
    RESULT_COLUMN_LIST = ["UUID", "ターゲット", "提案1", "提案2", "提案3"]

    result_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, db_index=True)
    target = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="target", db_column='target')
    suggest_1 = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="sugest_1", db_column='suggest_1')
    suggest_2 = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="sugest_2", db_column='suggest_2')
    suggest_3 = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="sugest_3", db_column='suggest_3')

    def get_list(self):
        return [self.result_id, self.target, self.suggest_1, self.suggest_2, self.suggest_3]

    def save_csv(csv_data):
        df = pd.read_csv(csv_data, header=0, sep=",", encoding="cp932")
        df = df.fillna("")

        result_list = []

        for _, row in df.iterrows():
            result =  Result()

            result.target = Company(company_id=row[0])
            result.suggest_1 = Company(company_id=row[1])
            result.suggest_2 = Company(company_id=row[2])
            result.suggest_3 = Company(company_id=row[3])

            result_list.append(result)

        Result.objects.all().delete()
        Result.objects.bulk_create(result_list)