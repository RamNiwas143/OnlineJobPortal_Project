# Generated by Django 3.2.4 on 2023-04-06 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_rename_images_studentuser_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentuser',
            name='gender',
        ),
        migrations.AddField(
            model_name='studentuser',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
