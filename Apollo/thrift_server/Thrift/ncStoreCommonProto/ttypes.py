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
import ncCdmStoreMgmCommon.ttypes

from thrift.transport import TTransport
all_structs = []


class ncBaseVolumeSpaceInfo(object):
    """
    BaseVolume容量信息

    Attributes:
     - volumeSize
     - freeSize

    """


    def __init__(self, volumeSize=None, freeSize=None,):
        self.volumeSize = volumeSize
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
                    self.volumeSize = iprot.readI64()
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
        oprot.writeStructBegin('ncBaseVolumeSpaceInfo')
        if self.volumeSize is not None:
            oprot.writeFieldBegin('volumeSize', TType.I64, 1)
            oprot.writeI64(self.volumeSize)
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


class ncBaseVolumeInfo(object):
    """
    BaseVolume信息（BaseVolume是SnapPool空间分配的基本单元）

    Attributes:
     - uuid
     - name
     - type
     - spaceInfo
     - pooluuid
     - groupuuid

    """


    def __init__(self, uuid=None, name=None, type=None, spaceInfo=None, pooluuid=None, groupuuid=None,):
        self.uuid = uuid
        self.name = name
        self.type = type
        self.spaceInfo = spaceInfo
        self.pooluuid = pooluuid
        self.groupuuid = groupuuid

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
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRUCT:
                    self.spaceInfo = ncBaseVolumeSpaceInfo()
                    self.spaceInfo.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.pooluuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.groupuuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncBaseVolumeInfo')
        if self.uuid is not None:
            oprot.writeFieldBegin('uuid', TType.STRING, 1)
            oprot.writeString(self.uuid.encode('utf-8') if sys.version_info[0] == 2 else self.uuid)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 2)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 3)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.spaceInfo is not None:
            oprot.writeFieldBegin('spaceInfo', TType.STRUCT, 4)
            self.spaceInfo.write(oprot)
            oprot.writeFieldEnd()
        if self.pooluuid is not None:
            oprot.writeFieldBegin('pooluuid', TType.STRING, 5)
            oprot.writeString(self.pooluuid.encode('utf-8') if sys.version_info[0] == 2 else self.pooluuid)
            oprot.writeFieldEnd()
        if self.groupuuid is not None:
            oprot.writeFieldBegin('groupuuid', TType.STRING, 6)
            oprot.writeString(self.groupuuid.encode('utf-8') if sys.version_info[0] == 2 else self.groupuuid)
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


class ncBaseVolumeInfoList(object):
    """
    BaseVolume列表

    Attributes:
     - baseVolInfoList

    """


    def __init__(self, baseVolInfoList=None,):
        self.baseVolInfoList = baseVolInfoList

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
                    self.baseVolInfoList = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = ncBaseVolumeInfo()
                        _elem5.read(iprot)
                        self.baseVolInfoList.append(_elem5)
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
        oprot.writeStructBegin('ncBaseVolumeInfoList')
        if self.baseVolInfoList is not None:
            oprot.writeFieldBegin('baseVolInfoList', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.baseVolInfoList))
            for iter6 in self.baseVolInfoList:
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


class ncSnapVolumeInfo(object):
    """
    SnapVolume信息

    Attributes:
     - timestamp
     - uuid
     - name
     - pooluuid
     - basevolumeuuid
     - groupuuid

    """


    def __init__(self, timestamp=None, uuid=None, name=None, pooluuid=None, basevolumeuuid=None, groupuuid=None,):
        self.timestamp = timestamp
        self.uuid = uuid
        self.name = name
        self.pooluuid = pooluuid
        self.basevolumeuuid = basevolumeuuid
        self.groupuuid = groupuuid

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
                    self.timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.uuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.pooluuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.basevolumeuuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.groupuuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncSnapVolumeInfo')
        if self.timestamp is not None:
            oprot.writeFieldBegin('timestamp', TType.I64, 1)
            oprot.writeI64(self.timestamp)
            oprot.writeFieldEnd()
        if self.uuid is not None:
            oprot.writeFieldBegin('uuid', TType.STRING, 2)
            oprot.writeString(self.uuid.encode('utf-8') if sys.version_info[0] == 2 else self.uuid)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 3)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.pooluuid is not None:
            oprot.writeFieldBegin('pooluuid', TType.STRING, 4)
            oprot.writeString(self.pooluuid.encode('utf-8') if sys.version_info[0] == 2 else self.pooluuid)
            oprot.writeFieldEnd()
        if self.basevolumeuuid is not None:
            oprot.writeFieldBegin('basevolumeuuid', TType.STRING, 5)
            oprot.writeString(self.basevolumeuuid.encode('utf-8') if sys.version_info[0] == 2 else self.basevolumeuuid)
            oprot.writeFieldEnd()
        if self.groupuuid is not None:
            oprot.writeFieldBegin('groupuuid', TType.STRING, 6)
            oprot.writeString(self.groupuuid.encode('utf-8') if sys.version_info[0] == 2 else self.groupuuid)
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


