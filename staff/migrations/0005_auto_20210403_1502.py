# Generated by Django 3.1.7 on 2021-04-03 09:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('staff', '0004_auto_20210403_1359'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register',
            new_name='staffregister',
        ),
    ]
