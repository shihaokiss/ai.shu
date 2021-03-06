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
import ncCommonType_Var.ttypes

from thrift.transport import TTransport
all_structs = []


class ncEtssVolumeInfo(object):
    """
    Attributes:
     - volumePath
     - volumeTotalSize
     - usedSize

    """


    def __init__(self, volumePath=None, volumeTotalSize=None, usedSize=None,):
        self.volumePath = volumePath
        self.volumeTotalSize = volumeTotalSize
        self.usedSize = usedSize

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
                    self.volumePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.volumeTotalSize = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.usedSize = iprot.readI64()
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
        oprot.writeStructBegin('ncEtssVolumeInfo')
        if self.volumePath is not None:
            oprot.writeFieldBegin('volumePath', TType.STRING, 1)
            oprot.writeString(self.volumePath.encode('utf-8') if sys.version_info[0] == 2 else self.volumePath)
            oprot.writeFieldEnd()
        if self.volumeTotalSize is not None:
            oprot.writeFieldBegin('volumeTotalSize', TType.I64, 2)
            oprot.writeI64(self.volumeTotalSize)
            oprot.writeFieldEnd()
        if self.usedSize is not None:
            oprot.writeFieldBegin('usedSize', TType.I64, 3)
            oprot.writeI64(self.usedSize)
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


class TapeImportStatus(object):
    """
    Attributes:
     - beginTime
     - endTime
     - status
     - failureReason
     - scannedCount
     - remainCount

    """


    def __init__(self, beginTime=None, endTime=None, status=None, failureReason=None, scannedCount=None, remainCount=None,):
        self.beginTime = beginTime
        self.endTime = endTime
        self.status = status
        self.failureReason = failureReason
        self.scannedCount = scannedCount
        self.remainCount = remainCount

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
                    self.beginTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.endTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.failureReason = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.scannedCount = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.remainCount = iprot.readI32()
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
        oprot.writeStructBegin('TapeImportStatus')
        if self.beginTime is not None:
            oprot.writeFieldBegin('beginTime', TType.I64, 1)
            oprot.writeI64(self.beginTime)
            oprot.writeFieldEnd()
        if self.endTime is not None:
            oprot.writeFieldBegin('endTime', TType.I64, 2)
            oprot.writeI64(self.endTime)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 3)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.failureReason is not None:
            oprot.writeFieldBegin('failureReason', TType.STRING, 4)
            oprot.writeString(self.failureReason.encode('utf-8') if sys.version_info[0] == 2 else self.failureReason)
            oprot.writeFieldEnd()
        if self.scannedCount is not None:
            oprot.writeFieldBegin('scannedCount', TType.I32, 5)
            oprot.writeI32(self.scannedCount)
            oprot.writeFieldEnd()
        if self.remainCount is not None:
            oprot.writeFieldBegin('remainCount', TType.I32, 6)
            oprot.writeI32(self.remainCount)
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
all_structs.append(ncEtssVolumeInfo)
ncEtssVolumeInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'volumePath', 'UTF8', None, ),  # 1
    (2, TType.I64, 'volumeTotalSize', None, None, ),  # 2
    (3, TType.I64, 'usedSize', None, None, ),  # 3
)
all_structs.append(TapeImportStatus)
TapeImportStatus.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'beginTime', None, None, ),  # 1
    (2, TType.I64, 'endTime', None, None, ),  # 2
    (3, TType.I32, 'status', None, None, ),  # 3
    (4, TType.STRING, 'failureReason', 'UTF8', None, ),  # 4
    (5, TType.I32, 'scannedCount', None, None, ),  # 5
    (6, TType.I32, 'remainCount', None, None, ),  # 6
)
fix_spec(all_structs)
del all_structs
