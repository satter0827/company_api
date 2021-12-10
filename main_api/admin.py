from django.contrib import admin
from .models import Company, Result
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CompanyResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Company

@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['company_id']
    list_display = ('name', 'name_english')

    # django-import-exportsの設定
    resource_class = CompanyResource

class ResultResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Result

@admin.register(Result)
class ResultAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['result_id']
    list_display = ('target', 'suggest_1', 'suggest_2', 'suggest_3')

    # django-import-exportsの設定
    resource_class = ResultResource