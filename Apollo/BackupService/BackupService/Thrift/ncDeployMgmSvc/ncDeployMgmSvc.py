# -*- coding: UTF-8 -*-
#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:coding=UTF-8
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    """
    部署服务相关接口

    """
    def update_task_status(self, ncDeployTaskInfo):
        """
        提交更新任务状态的请求

        @param body: 请求参数

        @throw 转抛内部调用异常

        Parameters:
         - ncDeployTaskInfo

        """
        pass

    def export_detail(self, monitor_id, body):
        """
        导出部署任务操作详情记录
        @ return


        Parameters:
         - monitor_id
         - body

        """
        pass


class Client(Iface):
    """
    部署服务相关接口

    """
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def update_task_status(self, ncDeployTaskInfo):
        """
        提交更新任务状态的请求

        @param body: 请求参数

        @throw 转抛内部调用异常

        Parameters:
         - ncDeployTaskInfo

        """
        self.send_update_task_status(ncDeployTaskInfo)
        self.recv_update_task_status()

    def send_update_task_status(self, ncDeployTaskInfo):
        self._oprot.writeMessageBegin('update_task_status', TMessageType.CALL, self._seqid)
        args = update_task_status_args()
        args.ncDeployTaskInfo = ncDeployTaskInfo
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_update_task_status(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = update_task_status_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.exp is not None:
            raise result.exp
        return

    def export_detail(self, monitor_id, body):
        """
        导出部署任务操作详情记录
        @ return


        Parameters:
         - monitor_id
         - body

        """
        self.send_export_detail(monitor_id, body)
        return self.recv_export_detail()

    def send_export_detail(self, monitor_id, body):
        self._oprot.writeMessageBegin('export_detail', TMessageType.CALL, self._seqid)
        args = export_detail_args()
        args.monitor_id = monitor_id
        args.body = body
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_export_detail(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = export_detail_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.error is not None:
            raise result.error
        raise TApplicationException(TApplicationException.MISSING_RESULT, "export_detail failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["update_task_status"] = Processor.process_update_task_status
        self._processMap["export_detail"] = Processor.process_export_detail
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_update_task_status(self, seqid, iprot, oprot):
        args = update_task_status_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = update_task_status_result()
        try:
            self._handler.update_task_status(args.ncDeployTaskInfo)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ncException.ttypes.ncException as exp:
            msg_type = TMessageType.REPLY
            result.exp = exp
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("update_task_status", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_export_detail(self, seqid, iprot, oprot):
        args = export_detail_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = export_detail_result()
        try:
            result.success = self._handler.export_detail(args.monitor_id, args.body)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ncException.ttypes.ncException as error:
            msg_type = TMessageType.REPLY
            result.error = error
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("export_detail", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class update_task_status_args(object):
    """
    Attributes:
     - ncDeployTaskInfo

    """


    def __init__(self, ncDeployTaskInfo=None,):
        self.ncDeployTaskInfo = ncDeployTaskInfo

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.ncDeployTaskInfo = ncDeploymentDefinition.ttypes.ncDeployTaskInfo()
                    self.ncDeployTaskInfo.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('update_task_status_args')
        if self.ncDeployTaskInfo is not None:
            oprot.writeFieldBegin('ncDeployTaskInfo', TType.STRUCT, 1)
            self.ncDeployTaskInfo.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(update_task_status_args)
update_task_status_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'ncDeployTaskInfo', [ncDeploymentDefinition.ttypes.ncDeployTaskInfo, None], None, ),  # 1
)


class update_task_status_result(object):
    """
    Attributes:
     - exp

    """


    def __init__(self, exp=None,):
        self.exp = exp

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.exp = ncException.ttypes.ncException()
                    self.exp.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('update_task_status_result')
        if self.exp is not None:
            oprot.writeFieldBegin('exp', TType.STRUCT, 1)
            self.exp.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(update_task_status_result)
update_task_status_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'exp', [ncException.ttypes.ncException, None], None, ),  # 1
)


class export_detail_args(object):
    """
    Attributes:
     - monitor_id
     - body

    """


    def __init__(self, monitor_id=None, body=None,):
        self.monitor_id = monitor_id
        self.body = body

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I64:
                    self.monitor_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.body = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val6 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.body[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('export_detail_args')
        if self.monitor_id is not None:
            oprot.writeFieldBegin('monitor_id', TType.I64, 1)
            oprot.writeI64(self.monitor_id)
            oprot.writeFieldEnd()
        if self.body is not None:
            oprot.writeFieldBegin('body', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.body))
            for kiter7, viter8 in self.body.items():
                oprot.writeString(kiter7.encode('utf-8') if sys.version_info[0] == 2 else kiter7)
                oprot.writeString(viter8.encode('utf-8') if sys.version_info[0] == 2 else viter8)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(export_detail_args)
export_detail_args.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'monitor_id', None, None, ),  # 1
    (2, TType.MAP, 'body', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
)


class export_detail_result(object):
    """
    Attributes:
     - success
     - error

    """


    def __init__(self, success=None, error=None,):
        self.success = success
        self.error = error

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.MAP:
                    self.success = {}
                    (_ktype10, _vtype11, _size9) = iprot.readMapBegin()
                    for _i13 in range(_size9):
                        _key14 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val15 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.success[_key14] = _val15
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.error = ncException.ttypes.ncException()
                    self.error.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('export_detail_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.MAP, 0)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.success))
            for kiter16, viter17 in self.success.items():
                oprot.writeString(kiter16.encode('utf-8') if sys.version_info[0] == 2 else kiter16)
                oprot.writeString(viter17.encode('utf-8') if sys.version_info[0] == 2 else viter17)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.error is not None:
            oprot.writeFieldBegin('error', TType.STRUCT, 1)
            self.error.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(export_detail_result)
export_detail_result.thrift_spec = (
    (0, TType.MAP, 'success', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 0
    (1, TType.STRUCT, 'error', [ncException.ttypes.ncException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs

