#
# -*- coding:utf-8 -*-
#
# Autogenerated by Thrift Compiler (1.0.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:coding=utf-8,new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class ncCloudStorage(object):
  """
  Attributes:
   - createTime
   - updateTtime
   - deleteTime
   - isDeleted
   - creatorId
   - name
   - cloudType
   - indexBucket
   - stgBucket
   - backupData
   - restoreData
   - status
   - ip
   - hostId
   - password
   - needSSL
   - description
   - usernames
   - cloudId
   - useType
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'createTime', None, None, ), # 1
    (2, TType.I64, 'updateTtime', None, None, ), # 2
    (3, TType.I64, 'deleteTime', None, None, ), # 3
    (4, TType.BOOL, 'isDeleted', None, None, ), # 4
    (5, TType.STRING, 'creatorId', None, None, ), # 5
    (6, TType.STRING, 'name', None, None, ), # 6
    (7, TType.I32, 'cloudType', None, None, ), # 7
    (8, TType.STRING, 'indexBucket', None, None, ), # 8
    (9, TType.STRING, 'stgBucket', None, None, ), # 9
    (10, TType.DOUBLE, 'backupData', None, None, ), # 10
    (11, TType.DOUBLE, 'restoreData', None, None, ), # 11
    (12, TType.I32, 'status', None, None, ), # 12
    (13, TType.STRING, 'ip', None, None, ), # 13
    (14, TType.STRING, 'hostId', None, None, ), # 14
    (15, TType.STRING, 'password', None, None, ), # 15
    (16, TType.BOOL, 'needSSL', None, None, ), # 16
    (17, TType.STRING, 'description', None, None, ), # 17
    (18, TType.LIST, 'usernames', (TType.STRING,None), None, ), # 18
    (19, TType.STRING, 'cloudId', None, None, ), # 19
    (20, TType.I32, 'useType', None, None, ), # 20
  )

  def __init__(self, createTime=None, updateTtime=None, deleteTime=None, isDeleted=None, creatorId=None, name=None, cloudType=None, indexBucket=None, stgBucket=None, backupData=None, restoreData=None, status=None, ip=None, hostId=None, password=None, needSSL=None, description=None, usernames=None, cloudId=None, useType=None,):
    self.createTime = createTime
    self.updateTtime = updateTtime
    self.deleteTime = deleteTime
    self.isDeleted = isDeleted
    self.creatorId = creatorId
    self.name = name
    self.cloudType = cloudType
    self.indexBucket = indexBucket
    self.stgBucket = stgBucket
    self.backupData = backupData
    self.restoreData = restoreData
    self.status = status
    self.ip = ip
    self.hostId = hostId
    self.password = password
    self.needSSL = needSSL
    self.description = description
    self.usernames = usernames
    self.cloudId = cloudId
    self.useType = useType

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.createTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.updateTtime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.deleteTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.BOOL:
          self.isDeleted = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.creatorId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.cloudType = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.indexBucket = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.stgBucket = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.DOUBLE:
          self.backupData = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.DOUBLE:
          self.restoreData = iprot.readDouble()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I32:
          self.status = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.STRING:
          self.ip = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.STRING:
          self.hostId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.STRING:
          self.password = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 16:
        if ftype == TType.BOOL:
          self.needSSL = iprot.readBool()
        else:
          iprot.skip(ftype)
      elif fid == 17:
        if ftype == TType.STRING:
          self.description = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 18:
        if ftype == TType.LIST:
          self.usernames = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readString().decode('utf-8')
            self.usernames.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 19:
        if ftype == TType.STRING:
          self.cloudId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 20:
        if ftype == TType.I32:
          self.useType = iprot.readI32()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ncCloudStorage')
    if self.createTime is not None:
      oprot.writeFieldBegin('createTime', TType.I64, 1)
      oprot.writeI64(self.createTime)
      oprot.writeFieldEnd()
    if self.updateTtime is not None:
      oprot.writeFieldBegin('updateTtime', TType.I64, 2)
      oprot.writeI64(self.updateTtime)
      oprot.writeFieldEnd()
    if self.deleteTime is not None:
      oprot.writeFieldBegin('deleteTime', TType.I64, 3)
      oprot.writeI64(self.deleteTime)
      oprot.writeFieldEnd()
    if self.isDeleted is not None:
      oprot.writeFieldBegin('isDeleted', TType.BOOL, 4)
      oprot.writeBool(self.isDeleted)
      oprot.writeFieldEnd()
    if self.creatorId is not None:
      oprot.writeFieldBegin('creatorId', TType.STRING, 5)
      oprot.writeString(self.creatorId.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 6)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.cloudType is not None:
      oprot.writeFieldBegin('cloudType', TType.I32, 7)
      oprot.writeI32(self.cloudType)
      oprot.writeFieldEnd()
    if self.indexBucket is not None:
      oprot.writeFieldBegin('indexBucket', TType.STRING, 8)
      oprot.writeString(self.indexBucket.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.stgBucket is not None:
      oprot.writeFieldBegin('stgBucket', TType.STRING, 9)
      oprot.writeString(self.stgBucket.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.backupData is not None:
      oprot.writeFieldBegin('backupData', TType.DOUBLE, 10)
      oprot.writeDouble(self.backupData)
      oprot.writeFieldEnd()
    if self.restoreData is not None:
      oprot.writeFieldBegin('restoreData', TType.DOUBLE, 11)
      oprot.writeDouble(self.restoreData)
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I32, 12)
      oprot.writeI32(self.status)
      oprot.writeFieldEnd()
    if self.ip is not None:
      oprot.writeFieldBegin('ip', TType.STRING, 13)
      oprot.writeString(self.ip.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.hostId is not None:
      oprot.writeFieldBegin('hostId', TType.STRING, 14)
      oprot.writeString(self.hostId.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.password is not None:
      oprot.writeFieldBegin('password', TType.STRING, 15)
      oprot.writeString(self.password.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.needSSL is not None:
      oprot.writeFieldBegin('needSSL', TType.BOOL, 16)
      oprot.writeBool(self.needSSL)
      oprot.writeFieldEnd()
    if self.description is not None:
      oprot.writeFieldBegin('description', TType.STRING, 17)
      oprot.writeString(self.description.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.usernames is not None:
      oprot.writeFieldBegin('usernames', TType.LIST, 18)
      oprot.writeListBegin(TType.STRING, len(self.usernames))
      for iter6 in self.usernames:
        oprot.writeString(iter6.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.cloudId is not None:
      oprot.writeFieldBegin('cloudId', TType.STRING, 19)
      oprot.writeString(self.cloudId.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.useType is not None:
      oprot.writeFieldBegin('useType', TType.I32, 20)
      oprot.writeI32(self.useType)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.createTime)
    value = (value * 31) ^ hash(self.updateTtime)
    value = (value * 31) ^ hash(self.deleteTime)
    value = (value * 31) ^ hash(self.isDeleted)
    value = (value * 31) ^ hash(self.creatorId)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.cloudType)
    value = (value * 31) ^ hash(self.indexBucket)
    value = (value * 31) ^ hash(self.stgBucket)
    value = (value * 31) ^ hash(self.backupData)
    value = (value * 31) ^ hash(self.restoreData)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.ip)
    value = (value * 31) ^ hash(self.hostId)
    value = (value * 31) ^ hash(self.password)
    value = (value * 31) ^ hash(self.needSSL)
    value = (value * 31) ^ hash(self.description)
    value = (value * 31) ^ hash(self.usernames)
    value = (value * 31) ^ hash(self.cloudId)
    value = (value * 31) ^ hash(self.useType)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
