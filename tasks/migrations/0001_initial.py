# Generated by Django 3.2 on 2021-05-17 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sigs', '0002_specialinterestgroup_management'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('topic', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('points', models.IntegerField()),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('starter_files', models.FileField(blank=True, null=True, upload_to='documents/starter_files/', verbose_name='Starter Files')),
                ('sig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='sigs.specialinterestgroup')),
            ],
        ),
        migrations.CreateModel(
            name='TaskSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('code_files', models.FileField(blank=True, null=True, upload_to='submissions/', verbose_name='Code')),
                ('output_files', models.FileField(blank=True, null=True, upload_to='submissions/', verbose_name='Output')),
                ('points_received', models.IntegerField(blank=True, default=0, null=True)),
                ('grading_status', models.BooleanField(choices=[(True, 'GRADED'), (False, 'PENDING')], default=False)),
                ('submitted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='task_submission', to='users.member')),
                ('submitted_for', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='task_submission', to='tasks.task')),
            ],
        ),
        migrations.CreateModel(
            name='LearningResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Article', 'ARTICLE'), ('Video', 'VIDEO'), ('Blog', 'BLOG'), ('Tool', 'TOOL'), ('Demo', 'DEMO')], max_length=20)),
                ('url', models.URLField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='tasks.task', verbose_name='Learning Resource')),
            ],
        ),
    ]
