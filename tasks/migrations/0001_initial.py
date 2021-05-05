from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sigs', '0001_initial'),
        ('users', '0002_member_sigs'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
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
                ('resources', models.ManyToManyField(blank=True, to='tasks.LearningResource')),
                ('sig', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sigs.specialinterestgroup')),
            ],
        ),
        migrations.CreateModel(
            name='TaskSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_on', models.DateTimeField(auto_now_add=True)),
                ('files', models.URLField()),
                ('points_received', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.BooleanField(default=False)),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.member')),
                ('submitted_for', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='tasks.task')),
            ],
        ),
    ]