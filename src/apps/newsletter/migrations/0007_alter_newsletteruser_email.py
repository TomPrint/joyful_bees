# Generated by Django 3.2.5 on 2021-10-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20211005_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletteruser',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
