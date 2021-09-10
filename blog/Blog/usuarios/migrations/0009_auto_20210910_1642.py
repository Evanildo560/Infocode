# Generated by Django 3.2.6 on 2021-09-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_customuser_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='link_fb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='link_git',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='link_tt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='aniversario',
            field=models.DateField(blank=True, null=True),
        ),
    ]
