# Generated by Django 4.2.9 on 2024-01-12 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_customuser_job"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="job",),
    ]