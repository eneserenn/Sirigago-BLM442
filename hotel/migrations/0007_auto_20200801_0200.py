# Generated by Django 3.0.8 on 2020-07-31 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_auto_20200801_0153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='amount',
            new_name='star',
        ),
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(default='', max_length=200),
        ),
    ]
