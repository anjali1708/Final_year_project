# Generated by Django 2.1.5 on 2019-03-05 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_project_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='abstract',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Abstract'),
        ),
    ]