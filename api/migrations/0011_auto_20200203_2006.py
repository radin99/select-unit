# Generated by Django 2.2.6 on 2020-02-03 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200203_1847'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='daily_time',
        ),
        migrations.RemoveField(
            model_name='course',
            name='day',
        ),
        migrations.AddField(
            model_name='course',
            name='class_times',
            field=models.CharField(default=None, max_length=350, null=True),
        ),
    ]
