# Generated by Django 2.2.24 on 2021-06-21 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0002_auto_20210615_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='status',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Concluida', 'Concluida'), ('Em andamento', 'Em andamento'), ('Anulada', 'Anulada')], max_length=30),
        ),
    ]
