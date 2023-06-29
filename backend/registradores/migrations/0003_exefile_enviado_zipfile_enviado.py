# Generated by Django 4.1.6 on 2023-06-29 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smtp', '0001_initial'),
        ('registradores', '0002_exefile_zipfile_delete_credenciales'),
    ]

    operations = [
        migrations.AddField(
            model_name='exefile',
            name='enviado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='smtp.enviados'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zipfile',
            name='enviado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='smtp.enviados'),
            preserve_default=False,
        ),
    ]
