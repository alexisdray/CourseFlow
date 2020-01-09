# Generated by Django 2.2.6 on 2019-10-18 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("course_flow_creation_distribution", "0006_auto_20191017_1850"),
    ]

    operations = [
        migrations.AddField(
            model_name="week",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="week",
            name="created_on",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="week",
            name="last_modified",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
