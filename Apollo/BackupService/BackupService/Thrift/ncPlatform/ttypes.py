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
import ncClient.ttypes

from thrift.transport import TTransport
all_structs = []


class ncPlatformDistriReq(object):
    """
    Attributes:
     - requestId
     - platformIds
     - userName
     - oper
     - role

    """


    def __init__(self, requestId=None, platformIds=None, userName=None, oper=None, role=None,):
        self.requestId = requestId
        self.platformIds = platformIds
        self.userName = userName
        self.oper = oper
        self.role = role

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.platformIds = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.platformIds.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.userName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.oper = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.role = iprot.readI32()
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
        oprot.writeStructBegin('ncPlatformDistriReq')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.platformIds is not None:
            oprot.writeFieldBegin('platformIds', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.platformIds))
            for iter6 in self.platformIds:
                oprot.writeString(iter6.encode('utf-8') if sys.version_info[0] == 2 else iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.userName is not None:
            oprot.writeFieldBegin('userName', TType.STRING, 3)
            oprot.writeString(self.userName.encode('utf-8') if sys.version_info[0] == 2 else self.userName)
            oprot.writeFieldEnd()
        if self.oper is not None:
            oprot.writeFieldBegin('oper', TType.I32, 4)
            oprot.writeI32(self.oper)
            oprot.writeFieldEnd()
        if self.role is not None:
            oprot.writeFieldBegin('role', TType.I32, 5)
            oprot.writeI32(self.role)
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


class ncPlatformDistriRes(object):
    """
    Attributes:
     - requestId
     - nodeIp
     - isFinished
     - oper
     - isErr
     - errs

    """


    def __init__(self, requestId=None, nodeIp=None, isFinished=None, oper=None, isErr=None, errs=None,):
        self.requestId = requestId
        self.nodeIp = nodeIp
        self.isFinished = isFinished
        self.oper = oper
        self.isErr = isErr
        self.errs = errs

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
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.nodeIp = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.BOOL:
                    self.isFinished = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.oper = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.isErr = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.LIST:
                    self.errs = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.errs.append(_elem12)
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
        oprot.writeStructBegin('ncPlatformDistriRes')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.nodeIp is not None:
            oprot.writeFieldBegin('nodeIp', TType.STRING, 2)
            oprot.writeString(self.nodeIp.encode('utf-8') if sys.version_info[0] == 2 else self.nodeIp)
            oprot.writeFieldEnd()
        if self.isFinished is not None:
            oprot.writeFieldBegin('isFinished', TType.BOOL, 3)
            oprot.writeBool(self.isFinished)
            oprot.writeFieldEnd()
        if self.oper is not None:
            oprot.writeFieldBegin('oper', TType.I32, 4)
            oprot.writeI32(self.oper)
            oprot.writeFieldEnd()
        if self.isErr is not None:
            oprot.writeFieldBegin('isErr', TType.BOOL, 5)
            oprot.writeBool(self.isErr)
            oprot.writeFieldEnd()
        if self.errs is not None:
            oprot.writeFieldBegin('errs', TType.LIST, 6)
            oprot.writeListBegin(TType.STRING, len(self.errs))
            for iter13 in self.errs:
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


class ncGetPlatformsReq(object):
    """
    Attributes:
     - authers
     - platformIds
     - ips
     - groupIds
     - types
     - deleted
     - decrypt

    """


    def __init__(self, authers=None, platformIds=None, ips=None, groupIds=None, types=None, deleted=False, decrypt=False,):
        self.authers = authers
        self.platformIds = platformIds
        self.ips = ips
        self.groupIds = groupIds
        self.types = types
        self.deleted = deleted
        self.decrypt = decrypt

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
                    self.authers = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.authers.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.platformIds = []
                    (_etype23, _size20) = iprot.readListBegin()
                    for _i24 in range(_size20):
                        _elem25 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.platformIds.append(_elem25)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.ips = []
                    (_etype29, _size26) = iprot.readListBegin()
                    for _i30 in range(_size26):
                        _elem31 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.ips.append(_elem31)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.groupIds = []
                    (_etype35, _size32) = iprot.readListBegin()
                    for _i36 in range(_size32):
                        _elem37 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.groupIds.append(_elem37)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.LIST:
                    self.types = []
                    (_etype41, _size38) = iprot.readListBegin()
                    for _i42 in range(_size38):
                        _elem43 = iprot.readI32()
                        self.types.append(_elem43)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BOOL:
                    self.deleted = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.BOOL:
                    self.decrypt = iprot.readBool()
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
        oprot.writeStructBegin('ncGetPlatformsReq')
        if self.authers is not None:
            oprot.writeFieldBegin('authers', TType.LIST, 1)
            oprot.writeListBegin(TType.STRING, len(self.authers))
            for iter44 in self.authers:
                oprot.writeString(iter44.encode('utf-8') if sys.version_info[0] == 2 else iter44)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.platformIds is not None:
            oprot.writeFieldBegin('platformIds', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.platformIds))
            for iter45 in self.platformIds:
                oprot.writeString(iter45.encode('utf-8') if sys.version_info[0] == 2 else iter45)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.ips is not None:
            oprot.writeFieldBegin('ips', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.ips))
            for iter46 in self.ips:
                oprot.writeString(iter46.encode('utf-8') if sys.version_info[0] == 2 else iter46)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.groupIds is not None:
            oprot.writeFieldBegin('groupIds', TType.LIST, 4)
            oprot.writeListBegin(TType.STRING, len(self.groupIds))
            for iter47 in self.groupIds:
                oprot.writeString(iter47.encode('utf-8') if sys.version_info[0] == 2 else iter47)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.types is not None:
            oprot.writeFieldBegin('types', TType.LIST, 5)
            oprot.writeListBegin(TType.I32, len(self.types))
            for iter48 in self.types:
                oprot.writeI32(iter48)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.deleted is not None:
            oprot.writeFieldBegin('deleted', TType.BOOL, 6)
            oprot.writeBool(self.deleted)
            oprot.writeFieldEnd()
        if self.decrypt is not None:
            oprot.writeFieldBegin('decrypt', TType.BOOL, 7)
            oprot.writeBool(self.decrypt)
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


