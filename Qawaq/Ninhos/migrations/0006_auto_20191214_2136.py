# Generated by Django 2.1.5 on 2019-12-14 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ninhos', '0005_auto_20191205_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historial',
            name='resultado',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='Preguntas',
            field=models.FilePathField(path='Ninhos/static/Preguntas'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='Respuestas',
            field=models.FilePathField(path='Ninhos/static/Respuestas'),
        ),
    ]
