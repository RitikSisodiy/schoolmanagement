# Generated by Django 3.2.6 on 2021-09-08 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0014_auto_20210908_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='message',
            new_name='massage',
        ),
    ]