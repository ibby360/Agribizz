# Generated by Django 3.1.6 on 2021-05-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0009_auto_20210503_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='postproduct',
            name='category',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
