# Generated by Django 3.1.7 on 2021-04-03 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentregister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schooler_no', models.CharField(max_length=25)),
                ('cast', models.CharField(max_length=20)),
                ('addmission_date', models.DateField()),
                ('sssid', models.CharField(max_length=20)),
                ('addhar_no', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=20)),
                ('IFSC', models.CharField(max_length=20)),
                ('TC', models.FileField(upload_to='certificate')),
                ('castcertificate', models.FileField(upload_to='certificate')),
                ('role', models.CharField(default='staff', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
