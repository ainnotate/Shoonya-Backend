# Generated by Django 3.1.14 on 2022-03-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0012_auto_20220328_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocktext',
            name='splitted_text',
            field=models.TextField(default='', verbose_name='splitted_text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blocktext',
            name='splitted_text_prediction',
            field=models.JSONField(blank=True, null=True, verbose_name='splitted_text_prediction'),
        ),
    ]
