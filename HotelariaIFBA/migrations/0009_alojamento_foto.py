# Generated by Django 2.2.24 on 2021-06-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0008_alojamento_diaria'),
    ]

    operations = [
        migrations.AddField(
            model_name='alojamento',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
