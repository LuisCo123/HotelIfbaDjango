# Generated by Django 2.2.24 on 2021-06-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0010_auto_20210629_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alojamento',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='HotelariaIFBA/roomImages/'),
        ),
    ]