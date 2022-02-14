# Generated by Django 4.0.2 on 2022-02-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('company_id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
