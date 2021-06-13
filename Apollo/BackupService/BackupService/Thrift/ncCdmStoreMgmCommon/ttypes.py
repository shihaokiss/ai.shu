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


class ncMDiskStatus(object):
    """
    MDisk状态

    """
    MANAGED = 1
    UNMANAGED = 2
    ABNORMAL = 3
    MIRATING = 4

    _VALUES_TO_NAMES = {
        1: "MANAGED",
        2: "UNMANAGED",
        3: "ABNORMAL",
        4: "MIRATING",
    }

    _NAMES_TO_VALUES = {
        "MANAGED": 1,
        "UNMANAGED": 2,
        "ABNORMAL": 3,
        "MIRATING": 4,
    }


class ncPoolType(object):
    """
    存储池类型

    """
    ALL = 0
    SNAPSHOT = 1
    DEDUP = 2
    CLOUD = 3

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "SNAPSHOT",
        2: "DEDUP",
        3: "CLOUD",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "SNAPSHOT": 1,
        "DEDUP": 2,
        "CLOUD": 3,
    }


class ncPoolStatus(object):
    """
    存储池状态

    """
    NORMAL = 0
    ABNORMAL = 1
    MIRATING = 4

    _VALUES_TO_NAMES = {
        0: "NORMAL",
        1: "ABNORMAL",
        4: "MIRATING",
    }

    _NAMES_TO_VALUES = {
        "NORMAL": 0,
        "ABNORMAL": 1,
        "MIRATING": 4,
    }


class ncVolumeStatus(object):
    """
    卷状态

    """
    ALL = 0
    ABNORMAL = 1
    NORMAL = 2
    CREATING = 3
    DELETING = 4

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "ABNORMAL",
        2: "NORMAL",
        3: "CREATING",
        4: "DELETING",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "ABNORMAL": 1,
        "NORMAL": 2,
        "CREATING": 3,
        "DELETING": 4,
    }


class ncVolumeType(object):
    """
    volume类型

    """
    BASE = 1
    SNAP = 2
    CLONE = 3

    _VALUES_TO_NAMES = {
        1: "BASE",
        2: "SNAP",
        3: "CLONE",
    }

    _NAMES_TO_VALUES = {
        "BASE": 1,
        "SNAP": 2,
        "CLONE": 3,
    }


class ncBaseVolumeType(object):
    """
    baseVolume类型

    """
    NORMAL = 1
    THIN = 2
    DYNAMIC = 3

    _VALUES_TO_NAMES = {
        1: "NORMAL",
        2: "THIN",
        3: "DYNAMIC",
    }

    _NAMES_TO_VALUES = {
        "NORMAL": 1,
        "THIN": 2,
        "DYNAMIC": 3,
    }


class ncFabricModule(object):
    """
    Fabric类型

    """
    LOOPBACK = 0
    ISCSI = 1
    FC = 2
    SRPT = 3
    SBP = 4
    TCMFC = 5
    VHOST = 6
    XENPVSCSI = 7
    IBMVSCSIS = 8

    _VALUES_TO_NAMES = {
        0: "LOOPBACK",
        1: "ISCSI",
        2: "FC",
        3: "SRPT",
        4: "SBP",
        5: "TCMFC",
        6: "VHOST",
        7: "XENPVSCSI",
        8: "IBMVSCSIS",
    }

    _NAMES_TO_VALUES = {
        "LOOPBACK": 0,
        "ISCSI": 1,
        "FC": 2,
        "SRPT": 3,
        "SBP": 4,
        "TCMFC": 5,
        "VHOST": 6,
        "XENPVSCSI": 7,
        "IBMVSCSIS": 8,
    }


class ncLinkStatus(object):
    """
    链路状态

    """
    ALL = 0
    NORMAL = 1
    USED = 2
    ABNORMAL = 3
    CREATING = 4
    DELETING = 5

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "NORMAL",
        2: "USED",
        3: "ABNORMAL",
        4: "CREATING",
        5: "DELETING",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "NORMAL": 1,
        "USED": 2,
        "ABNORMAL": 3,
        "CREATING": 4,
        "DELETING": 5,
    }


