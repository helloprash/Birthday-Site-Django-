# Generated by Django 3.0.3 on 2020-05-24 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_random_quote', '0013_auto_20200525_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='photo',
        ),
        migrations.AddField(
            model_name='quote',
            name='image_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]