# Generated by Django 3.0.8 on 2020-08-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_auto_20200801_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='detail',
            field=models.TextField(max_length=300),
        ),
    ]
