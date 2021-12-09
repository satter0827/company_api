from django.db import models
from django.db.models.query_utils import check_rel_lookup_compatibility
from django.utils.translation import TranslatorCommentWarning

class Company(models.Model):
    name = models.CharField(max_length=64)
    name_english = models.CharField(max_length=64)
    url = models.URLField()
    business_information = models.CharField(max_length=1024)
    error = models.CharField(max_length=64)
    pdf_etc = models.CharField(max_length=128)
    company_num = models.CharField(max_length=64)
    prefacture = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    address_etc = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    head_office_address = models.CharField(max_length=64)
    year_of_establishment = models.CharField(max_length=8)
    month_of_establishment = models.CharField(max_length=8)
    date_of_establishment = models.CharField(max_length=8)
    capital = models.CharField(max_length=64)
    full_time_employees = models.CharField(max_length=64)
    net_sales = models.CharField(max_length=64)
    operating_income = models.CharField(max_length=64)
    offering_period = models.CharField(max_length=64)
    listed_market_name = models.CharField(max_length=8)
    technology_code = models.CharField(max_length=64)
    technology_field = models.CharField(max_length=64)
    service_supply_code = models.CharField(max_length=64)
    service_supply = models.CharField(max_length=64)

    def get_list(self):
        return [self.name, self.name_english, self.url, self.business_information, self.error, self.pdf_etc, self.company_num,self.prefacture,
        self.city, self.address_etc, self.location, self.head_office_address, self.year_of_establishment, self.month_of_establishment,
        self.date_of_establishment, self.capital, self.full_time_employees, self.net_sales, self.operating_income, self.offering_period,
        self.listed_market_name, self.technology_code, self.technology_field, self.service_supply_code, self.service_supply]


