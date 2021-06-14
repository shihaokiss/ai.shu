# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/12
import json

from django.http import HttpResponse
from django.views import View

from service.mgr.job_mgr import JobMgr
from service.thrift_client.get_job_count import get_job_count


class BackupJobsHandler(View):

    def get(self, request):
        print("get func... %s" % request)
        result = get_job_count()
        print("get_job_count %s" % [result])
        if result.get('success', 0) > 0:
            job_orm = JobMgr().create(name='test%d' % JobMgr().count())
            print("create_job success %s" % [job_orm.name])
        response = HttpResponse(content_type='application/json', charset='UTF-8')
        response.content = json.dumps(result)
        return response
