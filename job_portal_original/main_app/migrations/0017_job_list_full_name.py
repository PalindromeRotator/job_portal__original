# Generated by Django 4.0.2 on 2022-02-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_job_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_list',
            name='full_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]