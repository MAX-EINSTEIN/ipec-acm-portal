# Generated by Django 3.2 on 2021-05-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20210505_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='starter_files',
            field=models.FileField(blank=True, null=True, upload_to='documents/starter_files/', verbose_name='Starter Files'),
        ),
    ]
