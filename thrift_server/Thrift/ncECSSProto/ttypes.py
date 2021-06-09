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



class ncCloudStorageInfo(object):
  """
  Attributes:
   - venderType
   - url
   - accessKey
   - secret
   - bucket
   - appid
   - storageId
   - backupSize
   - restoreSize
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'venderType', None, None, ), # 1
    (2, TType.STRING, 'url', None, None, ), # 2
    (3, TType.STRING, 'accessKey', None, None, ), # 3
    (4, TType.STRING, 'secret', None, None, ), # 4
    (5, TType.STRING, 'bucket', None, None, ), # 5
    (6, TType.I32, 'appid', None, None, ), # 6
    (7, TType.I64, 'storageId', None, None, ), # 7
    (8, TType.I64, 'backupSize', None, None, ), # 8
    (9, TType.I64, 'restoreSize', None, None, ), # 9
  )

  def __init__(self, venderType=None, url=None, accessKey=None, secret=None, bucket=None, appid=None, storageId=None, backupSize=None, restoreSize=None,):
    self.venderType = venderType
    self.url = url
    self.accessKey = accessKey
    self.secret = secret
    self.bucket = bucket
    self.appid = appid
    self.storageId = storageId
    self.backupSize = backupSize
    self.restoreSize = restoreSize

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
        if ftype == TType.STRING:
          self.venderType = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.url = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.accessKey = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.secret = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.bucket = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.appid = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.storageId = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.backupSize = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I64:
          self.restoreSize = iprot.readI64()
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
    oprot.writeStructBegin('ncCloudStorageInfo')
    if self.venderType is not None:
      oprot.writeFieldBegin('venderType', TType.STRING, 1)
      oprot.writeString(self.venderType.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.url is not None:
      oprot.writeFieldBegin('url', TType.STRING, 2)
      oprot.writeString(self.url.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.accessKey is not None:
      oprot.writeFieldBegin('accessKey', TType.STRING, 3)
      oprot.writeString(self.accessKey.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.secret is not None:
      oprot.writeFieldBegin('secret', TType.STRING, 4)
      oprot.writeString(self.secret.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.bucket is not None:
      oprot.writeFieldBegin('bucket', TType.STRING, 5)
      oprot.writeString(self.bucket.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.appid is not None:
      oprot.writeFieldBegin('appid', TType.I32, 6)
      oprot.writeI32(self.appid)
      oprot.writeFieldEnd()
    if self.storageId is not None:
      oprot.writeFieldBegin('storageId', TType.I64, 7)
      oprot.writeI64(self.storageId)
      oprot.writeFieldEnd()
    if self.backupSize is not None:
      oprot.writeFieldBegin('backupSize', TType.I64, 8)
      oprot.writeI64(self.backupSize)
      oprot.writeFieldEnd()
    if self.restoreSize is not None:
      oprot.writeFieldBegin('restoreSize', TType.I64, 9)
      oprot.writeI64(self.restoreSize)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.venderType)
    value = (value * 31) ^ hash(self.url)
    value = (value * 31) ^ hash(self.accessKey)
    value = (value * 31) ^ hash(self.secret)
    value = (value * 31) ^ hash(self.bucket)
    value = (value * 31) ^ hash(self.appid)
    value = (value * 31) ^ hash(self.storageId)
    value = (value * 31) ^ hash(self.backupSize)
    value = (value * 31) ^ hash(self.restoreSize)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncChunkInfo(object):
  """
  Attributes:
   - chunkId
   - dataFileId
   - dataFileOffset
   - chunkLength
   - isDelete
   - checksum
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'chunkId', None, None, ), # 1
    (2, TType.I64, 'dataFileId', None, None, ), # 2
    (3, TType.I32, 'dataFileOffset', None, None, ), # 3
    (4, TType.I32, 'chunkLength', None, None, ), # 4
    (5, TType.I32, 'isDelete', None, None, ), # 5
    (6, TType.I32, 'checksum', None, None, ), # 6
  )

  def __init__(self, chunkId=None, dataFileId=None, dataFileOffset=None, chunkLength=None, isDelete=None, checksum=None,):
    self.chunkId = chunkId
    self.dataFileId = dataFileId
    self.dataFileOffset = dataFileOffset
    self.chunkLength = chunkLength
    self.isDelete = isDelete
    self.checksum = checksum

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
          self.chunkId = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.dataFileId = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.dataFileOffset = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.chunkLength = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.isDelete = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.checksum = iprot.readI32()
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
    oprot.writeStructBegin('ncChunkInfo')
    if self.chunkId is not None:
      oprot.writeFieldBegin('chunkId', TType.I64, 1)
      oprot.writeI64(self.chunkId)
      oprot.writeFieldEnd()
    if self.dataFileId is not None:
      oprot.writeFieldBegin('dataFileId', TType.I64, 2)
      oprot.writeI64(self.dataFileId)
      oprot.writeFieldEnd()
    if self.dataFileOffset is not None:
      oprot.writeFieldBegin('dataFileOffset', TType.I32, 3)
      oprot.writeI32(self.dataFileOffset)
      oprot.writeFieldEnd()
    if self.chunkLength is not None:
      oprot.writeFieldBegin('chunkLength', TType.I32, 4)
      oprot.writeI32(self.chunkLength)
      oprot.writeFieldEnd()
    if self.isDelete is not None:
      oprot.writeFieldBegin('isDelete', TType.I32, 5)
      oprot.writeI32(self.isDelete)
      oprot.writeFieldEnd()
    if self.checksum is not None:
      oprot.writeFieldBegin('checksum', TType.I32, 6)
      oprot.writeI32(self.checksum)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.chunkId)
    value = (value * 31) ^ hash(self.dataFileId)
    value = (value * 31) ^ hash(self.dataFileOffset)
    value = (value * 31) ^ hash(self.chunkLength)
    value = (value * 31) ^ hash(self.isDelete)
    value = (value * 31) ^ hash(self.checksum)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncKeyVaule(object):
  """
  Attributes:
   - key
   - value
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'key', None, None, ), # 1
    (2, TType.STRING, 'value', None, None, ), # 2
  )

  def __init__(self, key=None, value=None,):
    self.key = key
    self.value = value

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
        if ftype == TType.STRING:
          self.key = iprot.readString()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.value = iprot.readString()
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
    oprot.writeStructBegin('ncKeyVaule')
    if self.key is not None:
      oprot.writeFieldBegin('key', TType.STRING, 1)
      oprot.writeString(self.key)
      oprot.writeFieldEnd()
    if self.value is not None:
      oprot.writeFieldBegin('value', TType.STRING, 2)
      oprot.writeString(self.value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.key)
    value = (value * 31) ^ hash(self.value)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncKeyVauleArray(object):
  """
  Attributes:
   - kvArr
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'kvArr', (TType.STRUCT,(ncKeyVaule, ncKeyVaule.thrift_spec)), None, ), # 1
  )

  def __init__(self, kvArr=None,):
    self.kvArr = kvArr

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
        if ftype == TType.LIST:
          self.kvArr = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = ncKeyVaule()
            _elem5.read(iprot)
            self.kvArr.append(_elem5)
          iprot.readListEnd()
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
    oprot.writeStructBegin('ncKeyVauleArray')
    if self.kvArr is not None:
      oprot.writeFieldBegin('kvArr', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.kvArr))
      for iter6 in self.kvArr:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.kvArr)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)