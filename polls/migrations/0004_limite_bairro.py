# Generated by Django 2.1.2 on 2018-11-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20181109_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Limite_Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'polls_limite_bairro',
                'managed': False,
            },
        ),
    ]
