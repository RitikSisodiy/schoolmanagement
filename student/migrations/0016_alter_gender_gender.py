# Generated by Django 3.2 on 2021-04-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
