# Generated by Django 5.0.6 on 2024-07-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_tax_options_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitem',
            name='coupon',
            field=models.ManyToManyField(blank=True, to='store.coupon'),
        ),
    ]
