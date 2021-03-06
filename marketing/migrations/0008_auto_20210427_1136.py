# Generated by Django 3.1.6 on 2021-04-27 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0007_auto_20210427_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postproduct',
            name='product_name',
            field=models.CharField(choices=[('Maize', 'Maize'), ('Rice', 'Rice'), ('Beans', 'Beans'), ('Carrot', 'Carrot'), ('Cabage', 'Cabage'), ('Beans', 'Beans')], max_length=100),
        ),
        migrations.AlterField(
            model_name='postproduct',
            name='region',
            field=models.CharField(choices=[('Arusha', 'Arusha'), ('Dar es Salaam', 'Dar es Salaam'), ('Geita', 'Geita'), ('Kagera', 'Kagera'), ('Mwanza', 'Mwanza'), ('Morogoro', 'Morogoro'), ('Shinyanga', 'Shinyanga'), ('Tabora', 'Tabora'), ('Singida', 'Singida'), ('Simiyu', 'Simiyu'), ('Mbeya', 'Mbeya')], max_length=50),
        ),
        migrations.AlterField(
            model_name='postproduct',
            name='scale',
            field=models.CharField(choices=[('Kg', 'Kg'), ('Debe', 'Debe'), ('Sack', 'Sack'), ('Tons', 'Tons')], max_length=50),
        ),
    ]
