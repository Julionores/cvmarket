# Generated by Django 4.0.3 on 2022-04-10 15:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cvblog', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_edit',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='date_edit',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='nomcv',
            field=models.CharField(default=django.utils.timezone.now, max_length=128, verbose_name='nom de votre cv'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lettre',
            name='date_edit',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
