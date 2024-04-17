# Generated by Django 3.2.14 on 2024-04-17 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0031_user_notification_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='approved_by',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='is_approved',
            field=models.BooleanField(default=True, help_text='Indicates whether user is approved by the admin or not.', verbose_name='is_approved'),
        ),
    ]
