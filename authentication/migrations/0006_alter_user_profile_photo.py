# Generated by Django 4.0.3 on 2022-04-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo de profil'),
        ),
    ]
