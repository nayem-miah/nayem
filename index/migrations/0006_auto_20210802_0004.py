# Generated by Django 3.2.5 on 2021-08-01 18:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_portfolio_hi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='created',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]