# Generated by Django 2.0.2 on 2018-08-28 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0009_auto_20180828_0951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main',
            old_name='address',
            new_name='address1',
        ),
    ]
