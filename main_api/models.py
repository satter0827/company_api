from django.db import models
from django.db.models.query_utils import check_rel_lookup_compatibility
from django.utils.translation import TranslatorCommentWarning

class Company(models.Model):
    # 企業名,企業名（英語）,ホームページ,事業情報,エラー,pdf等,法人番号,都道府県名,市区町村名
    # ,市区町村名以下,所在地,本店所在地,設立年,設立月,設立年月,資本金_現在,正社員数_現在
    # ,売上高_直近,営業利益_直近,株式公開 公開時期,株式公開 上場市場名,主力製品サービス関連技術分野コード
    # ,主力製品サービス関連技術分野,主力製品サービス供給形態コード,サービス供給形態

    name = models.CharField(max_length=64)
    name_english = models.CharField(max_length=64)
    url = models.URLField()
    business_information = models.CharField(max_length=1024)
    error = models.CharField(max_length=64)
    pdf_etc = models.CharField(max_length=128)
    company_num = models.IntegerField()
    prefacture = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    town = models.CharField(max_length=64)
    address_etc = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    head_office_address = models.CharField(max_length=64)
    year_of_establishment = models.CharField(max_length=8)
    month_of_establishment = models.CharField(max_length=8)
    date_of_establishment = models.CharField(max_length=8)
    capital = models.IntegerField()
    full_time_employees = models.IntegerField()
    net_sales = models.IntegerField()
    operating_income = models.IntegerField()
    offering_period = models.IntegerField()
    listed_market_name = models.CharField(max_length=8)
    technology_code = models.IntegerField()
    technology_field = models.CharField(max_length=64)
    service_supply_code = models.IntegerField()
    service_supply = models.CharField(max_length=64)


