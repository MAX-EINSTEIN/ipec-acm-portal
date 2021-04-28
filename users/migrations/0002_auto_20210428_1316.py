# Generated by Django 3.2 on 2021-04-28 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='member',
            name='college_email_id',
            field=models.EmailField(default='roll_no@ipec.org.in', max_length=254, verbose_name='College Email'),
        ),
        migrations.AlterField(
            model_name='member',
            name='contact_number',
            field=models.CharField(default='', max_length=10),
        ),
    ]
