# Generated by Django 3.2.6 on 2021-10-02 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comentario_teste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='publicacao',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='teste',
        ),
    ]
