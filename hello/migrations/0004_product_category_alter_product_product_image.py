# Generated by Django 4.0 on 2022-03-29 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_rename_satus_orderplaced_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FS', 'Fruits'), ('VG', 'Vegitable'), ('OT', 'Other')], default=4, max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='productimg'),
        ),
    ]