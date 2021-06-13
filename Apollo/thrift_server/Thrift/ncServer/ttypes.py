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


class ncServerStatus(object):
    OFFLINE = 0
    ONLINE = 1

    _VALUES_TO_NAMES = {
        0: "OFFLINE",
        1: "ONLINE",
    }

    _NAMES_TO_VALUES = {
        "OFFLINE": 0,
        "ONLINE": 1,
    }


class ncServer(object):
    """
    Attributes:
     - ip
     - mac
     - status
     - version
     - ipv6

    """


    def __init__(self, ip=None, mac=None, status=None, version=None, ipv6=None,):
        self.ip = ip
        self.mac = mac
        self.status = status
        self.version = version
        self.ipv6 = ipv6

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
                    self.ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.mac = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.version = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.ipv6 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncServer')
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.STRING, 1)
            oprot.writeString(self.ip.encode('utf-8') if sys.version_info[0] == 2 else self.ip)
            oprot.writeFieldEnd()
        if self.mac is not None:
            oprot.writeFieldBegin('mac', TType.STRING, 2)
            oprot.writeString(self.mac.encode('utf-8') if sys.version_info[0] == 2 else self.mac)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 3)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.STRING, 4)
            oprot.writeString(self.version.encode('utf-8') if sys.version_info[0] == 2 else self.version)
            oprot.writeFieldEnd()
        if self.ipv6 is not None:
            oprot.writeFieldBegin('ipv6', TType.STRING, 5)
            oprot.writeString(self.ipv6.encode('utf-8') if sys.version_info[0] == 2 else self.ipv6)
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


class ncGetServerRequest(object):
    """
    Attributes:
     - ip
     - mac
     - status
     - version
     - deleted

    """


    def __init__(self, ip=None, mac=None, status=None, version=None, deleted=False,):
        self.ip = ip
        self.mac = mac
        self.status = status
        self.version = version
        self.deleted = deleted

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
                    self.ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.mac = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.version = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.deleted = iprot.readBool()
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
        oprot.writeStructBegin('ncGetServerRequest')
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.STRING, 1)
            oprot.writeString(self.ip.encode('utf-8') if sys.version_info[0] == 2 else self.ip)
            oprot.writeFieldEnd()
        if self.mac is not None:
            oprot.writeFieldBegin('mac', TType.STRING, 2)
            oprot.writeString(self.mac.encode('utf-8') if sys.version_info[0] == 2 else self.mac)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 3)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.STRING, 4)
            oprot.writeString(self.version.encode('utf-8') if sys.version_info[0] == 2 else self.version)
            oprot.writeFieldEnd()
        if self.deleted is not None:
            oprot.writeFieldBegin('deleted', TType.BOOL, 5)
            oprot.writeBool(self.deleted)
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
all_structs.append(ncServer)
ncServer.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'ip', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'mac', 'UTF8', None, ),  # 2
    (3, TType.I32, 'status', None, None, ),  # 3
    (4, TType.STRING, 'version', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'ipv6', 'UTF8', None, ),  # 5
)
all_structs.append(ncGetServerRequest)
ncGetServerRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'ip', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'mac', 'UTF8', None, ),  # 2
    (3, TType.I32, 'status', None, None, ),  # 3
    (4, TType.STRING, 'version', 'UTF8', None, ),  # 4
    (5, TType.BOOL, 'deleted', None, False, ),  # 5
)
fix_spec(all_structs)
del all_structs