class ncTPlatform(object):
    """
    Attributes:
     - name
     - ip
     - port
     - auther
     - version
     - userPass
     - vplatformId
     - platCustomer
     - userCustomer
     - groupId
     - deleted
     - type
     - verification

    """


    def __init__(self, name=None, ip=None, port=None, auther=None, version=None, userPass=None, vplatformId=None, platCustomer=None, userCustomer=None, groupId=None, deleted=False, type=None, verification=None,):
        self.name = name
        self.ip = ip
        self.port = port
        self.auther = auther
        self.version = version
        self.userPass = userPass
        self.vplatformId = vplatformId
        self.platCustomer = platCustomer
        self.userCustomer = userCustomer
        self.groupId = groupId
        self.deleted = deleted
        self.type = type
        self.verification = verification

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
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.port = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.auther = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.version = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.MAP:
                    self.userPass = {}
                    (_ktype50, _vtype51, _size49) = iprot.readMapBegin()
                    for _i53 in range(_size49):
                        _key54 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val55 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.userPass[_key54] = _val55
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.vplatformId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.platCustomer = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.MAP:
                    self.userCustomer = {}
                    (_ktype57, _vtype58, _size56) = iprot.readMapBegin()
                    for _i60 in range(_size56):
                        _key61 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val62 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.userCustomer[_key61] = _val62
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.groupId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.BOOL:
                    self.deleted = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRING:
                    self.verification = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncTPlatform')
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.STRING, 2)
            oprot.writeString(self.ip.encode('utf-8') if sys.version_info[0] == 2 else self.ip)
            oprot.writeFieldEnd()
        if self.port is not None:
            oprot.writeFieldBegin('port', TType.STRING, 3)
            oprot.writeString(self.port.encode('utf-8') if sys.version_info[0] == 2 else self.port)
            oprot.writeFieldEnd()
        if self.auther is not None:
            oprot.writeFieldBegin('auther', TType.STRING, 4)
            oprot.writeString(self.auther.encode('utf-8') if sys.version_info[0] == 2 else self.auther)
            oprot.writeFieldEnd()
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.STRING, 5)
            oprot.writeString(self.version.encode('utf-8') if sys.version_info[0] == 2 else self.version)
            oprot.writeFieldEnd()
        if self.userPass is not None:
            oprot.writeFieldBegin('userPass', TType.MAP, 6)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.userPass))
            for kiter63, viter64 in self.userPass.items():
                oprot.writeString(kiter63.encode('utf-8') if sys.version_info[0] == 2 else kiter63)
                oprot.writeString(viter64.encode('utf-8') if sys.version_info[0] == 2 else viter64)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.vplatformId is not None:
            oprot.writeFieldBegin('vplatformId', TType.STRING, 7)
            oprot.writeString(self.vplatformId.encode('utf-8') if sys.version_info[0] == 2 else self.vplatformId)
            oprot.writeFieldEnd()
        if self.platCustomer is not None:
            oprot.writeFieldBegin('platCustomer', TType.STRING, 8)
            oprot.writeString(self.platCustomer.encode('utf-8') if sys.version_info[0] == 2 else self.platCustomer)
            oprot.writeFieldEnd()
        if self.userCustomer is not None:
            oprot.writeFieldBegin('userCustomer', TType.MAP, 9)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.userCustomer))
            for kiter65, viter66 in self.userCustomer.items():
                oprot.writeString(kiter65.encode('utf-8') if sys.version_info[0] == 2 else kiter65)
                oprot.writeString(viter66.encode('utf-8') if sys.version_info[0] == 2 else viter66)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.groupId is not None:
            oprot.writeFieldBegin('groupId', TType.STRING, 10)
            oprot.writeString(self.groupId.encode('utf-8') if sys.version_info[0] == 2 else self.groupId)
            oprot.writeFieldEnd()
        if self.deleted is not None:
            oprot.writeFieldBegin('deleted', TType.BOOL, 11)
            oprot.writeBool(self.deleted)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 12)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.verification is not None:
            oprot.writeFieldBegin('verification', TType.STRING, 13)
            oprot.writeString(self.verification.encode('utf-8') if sys.version_info[0] == 2 else self.verification)
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


