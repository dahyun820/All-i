# Generated by Django 5.0.6 on 2024-06-27 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('withmusic', '0002_music_artist_music_writer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='writer',
            new_name='author',
        ),
    ]
