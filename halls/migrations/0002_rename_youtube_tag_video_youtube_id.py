# Generated by Django 4.0.6 on 2022-07-12 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='youtube_tag',
            new_name='youtube_id',
        ),
    ]
