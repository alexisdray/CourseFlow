# Generated by Django 3.2.14 on 2022-09-30 19:48

from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    Project = apps.get_model('course_flow', 'project')
    for row in Project.objects.all():
        row.hash = uuid.uuid4()
        row.save(update_fields=['hash'])


class Migration(migrations.Migration):

    dependencies = [
        ('course_flow', '0090_project_hash'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
