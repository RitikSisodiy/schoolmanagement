# Generated by Django 3.2.6 on 2021-09-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0002_auto_20210920_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='cen_img',
            field=models.FileField(default='', upload_to='img'),
            preserve_default=False,
        ),
    ]