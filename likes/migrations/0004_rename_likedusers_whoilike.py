# Generated by Django 4.2.11 on 2024-03-28 15:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('likes', '0003_rename_likeduserids_likedusers_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LikedUsers',
            new_name='WhoILike',
        ),
    ]