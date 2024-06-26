# Generated by Django 5.0.4 on 2024-06-05 07:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={
                "ordering": ["-created_at"],
                "permissions": [("ban_comment", "Can ban comment")],
            },
        ),
        migrations.AlterModelOptions(
            name="review",
            options={
                "permissions": [("mark_as_spoiler", "Can change is_spoiler to True")]
            },
        ),
    ]
