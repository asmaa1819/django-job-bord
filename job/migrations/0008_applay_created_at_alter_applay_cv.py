# Generated by Django 4.1.5 on 2023-05-19 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_applay_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='applay',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='applay',
            name='cv',
            field=models.FileField(upload_to='Applay/'),
        ),
    ]