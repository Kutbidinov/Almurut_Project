# Generated by Django 5.0.7 on 2024-09-22 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductRating',
            new_name='ProductUserRating',
        ),
    ]
