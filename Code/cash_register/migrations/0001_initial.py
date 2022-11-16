# Generated by Django 4.1.3 on 2022-11-16 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.TextField(max_length=200)),
                ("code", models.IntegerField(default=0)),
                ("price", models.FloatField(default=0)),
            ],
        ),
    ]