# Generated by Django 4.0.3 on 2022-04-09 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='nomcv',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='nom de votre cv'),
        ),
    ]
