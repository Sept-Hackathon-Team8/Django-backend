# Generated by Django 3.1.13 on 2021-09-23 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pets', '0005_streak'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='breed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pet',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='accounts.customuser'),
            preserve_default=False,
        ),
    ]
