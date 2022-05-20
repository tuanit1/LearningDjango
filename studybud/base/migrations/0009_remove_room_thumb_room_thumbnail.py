# Generated by Django 4.0.3 on 2022-05-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_room_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='thumb',
        ),
        migrations.AddField(
            model_name='room',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]