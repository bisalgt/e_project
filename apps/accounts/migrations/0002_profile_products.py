# Generated by Django 3.0.5 on 2020-04-18 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='products.Product'),
        ),
    ]
