# Generated by Django 5.0.1 on 2024-01-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_id_alter_menu_id_alter_menu_inventory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ID',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='ID',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
