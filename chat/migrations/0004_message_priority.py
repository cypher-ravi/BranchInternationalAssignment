# Generated by Django 4.1.5 on 2023-01-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_customuser_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='priority',
            field=models.CharField(blank=True, choices=[('medium', 'medium'), ('low', 'low'), ('high', 'high')], max_length=50, null=True),
        ),
    ]
