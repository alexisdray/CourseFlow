# Generated by Django 2.2.6 on 2019-11-07 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_flow_creation_distribution', '0013_auto_20191104_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rightnodeicon',
            name='thumbnail_image',
        ),
        migrations.RemoveField(
            model_name='node',
            name='left_node_icon',
        ),
        migrations.RemoveField(
            model_name='node',
            name='right_node_icon',
        ),
        migrations.AddField(
            model_name='node',
            name='activity_classification',
            field=models.PositiveIntegerField(choices=[(0, 'Gather Information'), (1, 'Discuss'), (2, 'Solve'), (3, 'Analyze'), (4, 'Assess/Review Papers'), (5, 'Evaluate Peers'), (6, 'Debate'), (7, 'Game/Roleplay'), (8, 'Create/Design'), (9, 'Revise/Improve'), (10, 'Read'), (11, 'Write'), (12, 'Present'), (13, 'Experiment/Inquiry'), (14, 'Quiz/Test'), (15, 'Other')], default=0),
        ),
        migrations.AddField(
            model_name='node',
            name='parent_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_flow_creation_distribution.Node'),
        ),
        migrations.AddField(
            model_name='node',
            name='work_classification',
            field=models.PositiveIntegerField(choices=[(0, 'Individual Work'), (1, 'Work in Groups'), (2, 'Whole Class')], default=2),
        ),
        migrations.DeleteModel(
            name='LeftNodeIcon',
        ),
        migrations.DeleteModel(
            name='RightNodeIcon',
        ),
        migrations.DeleteModel(
            name='ThumbnailImage',
        ),
    ]
