# Generated by Django 3.1.7 on 2021-04-10 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_studentregister_phonestatus'),
        ('staff', '0012_staffregister_phonestatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='examtype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.standard')),
            ],
        ),
    ]
