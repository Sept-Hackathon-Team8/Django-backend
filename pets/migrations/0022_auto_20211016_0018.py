# Generated by Django 3.1.13 on 2021-10-16 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0021_assesment_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='streak',
            options={'ordering': ['-created_at']},
        ),
    ]
