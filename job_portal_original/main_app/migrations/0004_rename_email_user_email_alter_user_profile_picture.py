# Generated by Django 4.0.2 on 2022-02-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_user_achievements_user_firstname_user_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='eMail',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, default='user.png', upload_to=''),
        ),
    ]
