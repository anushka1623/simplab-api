# Generated by Django 3.2.2 on 2021-05-17 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Simplab_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='all_member_teams', to='Simplab_API.User'),
        ),
        migrations.CreateModel(
            name='Ass_Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, max_length=25)),
                ('student_email', models.EmailField(blank=True, max_length=254)),
                ('exp_observations_image', models.ImageField(upload_to='assignment_submissions/images/observations')),
                ('exp_result', models.TextField()),
                ('submission_file', models.FileField(blank=True, upload_to='submission_files')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Simplab_API.user')),
            ],
        ),
    ]