# Generated by Django 4.0.2 on 2022-02-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_user_gender_alter_user_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default='default', max_length=30),
        ),
    ]
