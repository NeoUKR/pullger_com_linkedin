# Generated by Django 4.0.5 on 2022-06-19 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('com_linkedin', '0005_remove_people_experience_uuid_companies_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companies',
            old_name='data_full_loaded',
            new_name='date_full_loaded',
        ),
        migrations.RenameField(
            model_name='companies',
            old_name='data_small_loaded',
            new_name='date_small_loaded',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='data_full_loaded',
            new_name='date_full_loaded',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='data_small_loaded',
            new_name='date_small_loaded',
        ),
        migrations.RenameField(
            model_name='people_experience',
            old_name='data_small_loaded',
            new_name='date_small_loaded',
        ),
    ]
