# Generated by Django 3.2.5 on 2021-07-11 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210711_0717'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserFilter',
            new_name='UserSearchHistory',
        ),
    ]