# Generated by Django 3.2.6 on 2021-09-08 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0009_schoolfeeinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='yearsormonth',
            field=models.CharField(default='Per month', max_length=150),
            preserve_default=False,
        ),
    ]
