# Generated by Django 3.2 on 2021-04-29 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_member_submissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='year',
            field=models.IntegerField(),
        ),
    ]
