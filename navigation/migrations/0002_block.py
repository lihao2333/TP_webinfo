# Generated by Django 2.0.2 on 2018-07-22 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='block')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=20)),
            ],
        ),
    ]
