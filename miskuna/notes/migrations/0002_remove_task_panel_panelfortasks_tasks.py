# Generated by Django 4.1.1 on 2022-09-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='panel',
        ),
        migrations.AddField(
            model_name='panelfortasks',
            name='tasks',
            field=models.ManyToManyField(to='notes.task'),
        ),
    ]