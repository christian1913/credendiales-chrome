# Generated by Django 4.1.6 on 2023-06-29 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smtp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enviados',
            name='estatus',
            field=models.BooleanField(default=False),
        ),
    ]
