# Generated by Django 3.0.8 on 2020-08-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='price',
            field=models.IntegerField(),
        ),
    ]
