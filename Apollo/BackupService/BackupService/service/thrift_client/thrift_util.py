from ncBackupSvc import ncBackupSvc
from service.thrift_client.client import ThriftClient
from settings import SELF_IP, PORTS


class ThriftExecTask(object):
    def __init__(self):
        pass

    def backup_exec_task(self, func, timeout_ms=30*1000, *args, **kwargs):
        return self._exec_task(dest_ip=SELF_IP, port=PORTS['BackupService']['thrift'], func=func,
                               timeout_ms=timeout_ms, *args, **kwargs)

    @staticmethod
    def _exec_task(dest_ip, port, func, timeout_ms=30*1000, *args, **kwargs):
        try:
            print("ThriftExecTask::exec_task %s" % [dest_ip, port, func, timeout_ms, args, kwargs])
            thrift_client = ThriftClient(dest_ip, port, timeout_ms=timeout_ms)
            result = thrift_client.request(ncBackupSvc, func, *args, **kwargs)
            print("ThriftExecTask::_exec_task success %s" % [result])
            return result
        except Exception as e:
            print("ThriftExecTask::_exec_task error %s" % [e])
            raise e
