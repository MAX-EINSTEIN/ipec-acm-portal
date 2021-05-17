# Generated by Django 3.2 on 2021-05-16 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20210516_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningresource',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='tasks.task', verbose_name='Learning Resource'),
        ),
        migrations.AlterField(
            model_name='learningresource',
            name='type',
            field=models.CharField(max_length=20),
        ),
    ]
