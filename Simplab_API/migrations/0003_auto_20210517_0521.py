# Generated by Django 3.2.2 on 2021-05-17 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Simplab_API', '0002_auto_20210517_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ass_submission',
            name='student_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='ass_submission',
            name='student_name',
            field=models.CharField(max_length=25),
        ),
    ]
