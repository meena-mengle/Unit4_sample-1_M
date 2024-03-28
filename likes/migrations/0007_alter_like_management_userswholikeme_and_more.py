# Generated by Django 4.2.11 on 2024-03-28 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0006_rename_like_like_management'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like_management',
            name='UserswhoLikeMe',
            field=models.ManyToManyField(blank=True, related_name='UserswhoLikeMe', to='likes.userswholikeme'),
        ),
        migrations.AlterField(
            model_name='like_management',
            name='WhoILike',
            field=models.ManyToManyField(blank=True, related_name='WhoILike', to='likes.whoilike'),
        ),
    ]
