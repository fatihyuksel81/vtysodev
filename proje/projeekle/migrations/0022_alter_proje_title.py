# Generated by Django 4.2.9 on 2024-01-17 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projeekle", "0021_remove_task_delay_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="proje",
            name="title",
            field=models.CharField(max_length=50, verbose_name="Başlık"),
        ),
    ]