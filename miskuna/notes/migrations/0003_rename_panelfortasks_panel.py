# Generated by Django 4.1.1 on 2022-09-10 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_remove_task_panel_panelfortasks_tasks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PanelForTasks',
            new_name='Panel',
        ),
    ]