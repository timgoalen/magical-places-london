# Generated by Django 3.2.20 on 2023-09-11 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='place',
            new_name='place_name',
        ),
    ]
