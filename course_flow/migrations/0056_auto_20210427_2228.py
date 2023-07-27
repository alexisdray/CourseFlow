# Generated by Django 2.2.20 on 2021-04-27 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course_flow", "0055_delete_outcomeworkflow"),
    ]

    operations = [
        migrations.CreateModel(
            name="OutcomeWorkflow",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("added_on", models.DateTimeField(auto_now_add=True)),
                ("rank", models.PositiveIntegerField(default=0)),
                (
                    "outcome",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course_flow.Outcome",
                    ),
                ),
                (
                    "workflow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course_flow.Workflow",
                    ),
                ),
            ],
            options={
                "verbose_name": "Outcome-Workflow Link",
                "verbose_name_plural": "Outcome-Workflow Links",
            },
        ),
        migrations.AddField(
            model_name="workflow",
            name="outcomes",
            field=models.ManyToManyField(
                blank=True,
                through="course_flow.OutcomeWorkflow",
                to="course_flow.Outcome",
            ),
        ),
    ]
