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
import ncStrategy_Var.ttypes

from thrift.transport import TTransport
all_structs = []


class ncStrategyInfo(object):
    """
    Attributes:
     - id
     - name
     - type
     - dataProtectTime
     - dataProtectUnit
     - logProtectTime
     - logProtectUnit
     - durationEnable
     - durationTime
     - durationUnit
     - retentionTime
     - retentionUnit

    """


    def __init__(self, id=None, name=None, type=None, dataProtectTime=None, dataProtectUnit=None, logProtectTime=None, logProtectUnit=None, durationEnable=None, durationTime=None, durationUnit=None, retentionTime=None, retentionUnit=None,):
        self.id = id
        self.name = name
        self.type = type
        self.dataProtectTime = dataProtectTime
        self.dataProtectUnit = dataProtectUnit
        self.logProtectTime = logProtectTime
        self.logProtectUnit = logProtectUnit
        self.durationEnable = durationEnable
        self.durationTime = durationTime
        self.durationUnit = durationUnit
        self.retentionTime = retentionTime
        self.retentionUnit = retentionUnit

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
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.dataProtectTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.dataProtectUnit = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.logProtectTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.logProtectUnit = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.durationEnable = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I64:
                    self.durationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.durationUnit = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I64:
                    self.retentionTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.retentionUnit = iprot.readI32()
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
        oprot.writeStructBegin('ncStrategyInfo')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.dataProtectTime is not None:
            oprot.writeFieldBegin('dataProtectTime', TType.I64, 4)
            oprot.writeI64(self.dataProtectTime)
            oprot.writeFieldEnd()
        if self.dataProtectUnit is not None:
            oprot.writeFieldBegin('dataProtectUnit', TType.I32, 5)
            oprot.writeI32(self.dataProtectUnit)
            oprot.writeFieldEnd()
        if self.logProtectTime is not None:
            oprot.writeFieldBegin('logProtectTime', TType.I64, 6)
            oprot.writeI64(self.logProtectTime)
            oprot.writeFieldEnd()
        if self.logProtectUnit is not None:
            oprot.writeFieldBegin('logProtectUnit', TType.I32, 7)
            oprot.writeI32(self.logProtectUnit)
            oprot.writeFieldEnd()
        if self.durationEnable is not None:
            oprot.writeFieldBegin('durationEnable', TType.I32, 8)
            oprot.writeI32(self.durationEnable)
            oprot.writeFieldEnd()
        if self.durationTime is not None:
            oprot.writeFieldBegin('durationTime', TType.I64, 9)
            oprot.writeI64(self.durationTime)
            oprot.writeFieldEnd()
        if self.durationUnit is not None:
            oprot.writeFieldBegin('durationUnit', TType.I32, 10)
            oprot.writeI32(self.durationUnit)
            oprot.writeFieldEnd()
        if self.retentionTime is not None:
            oprot.writeFieldBegin('retentionTime', TType.I64, 11)
            oprot.writeI64(self.retentionTime)
            oprot.writeFieldEnd()
        if self.retentionUnit is not None:
            oprot.writeFieldBegin('retentionUnit', TType.I32, 12)
            oprot.writeI32(self.retentionUnit)
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


class ncScheduleInfo(object):
    """
    Attributes:
     - strategyId
     - jobId
     - beginTime
     - execType

    """


    def __init__(self, strategyId=None, jobId=None, beginTime=None, execType=None,):
        self.strategyId = strategyId
        self.jobId = jobId
        self.beginTime = beginTime
        self.execType = execType

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
                if ftype == TType.STRING:
                    self.strategyId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.jobId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.beginTime = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.execType = iprot.readI32()
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
        oprot.writeStructBegin('ncScheduleInfo')
        if self.strategyId is not None:
            oprot.writeFieldBegin('strategyId', TType.STRING, 1)
            oprot.writeString(self.strategyId.encode('utf-8') if sys.version_info[0] == 2 else self.strategyId)
            oprot.writeFieldEnd()
        if self.jobId is not None:
            oprot.writeFieldBegin('jobId', TType.STRING, 2)
            oprot.writeString(self.jobId.encode('utf-8') if sys.version_info[0] == 2 else self.jobId)
            oprot.writeFieldEnd()
        if self.beginTime is not None:
            oprot.writeFieldBegin('beginTime', TType.STRING, 3)
            oprot.writeString(self.beginTime.encode('utf-8') if sys.version_info[0] == 2 else self.beginTime)
            oprot.writeFieldEnd()
        if self.execType is not None:
            oprot.writeFieldBegin('execType', TType.I32, 4)
            oprot.writeI32(self.execType)
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


