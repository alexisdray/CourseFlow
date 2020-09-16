# Generated by Django 2.2.16 on 2020-09-15 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('static', models.BooleanField(default=False)),
                ('is_original', models.BooleanField(default=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_activities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_original', models.BooleanField(default=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_original', models.BooleanField(default=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Column',
                'verbose_name_plural': 'Columns',
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='ComponentProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Component')),
            ],
            options={
                'verbose_name': 'Component-Program Link',
                'verbose_name_plural': 'Component-Program Links',
            },
        ),
        migrations.CreateModel(
            name='ComponentWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Component')),
            ],
            options={
                'verbose_name': 'Component-Week Link',
                'verbose_name_plural': 'Component-Week Links',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('static', models.BooleanField(default=False)),
                ('is_original', models.BooleanField(default=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the name of a new discipline.', max_length=100, unique=True, verbose_name='Discipline name')),
            ],
            options={
                'verbose_name': 'discipline',
                'verbose_name_plural': 'disciplines',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_original', models.BooleanField(default=True)),
                ('work_classification', models.PositiveIntegerField(choices=[(1, 'Individual Work'), (2, 'Work in Groups'), (3, 'Whole Class')], default=2)),
                ('activity_classification', models.PositiveIntegerField(choices=[(1, 'Gather Information'), (2, 'Discuss'), (3, 'Solve'), (4, 'Analyze'), (5, 'Assess/Review Papers'), (6, 'Evaluate Peers'), (7, 'Debate'), (8, 'Game/Roleplay'), (9, 'Create/Design'), (10, 'Revise/Improve'), (11, 'Read'), (12, 'Write'), (13, 'Present'), (14, 'Experiment/Inquiry'), (15, 'Quiz/Test'), (16, 'Other')], default=1)),
                ('classification', models.PositiveIntegerField(choices=[(0, 'Out of Class'), (1, 'In Class (Instructor)'), (2, 'In Class (Students)')], default=1)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authored_nodes', to=settings.AUTH_USER_MODEL)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='course_flow.Column')),
            ],
        ),
        migrations.CreateModel(
            name='NodeStrategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Node')),
            ],
            options={
                'verbose_name': 'Node-Strategy Link',
                'verbose_name_plural': 'Node-Strategy Links',
            },
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Outcome',
                'verbose_name_plural': 'Outcomes',
            },
        ),
        migrations.CreateModel(
            name='OutcomePreparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Outcome')),
            ],
            options={
                'verbose_name': 'Outcome-Preparation Link',
                'verbose_name_plural': 'Outcome-Preparation Links',
            },
        ),
        migrations.CreateModel(
            name='OutcomeProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Outcome')),
            ],
            options={
                'verbose_name': 'Outcome-Program Link',
                'verbose_name_plural': 'Outcome-Program Links',
            },
        ),
        migrations.CreateModel(
            name='OutcomeStrategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Outcome')),
            ],
            options={
                'verbose_name': 'Outcome-Strategy Link',
                'verbose_name_plural': 'Outcome-Strategy Links',
            },
        ),
        migrations.CreateModel(
            name='OutcomeWeek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Outcome')),
            ],
            options={
                'verbose_name': 'Outcome-Week Link',
                'verbose_name_plural': 'Outcome-Week Links',
            },
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('default', models.BooleanField(default=False)),
                ('is_original', models.BooleanField(default=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('nodes', models.ManyToManyField(blank=True, through='course_flow.NodeStrategy', to='course_flow.Node')),
                ('outcomes', models.ManyToManyField(blank=True, through='course_flow.OutcomeStrategy', to='course_flow.Outcome')),
                ('parent_strategy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_flow.Strategy')),
            ],
            options={
                'verbose_name': 'Strategy',
                'verbose_name_plural': 'Strategies',
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('components', models.ManyToManyField(blank=True, through='course_flow.ComponentWeek', to='course_flow.Component')),
                ('outcomes', models.ManyToManyField(blank=True, through='course_flow.OutcomeWeek', to='course_flow.Outcome')),
            ],
        ),
        migrations.CreateModel(
            name='WeekCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Course')),
                ('week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Week')),
            ],
            options={
                'verbose_name': 'Week-Course Link',
                'verbose_name_plural': 'Week-Course Links',
            },
        ),
        migrations.CreateModel(
            name='StrategyActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Activity')),
                ('strategy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Strategy')),
            ],
            options={
                'verbose_name': 'Strategy-Activity Link',
                'verbose_name_plural': 'Strategy-Activity Links',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('components', models.ManyToManyField(blank=True, through='course_flow.ComponentProgram', to='course_flow.Component')),
                ('outcomes', models.ManyToManyField(blank=True, through='course_flow.OutcomeProgram', to='course_flow.Outcome')),
            ],
        ),
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=400)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_original', models.BooleanField(default=True)),
                ('hash', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('outcomes', models.ManyToManyField(blank=True, through='course_flow.OutcomePreparation', to='course_flow.Outcome')),
                ('parent_preparation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_flow.Preparation')),
            ],
        ),
        migrations.AddField(
            model_name='outcomeweek',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Week'),
        ),
        migrations.AddField(
            model_name='outcomestrategy',
            name='strategy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Strategy'),
        ),
        migrations.AddField(
            model_name='outcomeprogram',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Program'),
        ),
        migrations.AddField(
            model_name='outcomepreparation',
            name='preparation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Preparation'),
        ),
        migrations.CreateModel(
            name='OutcomeNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Node')),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Outcome')),
            ],
            options={
                'verbose_name': 'Outcome-Node Link',
                'verbose_name_plural': 'Outcome-Node Links',
            },
        ),
        migrations.CreateModel(
            name='OutcomeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Course')),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Outcome')),
            ],
            options={
                'verbose_name': 'Outcome-Course Link',
                'verbose_name_plural': 'Outcome-Course Links',
            },
        ),
        migrations.CreateModel(
            name='OutcomeAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Assessment')),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Outcome')),
            ],
            options={
                'verbose_name': 'Outcome-Assessment Link',
                'verbose_name_plural': 'Outcome-Assessment Links',
            },
        ),
        migrations.CreateModel(
            name='OutcomeArtifact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('artifact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Artifact')),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Outcome')),
            ],
            options={
                'verbose_name': 'Outcome-Artifact Link',
                'verbose_name_plural': 'Outcome-Artifact Links',
            },
        ),
        migrations.CreateModel(
            name='OutcomeActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Activity')),
                ('outcome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Outcome')),
            ],
            options={
                'verbose_name': 'Outcome-Activity Link',
                'verbose_name_plural': 'Outcome-Activity Links',
            },
        ),
        migrations.AddField(
            model_name='nodestrategy',
            name='strategy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Strategy'),
        ),
        migrations.CreateModel(
            name='NodeCompletionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Node')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Node Completion Status',
                'verbose_name_plural': 'Node Completion Statuses',
            },
        ),
        migrations.AddField(
            model_name='node',
            name='outcomes',
            field=models.ManyToManyField(blank=True, through='course_flow.OutcomeNode', to='course_flow.Outcome'),
        ),
        migrations.AddField(
            model_name='node',
            name='parent_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_flow.Node'),
        ),
        migrations.AddField(
            model_name='node',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='assigned_nodes', through='course_flow.NodeCompletionStatus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_flow.Discipline'),
        ),
        migrations.AddField(
            model_name='course',
            name='outcomes',
            field=models.ManyToManyField(blank=True, through='course_flow.OutcomeCourse', to='course_flow.Outcome'),
        ),
        migrations.AddField(
            model_name='course',
            name='parent_course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_flow.Course'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='assigned_courses', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='weeks',
            field=models.ManyToManyField(blank=True, through='course_flow.WeekCourse', to='course_flow.Week'),
        ),
        migrations.AddField(
            model_name='componentweek',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Week'),
        ),
        migrations.AddField(
            model_name='componentprogram',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Program'),
        ),
        migrations.CreateModel(
            name='ComponentCompletionStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_completed', models.BooleanField(default=False)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Component')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Component Completion Status',
                'verbose_name_plural': 'Component Completion Statuses',
            },
        ),
        migrations.AddField(
            model_name='component',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='assigned_componenets', through='course_flow.ComponentCompletionStatus', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='ColumnActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('rank', models.PositiveIntegerField(default=0)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Activity')),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_flow.Column')),
            ],
            options={
                'verbose_name': 'Column-Activity Link',
                'verbose_name_plural': 'Column-Activity Links',
            },
        ),
        migrations.AddField(
            model_name='assessment',
            name='outcomes',
            field=models.ManyToManyField(blank=True, through='course_flow.OutcomeAssessment', to='course_flow.Outcome'),
        ),
        migrations.AddField(
            model_name='assessment',
            name='parent_assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_flow.Assessment'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='outcomes',
            field=models.ManyToManyField(blank=True, through='course_flow.OutcomeArtifact', to='course_flow.Outcome'),
        ),
        migrations.AddField(
            model_name='artifact',
            name='parent_artifact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_flow.Artifact'),
        ),
        migrations.AddField(
            model_name='activity',
            name='columns',
            field=models.ManyToManyField(blank=True, through='course_flow.ColumnActivity', to='course_flow.Column'),
        ),
        migrations.AddField(
            model_name='activity',
            name='outcomes',
            field=models.ManyToManyField(blank=True, through='course_flow.OutcomeActivity', to='course_flow.Outcome'),
        ),
        migrations.AddField(
            model_name='activity',
            name='parent_activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='course_flow.Activity'),
        ),
        migrations.AddField(
            model_name='activity',
            name='strategies',
            field=models.ManyToManyField(blank=True, through='course_flow.StrategyActivity', to='course_flow.Strategy'),
        ),
        migrations.AddField(
            model_name='activity',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='assigned_activities', to=settings.AUTH_USER_MODEL),
        ),
    ]
