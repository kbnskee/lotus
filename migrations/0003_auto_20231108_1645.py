# Generated by Django 3.1.2 on 2023-11-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotus', '0002_auto_20231023_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
