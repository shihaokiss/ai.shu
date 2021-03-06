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


class ncEcssVolumeInfo(object):
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
        oprot.writeStructBegin('ncEcssVolumeInfo')
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


class ncBucketStatus(object):
    """
    ?????????

    Attributes:
     - bucketName
     - isExists

    """


    def __init__(self, bucketName=None, isExists=True,):
        self.bucketName = bucketName
        self.isExists = isExists

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
                    self.bucketName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.isExists = iprot.readBool()
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
        oprot.writeStructBegin('ncBucketStatus')
        if self.bucketName is not None:
            oprot.writeFieldBegin('bucketName', TType.STRING, 1)
            oprot.writeString(self.bucketName.encode('utf-8') if sys.version_info[0] == 2 else self.bucketName)
            oprot.writeFieldEnd()
        if self.isExists is not None:
            oprot.writeFieldBegin('isExists', TType.BOOL, 2)
            oprot.writeBool(self.isExists)
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


class ncCloudStorageInfo(object):
    """
    ???????????????

    Attributes:
     - url
     - accessKey
     - secretKey
     - bucketInfos
     - needSSL
     - cloudType
     - userId
     - certVerifyMode
     - certFingerprint

    """


    def __init__(self, url=None, accessKey=None, secretKey=None, bucketInfos=None, needSSL=None, cloudType=None, userId=None, certVerifyMode=2, certFingerprint=None,):
        self.url = url
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.bucketInfos = bucketInfos
        self.needSSL = needSSL
        self.cloudType = cloudType
        self.userId = userId
        self.certVerifyMode = certVerifyMode
        self.certFingerprint = certFingerprint

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
                    self.url = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.accessKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.secretKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.LIST:
                    self.bucketInfos = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.bucketInfos.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.BOOL:
                    self.needSSL = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.cloudType = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.userId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.certVerifyMode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.certFingerprint = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncCloudStorageInfo')
        if self.url is not None:
            oprot.writeFieldBegin('url', TType.STRING, 1)
            oprot.writeString(self.url.encode('utf-8') if sys.version_info[0] == 2 else self.url)
            oprot.writeFieldEnd()
        if self.accessKey is not None:
            oprot.writeFieldBegin('accessKey', TType.STRING, 2)
            oprot.writeString(self.accessKey.encode('utf-8') if sys.version_info[0] == 2 else self.accessKey)
            oprot.writeFieldEnd()
        if self.secretKey is not None:
            oprot.writeFieldBegin('secretKey', TType.STRING, 3)
            oprot.writeString(self.secretKey.encode('utf-8') if sys.version_info[0] == 2 else self.secretKey)
            oprot.writeFieldEnd()
        if self.bucketInfos is not None:
            oprot.writeFieldBegin('bucketInfos', TType.LIST, 4)
            oprot.writeListBegin(TType.STRING, len(self.bucketInfos))
            for iter6 in self.bucketInfos:
                oprot.writeString(iter6.encode('utf-8') if sys.version_info[0] == 2 else iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.needSSL is not None:
            oprot.writeFieldBegin('needSSL', TType.BOOL, 5)
            oprot.writeBool(self.needSSL)
            oprot.writeFieldEnd()
        if self.cloudType is not None:
            oprot.writeFieldBegin('cloudType', TType.STRING, 6)
            oprot.writeString(self.cloudType.encode('utf-8') if sys.version_info[0] == 2 else self.cloudType)
            oprot.writeFieldEnd()
        if self.userId is not None:
            oprot.writeFieldBegin('userId', TType.STRING, 7)
            oprot.writeString(self.userId.encode('utf-8') if sys.version_info[0] == 2 else self.userId)
            oprot.writeFieldEnd()
        if self.certVerifyMode is not None:
            oprot.writeFieldBegin('certVerifyMode', TType.I32, 8)
            oprot.writeI32(self.certVerifyMode)
            oprot.writeFieldEnd()
        if self.certFingerprint is not None:
            oprot.writeFieldBegin('certFingerprint', TType.STRING, 9)
            oprot.writeString(self.certFingerprint.encode('utf-8') if sys.version_info[0] == 2 else self.certFingerprint)
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


class ncCloudCertInfo(object):
    """
    ????????????

    Attributes:
     - content
     - status
     - fingerprint
     - issuedBy
     - issuedTo
     - startTime
     - endTime

    """


    def __init__(self, content=None, status=0, fingerprint=None, issuedBy=None, issuedTo=None, startTime=None, endTime=None,):
        self.content = content
        self.status = status
        self.fingerprint = fingerprint
        self.issuedBy = issuedBy
        self.issuedTo = issuedTo
        self.startTime = startTime
        self.endTime = endTime

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
                    self.content = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.status = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.fingerprint = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.issuedBy = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.issuedTo = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.startTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.endTime = iprot.readI64()
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
        oprot.writeStructBegin('ncCloudCertInfo')
        if self.content is not None:
            oprot.writeFieldBegin('content', TType.STRING, 1)
            oprot.writeString(self.content.encode('utf-8') if sys.version_info[0] == 2 else self.content)
            oprot.writeFieldEnd()
        if self.status is not None:
            oprot.writeFieldBegin('status', TType.I32, 2)
            oprot.writeI32(self.status)
            oprot.writeFieldEnd()
        if self.fingerprint is not None:
            oprot.writeFieldBegin('fingerprint', TType.STRING, 3)
            oprot.writeString(self.fingerprint.encode('utf-8') if sys.version_info[0] == 2 else self.fingerprint)
            oprot.writeFieldEnd()
        if self.issuedBy is not None:
            oprot.writeFieldBegin('issuedBy', TType.STRING, 4)
            oprot.writeString(self.issuedBy.encode('utf-8') if sys.version_info[0] == 2 else self.issuedBy)
            oprot.writeFieldEnd()
        if self.issuedTo is not None:
            oprot.writeFieldBegin('issuedTo', TType.STRING, 5)
            oprot.writeString(self.issuedTo.encode('utf-8') if sys.version_info[0] == 2 else self.issuedTo)
            oprot.writeFieldEnd()
        if self.startTime is not None:
            oprot.writeFieldBegin('startTime', TType.I64, 6)
            oprot.writeI64(self.startTime)
            oprot.writeFieldEnd()
        if self.endTime is not None:
            oprot.writeFieldBegin('endTime', TType.I64, 7)
            oprot.writeI64(self.endTime)
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


class ncTaskSetInfo(object):
    """
    D2D2C???????????????

    Attributes:
     - taskSetSign
     - taskSetName
     - mediaVip
     - isDeleted
     - taskSetId

    """


    def __init__(self, taskSetSign=None, taskSetName=None, mediaVip=None, isDeleted=None, taskSetId=None,):
        self.taskSetSign = taskSetSign
        self.taskSetName = taskSetName
        self.mediaVip = mediaVip
        self.isDeleted = isDeleted
        self.taskSetId = taskSetId

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
                    self.taskSetSign = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.taskSetName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.mediaVip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.isDeleted = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.taskSetId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncTaskSetInfo')
        if self.taskSetSign is not None:
            oprot.writeFieldBegin('taskSetSign', TType.STRING, 1)
            oprot.writeString(self.taskSetSign.encode('utf-8') if sys.version_info[0] == 2 else self.taskSetSign)
            oprot.writeFieldEnd()
        if self.taskSetName is not None:
            oprot.writeFieldBegin('taskSetName', TType.STRING, 2)
            oprot.writeString(self.taskSetName.encode('utf-8') if sys.version_info[0] == 2 else self.taskSetName)
            oprot.writeFieldEnd()
        if self.mediaVip is not None:
            oprot.writeFieldBegin('mediaVip', TType.STRING, 3)
            oprot.writeString(self.mediaVip.encode('utf-8') if sys.version_info[0] == 2 else self.mediaVip)
            oprot.writeFieldEnd()
        if self.isDeleted is not None:
            oprot.writeFieldBegin('isDeleted', TType.BOOL, 4)
            oprot.writeBool(self.isDeleted)
            oprot.writeFieldEnd()
        if self.taskSetId is not None:
            oprot.writeFieldBegin('taskSetId', TType.STRING, 5)
            oprot.writeString(self.taskSetId.encode('utf-8') if sys.version_info[0] == 2 else self.taskSetId)
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


class ncTaskSetInfoSet(object):
    """
    D2D2C?????????????????????

    Attributes:
     - infos
     - totalNum
     - requestId
     - finished

    """


    def __init__(self, infos=None, totalNum=None, requestId=None, finished=None,):
        self.infos = infos
        self.totalNum = totalNum
        self.requestId = requestId
        self.finished = finished

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
                    self.infos = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = ncTaskSetInfo()
                        _elem12.read(iprot)
                        self.infos.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.I32:
                    self.totalNum = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.BOOL:
                    self.finished = iprot.readBool()
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
        oprot.writeStructBegin('ncTaskSetInfoSet')
        if self.infos is not None:
            oprot.writeFieldBegin('infos', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.infos))
            for iter13 in self.infos:
                iter13.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.totalNum is not None:
            oprot.writeFieldBegin('totalNum', TType.I32, 2)
            oprot.writeI32(self.totalNum)
            oprot.writeFieldEnd()
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 3)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.finished is not None:
            oprot.writeFieldBegin('finished', TType.BOOL, 4)
            oprot.writeBool(self.finished)
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


