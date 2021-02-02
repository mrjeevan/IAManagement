# Generated by Django 3.1.4 on 2021-01-17 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_auto_20210117_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iamarks',
            name='ss_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.semsec', verbose_name='Sem & Sec'),
        ),
        migrations.AlterField(
            model_name='iamarks',
            name='usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student', verbose_name='Student'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='credit',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subcode',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
