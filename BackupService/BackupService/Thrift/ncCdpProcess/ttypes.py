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


class ncCDPJobCountInfo(object):
    """
    Attributes:
     - stopped
     - abnormal
     - running

    """


    def __init__(self, stopped=None, abnormal=None, running=None,):
        self.stopped = stopped
        self.abnormal = abnormal
        self.running = running

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
                if ftype == TType.I32:
                    self.stopped = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.abnormal = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.running = iprot.readI32()
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
        oprot.writeStructBegin('ncCDPJobCountInfo')
        if self.stopped is not None:
            oprot.writeFieldBegin('stopped', TType.I32, 1)
            oprot.writeI32(self.stopped)
            oprot.writeFieldEnd()
        if self.abnormal is not None:
            oprot.writeFieldBegin('abnormal', TType.I32, 2)
            oprot.writeI32(self.abnormal)
            oprot.writeFieldEnd()
        if self.running is not None:
            oprot.writeFieldBegin('running', TType.I32, 3)
            oprot.writeI32(self.running)
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


class ncCDPJobRunningUserInfo(object):
    """
    Attributes:
     - has_backupjob_users
     - has_repljob_users

    """


    def __init__(self, has_backupjob_users=None, has_repljob_users=None,):
        self.has_backupjob_users = has_backupjob_users
        self.has_repljob_users = has_repljob_users

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
                if ftype == TType.LIST:
                    self.has_backupjob_users = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.has_backupjob_users.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.has_repljob_users = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.has_repljob_users.append(_elem11)
                    iprot.readListEnd()
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
        oprot.writeStructBegin('ncCDPJobRunningUserInfo')
        if self.has_backupjob_users is not None:
            oprot.writeFieldBegin('has_backupjob_users', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.has_backupjob_users))
            for iter12 in self.has_backupjob_users:
                oprot.writeString(iter12.encode('utf-8') if sys.version_info[0] == 2 else iter12)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.has_repljob_users is not None:
            oprot.writeFieldBegin('has_repljob_users', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.has_repljob_users))
            for iter13 in self.has_repljob_users:
                oprot.writeString(iter13.encode('utf-8') if sys.version_info[0] == 2 else iter13)
            oprot.writeListEnd()
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


class ncHostCdmLunInfo(object):
    """
    Attributes:
     - volumeName
     - diskName
     - cfgString

    """


    def __init__(self, volumeName=None, diskName=None, cfgString=None,):
        self.volumeName = volumeName
        self.diskName = diskName
        self.cfgString = cfgString

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
                    self.volumeName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.diskName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.cfgString = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncHostCdmLunInfo')
        if self.volumeName is not None:
            oprot.writeFieldBegin('volumeName', TType.STRING, 1)
            oprot.writeString(self.volumeName.encode('utf-8') if sys.version_info[0] == 2 else self.volumeName)
            oprot.writeFieldEnd()
        if self.diskName is not None:
            oprot.writeFieldBegin('diskName', TType.STRING, 2)
            oprot.writeString(self.diskName.encode('utf-8') if sys.version_info[0] == 2 else self.diskName)
            oprot.writeFieldEnd()
        if self.cfgString is not None:
            oprot.writeFieldBegin('cfgString', TType.STRING, 3)
            oprot.writeString(self.cfgString.encode('utf-8') if sys.version_info[0] == 2 else self.cfgString)
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


class ncVolumeInfo(object):
    """
    Attributes:
     - volumeName
     - diskName
     - diskSize

    """


    def __init__(self, volumeName=None, diskName=None, diskSize=None,):
        self.volumeName = volumeName
        self.diskName = diskName
        self.diskSize = diskSize

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
                    self.volumeName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.diskName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.diskSize = iprot.readI64()
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
        oprot.writeStructBegin('ncVolumeInfo')
        if self.volumeName is not None:
            oprot.writeFieldBegin('volumeName', TType.STRING, 1)
            oprot.writeString(self.volumeName.encode('utf-8') if sys.version_info[0] == 2 else self.volumeName)
            oprot.writeFieldEnd()
        if self.diskName is not None:
            oprot.writeFieldBegin('diskName', TType.STRING, 2)
            oprot.writeString(self.diskName.encode('utf-8') if sys.version_info[0] == 2 else self.diskName)
            oprot.writeFieldEnd()
        if self.diskSize is not None:
            oprot.writeFieldBegin('diskSize', TType.I64, 3)
            oprot.writeI64(self.diskSize)
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
all_structs.append(ncCDPJobCountInfo)
ncCDPJobCountInfo.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'stopped', None, None, ),  # 1
    (2, TType.I32, 'abnormal', None, None, ),  # 2
    (3, TType.I32, 'running', None, None, ),  # 3
)
all_structs.append(ncCDPJobRunningUserInfo)
ncCDPJobRunningUserInfo.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'has_backupjob_users', (TType.STRING, 'UTF8', False), None, ),  # 1
    (2, TType.LIST, 'has_repljob_users', (TType.STRING, 'UTF8', False), None, ),  # 2
)
all_structs.append(ncHostCdmLunInfo)
ncHostCdmLunInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'volumeName', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'diskName', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'cfgString', 'UTF8', None, ),  # 3
)
all_structs.append(ncVolumeInfo)
ncVolumeInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'volumeName', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'diskName', 'UTF8', None, ),  # 2
    (3, TType.I64, 'diskSize', None, None, ),  # 3
)
fix_spec(all_structs)
del all_structs
