# Generated by Django 4.0.5 on 2022-06-19 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('com_linkedin', '0003_rename_uuid_companies_people_experience_companies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people_experience',
            name='companies',
        ),
        migrations.RemoveField(
            model_name='people_experience',
            name='people',
        ),
        migrations.AddField(
            model_name='people_experience',
            name='uuid_companies',
            field=models.ForeignKey(db_column='uuid_companies', default=2, on_delete=django.db.models.deletion.CASCADE, to='com_linkedin.companies', verbose_name='companies'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='people_experience',
            name='uuid_people',
            field=models.ForeignKey(db_column='uuid_people', default=887, on_delete=django.db.models.deletion.CASCADE, to='com_linkedin.people', verbose_name='people'),
            preserve_default=False,
        ),
    ]