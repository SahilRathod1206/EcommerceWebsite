# Generated by Django 5.0 on 2024-01-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomApp', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
