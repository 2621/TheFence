# Generated by Django 2.1.2 on 2018-10-21 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20181020_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ID',
        ),
    ]
