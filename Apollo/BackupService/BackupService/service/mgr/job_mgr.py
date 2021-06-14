# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/14
from BackupService.models import Job


class JobMgr(object):

    @classmethod
    def create(cls, **kwargs):
        try:
            job_orm = Job.objects.create(**kwargs)
            print("JobMgr::create success")
        except Exception as e:
            print("JobMgr::create error %s" % [e])
            job_orm = None
        finally:
            return job_orm

    @classmethod
    def count(cls):
        try:
            count = Job.objects.all().count()
        except Exception as e:
            print("JobMgr::count error %s" % [e])
            count = 0
        finally:
            return count