class ncSnapPoolType(object):
    OLDAB = 1
    HWFS = 2
    NEWAB = 3

    _VALUES_TO_NAMES = {
        1: "OLDAB",
        2: "HWFS",
        3: "NEWAB",
    }

    _NAMES_TO_VALUES = {
        "OLDAB": 1,
        "HWFS": 2,
        "NEWAB": 3,
    }


class ncMDiskSpaceInfo(object):
    """
    MDisk容量信息

    Attributes:
     - diskSize
     - freeSize

    """


    def __init__(self, diskSize=None, freeSize=None,):
        self.diskSize = diskSize
        self.freeSize = freeSize

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
                    self.diskSize = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.freeSize = iprot.readI64()
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
        oprot.writeStructBegin('ncMDiskSpaceInfo')
        if self.diskSize is not None:
            oprot.writeFieldBegin('diskSize', TType.I64, 1)
            oprot.writeI64(self.diskSize)
            oprot.writeFieldEnd()
        if self.freeSize is not None:
            oprot.writeFieldBegin('freeSize', TType.I64, 2)
            oprot.writeI64(self.freeSize)
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


class ncMDiskInfo(object):
    """
    MDisk信息（MDisk是构建SnapPool和DedupPool的基本单元）

    Attributes:
     - uuid
     - name
     - path
     - vendor
     - poolUuid
     - status
     - spaceInfo
     - pooluuid
     - nodeIp
     - storagePoolId
     - baseVolumeId
     - storageType
     - poolId

    """


    def __init__(self, uuid=None, name=None, path=None, vendor=None, poolUuid=None, status=None, spaceInfo=None, pooluuid=None, nodeIp=None, storagePoolId=None, baseVolumeId=None, storageType=None, poolId=None,):
        self.uuid = uuid
        self.name = name
        self.path = path
        self.vendor = vendor
        self.poolUuid = poolUuid
        self.status = status
        self.spaceInfo = spaceInfo
        self.pooluuid = pooluuid
        self.nodeIp = nodeIp
        self.storagePoolId = storagePoolId
        self.baseVolumeId = baseVolumeId
        self.storageType = storageType
        self.poolId = poolId

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
                    self.uuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.path = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.vendor = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.poolUuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRUCT:
                    self.spaceInfo = ncMDiskSpaceInfo()
                    self.spaceInfo.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.pooluuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.nodeIp = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.storagePoolId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.baseVolumeId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.storageType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRING:
                    self.poolId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncMDiskInfo')
        if self.uuid is not None:
            oprot.writeFieldBegin('uuid', TType.STRING, 1)
            oprot.writeString(self.uuid.encode('utf-8') if sys.version_info[0] == 2 else self.uuid)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.path is not None:
            oprot.writeFieldBegin('path', TType.STRING, 3)
            oprot.writeString(self.path.encode('utf-8') if sys.version_info[0] == 2 else self.path)
            oprot.writeFieldEnd()
        if self.vendor is not None:
            oprot.writeFieldBegin('vendor', TType.STRING, 4)
            oprot.writeString(self.vendor.encode('utf-8') if sys.version_info[0] == 2 else self.vendor)
            oprot.writeFieldEnd()
        if self.poolUuid is not None:
            oprot.writeFieldBegin('poolUuid', TType.STRING, 5)
            oprot.writeString(self.poolUuid.encode('utf-8') if sys.version_info[0] == 2 else self.poolUuid)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 6)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.spaceInfo is not None:
            oprot.writeFieldBegin('spaceInfo', TType.STRUCT, 7)
            self.spaceInfo.write(oprot)
            oprot.writeFieldEnd()
        if self.pooluuid is not None:
            oprot.writeFieldBegin('pooluuid', TType.STRING, 8)
            oprot.writeString(self.pooluuid.encode('utf-8') if sys.version_info[0] == 2 else self.pooluuid)
            oprot.writeFieldEnd()
        if self.nodeIp is not None:
            oprot.writeFieldBegin('nodeIp', TType.STRING, 9)
            oprot.writeString(self.nodeIp.encode('utf-8') if sys.version_info[0] == 2 else self.nodeIp)
            oprot.writeFieldEnd()
        if self.storagePoolId is not None:
            oprot.writeFieldBegin('storagePoolId', TType.STRING, 10)
            oprot.writeString(self.storagePoolId.encode('utf-8') if sys.version_info[0] == 2 else self.storagePoolId)
            oprot.writeFieldEnd()
        if self.baseVolumeId is not None:
            oprot.writeFieldBegin('baseVolumeId', TType.STRING, 11)
            oprot.writeString(self.baseVolumeId.encode('utf-8') if sys.version_info[0] == 2 else self.baseVolumeId)
            oprot.writeFieldEnd()
        if self.storageType is not None:
            oprot.writeFieldBegin('storageType', TType.I32, 12)
            oprot.writeI32(self.storageType)
            oprot.writeFieldEnd()
        if self.poolId is not None:
            oprot.writeFieldBegin('poolId', TType.STRING, 13)
            oprot.writeString(self.poolId.encode('utf-8') if sys.version_info[0] == 2 else self.poolId)
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


