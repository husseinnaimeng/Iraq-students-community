# Generated by Django 4.1.7 on 2023-04-12 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
        ('summary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subject.subject'),
        ),
    ]
