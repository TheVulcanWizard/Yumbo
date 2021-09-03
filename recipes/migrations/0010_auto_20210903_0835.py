# Generated by Django 3.2.7 on 2021-09-03 13:35

from django.db import migrations, models
import recipes.models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_ingredient_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='header',
            field=models.CharField(default='No Header', max_length=140, verbose_name='Direction Header'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default=recipes.models.random_img, upload_to='recipe_pics'),
        ),
    ]
