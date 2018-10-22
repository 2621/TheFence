# Generated by Django 2.1.2 on 2018-10-21 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefone',
            field=models.IntegerField(blank=True),
        ),
    ]