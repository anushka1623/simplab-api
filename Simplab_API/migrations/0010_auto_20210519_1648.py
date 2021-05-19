# Generated by Django 3.2.2 on 2021-05-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simplab_API', '0009_auto_20210519_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='exp_observations_image',
            field=models.ImageField(blank=True, upload_to='assignment_submissions/images/observations'),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='student_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='student_name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='submission_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='submission_time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]