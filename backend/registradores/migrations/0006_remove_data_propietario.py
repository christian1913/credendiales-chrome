# Generated by Django 4.1.6 on 2023-06-30 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registradores', '0005_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='propietario',
        ),
    ]
