# Generated by Django 2.1.2 on 2018-10-21 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20181021_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='aparelho2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='aparelho3',
        ),
    ]
