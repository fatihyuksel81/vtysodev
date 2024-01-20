# Generated by Django 4.2.9 on 2024-01-06 18:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projeekle", "0005_remove_proje_members"),
    ]

    operations = [
        migrations.AddField(
            model_name="proje",
            name="members",
            field=models.ManyToManyField(
                blank=True,
                related_name="projects_as_member",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Üyeler",
            ),
        ),
    ]