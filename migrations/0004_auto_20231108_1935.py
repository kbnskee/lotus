# Generated by Django 3.1.2 on 2023-11-08 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotus', '0003_auto_20231108_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]