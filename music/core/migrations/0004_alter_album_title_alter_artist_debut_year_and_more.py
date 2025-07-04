# Generated by Django 5.2.3 on 2025-06-16 12:54

import core.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_artist_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='artist',
            name='debut_year',
            field=models.IntegerField(validators=[core.models.validate_debut_year]),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
