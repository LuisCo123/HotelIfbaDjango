# Generated by Django 2.2.24 on 2021-07-02 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0017_auto_20210702_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicosutilizados',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
