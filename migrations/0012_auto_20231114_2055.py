# Generated by Django 3.1.2 on 2023-11-14 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotus', '0011_auto_20231111_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usergroup', to=settings.AUTH_USER_MODEL),
        ),
    ]
