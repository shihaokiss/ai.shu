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
            success=1,
            running=1,
        )
