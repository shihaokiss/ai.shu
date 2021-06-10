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

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'attributes', (TType.STRING,None,TType.STRING,None), None, ), # 1
    (2, TType.MAP, 'infolists', (TType.STRING,None,TType.LIST,(TType.STRING,None)), None, ), # 2
  )

  def __init__(self, attributes=None, infolists=None,):
    self.attributes = attributes
    self.infolists = infolists

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
        if ftype == TType.MAP:
          self.attributes = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString().decode('utf-8')
            _val6 = iprot.readString().decode('utf-8')
            self.attributes[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.infolists = {}
          (_ktype8, _vtype9, _size7 ) = iprot.readMapBegin()
          for _i11 in xrange(_size7):
            _key12 = iprot.readString().decode('utf-8')
            _val13 = []
            (_etype17, _size14) = iprot.readListBegin()
            for _i18 in xrange(_size14):
              _elem19 = iprot.readString().decode('utf-8')
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
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ncOracleClientMetaInfo')
    if self.attributes is not None:
      oprot.writeFieldBegin('attributes', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.attributes))
      for kiter20,viter21 in self.attributes.items():
        oprot.writeString(kiter20.encode('utf-8'))
        oprot.writeString(viter21.encode('utf-8'))
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.infolists is not None:
      oprot.writeFieldBegin('infolists', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.LIST, len(self.infolists))
      for kiter22,viter23 in self.infolists.items():
        oprot.writeString(kiter22.encode('utf-8'))
        oprot.writeListBegin(TType.STRING, len(viter23))
        for iter24 in viter23:
          oprot.writeString(iter24.encode('utf-8'))
        oprot.writeListEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.attributes)
    value = (value * 31) ^ hash(self.infolists)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
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

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'version', None, None, ), # 1
    (2, TType.I32, 'clienttype', None, None, ), # 2
    (3, TType.LIST, 'metas', (TType.STRUCT,(ncOracleClientMetaInfo, ncOracleClientMetaInfo.thrift_spec)), None, ), # 3
  )

  def __init__(self, version=None, clienttype=None, metas=None,):
    self.version = version
    self.clienttype = clienttype
    self.metas = metas

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
          for _i29 in xrange(_size25):
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
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
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
      raise TProtocol.TProtocolException(message='Required field version is unset!')
    if self.clienttype is None:
      raise TProtocol.TProtocolException(message='Required field clienttype is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.version)
    value = (value * 31) ^ hash(self.clienttype)
    value = (value * 31) ^ hash(self.metas)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
