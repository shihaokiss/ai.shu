# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/12

from django.db import migrations, models

from BackupService.models import get_uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BackupService', '0001_initial')
    ]

    operations = [
        migrations.CreateModel(
            name='JobInstance',
            fields=[
                ('id', models.CharField(default=get_uuid, max_length=36, primary_key=True, serialize=False)),
                ('job_name', models.CharField(db_index=True, default='', max_length=100)),
            ],
            options={
                'abstract': False,
            },
        )
    ]
