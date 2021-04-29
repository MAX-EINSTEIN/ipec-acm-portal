# Generated by Django 3.2 on 2021-04-28 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialInterestGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('session', models.IntegerField()),
                ('group_link', models.URLField(blank=True, null=True)),
                ('syllabus_link', models.URLField(blank=True, null=True)),
                ('management', models.ManyToManyField(to='users.ACMTeamMember')),
                ('members', models.ManyToManyField(blank=True, to='users.Member')),
            ],
        ),
    ]
