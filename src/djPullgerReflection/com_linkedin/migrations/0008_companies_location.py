# Generated by Django 4.0.5 on 2022-06-21 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('com_linkedin', '0007_companies_company_size_companies_employee_linkedin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='location',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
