# Generated by Django 4.1.2 on 2022-10-27 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='rg',
            new_name='ra',
        ),
    ]