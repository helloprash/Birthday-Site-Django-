# Generated by Django 3.0.3 on 2020-05-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_random_quote', '0014_auto_20200525_0056'),
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