# Generated by Django 5.0.7 on 2024-08-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(null=True, upload_to='products/%Y/%m/%d'),
        ),
    ]
