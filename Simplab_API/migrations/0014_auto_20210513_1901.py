# Generated by Django 3.2.2 on 2021-05-13 19:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Simplab_API', '0013_alter_experiment_assignment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='students',
            field=models.ManyToManyField(blank=True, default=[models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Simplab_API.user')], related_name='all_students_enrolled', to='Simplab_API.User'),
        ),
        migrations.AlterField(
            model_name='user_detail',
            name='email',
            field=models.EmailField(blank=True, default=django.utils.timezone.now, max_length=254),
        ),
    ]
