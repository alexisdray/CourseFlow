# Generated by Django 2.2.16 on 2020-09-28 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_flow', '0009_auto_20200917_2040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workflow',
            old_name='parent_activity',
            new_name='parent_workflow',
        ),
    ]