# Generated by Django 3.2.6 on 2021-09-20 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0003_schoolfeeinfo_cen_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='cen_content',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='content1',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='title1',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
