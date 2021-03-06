# Generated by Django 4.0.5 on 2022-06-19 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('com_linkedin', '0004_remove_people_experience_companies_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people_experience',
            name='uuid_companies',
        ),
        migrations.RemoveField(
            model_name='people_experience',
            name='uuid_people',
        ),
        migrations.AddField(
            model_name='people_experience',
            name='companies',
            field=models.ForeignKey(db_column='uuid_companies', default=55555, on_delete=django.db.models.deletion.CASCADE, to='com_linkedin.companies', verbose_name='uuid_companies'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='people_experience',
            name='people',
            field=models.ForeignKey(db_column='uuid_people', default=444, on_delete=django.db.models.deletion.CASCADE, to='com_linkedin.people', verbose_name='uuid_people'),
            preserve_default=False,
        ),
    ]
