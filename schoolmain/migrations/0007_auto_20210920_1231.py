# Generated by Django 3.2.6 on 2021-09-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0006_schoolfeeinfo_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='content3',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='content33',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='image3',
            field=models.FileField(default='', upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='title3',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
