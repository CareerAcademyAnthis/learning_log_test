# Generated by Django 4.0.4 on 2022-04-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='date_addedd',
            new_name='date_added',
        ),
    ]
