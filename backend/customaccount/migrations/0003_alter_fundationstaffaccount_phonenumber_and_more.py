# Generated by Django 4.1.7 on 2023-04-12 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customaccount', '0002_studentaccount_fundationstaffaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundationstaffaccount',
            name='phoneNumber',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='studentaccount',
            name='phoneNumber',
            field=models.CharField(max_length=10),
        ),
    ]