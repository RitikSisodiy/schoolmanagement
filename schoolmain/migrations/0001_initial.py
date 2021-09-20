# Generated by Django 3.2.6 on 2021-09-20 06:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=200)),
                ('img', models.FileField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='admissionform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('contact_no', models.IntegerField()),
                ('messages', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('looking_for', models.CharField(max_length=50)),
                ('massage', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='kidsinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('studying', models.CharField(max_length=500)),
                ('requirement', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='recentprogram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=31)),
                ('month', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('time', models.DurationField()),
                ('heading_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='schoocontact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=15)),
                ('lookingfor', models.CharField(max_length=25)),
                ('massage', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='schoolfeeinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standards', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('annualfee', models.IntegerField()),
                ('yearlysormonthly', models.CharField(max_length=150)),
                ('content', ckeditor.fields.RichTextField()),
                ('cen_image', models.FileField(upload_to='img')),
                ('cen_content', models.CharField(max_length=250)),
                ('title1', models.CharField(max_length=50)),
                ('content1', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='schoolifo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='schoolinfo')),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=15)),
                ('phone2', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=25)),
            ],
        ),
    ]
