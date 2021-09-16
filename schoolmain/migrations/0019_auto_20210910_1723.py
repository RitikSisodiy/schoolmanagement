# Generated by Django 3.2.6 on 2021-09-10 11:53

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0018_alter_schoolfeeinfo_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('content', models.CharField(max_length=500)),
                ('curri_content', models.CharField(max_length=500)),
                ('curri_point', ckeditor.fields.RichTextField()),
                ('accademics_content', models.CharField(max_length=500)),
                ('event_content', models.CharField(max_length=500)),
                ('club_content', models.CharField(max_length=500)),
                ('content_img', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.AlterField(
            model_name='schoolfeeinfo',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]