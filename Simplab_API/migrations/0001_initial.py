# Generated by Django 3.2.2 on 2021-05-17 04:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.TextField(blank=True)),
                ('exp_name', models.CharField(blank=True, max_length=100)),
                ('aim', models.TextField(blank=True)),
                ('procedure', models.TextField(blank=True)),
                ('calculations', models.ImageField(blank=True, upload_to='exp_images')),
                ('precautions', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Experiment_Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('exp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Simplab_API.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User_Detail',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Simplab_API.user')),
                ('username', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('profile_image', models.ImageField(blank=True, upload_to='profile_images')),
                ('organization', models.CharField(blank=True, default='not selected', max_length=15)),
                ('contact', models.CharField(blank=True, default='+911234567890', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Simplab_API.user')),
                ('students', models.ManyToManyField(blank=True, default=['7'], related_name='all_member_teams', to='Simplab_API.User')),
            ],
        ),
        migrations.AddField(
            model_name='experiment_assignment',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_team_experiments', to='Simplab_API.team'),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('message', models.TextField(blank=True)),
                ('is_file', models.BooleanField(blank=True, default=False)),
                ('chat_file', models.FileField(blank=True, upload_to='chat_files')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Simplab_API.user')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Simplab_API.team')),
            ],
        ),
    ]