class ncSnapVolumeInfoList(object):
    """
    SnapVolume列表

    Attributes:
     - snapVolInfoList

    """


    def __init__(self, snapVolInfoList=None,):
        self.snapVolInfoList = snapVolInfoList

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
                    self.snapVolInfoList = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = ncSnapVolumeInfo()
                        _elem12.read(iprot)
                        self.snapVolInfoList.append(_elem12)
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
        oprot.writeStructBegin('ncSnapVolumeInfoList')
        if self.snapVolInfoList is not None:
            oprot.writeFieldBegin('snapVolInfoList', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.snapVolInfoList))
            for iter13 in self.snapVolInfoList:
                iter13.write(oprot)
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


class ncCloneVolumeInfo(object):
    """
    CloneVolume信息

    Attributes:
     - timestamp
     - uuid
     - name
     - pooluuid
     - basevolumeuuid
     - snapvolumeuuid
     - groupuuid

    """


    def __init__(self, timestamp=None, uuid=None, name=None, pooluuid=None, basevolumeuuid=None, snapvolumeuuid=None, groupuuid=None,):
        self.timestamp = timestamp
        self.uuid = uuid
        self.name = name
        self.pooluuid = pooluuid
        self.basevolumeuuid = basevolumeuuid
        self.snapvolumeuuid = snapvolumeuuid
        self.groupuuid = groupuuid

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
                    self.timestamp = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.uuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.pooluuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.basevolumeuuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.snapvolumeuuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.groupuuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncCloneVolumeInfo')
        if self.timestamp is not None:
            oprot.writeFieldBegin('timestamp', TType.I64, 1)
            oprot.writeI64(self.timestamp)
            oprot.writeFieldEnd()
        if self.uuid is not None:
            oprot.writeFieldBegin('uuid', TType.STRING, 2)
            oprot.writeString(self.uuid.encode('utf-8') if sys.version_info[0] == 2 else self.uuid)
            oprot.writeFieldEnd()
        if self.name is not None:
            oprot.writeFieldBegin('name', TType.STRING, 3)
            oprot.writeString(self.name.encode('utf-8') if sys.version_info[0] == 2 else self.name)
            oprot.writeFieldEnd()
        if self.pooluuid is not None:
            oprot.writeFieldBegin('pooluuid', TType.STRING, 4)
            oprot.writeString(self.pooluuid.encode('utf-8') if sys.version_info[0] == 2 else self.pooluuid)
            oprot.writeFieldEnd()
        if self.basevolumeuuid is not None:
            oprot.writeFieldBegin('basevolumeuuid', TType.STRING, 5)
            oprot.writeString(self.basevolumeuuid.encode('utf-8') if sys.version_info[0] == 2 else self.basevolumeuuid)
            oprot.writeFieldEnd()
        if self.snapvolumeuuid is not None:
            oprot.writeFieldBegin('snapvolumeuuid', TType.STRING, 6)
            oprot.writeString(self.snapvolumeuuid.encode('utf-8') if sys.version_info[0] == 2 else self.snapvolumeuuid)
            oprot.writeFieldEnd()
        if self.groupuuid is not None:
            oprot.writeFieldBegin('groupuuid', TType.STRING, 7)
            oprot.writeString(self.groupuuid.encode('utf-8') if sys.version_info[0] == 2 else self.groupuuid)
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