class ncMDiskInfoList(object):
    """
    MDisk列表

    Attributes:
     - mdiskInfoList

    """


    def __init__(self, mdiskInfoList=None,):
        self.mdiskInfoList = mdiskInfoList

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
                    self.mdiskInfoList = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = ncMDiskInfo()
                        _elem5.read(iprot)
                        self.mdiskInfoList.append(_elem5)
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
        oprot.writeStructBegin('ncMDiskInfoList')
        if self.mdiskInfoList is not None:
            oprot.writeFieldBegin('mdiskInfoList', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.mdiskInfoList))
            for iter6 in self.mdiskInfoList:
                iter6.write(oprot)
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


class ncLinkInfo(object):
    """
    链路信息

    Attributes:
     - link_id
     - fabric_type
     - server_wwn
     - client_wwn
     - server_id
     - client_id
     - server_name
     - client_name
     - client_type
     - client_ip
     - portal_ip
     - portal_port
     - pool_id
     - third_party_storage_id
     - pool_type

    """


    def __init__(self, link_id=None, fabric_type=None, server_wwn=None, client_wwn=None, server_id=None, client_id=None, server_name=None, client_name=None, client_type=None, client_ip=None, portal_ip=None, portal_port=None, pool_id=None, third_party_storage_id=None, pool_type=None,):
        self.link_id = link_id
        self.fabric_type = fabric_type
        self.server_wwn = server_wwn
        self.client_wwn = client_wwn
        self.server_id = server_id
        self.client_id = client_id
        self.server_name = server_name
        self.client_name = client_name
        self.client_type = client_type
        self.client_ip = client_ip
        self.portal_ip = portal_ip
        self.portal_port = portal_port
        self.pool_id = pool_id
        self.third_party_storage_id = third_party_storage_id
        self.pool_type = pool_type

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
                    self.link_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.fabric_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.server_wwn = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.client_wwn = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.server_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.client_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.server_name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.client_name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.client_type = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.client_ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.portal_ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.portal_port = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRING:
                    self.pool_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.STRING:
                    self.third_party_storage_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I32:
                    self.pool_type = iprot.readI32()
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
        oprot.writeStructBegin('ncLinkInfo')
        if self.link_id is not None:
            oprot.writeFieldBegin('link_id', TType.STRING, 1)
            oprot.writeString(self.link_id.encode('utf-8') if sys.version_info[0] == 2 else self.link_id)
            oprot.writeFieldEnd()
        if self.fabric_type is not None:
            oprot.writeFieldBegin('fabric_type', TType.I32, 2)
            oprot.writeI32(self.fabric_type)
            oprot.writeFieldEnd()
        if self.server_wwn is not None:
            oprot.writeFieldBegin('server_wwn', TType.STRING, 3)
            oprot.writeString(self.server_wwn.encode('utf-8') if sys.version_info[0] == 2 else self.server_wwn)
            oprot.writeFieldEnd()
        if self.client_wwn is not None:
            oprot.writeFieldBegin('client_wwn', TType.STRING, 4)
            oprot.writeString(self.client_wwn.encode('utf-8') if sys.version_info[0] == 2 else self.client_wwn)
            oprot.writeFieldEnd()
        if self.server_id is not None:
            oprot.writeFieldBegin('server_id', TType.STRING, 5)
            oprot.writeString(self.server_id.encode('utf-8') if sys.version_info[0] == 2 else self.server_id)
            oprot.writeFieldEnd()
        if self.client_id is not None:
            oprot.writeFieldBegin('client_id', TType.STRING, 6)
            oprot.writeString(self.client_id.encode('utf-8') if sys.version_info[0] == 2 else self.client_id)
            oprot.writeFieldEnd()
        if self.server_name is not None:
            oprot.writeFieldBegin('server_name', TType.STRING, 7)
            oprot.writeString(self.server_name.encode('utf-8') if sys.version_info[0] == 2 else self.server_name)
            oprot.writeFieldEnd()
        if self.client_name is not None:
            oprot.writeFieldBegin('client_name', TType.STRING, 8)
            oprot.writeString(self.client_name.encode('utf-8') if sys.version_info[0] == 2 else self.client_name)
            oprot.writeFieldEnd()
        if self.client_type is not None:
            oprot.writeFieldBegin('client_type', TType.STRING, 9)
            oprot.writeString(self.client_type.encode('utf-8') if sys.version_info[0] == 2 else self.client_type)
            oprot.writeFieldEnd()
        if self.client_ip is not None:
            oprot.writeFieldBegin('client_ip', TType.STRING, 10)
            oprot.writeString(self.client_ip.encode('utf-8') if sys.version_info[0] == 2 else self.client_ip)
            oprot.writeFieldEnd()
        if self.portal_ip is not None:
            oprot.writeFieldBegin('portal_ip', TType.STRING, 11)
            oprot.writeString(self.portal_ip.encode('utf-8') if sys.version_info[0] == 2 else self.portal_ip)
            oprot.writeFieldEnd()
        if self.portal_port is not None:
            oprot.writeFieldBegin('portal_port', TType.I32, 12)
            oprot.writeI32(self.portal_port)
            oprot.writeFieldEnd()
        if self.pool_id is not None:
            oprot.writeFieldBegin('pool_id', TType.STRING, 13)
            oprot.writeString(self.pool_id.encode('utf-8') if sys.version_info[0] == 2 else self.pool_id)
            oprot.writeFieldEnd()
        if self.third_party_storage_id is not None:
            oprot.writeFieldBegin('third_party_storage_id', TType.STRING, 14)
            oprot.writeString(self.third_party_storage_id.encode('utf-8') if sys.version_info[0] == 2 else self.third_party_storage_id)
            oprot.writeFieldEnd()
        if self.pool_type is not None:
            oprot.writeFieldBegin('pool_type', TType.I32, 15)
            oprot.writeI32(self.pool_type)
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


