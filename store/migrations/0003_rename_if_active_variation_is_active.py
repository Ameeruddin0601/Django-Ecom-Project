# Generated by Django 4.0.1 on 2022-03-14 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='if_active',
            new_name='is_active',
        ),
    ]
