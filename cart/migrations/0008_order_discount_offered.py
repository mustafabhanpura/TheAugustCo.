# Generated by Django 2.0.1 on 2018-06-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount_offered',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
