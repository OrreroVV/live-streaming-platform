# Generated by Django 3.2.8 on 2024-05-17 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamingPlatform', '0006_auto_20240516_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livecounts',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]