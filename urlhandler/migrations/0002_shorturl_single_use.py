# Generated by Django 3.0.8 on 2020-07-23 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urlhandler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='single_use',
            field=models.BooleanField(default=False),
        ),
    ]
