# Generated by Django 2.0.1 on 2018-06-28 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_auto_20180628_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='email',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
