# Generated by Django 3.2.6 on 2021-09-08 08:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0011_rename_yearsormonth_schoolfeeinfo_yearlysormonthly'),
    ]

    operations = [
        migrations.AddField(
            model_name='schoolfeeinfo',
            name='content',
            field=ckeditor.fields.RichTextField(default='dewdwfw'),
            preserve_default=False,
        ),
    ]