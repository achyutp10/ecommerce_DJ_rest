# Generated by Django 5.0.6 on 2024-07-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]