# Generated by Django 3.2 on 2021-04-28 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigs', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='sigs',
            field=models.ManyToManyField(blank=True, limit_choices_to=3, to='sigs.SpecialInterestGroup'),
        ),
    ]
