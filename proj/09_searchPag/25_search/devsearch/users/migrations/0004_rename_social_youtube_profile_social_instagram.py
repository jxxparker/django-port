# Generated by Django 4.0.3 on 2022-06-29 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='social_youtube',
            new_name='social_instagram',
        ),
    ]