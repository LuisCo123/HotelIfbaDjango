# Generated by Django 2.2.24 on 2021-06-30 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0007_auto_20210628_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='alojamento',
            name='diaria',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
