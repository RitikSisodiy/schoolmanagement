# Generated by Django 3.2.6 on 2021-09-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmain', '0021_admissionform'),
    ]

    operations = [
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
    ]
