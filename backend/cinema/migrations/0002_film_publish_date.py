# Generated by Django 4.1.9 on 2023-06-22 16:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="publish_date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
