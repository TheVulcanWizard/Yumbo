# Generated by Django 3.0.8 on 2020-07-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='recipe_pics/default.jpg', upload_to='recipe_pics'),
        ),
    ]
