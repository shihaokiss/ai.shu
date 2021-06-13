# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/9


from ncBackupSvc import ncBackupSvc
from service.thrift_client.client import ThriftClient


def get_job_count():
    thrift_client = ThriftClient('192.168.1.3', 8888)
    job_count_info = thrift_client.request(ncBackupSvc, 'get_job_count_info', 10000, 'xxxx')
    return {"failed": job_count_info.failed, "success": job_count_info.success, "running": job_count_info.running}


if __name__ == "__main__":
    get_job_count()
