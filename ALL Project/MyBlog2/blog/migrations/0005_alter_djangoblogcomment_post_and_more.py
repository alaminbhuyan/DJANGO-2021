# Generated by Django 4.0 on 2022-01-12 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_mlblogcomment_dlblogcomment_djangoblogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoblogcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.djangoblogpost'),
        ),
        migrations.AlterField(
            model_name='dlblogcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.dlblogpost'),
        ),
        migrations.AlterField(
            model_name='mlblogcomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.mlblogpost'),
        ),
    ]
