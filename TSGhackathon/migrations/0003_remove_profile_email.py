# Generated by Django 2.2.9 on 2021-12-19 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TSGhackathon', '0002_profile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
