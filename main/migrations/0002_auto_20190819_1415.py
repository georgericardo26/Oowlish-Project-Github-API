# Generated by Django 2.2.4 on 2019-08-19 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repository',
            old_name='id_user',
            new_name='id_repos',
        ),
    ]
