# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/9

from ncBackupSvc import ncBackupSvc
from service.thrift_client.client import ThriftClient


def check_user_has_data():
    thrift_client = ThriftClient('192.168.1.3', 8888)
    type_list = thrift_client.request(ncBackupSvc, 'check_user_has_data', 'xxxx')
    print(type_list)


if __name__ == "__main__":
    check_user_has_data()
