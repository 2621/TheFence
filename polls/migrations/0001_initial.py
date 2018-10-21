# Generated by Django 2.0.8 on 2018-10-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ID', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('telefone', models.PositiveIntegerField()),
            ],
        ),
    ]
