# Generated by Django 4.2.11 on 2024-03-23 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0018_remove_profile_vaccinations_profile_covid_booster_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='covid_vaccinations',
            new_name='covid_vaccination',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='monkeypox_vaccinations',
            new_name='monkeypox_vaccination',
        ),
    ]