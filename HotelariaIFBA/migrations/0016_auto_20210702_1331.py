# Generated by Django 2.2.24 on 2021-07-02 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0015_auto_20210702_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empregados',
            old_name='Empresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='nome',
            new_name='empresa',
        ),
    ]
