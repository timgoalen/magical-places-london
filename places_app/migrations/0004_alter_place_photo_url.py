# Generated by Django 3.2.21 on 2023-09-27 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0003_place_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='photo_url',
            field=models.TextField(),
        ),
    ]