class ncInKvmTPlatform(object):
    """
    Attributes:
     - name
     - ip
     - solts
     - cores
     - memory
     - cpuCoreNum

    """


    def __init__(self, name=None, ip=None, solts=None, cores=None, memory=None, cpuCoreNum=None,):
        self.name = name
        self.ip = ip
        self.solts = solts
        self.cores = cores
        self.memory = memory
        self.cpuCoreNum = cpuCoreNum

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
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.solts = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.cores = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.memory = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.cpuCoreNum = iprot.readI32()
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
        oprot.writeStructBegin('ncInKvmTPlatform')
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 1)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.STRING, 2)
            oprot.writeString(self.ip.encode('utf-8') if sys.version_info[0] == 2 else self.ip)
            oprot.writeFieldEnd()
        if self.solts is not None:
            oprot.writeFieldBegin('solts', TType.I32, 3)
            oprot.writeI32(self.solts)
            oprot.writeFieldEnd()
        if self.cores is not None:
            oprot.writeFieldBegin('cores', TType.I32, 4)
            oprot.writeI32(self.cores)
            oprot.writeFieldEnd()
        if self.memory is not None:
            oprot.writeFieldBegin('memory', TType.I64, 5)
            oprot.writeI64(self.memory)
            oprot.writeFieldEnd()
        if self.cpuCoreNum is not None:
            oprot.writeFieldBegin('cpuCoreNum', TType.I32, 6)
            oprot.writeI32(self.cpuCoreNum)
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
all_structs.append(ncPlatformDistriReq)
ncPlatformDistriReq.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.LIST, 'platformIds', (TType.STRING, 'UTF8', False), None, ),  # 2
    (3, TType.STRING, 'userName', 'UTF8', None, ),  # 3
    (4, TType.I32, 'oper', None, None, ),  # 4
    (5, TType.I32, 'role', None, None, ),  # 5
)
all_structs.append(ncPlatformDistriRes)
ncPlatformDistriRes.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'nodeIp', 'UTF8', None, ),  # 2
    (3, TType.BOOL, 'isFinished', None, None, ),  # 3
    (4, TType.I32, 'oper', None, None, ),  # 4
    (5, TType.BOOL, 'isErr', None, None, ),  # 5
    (6, TType.LIST, 'errs', (TType.STRING, 'UTF8', False), None, ),  # 6
)
all_structs.append(ncGetPlatformsReq)
ncGetPlatformsReq.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'authers', (TType.STRING, 'UTF8', False), None, ),  # 1
    (2, TType.LIST, 'platformIds', (TType.STRING, 'UTF8', False), None, ),  # 2
    (3, TType.LIST, 'ips', (TType.STRING, 'UTF8', False), None, ),  # 3
    (4, TType.LIST, 'groupIds', (TType.STRING, 'UTF8', False), None, ),  # 4
    (5, TType.LIST, 'types', (TType.I32, None, False), None, ),  # 5
    (6, TType.BOOL, 'deleted', None, False, ),  # 6
    (7, TType.BOOL, 'decrypt', None, False, ),  # 7
)
all_structs.append(ncTPlatform)
ncTPlatform.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'name', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'ip', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'port', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'auther', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'version', 'UTF8', None, ),  # 5
    (6, TType.MAP, 'userPass', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 6
    (7, TType.STRING, 'vplatformId', 'UTF8', None, ),  # 7
    (8, TType.STRING, 'platCustomer', 'UTF8', None, ),  # 8
    (9, TType.MAP, 'userCustomer', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 9
    (10, TType.STRING, 'groupId', 'UTF8', None, ),  # 10
    (11, TType.BOOL, 'deleted', None, False, ),  # 11
    (12, TType.I32, 'type', None, None, ),  # 12
    (13, TType.STRING, 'verification', 'UTF8', None, ),  # 13
)
all_structs.append(ncInKvmTPlatform)
ncInKvmTPlatform.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'name', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'ip', 'UTF8', None, ),  # 2
    (3, TType.I32, 'solts', None, None, ),  # 3
    (4, TType.I32, 'cores', None, None, ),  # 4
    (5, TType.I64, 'memory', None, None, ),  # 5
    (6, TType.I32, 'cpuCoreNum', None, None, ),  # 6
)
fix_spec(all_structs)
del all_structs