# Generated by Django 2.1.5 on 2019-02-27 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.BooleanField(default=0),
        ),
    ]