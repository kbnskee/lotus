# Generated by Django 3.1.2 on 2023-12-14 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotus', '0018_auto_20231205_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
