# Generated by Django 5.1 on 2024-09-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_alter_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
