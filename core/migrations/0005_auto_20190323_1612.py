# Generated by Django 2.1.5 on 2019-03-23 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190323_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='milestone',
            old_name='group',
            new_name='semester',
        ),
    ]
