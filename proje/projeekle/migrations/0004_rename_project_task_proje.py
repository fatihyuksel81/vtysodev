# Generated by Django 4.2.9 on 2024-01-05 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projeekle", "0003_task"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task", old_name="project", new_name="proje",
        ),
    ]
