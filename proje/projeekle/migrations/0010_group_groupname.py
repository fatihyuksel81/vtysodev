# Generated by Django 4.2.9 on 2024-01-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projeekle", "0009_proje_group_alter_group_proje"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="groupname",
            field=models.CharField(
                default="Varsayılan Grup İsmi", max_length=50, verbose_name="Gurup Adı"
            ),
        ),
    ]