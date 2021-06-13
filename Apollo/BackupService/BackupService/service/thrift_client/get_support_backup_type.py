# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/9

from ncBackupSvc import ncBackupSvc
from service.thrift_client.client import ThriftClient


def get_support_backup_type():
    thrift_client = ThriftClient('192.168.1.3', 8888)
    type_list = thrift_client.request(ncBackupSvc, 'get_support_backup_type', 'xxxx')
    print(type_list)


if __name__ == "__main__":
    get_support_backup_type()
