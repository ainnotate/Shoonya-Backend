# Generated by Django 3.2.14 on 2024-04-22 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_auto_20240417_1028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='approved_by',
            new_name='invited_by',
        ),
    ]
