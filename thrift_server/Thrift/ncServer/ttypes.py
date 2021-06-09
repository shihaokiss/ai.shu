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


class ncServerStatus(object):
  OFFLINE = 0
  ONLINE = 1

  _VALUES_TO_NAMES = {
    0: "OFFLINE",
    1: "ONLINE",
  }

  _NAMES_TO_VALUES = {
    "OFFLINE": 0,
    "ONLINE": 1,
  }


class ncServer(object):
  """
  Attributes:
   - ip
   - mac
   - status
   - version
   - ipv6
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'ip', None, None, ), # 1
    (2, TType.STRING, 'mac', None, None, ), # 2
    (3, TType.I32, 'status', None, None, ), # 3
    (4, TType.STRING, 'version', None, None, ), # 4
    (5, TType.STRING, 'ipv6', None, None, ), # 5
  )

  def __init__(self, ip=None, mac=None, status=None, version=None, ipv6=None,):
    self.ip = ip
    self.mac = mac
    self.status = status
    self.version = version
    self.ipv6 = ipv6

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
          self.ip = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.mac = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.status = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.version = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.ipv6 = iprot.readString().decode('utf-8')
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
    oprot.writeStructBegin('ncServer')
    if self.ip is not None:
      oprot.writeFieldBegin('ip', TType.STRING, 1)
      oprot.writeString(self.ip.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.mac is not None:
      oprot.writeFieldBegin('mac', TType.STRING, 2)
      oprot.writeString(self.mac.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I32, 3)
      oprot.writeI32(self.status)
      oprot.writeFieldEnd()
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.STRING, 4)
      oprot.writeString(self.version.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.ipv6 is not None:
      oprot.writeFieldBegin('ipv6', TType.STRING, 5)
      oprot.writeString(self.ipv6.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.ip)
    value = (value * 31) ^ hash(self.mac)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.version)
    value = (value * 31) ^ hash(self.ipv6)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncGetServerRequest(object):
  """
  Attributes:
   - ip
   - mac
   - status
   - version
   - deleted
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'ip', None, None, ), # 1
    (2, TType.STRING, 'mac', None, None, ), # 2
    (3, TType.I32, 'status', None, None, ), # 3
    (4, TType.STRING, 'version', None, None, ), # 4
    (5, TType.BOOL, 'deleted', None, False, ), # 5
  )

  def __init__(self, ip=None, mac=None, status=None, version=None, deleted=thrift_spec[5][4],):
    self.ip = ip
    self.mac = mac
    self.status = status
    self.version = version
    self.deleted = deleted

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
          self.ip = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.mac = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.status = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.version = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.BOOL:
          self.deleted = iprot.readBool()
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
    oprot.writeStructBegin('ncGetServerRequest')
    if self.ip is not None:
      oprot.writeFieldBegin('ip', TType.STRING, 1)
      oprot.writeString(self.ip.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.mac is not None:
      oprot.writeFieldBegin('mac', TType.STRING, 2)
      oprot.writeString(self.mac.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I32, 3)
      oprot.writeI32(self.status)
      oprot.writeFieldEnd()
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.STRING, 4)
      oprot.writeString(self.version.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.deleted is not None:
      oprot.writeFieldBegin('deleted', TType.BOOL, 5)
      oprot.writeBool(self.deleted)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.ip)
    value = (value * 31) ^ hash(self.mac)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.version)
    value = (value * 31) ^ hash(self.deleted)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)