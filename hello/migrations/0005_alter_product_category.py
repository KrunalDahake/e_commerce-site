# Generated by Django 4.0 on 2022-03-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0004_product_category_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FS', 'Fruits'), ('VG', 'Vegitable'), ('OT', 'Other')], max_length=3),
        ),
    ]
