from BackupService.models import Job
from service.thrift_client.thrift_util import ThriftExecTask


class BackupJobsService(object):
    def __init__(self, request):
        self.request = request

    def get_dict(self):
        print("BackupJobsService::get_job_count start %s" % [self.request])
        response = {"id": "", "name": ""}
        result = ThriftExecTask().backup_exec_task("get_job_count_info", startTime=10, userId='xxxx')
        print("BackupJobsService::get_job_count %s" % [result])
        if result.success > 0:
            job_orm = Job.objects.create(name='test%d' % Job.objects.all().count())
            print("BackupJobsService::create_job success %s" % [job_orm.name])
            response["id"] = job_orm.id
            response["name"] = job_orm.name
        return response
