# Generated by Django 4.2.9 on 2024-01-12 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projeekle", "0020_alter_task_delay_time"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="delay_time",),
    ]