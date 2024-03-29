# Generated by Django 3.1.4 on 2021-02-04 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=15)),
                ('specialization', models.CharField(choices=[('AI/ML', 'AI/ML'), ('CSE', 'CSE'), ('CyberSecurity', 'CyberSecurity'), ('Networking', 'Networking'), ('Languages', 'Languages'), ('DBMS', 'DBMS'), ('Management', 'Management'), ('Basic Science', 'Basic Science'), ('Physical Edu', 'Physical Edu'), ('Electronics', 'Electronics'), ('Other', 'Other')], max_length=25, verbose_name='Specilised in ')),
                ('Fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Fid')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcode', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('sem', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1)),
                ('credit', models.PositiveIntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=50)),
                ('phno', models.CharField(max_length=12)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
                ('usn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usn')),
            ],
            options={
                'ordering': ['usn'],
            },
        ),
        migrations.CreateModel(
            name='SemSec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1, unique=True)),
                ('usn', models.ManyToManyField(to='management.Student', verbose_name='Students')),
            ],
        ),
        migrations.CreateModel(
            name='Incharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_cordinator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_cord', to='management.faculty')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.semsec')),
                ('cr1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cr1', to='management.student', verbose_name='CR 1')),
                ('cr2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cr2', to='management.student', verbose_name='CR 2')),
                ('sem_cordinator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sem_cord', to='management.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='subject',
            field=models.ManyToManyField(to='management.Subject', verbose_name='Subject'),
        ),
        migrations.CreateModel(
            name='IAmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ispresent', models.BooleanField(default=True, verbose_name='Present / Absent')),
                ('internals', models.CharField(choices=[('IA1', 'IA1'), ('IA2', 'IA2'), ('IA3', 'IA3')], max_length=3)),
                ('a1', models.PositiveIntegerField(default=0, verbose_name='1a')),
                ('a2', models.PositiveIntegerField(default=0, verbose_name='1b')),
                ('a3', models.PositiveIntegerField(default=0, verbose_name='1c')),
                ('b1', models.PositiveIntegerField(default=0, verbose_name='2a')),
                ('b2', models.PositiveIntegerField(default=0, verbose_name='2b')),
                ('b3', models.PositiveIntegerField(default=0, verbose_name='2c')),
                ('c1', models.PositiveIntegerField(default=0, verbose_name='3a')),
                ('c2', models.PositiveIntegerField(default=0, verbose_name='3b')),
                ('c3', models.PositiveIntegerField(default=0, verbose_name='3c')),
                ('d1', models.PositiveIntegerField(default=0, verbose_name='4a')),
                ('d2', models.PositiveIntegerField(default=0, verbose_name='4b')),
                ('d3', models.PositiveIntegerField(default=0, verbose_name='4c')),
                ('total_marks', models.PositiveIntegerField(default=0, verbose_name='Total')),
                ('assignment', models.PositiveIntegerField(default=0, verbose_name='Assignment')),
                ('average_marks', models.PositiveIntegerField(default=0, verbose_name='Average')),
                ('finial_marks', models.PositiveIntegerField(default=0, verbose_name='Finial')),
                ('sem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.semsec', verbose_name='Semister')),
                ('sub_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.subject', verbose_name='Subject code')),
                ('usn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student', verbose_name='Student')),
            ],
            options={
                'unique_together': {('usn', 'sub_code', 'internals')},
            },
        ),
    ]
