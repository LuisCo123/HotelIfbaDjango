# Generated by Django 2.2.24 on 2021-07-02 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0016_auto_20210702_1331'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alojamento',
            old_name='numero',
            new_name='alojamento',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nome',
            new_name='cliente',
        ),
        migrations.RenameField(
            model_name='reserva',
            old_name='listaDeServico',
            new_name='servico',
        ),
    ]
