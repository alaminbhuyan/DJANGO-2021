# Generated by Django 4.0 on 2022-01-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Student_Name')),
                ('stu_ID', models.CharField(max_length=15, verbose_name='Student_ID')),
                ('course', models.CharField(max_length=50, verbose_name='Course_name')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Teacher_Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Teacher_email')),
                ('take_subject', models.CharField(max_length=50, verbose_name='Subject_name')),
            ],
        ),
    ]