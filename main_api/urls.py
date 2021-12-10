from django.conf.urls import url, include
from . import views
from rest_framework import routers
from .views import CompanyViewSet, CompanyCsvView, ResultViewSet, ResultCsvView

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)
router.register('result', ResultViewSet)

urlpatterns = [
    url("company_csv", CompanyCsvView.as_view(), name="company_csv"),
    url("result_csv", ResultCsvView.as_view(), name="result_csv"),
]
