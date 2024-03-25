# Generated by Django 4.2.11 on 2024-03-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0014_remove_profile_favorite_books_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='education_level',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='looking_for_tribes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tribes',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='weight',
        ),
        migrations.AlterField(
            model_name='profile',
            name='looking_for',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='relationship_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]