# Generated by Django 3.2.5 on 2021-08-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210805_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='Add description here', max_length=500),
        ),
    ]