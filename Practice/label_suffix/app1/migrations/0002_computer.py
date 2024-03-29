# Generated by Django 3.2.4 on 2021-06-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processor', models.CharField(max_length=60)),
                ('motherboard', models.CharField(max_length=80)),
                ('powerSupply', models.CharField(max_length=70)),
                ('caseing', models.CharField(max_length=70)),
                ('ram', models.CharField(max_length=60)),
                ('total_price', models.FloatField()),
            ],
        ),
    ]
