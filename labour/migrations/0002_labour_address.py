# Generated by Django 5.1.7 on 2025-03-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labour',
            name='address',
            field=models.CharField(blank=True, max_length=999, null=True),
        ),
    ]
