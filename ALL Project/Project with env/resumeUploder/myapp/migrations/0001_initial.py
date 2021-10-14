# Generated by Django 3.2.8 on 2021-10-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('pin', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Dhaka North', 'Dhaka North'), ('Dhaka South', 'Dhaka South'), ('Chittagong', 'Chittagong'), ('Gazipur', 'Gazipur'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Mymensingh', 'Mymensingh'), ('Sylhet', 'Sylhet'), ('Comilla', 'Comilla'), ('Barisal', 'Barisal'), ('Rangpur', 'Rangpur'), ('Narayanganj', 'Narayanganj')], max_length=80)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=70)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileImg')),
                ('my_files', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]
