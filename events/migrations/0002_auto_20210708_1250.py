# Generated by Django 3.2.5 on 2021-07-08 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventtopics',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='eventtopics',
            old_name='topic_id',
            new_name='topic',
        ),
    ]
