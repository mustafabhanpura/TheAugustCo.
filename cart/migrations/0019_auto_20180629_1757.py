# Generated by Django 2.0.1 on 2018-06-29 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0018_auto_20180629_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='det',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Order'),
        ),
    ]
