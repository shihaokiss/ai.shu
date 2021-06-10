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
import ncClient.ttypes
import ncCCResource_Var.ttypes
import ncCommonType_Var.ttypes

from thrift.transport import TTransport
all_structs = []


class ncSiteInfoCheck(object):
    """
    Attributes:
     - id
     - ossIdCSId

    """


    def __init__(self, id=None, ossIdCSId=None,):
        self.id = id
        self.ossIdCSId = ossIdCSId

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
                if ftype == TType.MAP:
                    self.ossIdCSId = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val6 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.ossIdCSId[_key5] = _val6
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
        oprot.writeStructBegin('ncSiteInfoCheck')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.ossIdCSId is not None:
            oprot.writeFieldBegin('ossIdCSId', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.ossIdCSId))
            for kiter7, viter8 in self.ossIdCSId.items():
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


class ncAppSystemCheck(object):
    """
    Attributes:
     - appId
     - master
     - slaves
     - clientIds

    """


    def __init__(self, appId=None, master=None, slaves=None, clientIds=None,):
        self.appId = appId
        self.master = master
        self.slaves = slaves
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
                if ftype == TType.STRING:
                    self.appId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.master = ncSiteInfoCheck()
                    self.master.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.slaves = []
                    (_etype12, _size9) = iprot.readListBegin()
                    for _i13 in range(_size9):
                        _elem14 = ncSiteInfoCheck()
                        _elem14.read(iprot)
                        self.slaves.append(_elem14)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.clientIds = []
                    (_etype18, _size15) = iprot.readListBegin()
                    for _i19 in range(_size15):
                        _elem20 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.clientIds.append(_elem20)
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
        oprot.writeStructBegin('ncAppSystemCheck')
        if self.appId is not None:
            oprot.writeFieldBegin('appId', TType.STRING, 1)
            oprot.writeString(self.appId.encode('utf-8') if sys.version_info[0] == 2 else self.appId)
            oprot.writeFieldEnd()
        if self.master is not None:
            oprot.writeFieldBegin('master', TType.STRUCT, 2)
            self.master.write(oprot)
            oprot.writeFieldEnd()
        if self.slaves is not None:
            oprot.writeFieldBegin('slaves', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.slaves))
            for iter21 in self.slaves:
                iter21.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.clientIds is not None:
            oprot.writeFieldBegin('clientIds', TType.LIST, 4)
            oprot.writeListBegin(TType.STRING, len(self.clientIds))
            for iter22 in self.clientIds:
                oprot.writeString(iter22.encode('utf-8') if sys.version_info[0] == 2 else iter22)
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


class ncDatasourceCheckReq(object):
    """
    Attributes:
     - ccloudCheck
     - username

    """


    def __init__(self, ccloudCheck=None, username=None,):
        self.ccloudCheck = ccloudCheck
        self.username = username

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
                    self.ccloudCheck = ncAppSystemCheck()
                    self.ccloudCheck.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncDatasourceCheckReq')
        if self.ccloudCheck is not None:
            oprot.writeFieldBegin('ccloudCheck', TType.STRUCT, 1)
            self.ccloudCheck.write(oprot)
            oprot.writeFieldEnd()
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 2)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
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


class ncOSSInfo(object):
    """
    Attributes:
     - id
     - name
     - ipDomain
     - port

    """


    def __init__(self, id=None, name=None, ipDomain=None, port=None,):
        self.id = id
        self.name = name
        self.ipDomain = ipDomain
        self.port = port

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
                if ftype == TType.STRING:
                    self.ipDomain = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.port = iprot.readI64()
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
        oprot.writeStructBegin('ncOSSInfo')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.ipDomain is not None:
            oprot.writeFieldBegin('ipDomain', TType.STRING, 3)
            oprot.writeString(self.ipDomain.encode('utf-8') if sys.version_info[0] == 2 else self.ipDomain)
            oprot.writeFieldEnd()
        if self.port is not None:
            oprot.writeFieldBegin('port', TType.I64, 4)
            oprot.writeI64(self.port)
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


class ncCloudStorageInfos(object):
    """
    Attributes:
     - id
     - ip
     - name
     - type
     - accessId
     - accessKey

    """


    def __init__(self, id=None, ip=None, name=None, type=None, accessId=None, accessKey=None,):
        self.id = id
        self.ip = ip
        self.name = name
        self.type = type
        self.accessId = accessId
        self.accessKey = accessKey

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
                    self.ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.accessId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.accessKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncCloudStorageInfos')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.STRING, 2)
            oprot.writeString(self.ip.encode('utf-8') if sys.version_info[0] == 2 else self.ip)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 3)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 4)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.accessId is not None:
            oprot.writeFieldBegin('accessId', TType.STRING, 5)
            oprot.writeString(self.accessId.encode('utf-8') if sys.version_info[0] == 2 else self.accessId)
            oprot.writeFieldEnd()
        if self.accessKey is not None:
            oprot.writeFieldBegin('accessKey', TType.STRING, 6)
            oprot.writeString(self.accessKey.encode('utf-8') if sys.version_info[0] == 2 else self.accessKey)
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


