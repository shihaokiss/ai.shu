# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/12
from django.db import models
import uuid


def get_uuid():
    return uuid.uuid1().hex


class Job(models.Model):

    id = models.CharField(primary_key=True, max_length=36, default=get_uuid)
    name = models.CharField(max_length=100, default='', db_index=True)


class JobInstance(models.Model):

    id = models.CharField(primary_key=True, max_length=36, default=get_uuid)
    job_name = models.CharField(max_length=100, default='', db_index=True)

