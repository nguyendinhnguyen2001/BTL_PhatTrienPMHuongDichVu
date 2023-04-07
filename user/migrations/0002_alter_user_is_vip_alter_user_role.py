# Generated by Django 4.1.7 on 2023-04-03 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_vip",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(default="member", max_length=200),
        ),
    ]