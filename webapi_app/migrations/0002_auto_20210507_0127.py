# Generated by Django 3.2.2 on 2021-05-07 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapi_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geolocation',
            old_name='lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='geolocation',
            old_name='lng',
            new_name='longitude',
        ),
    ]