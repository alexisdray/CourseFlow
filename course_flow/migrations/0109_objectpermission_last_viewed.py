# Generated by Django 3.2.15 on 2023-02-08 14:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course_flow", "0108_alter_objectpermission_content_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="objectpermission",
            name="last_viewed",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
