# Generated by Django 4.0.1 on 2022-11-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='weight',
            field=models.IntegerField(default=300),
        ),
    ]