class ncScheduleStartTimeInfo(object):
    """
    Attributes:
     - scheduleId
     - execType

    """


    def __init__(self, scheduleId=None, execType=None,):
        self.scheduleId = scheduleId
        self.execType = execType

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
                if ftype == TType.STRING:
                    self.scheduleId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.execType = iprot.readI32()
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
        oprot.writeStructBegin('ncScheduleStartTimeInfo')
        if self.scheduleId is not None:
            oprot.writeFieldBegin('scheduleId', TType.STRING, 1)
            oprot.writeString(self.scheduleId.encode('utf-8') if sys.version_info[0] == 2 else self.scheduleId)
            oprot.writeFieldEnd()
        if self.execType is not None:
            oprot.writeFieldBegin('execType', TType.I32, 2)
            oprot.writeI32(self.execType)
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


class ncScheduleStartTimeResponse(object):
    """
    Attributes:
     - scheduleId
     - execType
     - beginTime

    """


    def __init__(self, scheduleId=None, execType=None, beginTime=None,):
        self.scheduleId = scheduleId
        self.execType = execType
        self.beginTime = beginTime

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
                if ftype == TType.STRING:
                    self.scheduleId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.execType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.beginTime = iprot.readI64()
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
        oprot.writeStructBegin('ncScheduleStartTimeResponse')
        if self.scheduleId is not None:
            oprot.writeFieldBegin('scheduleId', TType.STRING, 1)
            oprot.writeString(self.scheduleId.encode('utf-8') if sys.version_info[0] == 2 else self.scheduleId)
            oprot.writeFieldEnd()
        if self.execType is not None:
            oprot.writeFieldBegin('execType', TType.I32, 2)
            oprot.writeI32(self.execType)
            oprot.writeFieldEnd()
        if self.beginTime is not None:
            oprot.writeFieldBegin('beginTime', TType.I64, 3)
            oprot.writeI64(self.beginTime)
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
all_structs.append(ncStrategyInfo)
ncStrategyInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
    (3, TType.I32, 'type', None, None, ),  # 3
    (4, TType.I64, 'dataProtectTime', None, None, ),  # 4
    (5, TType.I32, 'dataProtectUnit', None, None, ),  # 5
    (6, TType.I64, 'logProtectTime', None, None, ),  # 6
    (7, TType.I32, 'logProtectUnit', None, None, ),  # 7
    (8, TType.I32, 'durationEnable', None, None, ),  # 8
    (9, TType.I64, 'durationTime', None, None, ),  # 9
    (10, TType.I32, 'durationUnit', None, None, ),  # 10
    (11, TType.I64, 'retentionTime', None, None, ),  # 11
    (12, TType.I32, 'retentionUnit', None, None, ),  # 12
)
all_structs.append(ncScheduleInfo)
ncScheduleInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'strategyId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'jobId', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'beginTime', 'UTF8', None, ),  # 3
    (4, TType.I32, 'execType', None, None, ),  # 4
)
all_structs.append(ncScheduleStartTimeInfo)
ncScheduleStartTimeInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'scheduleId', 'UTF8', None, ),  # 1
    (2, TType.I32, 'execType', None, None, ),  # 2
)
all_structs.append(ncScheduleStartTimeResponse)
ncScheduleStartTimeResponse.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'scheduleId', 'UTF8', None, ),  # 1
    (2, TType.I32, 'execType', None, None, ),  # 2
    (3, TType.I64, 'beginTime', None, None, ),  # 3
)
fix_spec(all_structs)
del all_structs