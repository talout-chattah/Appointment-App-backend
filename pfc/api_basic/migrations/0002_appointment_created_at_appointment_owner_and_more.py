# Generated by Django 4.0.4 on 2022-04-16 14:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 4, 16, 14, 2, 32, 439786, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='owner',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]