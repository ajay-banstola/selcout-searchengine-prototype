# Generated by Django 2.0 on 2018-08-10 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_auto_20180810_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='user',
            new_name='users',
        ),
    ]