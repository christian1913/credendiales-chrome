# Generated by Django 4.1.6 on 2023-06-29 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plantillas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('asunto', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
                ('imagen', models.ImageField(upload_to='imagenes')),
                ('plantilla', models.TextField()),
                ('redireccion', models.CharField(blank=True, max_length=200, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='imagenes')),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opciones.emisores')),
                ('propietario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
