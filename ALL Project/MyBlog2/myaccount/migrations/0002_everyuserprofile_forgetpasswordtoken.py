# Generated by Django 4.0 on 2022-01-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='everyuserprofile',
            name='forgetPasswordToken',
            field=models.CharField(default='', max_length=150, verbose_name='ForgetPasswordToken'),
            preserve_default=False,
        ),
    ]