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


class ncVirtualSafetyInfos(object):
    """
    Attributes:
     - virtualPlatformIds
     - projectIds
     - clientIds

    """


    def __init__(self, virtualPlatformIds=None, projectIds=None, clientIds=None,):
        self.virtualPlatformIds = virtualPlatformIds
        self.projectIds = projectIds
        self.clientIds = clientIds

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
                    self.virtualPlatformIds = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.virtualPlatformIds.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.projectIds = []
                    (_etype9, _size6) = iprot.readListBegin()
                    for _i10 in range(_size6):
                        _elem11 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.projectIds.append(_elem11)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.clientIds = []
                    (_etype15, _size12) = iprot.readListBegin()
                    for _i16 in range(_size12):
                        _elem17 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.clientIds.append(_elem17)
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
        oprot.writeStructBegin('ncVirtualSafetyInfos')
        if self.virtualPlatformIds is not None:
            oprot.writeFieldBegin('virtualPlatformIds', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.virtualPlatformIds))
            for iter18 in self.virtualPlatformIds:
                oprot.writeString(iter18.encode('utf-8') if sys.version_info[0] == 2 else iter18)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.projectIds is not None:
            oprot.writeFieldBegin('projectIds', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.projectIds))
            for iter19 in self.projectIds:
                oprot.writeString(iter19.encode('utf-8') if sys.version_info[0] == 2 else iter19)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.clientIds is not None:
            oprot.writeFieldBegin('clientIds', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.clientIds))
            for iter20 in self.clientIds:
                oprot.writeString(iter20.encode('utf-8') if sys.version_info[0] == 2 else iter20)
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


class ncVirtualSafeUserInfo(object):
    """
    Attributes:
     - id
     - auth_user
     - isBuildIn

    """


    def __init__(self, id=None, auth_user=None, isBuildIn=False,):
        self.id = id
        self.auth_user = auth_user
        self.isBuildIn = isBuildIn

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
                    self.auth_user = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.isBuildIn = iprot.readBool()
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
        oprot.writeStructBegin('ncVirtualSafeUserInfo')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.auth_user is not None:
            oprot.writeFieldBegin('auth_user', TType.STRING, 2)
            oprot.writeString(self.auth_user.encode('utf-8') if sys.version_info[0] == 2 else self.auth_user)
            oprot.writeFieldEnd()
        if self.isBuildIn is not None:
            oprot.writeFieldBegin('isBuildIn', TType.BOOL, 3)
            oprot.writeBool(self.isBuildIn)
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


class ncVirtualSafetyUsers(object):
    """
    Attributes:
     - virtualPlatformUsers
     - projectUsers
     - clientUsers

    """


    def __init__(self, virtualPlatformUsers=None, projectUsers=None, clientUsers=None,):
        self.virtualPlatformUsers = virtualPlatformUsers
        self.projectUsers = projectUsers
        self.clientUsers = clientUsers

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
                    self.virtualPlatformUsers = []
                    (_etype24, _size21) = iprot.readListBegin()
                    for _i25 in range(_size21):
                        _elem26 = ncVirtualSafeUserInfo()
                        _elem26.read(iprot)
                        self.virtualPlatformUsers.append(_elem26)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.projectUsers = []
                    (_etype30, _size27) = iprot.readListBegin()
                    for _i31 in range(_size27):
                        _elem32 = ncVirtualSafeUserInfo()
                        _elem32.read(iprot)
                        self.projectUsers.append(_elem32)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.clientUsers = []
                    (_etype36, _size33) = iprot.readListBegin()
                    for _i37 in range(_size33):
                        _elem38 = ncVirtualSafeUserInfo()
                        _elem38.read(iprot)
                        self.clientUsers.append(_elem38)
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
        oprot.writeStructBegin('ncVirtualSafetyUsers')
        if self.virtualPlatformUsers is not None:
            oprot.writeFieldBegin('virtualPlatformUsers', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.virtualPlatformUsers))
            for iter39 in self.virtualPlatformUsers:
                iter39.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.projectUsers is not None:
            oprot.writeFieldBegin('projectUsers', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.projectUsers))
            for iter40 in self.projectUsers:
                iter40.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.clientUsers is not None:
            oprot.writeFieldBegin('clientUsers', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.clientUsers))
            for iter41 in self.clientUsers:
                iter41.write(oprot)
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
all_structs.append(ncVirtualSafetyInfos)
ncVirtualSafetyInfos.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'virtualPlatformIds', (TType.STRING, 'UTF8', False), None, ),  # 1
    (2, TType.LIST, 'projectIds', (TType.STRING, 'UTF8', False), None, ),  # 2
    (3, TType.LIST, 'clientIds', (TType.STRING, 'UTF8', False), None, ),  # 3
)
all_structs.append(ncVirtualSafeUserInfo)
ncVirtualSafeUserInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'auth_user', 'UTF8', None, ),  # 2
    (3, TType.BOOL, 'isBuildIn', None, False, ),  # 3
)
all_structs.append(ncVirtualSafetyUsers)
ncVirtualSafetyUsers.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'virtualPlatformUsers', (TType.STRUCT, [ncVirtualSafeUserInfo, None], False), None, ),  # 1
    (2, TType.LIST, 'projectUsers', (TType.STRUCT, [ncVirtualSafeUserInfo, None], False), None, ),  # 2
    (3, TType.LIST, 'clientUsers', (TType.STRUCT, [ncVirtualSafeUserInfo, None], False), None, ),  # 3
)
fix_spec(all_structs)
del all_structs
