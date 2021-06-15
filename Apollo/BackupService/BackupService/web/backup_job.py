# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/12
import json

from django.http import HttpResponse
from django.views import View

from service.backup_job import BackupJobsService


class BackupJobsHandler(View):

    def get(self, request):
        print("BackupJobsHandler::get func... %s" % request)
        result = BackupJobsService(request).get_dict()
        print("BackupJobsHandler::get success... %s" % result)
        response = HttpResponse(content_type='application/json', charset='UTF-8')
        response.content = json.dumps(result)
        return response
