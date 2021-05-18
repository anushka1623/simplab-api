# Generated by Django 3.2.2 on 2021-05-17 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Simplab_API', '0005_rename_ass_submission_assignmentsubmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='sender_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='chat',
            name='sender_profile',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='chat',
            name='sent_time',
            field=models.TimeField(blank=-1, default=django.utils.timezone.now),
        ),
    ]