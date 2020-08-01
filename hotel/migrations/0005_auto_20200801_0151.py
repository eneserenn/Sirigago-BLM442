# Generated by Django 3.0.8 on 2020-07-31 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20200801_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='keywords',
        ),
        migrations.AddField(
            model_name='product',
            name='keyword',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
