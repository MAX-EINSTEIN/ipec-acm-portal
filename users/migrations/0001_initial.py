# Generated by Django 3.2 on 2021-05-17 03:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sigs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('roll_no', models.CharField(default='', max_length=20, unique=True)),
                ('bio', models.TextField(blank=True, default='Write something about yourself here')),
                ('branch', models.CharField(default='CSE', max_length=50)),
                ('year', models.IntegerField(default=1)),
                ('section', models.CharField(default='A', max_length=1)),
                ('college_email_id', models.EmailField(default='@ipec.org.in', max_length=254, verbose_name='College Email')),
                ('contact_number', models.CharField(default='', max_length=10)),
                ('profile_image', models.ImageField(blank=True, default='/media/images/profile/default.jpg', upload_to='images/profile/')),
                ('experience', models.TextField(blank=True, default='')),
                ('projects', models.TextField(blank=True, default='')),
                ('is_acm_team', models.BooleanField(default=False, null=True)),
                ('sigs', models.ManyToManyField(blank=True, related_name='sigs_joined', to='sigs.SpecialInterestGroup')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(choices=[('CHAIR', 'CHAIR'), ('VICE_CHAIR', 'VICE CHAIR'), ('PRIME_CORE', 'PRIME CORE'), ('CORE', 'CORE'), ('HEAD', 'SIG HEAD'), ('SUB_HEAD', 'SIG SUBHEAD'), ('COORDINATOR', 'COORDINATOR'), ('SUB_COORDINATOR', 'SUB COORDINATOR'), ('MEMBER', 'SIG MEMBER')], default='MEMBER', max_length=50)),
                ('joined_on', models.DateField(blank=True, null=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='role', to='users.member', verbose_name='Member')),
            ],
        ),
    ]
