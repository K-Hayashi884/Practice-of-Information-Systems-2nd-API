# Generated by Django 4.2.2 on 2023-07-04 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Headline",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("video_id", models.TextField()),
                ("timestamp", models.FloatField()),
                ("headline", models.TextField()),
            ],
        ),
    ]
