# Generated by Django 4.1.7 on 2023-04-12 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('summary', '0003_alter_summarytimeline_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='author',
        ),
        migrations.AddField(
            model_name='summary',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userSummaries', to=settings.AUTH_USER_MODEL),
        ),
    ]
