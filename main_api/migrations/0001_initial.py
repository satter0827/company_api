# Generated by Django 3.1.4 on 2021-12-06 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('name_english', models.CharField(max_length=64)),
                ('url', models.URLField()),
                ('business_information', models.CharField(max_length=1024)),
                ('error', models.CharField(max_length=64)),
                ('pdf_etc', models.CharField(max_length=128)),
                ('company_num', models.IntegerField()),
                ('prefacture', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('town', models.CharField(max_length=64)),
                ('address_etc', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
                ('head_office_address', models.CharField(max_length=64)),
                ('year_of_establishment', models.CharField(max_length=8)),
                ('month_of_establishment', models.CharField(max_length=8)),
                ('date_of_establishment', models.CharField(max_length=8)),
                ('capital', models.IntegerField()),
                ('full_time_employees', models.IntegerField()),
                ('net_sales', models.IntegerField()),
                ('operating_income', models.IntegerField()),
                ('offering_period', models.IntegerField()),
                ('listed_market_name', models.CharField(max_length=8)),
                ('technology_code', models.IntegerField()),
                ('technology_field', models.CharField(max_length=64)),
                ('service_supply_code', models.IntegerField()),
                ('service_supply', models.CharField(max_length=64)),
            ],
        ),
    ]
