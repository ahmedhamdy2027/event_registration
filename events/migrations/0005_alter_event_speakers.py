# Generated by Django 5.1 on 2024-08-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_speakers_event_organizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Speakers',
            field=models.CharField(default='Yossef mohamed', max_length=255),
        ),
    ]
