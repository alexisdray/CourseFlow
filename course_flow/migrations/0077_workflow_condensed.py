# Generated by Django 2.2.25 on 2022-01-11 21:54

from django.db import migrations, models

from course_flow.models import Program


def forwards_func(apps, schema_editor):
    Program.objects.all().update(condensed=True)


class Migration(migrations.Migration):

    dependencies = [
        ("course_flow", "0076_auto_20211217_2107"),
    ]

    operations = [
        migrations.AddField(
            model_name="workflow",
            name="condensed",
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(forwards_func),
    ]
