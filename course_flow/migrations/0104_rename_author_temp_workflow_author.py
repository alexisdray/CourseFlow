# Generated by Django 3.2.15 on 2023-02-05 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course_flow", "0103_auto_20230205_1626"),
    ]

    operations = [
        migrations.RenameField(
            model_name="workflow",
            old_name="author_temp",
            new_name="author",
        ),
    ]
