# Generated by Django 3.0.3 on 2020-08-20 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0006_auto_20200820_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='average_rating',
        ),
    ]
