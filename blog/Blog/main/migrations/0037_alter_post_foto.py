# Generated by Django 3.2.6 on 2021-09-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_post_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='foto',
            field=models.ImageField(blank=True, default='static/img/default_profile_image.jpg', null=True, upload_to='static/img/'),
        ),
    ]
