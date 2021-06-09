# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/9
from client import ThriftClient
from ncBackupSvc import ncBackupSvc


def get_job_count():
    thrift_client = ThriftClient('192.168.1.3', 8888)
    job_count_info = thrift_client.request(ncBackupSvc, 'get_job_count_info', 10000, 'xxxx')
    print(job_count_info)


if __name__ == "__main__":
    get_job_count()
