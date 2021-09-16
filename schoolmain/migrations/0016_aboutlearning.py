# Generated by Django 3.2.6 on 2021-09-08 13:28

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0015_rename_message_contactform_massage'),
    ]

    operations = [
        migrations.CreateModel(
            name='aboutlearning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(max_length=200)),
                ('classes', models.CharField(max_length=100)),
                ('information', models.CharField(max_length=1000)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]