# Generated by Django 3.1.13 on 2021-10-02 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0004_auto_20211002_0902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='icon_url',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='img_url',
            new_name='image',
        ),
    ]