class ncTaskSetRequest(object):
    """
    D2D2C?????????????????????

    Attributes:
     - requestId
     - index
     - count

    """


    def __init__(self, requestId=None, index=None, count=None,):
        self.requestId = requestId
        self.index = index
        self.count = count

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
                if ftype == TType.I64:
                    self.index = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.count = iprot.readI32()
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
        oprot.writeStructBegin('ncTaskSetRequest')
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 1)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
            oprot.writeFieldEnd()
        if self.index is not None:
            oprot.writeFieldBegin('index', TType.I64, 2)
            oprot.writeI64(self.index)
            oprot.writeFieldEnd()
        if self.count is not None:
            oprot.writeFieldBegin('count', TType.I32, 3)
            oprot.writeI32(self.count)
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


class ncBucketInfoReply(object):
    """
    Attributes:
     - finished
     - infos
     - requestId

    """


    def __init__(self, finished=None, infos=None, requestId=None,):
        self.finished = finished
        self.infos = infos
        self.requestId = requestId

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
                if ftype == TType.BOOL:
                    self.finished = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.infos = []
                    (_etype17, _size14) = iprot.readListBegin()
                    for _i18 in range(_size14):
                        _elem19 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.infos.append(_elem19)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.requestId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncBucketInfoReply')
        if self.finished is not None:
            oprot.writeFieldBegin('finished', TType.BOOL, 1)
            oprot.writeBool(self.finished)
            oprot.writeFieldEnd()
        if self.infos is not None:
            oprot.writeFieldBegin('infos', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.infos))
            for iter20 in self.infos:
                oprot.writeString(iter20.encode('utf-8') if sys.version_info[0] == 2 else iter20)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        if self.requestId is not None:
            oprot.writeFieldBegin('requestId', TType.STRING, 3)
            oprot.writeString(self.requestId.encode('utf-8') if sys.version_info[0] == 2 else self.requestId)
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
all_structs.append(ncEcssVolumeInfo)
ncEcssVolumeInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'volumePath', 'UTF8', None, ),  # 1
    (2, TType.I64, 'volumeTotalSize', None, None, ),  # 2
    (3, TType.I64, 'usedSize', None, None, ),  # 3
)
all_structs.append(ncBucketStatus)
ncBucketStatus.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'bucketName', 'UTF8', None, ),  # 1
    (2, TType.BOOL, 'isExists', None, True, ),  # 2
)
all_structs.append(ncCloudStorageInfo)
ncCloudStorageInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'url', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'accessKey', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'secretKey', 'UTF8', None, ),  # 3
    (4, TType.LIST, 'bucketInfos', (TType.STRING, 'UTF8', False), None, ),  # 4
    (5, TType.BOOL, 'needSSL', None, None, ),  # 5
    (6, TType.STRING, 'cloudType', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'userId', 'UTF8', None, ),  # 7
    (8, TType.I32, 'certVerifyMode', None, 2, ),  # 8
    (9, TType.STRING, 'certFingerprint', 'UTF8', None, ),  # 9
)
all_structs.append(ncCloudCertInfo)
ncCloudCertInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'content', 'UTF8', None, ),  # 1
    (2, TType.I32, 'status', None, 0, ),  # 2
    (3, TType.STRING, 'fingerprint', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'issuedBy', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'issuedTo', 'UTF8', None, ),  # 5
    (6, TType.I64, 'startTime', None, None, ),  # 6
    (7, TType.I64, 'endTime', None, None, ),  # 7
)
all_structs.append(ncTaskSetInfo)
ncTaskSetInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'taskSetSign', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'taskSetName', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'mediaVip', 'UTF8', None, ),  # 3
    (4, TType.BOOL, 'isDeleted', None, None, ),  # 4
    (5, TType.STRING, 'taskSetId', 'UTF8', None, ),  # 5
)
all_structs.append(ncTaskSetInfoSet)
ncTaskSetInfoSet.thrift_spec = (
    None,  # 0
    (1, TType.LIST, 'infos', (TType.STRUCT, [ncTaskSetInfo, None], False), None, ),  # 1
    (2, TType.I32, 'totalNum', None, None, ),  # 2
    (3, TType.STRING, 'requestId', 'UTF8', None, ),  # 3
    (4, TType.BOOL, 'finished', None, None, ),  # 4
)
all_structs.append(ncTaskSetRequest)
ncTaskSetRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'requestId', 'UTF8', None, ),  # 1
    (2, TType.I64, 'index', None, None, ),  # 2
    (3, TType.I32, 'count', None, None, ),  # 3
)
all_structs.append(ncBucketInfoReply)
ncBucketInfoReply.thrift_spec = (
    None,  # 0
    (1, TType.BOOL, 'finished', None, None, ),  # 1
    (2, TType.LIST, 'infos', (TType.STRING, 'UTF8', False), None, ),  # 2
    (3, TType.STRING, 'requestId', 'UTF8', None, ),  # 3
)
fix_spec(all_structs)
del all_structs
