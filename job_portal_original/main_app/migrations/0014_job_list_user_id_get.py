# Generated by Django 4.0.2 on 2022-02-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_job_list_job_id_get'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_list',
            name='user_id_get',
            field=models.IntegerField(default='0'),
        ),
    ]
