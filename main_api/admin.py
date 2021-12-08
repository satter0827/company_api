from django.contrib import admin
from .models import Company
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CompanyResource(resources.ModelResource):
    # Modelに対するdjango-import-exportの設定
    class Meta:
        model = Company

@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    # ImportExportModelAdminを利用するようにする
    ordering = ['id']
    list_display = ('name', 'name_english')

    # django-import-exportsの設定
    resource_class = CompanyResource