class ncCloneVolumeInfoList(object):
    """
    CloneVolume列表

    Attributes:
     - cloneVolInfoList

    """


    def __init__(self, cloneVolInfoList=None,):
        self.cloneVolInfoList = cloneVolInfoList

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
                    self.cloneVolInfoList = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = ncCloneVolumeInfo()
                        _elem19.read(iprot)
                        self.cloneVolInfoList.append(_elem19)
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
        oprot.writeStructBegin('ncCloneVolumeInfoList')
        if self.cloneVolInfoList is not None:
            oprot.writeFieldBegin('cloneVolInfoList', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.cloneVolInfoList))
            for iter20 in self.cloneVolInfoList:
                iter20.write(oprot)
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


class ncVolumeSpaceInfo(object):
    """
    Volume 空间使用信息

    Attributes:
     - volumeSize
     - allocSize
     - shareSize
     - preallocSize

    """


    def __init__(self, volumeSize=None, allocSize=None, shareSize=None, preallocSize=None,):
        self.volumeSize = volumeSize
        self.allocSize = allocSize
        self.shareSize = shareSize
        self.preallocSize = preallocSize

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
                    self.volumeSize = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I64:
                    self.allocSize = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.shareSize = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.preallocSize = iprot.readI64()
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
        oprot.writeStructBegin('ncVolumeSpaceInfo')
        if self.volumeSize is not None:
            oprot.writeFieldBegin('volumeSize', TType.I64, 1)
            oprot.writeI64(self.volumeSize)
            oprot.writeFieldEnd()
        if self.allocSize is not None:
            oprot.writeFieldBegin('allocSize', TType.I64, 2)
            oprot.writeI64(self.allocSize)
            oprot.writeFieldEnd()
        if self.shareSize is not None:
            oprot.writeFieldBegin('shareSize', TType.I64, 3)
            oprot.writeI64(self.shareSize)
            oprot.writeFieldEnd()
        if self.preallocSize is not None:
            oprot.writeFieldBegin('preallocSize', TType.I64, 4)
            oprot.writeI64(self.preallocSize)
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
all_structs.append(ncBaseVolumeSpaceInfo)
ncBaseVolumeSpaceInfo.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'volumeSize', None, None, ),  # 1
    (2, TType.I64, 'freeSize', None, None, ),  # 2
)
all_structs.append(ncBaseVolumeInfo)
ncBaseVolumeInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'uuid', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'name', 'UTF8', None, ),  # 2
    (3, TType.I32, 'type', None, None, ),  # 3
    (4, TType.STRUCT, 'spaceInfo', [ncBaseVolumeSpaceInfo, None], None, ),  # 4
    (5, TType.STRING, 'pooluuid', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'groupuuid', 'UTF8', None, ),  # 6
)
all_structs.append(ncBaseVolumeInfoList)
ncBaseVolumeInfoList.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'baseVolInfoList', (TType.STRUCT, [ncBaseVolumeInfo, None], False), None, ),  # 1
)
all_structs.append(ncSnapVolumeInfo)
ncSnapVolumeInfo.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'timestamp', None, None, ),  # 1
    (2, TType.STRING, 'uuid', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'name', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'pooluuid', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'basevolumeuuid', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'groupuuid', 'UTF8', None, ),  # 6
)
all_structs.append(ncSnapVolumeInfoList)
ncSnapVolumeInfoList.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'snapVolInfoList', (TType.STRUCT, [ncSnapVolumeInfo, None], False), None, ),  # 1
)
all_structs.append(ncCloneVolumeInfo)
ncCloneVolumeInfo.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'timestamp', None, None, ),  # 1
    (2, TType.STRING, 'uuid', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'name', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'pooluuid', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'basevolumeuuid', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'snapvolumeuuid', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'groupuuid', 'UTF8', None, ),  # 7
)
all_structs.append(ncCloneVolumeInfoList)
ncCloneVolumeInfoList.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'cloneVolInfoList', (TType.STRUCT, [ncCloneVolumeInfo, None], False), None, ),  # 1
)
all_structs.append(ncVolumeSpaceInfo)
ncVolumeSpaceInfo.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'volumeSize', None, None, ),  # 1
    (2, TType.I64, 'allocSize', None, None, ),  # 2
    (3, TType.I64, 'shareSize', None, None, ),  # 3
    (4, TType.I64, 'preallocSize', None, None, ),  # 4
)
fix_spec(all_structs)
del all_structs