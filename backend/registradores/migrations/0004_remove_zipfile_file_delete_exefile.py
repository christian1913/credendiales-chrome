# Generated by Django 4.1.6 on 2023-06-29 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registradores', '0003_exefile_enviado_zipfile_enviado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zipfile',
            name='file',
        ),
        migrations.DeleteModel(
            name='ExeFile',
        ),
    ]
