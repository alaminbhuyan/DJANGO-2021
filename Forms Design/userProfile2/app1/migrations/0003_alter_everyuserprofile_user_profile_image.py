# Generated by Django 3.2.9 on 2021-12-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_everyuserprofile_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='everyuserprofile',
            name='user_profile_image',
            field=models.ImageField(default='profile_images/avater.png', upload_to='profile_images'),
        ),
    ]