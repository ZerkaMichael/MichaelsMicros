# Generated by Django 4.1.5 on 2023-03-31 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item_orderitem_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plant',
            new_name='Product',
        ),
    ]
