# Generated by Django 3.2.5 on 2021-08-23 00:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210822_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicacao',
            name='sinopse',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
