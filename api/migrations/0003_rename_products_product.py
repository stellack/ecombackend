# Generated by Django 4.2.1 on 2023-05-10 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]