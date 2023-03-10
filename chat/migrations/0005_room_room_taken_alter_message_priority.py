# Generated by Django 4.1.5 on 2023-01-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_message_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_taken',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='priority',
            field=models.CharField(blank=True, choices=[('medium', 'medium'), ('high', 'high'), ('low', 'low')], max_length=50, null=True),
        ),
    ]
