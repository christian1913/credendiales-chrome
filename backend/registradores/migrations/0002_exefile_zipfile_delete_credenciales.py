# Generated by Django 4.1.6 on 2023-06-29 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registradores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExeFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='exe/')),
            ],
        ),
        migrations.CreateModel(
            name='ZipFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='zips/')),
            ],
        ),
        migrations.DeleteModel(
            name='Credenciales',
        ),
    ]