class ncSyncSnapVolumeProgress(object):
    """
    Attributes:
     - totalSize
     - syncSize
     - outputMsg
     - execSpeed
     - isFinished

    """


    def __init__(self, totalSize=None, syncSize=None, outputMsg=None, execSpeed=None, isFinished=None,):
        self.totalSize = totalSize
        self.syncSize = syncSize
        self.outputMsg = outputMsg
        self.execSpeed = execSpeed
        self.isFinished = isFinished

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
                    self.totalSize = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.syncSize = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.outputMsg = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.execSpeed = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.BOOL:
                    self.isFinished = iprot.readBool()
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
        oprot.writeStructBegin('ncSyncSnapVolumeProgress')
        if self.totalSize is not None:
            oprot.writeFieldBegin('totalSize', TType.I64, 1)
            oprot.writeI64(self.totalSize)
            oprot.writeFieldEnd()
        if self.syncSize is not None:
            oprot.writeFieldBegin('syncSize', TType.I64, 2)
            oprot.writeI64(self.syncSize)
            oprot.writeFieldEnd()
        if self.outputMsg is not None:
            oprot.writeFieldBegin('outputMsg', TType.STRING, 4)
            oprot.writeString(self.outputMsg.encode('utf-8') if sys.version_info[0] == 2 else self.outputMsg)
            oprot.writeFieldEnd()
        if self.execSpeed is not None:
            oprot.writeFieldBegin('execSpeed', TType.I64, 5)
            oprot.writeI64(self.execSpeed)
            oprot.writeFieldEnd()
        if self.isFinished is not None:
            oprot.writeFieldBegin('isFinished', TType.BOOL, 6)
            oprot.writeBool(self.isFinished)
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
all_structs.append(ncMDiskSpaceInfo)
ncMDiskSpaceInfo.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'diskSize', None, None, ),  # 1
    (2, TType.I64, 'freeSize', None, None, ),  # 2
)
all_structs.append(ncMDiskInfo)
ncMDiskInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'uuid', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'path', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'vendor', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'poolUuid', 'UTF8', None, ),  # 5
    (6, TType.I32, 'status', None, None, ),  # 6
    (7, TType.STRUCT, 'spaceInfo', [ncMDiskSpaceInfo, None], None, ),  # 7
    (8, TType.STRING, 'pooluuid', 'UTF8', None, ),  # 8
    (9, TType.STRING, 'nodeIp', 'UTF8', None, ),  # 9
    (10, TType.STRING, 'storagePoolId', 'UTF8', None, ),  # 10
    (11, TType.STRING, 'baseVolumeId', 'UTF8', None, ),  # 11
    (12, TType.I32, 'storageType', None, None, ),  # 12
    (13, TType.STRING, 'poolId', 'UTF8', None, ),  # 13
)
all_structs.append(ncMDiskInfoList)
ncMDiskInfoList.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'mdiskInfoList', (TType.STRUCT, [ncMDiskInfo, None], False), None, ),  # 1
)
all_structs.append(ncLinkInfo)
ncLinkInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'link_id', 'UTF8', None, ),  # 1
    (2, TType.I32, 'fabric_type', None, None, ),  # 2
    (3, TType.STRING, 'server_wwn', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'client_wwn', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'server_id', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'client_id', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'server_name', 'UTF8', None, ),  # 7
    (8, TType.STRING, 'client_name', 'UTF8', None, ),  # 8
    (9, TType.STRING, 'client_type', 'UTF8', None, ),  # 9
    (10, TType.STRING, 'client_ip', 'UTF8', None, ),  # 10
    (11, TType.STRING, 'portal_ip', 'UTF8', None, ),  # 11
    (12, TType.I32, 'portal_port', None, None, ),  # 12
    (13, TType.STRING, 'pool_id', 'UTF8', None, ),  # 13
    (14, TType.STRING, 'third_party_storage_id', 'UTF8', None, ),  # 14
    (15, TType.I32, 'pool_type', None, None, ),  # 15
)
all_structs.append(ncSyncSnapVolumeProgress)
ncSyncSnapVolumeProgress.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'totalSize', None, None, ),  # 1
    (2, TType.I64, 'syncSize', None, None, ),  # 2
    None,  # 3
    (4, TType.STRING, 'outputMsg', 'UTF8', None, ),  # 4
    (5, TType.I64, 'execSpeed', None, None, ),  # 5
    (6, TType.BOOL, 'isFinished', None, None, ),  # 6
)
fix_spec(all_structs)
del all_structs