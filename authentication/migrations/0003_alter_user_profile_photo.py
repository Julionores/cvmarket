# Generated by Django 4.0.3 on 2022-04-10 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_date_created_user_date_edit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='photo de profil'),
        ),
    ]