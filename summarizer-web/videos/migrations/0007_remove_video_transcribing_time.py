# Generated by Django 5.1.1 on 2024-10-08 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_rename_download_end_date_video_date_uploaded_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='transcribing_time',
        ),
    ]
