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

from thrift.transport import TTransport
all_structs = []


class ncIoInfo(object):
    """
    Attributes:
     - sec
     - io_num

    """


    def __init__(self, sec=None, io_num=None,):
        self.sec = sec
        self.io_num = io_num

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
                    self.sec = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.io_num = iprot.readI32()
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
        oprot.writeStructBegin('ncIoInfo')
        if self.sec is not None:
            oprot.writeFieldBegin('sec', TType.I64, 1)
            oprot.writeI64(self.sec)
            oprot.writeFieldEnd()
        if self.io_num is not None:
            oprot.writeFieldBegin('io_num', TType.I32, 2)
            oprot.writeI32(self.io_num)
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


class ncPartInfo(object):
    """
    Attributes:
     - volName
     - partNo
     - fsType

    """


    def __init__(self, volName=None, partNo=None, fsType=None,):
        self.volName = volName
        self.partNo = partNo
        self.fsType = fsType

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
                    self.volName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.partNo = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.fsType = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncPartInfo')
        if self.volName is not None:
            oprot.writeFieldBegin('volName', TType.STRING, 1)
            oprot.writeString(self.volName.encode('utf-8') if sys.version_info[0] == 2 else self.volName)
            oprot.writeFieldEnd()
        if self.partNo is not None:
            oprot.writeFieldBegin('partNo', TType.I32, 2)
            oprot.writeI32(self.partNo)
            oprot.writeFieldEnd()
        if self.fsType is not None:
            oprot.writeFieldBegin('fsType', TType.STRING, 3)
            oprot.writeString(self.fsType.encode('utf-8') if sys.version_info[0] == 2 else self.fsType)
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
all_structs.append(ncIoInfo)
ncIoInfo.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'sec', None, None, ),  # 1
    (2, TType.I32, 'io_num', None, None, ),  # 2
)
all_structs.append(ncPartInfo)
ncPartInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'volName', 'UTF8', None, ),  # 1
    (2, TType.I32, 'partNo', None, None, ),  # 2
    (3, TType.STRING, 'fsType', 'UTF8', None, ),  # 3
)
fix_spec(all_structs)
del all_structs
