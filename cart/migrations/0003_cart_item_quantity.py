# Generated by Django 3.2 on 2022-08-14 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20220814_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart_item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
