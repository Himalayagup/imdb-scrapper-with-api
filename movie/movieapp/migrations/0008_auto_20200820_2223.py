# Generated by Django 3.0.3 on 2020-08-20 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0007_remove_movie_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='wished_movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.Movie'),
        ),
    ]
