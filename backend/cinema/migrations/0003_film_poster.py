# Generated by Django 4.1.9 on 2023-06-26 00:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0002_film_publish_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="poster",
            field=models.FileField(default=None, upload_to=""),
        ),
    ]
