# Generated by Django 2.2.24 on 2021-06-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0004_auto_20210628_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alojamento',
            name='status',
            field=models.CharField(choices=[('Disponivel', 'Disponivel'), ('Indisponivel', 'Indisponivel')], max_length=30),
        ),
    ]
