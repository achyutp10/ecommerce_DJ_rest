# Generated by Django 5.0.6 on 2024-07-17 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='email',
            field=models.CharField(blank=True, help_text='Shop Email', max_length=100, null=True),
        ),
    ]
