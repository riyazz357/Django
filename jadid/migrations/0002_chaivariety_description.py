# Generated by Django 5.2.4 on 2025-07-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jadid", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chaivariety",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
