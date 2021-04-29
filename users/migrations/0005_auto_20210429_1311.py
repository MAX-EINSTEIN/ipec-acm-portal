# Generated by Django 3.2 on 2021-04-29 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigs', '0001_initial'),
        ('users', '0004_alter_member_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='sigs',
            field=models.ManyToManyField(blank=True, to='sigs.SpecialInterestGroup'),
        ),
        migrations.AlterField(
            model_name='member',
            name='year',
            field=models.IntegerField(default=1),
        ),
    ]
