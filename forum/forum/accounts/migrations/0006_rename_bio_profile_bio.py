# Generated by Django 4.0.3 on 2022-04-07 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Bio',
            new_name='bio',
        ),
    ]
