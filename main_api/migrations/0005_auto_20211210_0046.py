# Generated by Django 3.1.4 on 2021-12-09 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_api', '0004_auto_20211210_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='pdf_etc',
            field=models.CharField(max_length=2048),
        ),
    ]
