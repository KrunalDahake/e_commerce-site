# Generated by Django 4.0 on 2022-04-08 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
