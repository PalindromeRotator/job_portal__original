# Generated by Django 4.0.2 on 2022-02-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_job_list_user_id_get'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='password',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