class ncSiteInfo(object):
    """
    Attributes:
     - id
     - name
     - ipDomain
     - version
     - authUser
     - appId
     - appKey
     - ossInfos
     - type
     - port

    """


    def __init__(self, id=None, name=None, ipDomain=None, version=None, authUser=None, appId=None, appKey=None, ossInfos=None, type=None, port=None,):
        self.id = id
        self.name = name
        self.ipDomain = ipDomain
        self.version = version
        self.authUser = authUser
        self.appId = appId
        self.appKey = appKey
        self.ossInfos = ossInfos
        self.type = type
        self.port = port

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
                if ftype == TType.STRING:
                    self.ipDomain = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.version = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.authUser = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.appId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.appKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.MAP:
                    self.ossInfos = {}
                    (_ktype24, _vtype25, _size23) = iprot.readMapBegin()
                    for _i27 in range(_size23):
                        _key28 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val29 = ncCloudStorageInfos()
                        _val29.read(iprot)
                        self.ossInfos[_key28] = _val29
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.port = iprot.readI32()
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
        oprot.writeStructBegin('ncSiteInfo')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.ipDomain is not None:
            oprot.writeFieldBegin('ipDomain', TType.STRING, 3)
            oprot.writeString(self.ipDomain.encode('utf-8') if sys.version_info[0] == 2 else self.ipDomain)
            oprot.writeFieldEnd()
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.STRING, 4)
            oprot.writeString(self.version.encode('utf-8') if sys.version_info[0] == 2 else self.version)
            oprot.writeFieldEnd()
        if self.authUser is not None:
            oprot.writeFieldBegin('authUser', TType.STRING, 5)
            oprot.writeString(self.authUser.encode('utf-8') if sys.version_info[0] == 2 else self.authUser)
            oprot.writeFieldEnd()
        if self.appId is not None:
            oprot.writeFieldBegin('appId', TType.STRING, 6)
            oprot.writeString(self.appId.encode('utf-8') if sys.version_info[0] == 2 else self.appId)
            oprot.writeFieldEnd()
        if self.appKey is not None:
            oprot.writeFieldBegin('appKey', TType.STRING, 7)
            oprot.writeString(self.appKey.encode('utf-8') if sys.version_info[0] == 2 else self.appKey)
            oprot.writeFieldEnd()
        if self.ossInfos is not None:
            oprot.writeFieldBegin('ossInfos', TType.MAP, 8)
            oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.ossInfos))
            for kiter30, viter31 in self.ossInfos.items():
                oprot.writeString(kiter30.encode('utf-8') if sys.version_info[0] == 2 else kiter30)
                viter31.write(oprot)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 9)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.port is not None:
            oprot.writeFieldBegin('port', TType.I32, 10)
            oprot.writeI32(self.port)
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


class ncAPPSystemInfo(object):
    """
    Attributes:
     - id
     - name

    """


    def __init__(self, id=None, name=None,):
        self.id = id
        self.name = name

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
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ncAPPSystemInfo')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
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


class ncDatasourceResult(object):
    """
    Attributes:
     - appSys
     - master
     - slaves
     - clients

    """


    def __init__(self, appSys=None, master=None, slaves=None, clients=None,):
        self.appSys = appSys
        self.master = master
        self.slaves = slaves
        self.clients = clients

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
                    self.appSys = ncAPPSystemInfo()
                    self.appSys.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.master = ncSiteInfo()
                    self.master.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.slaves = []
                    (_etype35, _size32) = iprot.readListBegin()
                    for _i36 in range(_size32):
                        _elem37 = ncSiteInfo()
                        _elem37.read(iprot)
                        self.slaves.append(_elem37)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.clients = []
                    (_etype41, _size38) = iprot.readListBegin()
                    for _i42 in range(_size38):
                        _elem43 = ncClient.ttypes.ncTClient()
                        _elem43.read(iprot)
                        self.clients.append(_elem43)
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
        oprot.writeStructBegin('ncDatasourceResult')
        if self.appSys is not None:
            oprot.writeFieldBegin('appSys', TType.STRUCT, 1)
            self.appSys.write(oprot)
            oprot.writeFieldEnd()
        if self.master is not None:
            oprot.writeFieldBegin('master', TType.STRUCT, 2)
            self.master.write(oprot)
            oprot.writeFieldEnd()
        if self.slaves is not None:
            oprot.writeFieldBegin('slaves', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.slaves))
            for iter44 in self.slaves:
                iter44.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.clients is not None:
            oprot.writeFieldBegin('clients', TType.LIST, 4)
            oprot.writeListBegin(TType.STRUCT, len(self.clients))
            for iter45 in self.clients:
                iter45.write(oprot)
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


