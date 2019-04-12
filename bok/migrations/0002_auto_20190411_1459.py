# Generated by Django 2.1.2 on 2019-04-11 05:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bok', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='token',
            field=models.UUIDField(default=uuid.UUID('ee842f40-5c1e-11e9-900d-7c763549e4c1'), unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='token',
            field=models.UUIDField(default=uuid.UUID('ee842f41-5c1e-11e9-84af-7c763549e4c1'), unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='token',
            field=models.UUIDField(default=uuid.UUID('ee84563a-5c1e-11e9-aaaa-7c763549e4c1'), unique=True),
        ),
    ]