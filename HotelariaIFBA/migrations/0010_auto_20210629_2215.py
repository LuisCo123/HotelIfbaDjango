# Generated by Django 2.2.24 on 2021-06-30 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0009_alojamento_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alojamento',
            name='diaria',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