class ncCephInfo(object):
    """
    Attributes:
     - capacity
     - status
     - userId
     - username
     - url
     - urlHostId

    """


    def __init__(self, capacity=None, status=None, userId=None, username=None, url=None, urlHostId=None,):
        self.capacity = capacity
        self.status = status
        self.userId = userId
        self.username = username
        self.url = url
        self.urlHostId = urlHostId

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
                    self.capacity = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.userId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.url = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.urlHostId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncCephInfo')
        if self.capacity is not None:
            oprot.writeFieldBegin('capacity', TType.I64, 1)
            oprot.writeI64(self.capacity)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 2)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.userId is not None:
            oprot.writeFieldBegin('userId', TType.STRING, 3)
            oprot.writeString(self.userId.encode('utf-8') if sys.version_info[0] == 2 else self.userId)
            oprot.writeFieldEnd()
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 4)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
            oprot.writeFieldEnd()
        if self.url is not None:
            oprot.writeFieldBegin('url', TType.STRING, 5)
            oprot.writeString(self.url.encode('utf-8') if sys.version_info[0] == 2 else self.url)
            oprot.writeFieldEnd()
        if self.urlHostId is not None:
            oprot.writeFieldBegin('urlHostId', TType.STRING, 6)
            oprot.writeString(self.urlHostId.encode('utf-8') if sys.version_info[0] == 2 else self.urlHostId)
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
all_structs.append(ncSiteInfoCheck)
ncSiteInfoCheck.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
    (2, TType.MAP, 'ossIdCSId', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 2
)
all_structs.append(ncAppSystemCheck)
ncAppSystemCheck.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'appId', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'master', [ncSiteInfoCheck, None], None, ),  # 2
    (3, TType.LIST, 'slaves', (TType.STRUCT, [ncSiteInfoCheck, None], False), None, ),  # 3
    (4, TType.LIST, 'clientIds', (TType.STRING, 'UTF8', False), None, ),  # 4
)
all_structs.append(ncDatasourceCheckReq)
ncDatasourceCheckReq.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'ccloudCheck', [ncAppSystemCheck, None], None, ),  # 1
    (2, TType.STRING, 'username', 'UTF8', None, ),  # 2
)
all_structs.append(ncOSSInfo)
ncOSSInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'ipDomain', 'UTF8', None, ),  # 3
    (4, TType.I64, 'port', None, None, ),  # 4
)
all_structs.append(ncCloudStorageInfos)
ncCloudStorageInfos.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'ip', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'name', 'UTF8', None, ),  # 3
    (4, TType.I32, 'type', None, None, ),  # 4
    (5, TType.STRING, 'accessId', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'accessKey', 'UTF8', None, ),  # 6
)
all_structs.append(ncSiteInfo)
ncSiteInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'ipDomain', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'version', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'authUser', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'appId', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'appKey', 'UTF8', None, ),  # 7
    (8, TType.MAP, 'ossInfos', (TType.STRING, 'UTF8', TType.STRUCT, [ncCloudStorageInfos, None], False), None, ),  # 8
    (9, TType.I32, 'type', None, None, ),  # 9
    (10, TType.I32, 'port', None, None, ),  # 10
)
all_structs.append(ncAPPSystemInfo)
ncAPPSystemInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
)
all_structs.append(ncDatasourceResult)
ncDatasourceResult.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'appSys', [ncAPPSystemInfo, None], None, ),  # 1
    (2, TType.STRUCT, 'master', [ncSiteInfo, None], None, ),  # 2
    (3, TType.LIST, 'slaves', (TType.STRUCT, [ncSiteInfo, None], False), None, ),  # 3
    (4, TType.LIST, 'clients', (TType.STRUCT, [ncClient.ttypes.ncTClient, None], False), None, ),  # 4
)
all_structs.append(ncCephInfo)
ncCephInfo.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'capacity', None, None, ),  # 1
    (2, TType.I32, 'status', None, None, ),  # 2
    (3, TType.STRING, 'userId', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'username', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'url', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'urlHostId', 'UTF8', None, ),  # 6
)
fix_spec(all_structs)
del all_structs
