# Generated by Django 4.0.2 on 2022-02-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('profile_picture', models.ImageField(blank=True, default='user_profile.png', upload_to='')),
                ('username', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('eMail', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
