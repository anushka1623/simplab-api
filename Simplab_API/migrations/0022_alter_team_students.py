# Generated by Django 3.2.2 on 2021-05-14 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simplab_API', '0021_alter_team_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='students',
            field=models.ManyToManyField(blank=True, default=['7'], related_name='all_member_teams', to='Simplab_API.User'),
        ),
    ]