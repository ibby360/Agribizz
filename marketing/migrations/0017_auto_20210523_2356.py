# Generated by Django 3.1.6 on 2021-05-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0016_auto_20210523_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproduct',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]