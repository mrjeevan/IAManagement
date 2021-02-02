# Generated by Django 3.1.4 on 2021-01-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20210116_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semsec',
            name='sem',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='usn',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='sem',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=1),
        ),
    ]