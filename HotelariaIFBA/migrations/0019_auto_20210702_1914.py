# Generated by Django 2.2.24 on 2021-07-02 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelariaIFBA', '0018_servicosutilizados_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='cliente',
            new_name='nome',
        ),
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.CharField(default='defaultUser', max_length=30),
            preserve_default=False,
        ),
    ]
