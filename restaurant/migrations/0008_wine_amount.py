# Generated by Django 4.0.1 on 2022-11-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_dish_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='amount',
            field=models.IntegerField(default=1000),
        ),
    ]