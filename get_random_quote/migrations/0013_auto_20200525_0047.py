# Generated by Django 3.0.3 on 2020-05-24 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_random_quote', '0012_auto_20200524_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='image_name',
        ),
        migrations.AddField(
            model_name='quote',
            name='photo',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]