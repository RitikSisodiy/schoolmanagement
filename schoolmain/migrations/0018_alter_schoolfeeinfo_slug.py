# Generated by Django 3.2.6 on 2021-09-09 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0017_schoolfeeinfo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schoolfeeinfo',
            name='slug',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
