from django.conf.urls import url, include
from . import views
from rest_framework import routers
from .views import CompanyViewSet, CompanyCsvView

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)

urlpatterns = [
    url("csv_upload", CompanyCsvView.as_view(), name="csv_upload"),
]
