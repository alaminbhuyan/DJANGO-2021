# Generated by Django 4.0 on 2022-01-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangoblogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='dlblogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='mlblogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='pythonblogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
    ]
