# Generated by Django 3.0.3 on 2020-05-24 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_random_quote', '0007_auto_20200524_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='image',
            new_name='Photo',
        ),
    ]