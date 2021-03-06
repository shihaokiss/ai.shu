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


class ncOracleClientType(object):
    UNDEFINED = 0
    STAND_ALONE = 1
    RAC = 2
    COUPLE = 3

    _VALUES_TO_NAMES = {
        0: "UNDEFINED",
        1: "STAND_ALONE",
        2: "RAC",
        3: "COUPLE",
    }

    _NAMES_TO_VALUES = {
        "UNDEFINED": 0,
        "STAND_ALONE": 1,
        "RAC": 2,
        "COUPLE": 3,
    }


class ncRestoreObjectEnum(object):
    ORACLE_INSTANCE = 0
    ORACLE_TABLE_SPACE = 1
    ORACLE_DATA_FILE = 2
    ORACLE_LOG_FILE = 3
    ORACLE_CONTROL_FILE = 4
    ORACLE_SPFILE = 5
    ORACLE_TABLE = 6

    _VALUES_TO_NAMES = {
        0: "ORACLE_INSTANCE",
        1: "ORACLE_TABLE_SPACE",
        2: "ORACLE_DATA_FILE",
        3: "ORACLE_LOG_FILE",
        4: "ORACLE_CONTROL_FILE",
        5: "ORACLE_SPFILE",
        6: "ORACLE_TABLE",
    }

    _NAMES_TO_VALUES = {
        "ORACLE_INSTANCE": 0,
        "ORACLE_TABLE_SPACE": 1,
        "ORACLE_DATA_FILE": 2,
        "ORACLE_LOG_FILE": 3,
        "ORACLE_CONTROL_FILE": 4,
        "ORACLE_SPFILE": 5,
        "ORACLE_TABLE": 6,
    }


class ncOracleClientMetaInfo(object):
    """
    Attributes:
     - attributes
     - infolists

    """


    def __init__(self, attributes=None, infolists=None,):
        self.attributes = attributes
        self.infolists = infolists

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
                if ftype == TType.MAP:
                    self.attributes = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val6 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.attributes[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.MAP:
                    self.infolists = {}
                    (_ktype8, _vtype9, _size7) = iprot.readMapBegin()
                    for _i11 in range(_size7):
                        _key12 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val13 = []
                        (_etype17, _size14) = iprot.readListBegin()
                        for _i18 in range(_size14):
                            _elem19 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                            _val13.append(_elem19)
                        iprot.readListEnd()
                        self.infolists[_key12] = _val13
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
        oprot.writeStructBegin('ncOracleClientMetaInfo')
        if self.attributes is not None:
            oprot.writeFieldBegin('attributes', TType.MAP, 1)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.attributes))
            for kiter20, viter21 in self.attributes.items():
                oprot.writeString(kiter20.encode('utf-8') if sys.version_info[0] == 2 else kiter20)
                oprot.writeString(viter21.encode('utf-8') if sys.version_info[0] == 2 else viter21)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.infolists is not None:
            oprot.writeFieldBegin('infolists', TType.MAP, 2)
            oprot.writeMapBegin(TType.STRING, TType.LIST, len(self.infolists))
            for kiter22, viter23 in self.infolists.items():
                oprot.writeString(kiter22.encode('utf-8') if sys.version_info[0] == 2 else kiter22)
                oprot.writeListBegin(TType.STRING, len(viter23))
                for iter24 in viter23:
                    oprot.writeString(iter24.encode('utf-8') if sys.version_info[0] == 2 else iter24)
                oprot.writeListEnd()
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


class ncOracleBackupMetaInfo(object):
    """
    Attributes:
     - version
     - clienttype
     - metas

    """


    def __init__(self, version=None, clienttype=None, metas=None,):
        self.version = version
        self.clienttype = clienttype
        self.metas = metas

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
                    self.version = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.clienttype = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.metas = []
                    (_etype28, _size25) = iprot.readListBegin()
                    for _i29 in range(_size25):
                        _elem30 = ncOracleClientMetaInfo()
                        _elem30.read(iprot)
                        self.metas.append(_elem30)
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
        oprot.writeStructBegin('ncOracleBackupMetaInfo')
        if self.version is not None:
            oprot.writeFieldBegin('version', TType.I32, 1)
            oprot.writeI32(self.version)
            oprot.writeFieldEnd()
        if self.clienttype is not None:
            oprot.writeFieldBegin('clienttype', TType.I32, 2)
            oprot.writeI32(self.clienttype)
            oprot.writeFieldEnd()
        if self.metas is not None:
            oprot.writeFieldBegin('metas', TType.LIST, 3)
            oprot.writeListBegin(TType.STRUCT, len(self.metas))
            for iter31 in self.metas:
                iter31.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.version is None:
            raise TProtocolException(message='Required field version is unset!')
        if self.clienttype is None:
            raise TProtocolException(message='Required field clienttype is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ncOracleClientMetaInfo)
ncOracleClientMetaInfo.thrift_spec = (
    None,  # 0
    (1, TType.MAP, 'attributes', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 1
    (2, TType.MAP, 'infolists', (TType.STRING, 'UTF8', TType.LIST, (TType.STRING, 'UTF8', False), False), None, ),  # 2
)
all_structs.append(ncOracleBackupMetaInfo)
ncOracleBackupMetaInfo.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'version', None, None, ),  # 1
    (2, TType.I32, 'clienttype', None, None, ),  # 2
    (3, TType.LIST, 'metas', (TType.STRUCT, [ncOracleClientMetaInfo, None], False), None, ),  # 3
)
fix_spec(all_structs)
del all_structs
