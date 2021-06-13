# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/9

from ncBackupSvc.ncBackupSvc import Iface
from ncJob.ttypes import ncBackupJobCountInfo


class BackupSvcProcessor(Iface):
    def __init__(self):
        pass

    def get_job_count_info(self, startTime, userId):
        """
        获取任务状态数据
        """

        return ncBackupJobCountInfo(
            failed=1,
            success=0,
            running=1,
        )

    def get_support_backup_type(self, job_id):
        """
        获取支持备份类型列表
        """

        return [111, 222, 333]

    def check_user_has_data(self, user_list):
        """
        获取有数据的任务列表
        """

        return ["aaa", "bbb", "ccc"]
