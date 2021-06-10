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



class TapeQueryCond(object):
  """
  Attributes:
   - cond
  """

  thrift_spec = (
    None, # 0
    (1, TType.MAP, 'cond', (TType.STRING,None,TType.LIST,(TType.STRING,None)), None, ), # 1
  )

  def __init__(self, cond=None,):
    self.cond = cond

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
          self.cond = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString().decode('utf-8')
            _val6 = []
            (_etype10, _size7) = iprot.readListBegin()
            for _i11 in xrange(_size7):
              _elem12 = iprot.readString().decode('utf-8')
              _val6.append(_elem12)
            iprot.readListEnd()
            self.cond[_key5] = _val6
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
    oprot.writeStructBegin('TapeQueryCond')
    if self.cond is not None:
      oprot.writeFieldBegin('cond', TType.MAP, 1)
      oprot.writeMapBegin(TType.STRING, TType.LIST, len(self.cond))
      for kiter13,viter14 in self.cond.items():
        oprot.writeString(kiter13.encode('utf-8'))
        oprot.writeListBegin(TType.STRING, len(viter14))
        for iter15 in viter14:
          oprot.writeString(iter15.encode('utf-8'))
        oprot.writeListEnd()
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.cond)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeSetCycle(object):
  """
  Attributes:
   - cycleValue
   - cycleType
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'cycleValue', None, None, ), # 1
    (2, TType.I32, 'cycleType', None, None, ), # 2
  )

  def __init__(self, cycleValue=None, cycleType=None,):
    self.cycleValue = cycleValue
    self.cycleType = cycleType

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
          self.cycleValue = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.cycleType = iprot.readI32()
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
    oprot.writeStructBegin('TapeSetCycle')
    if self.cycleValue is not None:
      oprot.writeFieldBegin('cycleValue', TType.I32, 1)
      oprot.writeI32(self.cycleValue)
      oprot.writeFieldEnd()
    if self.cycleType is not None:
      oprot.writeFieldBegin('cycleType', TType.I32, 2)
      oprot.writeI32(self.cycleType)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.cycleValue)
    value = (value * 31) ^ hash(self.cycleType)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeSetInfo(object):
  """
  Attributes:
   - name
   - libName
   - libSerialNo
   - cycle
   - driveNum
   - createTime
   - modifyTime
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'libName', None, None, ), # 2
    (3, TType.STRING, 'libSerialNo', None, None, ), # 3
    (4, TType.STRUCT, 'cycle', (TapeSetCycle, TapeSetCycle.thrift_spec), None, ), # 4
    (5, TType.I32, 'driveNum', None, None, ), # 5
    (6, TType.STRING, 'createTime', None, None, ), # 6
    (7, TType.STRING, 'modifyTime', None, None, ), # 7
  )

  def __init__(self, name=None, libName=None, libSerialNo=None, cycle=None, driveNum=None, createTime=None, modifyTime=None,):
    self.name = name
    self.libName = libName
    self.libSerialNo = libSerialNo
    self.cycle = cycle
    self.driveNum = driveNum
    self.createTime = createTime
    self.modifyTime = modifyTime

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
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.libName = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.libSerialNo = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRUCT:
          self.cycle = TapeSetCycle()
          self.cycle.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.driveNum = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.createTime = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.modifyTime = iprot.readString().decode('utf-8')
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
    oprot.writeStructBegin('TapeSetInfo')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.libName is not None:
      oprot.writeFieldBegin('libName', TType.STRING, 2)
      oprot.writeString(self.libName.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.libSerialNo is not None:
      oprot.writeFieldBegin('libSerialNo', TType.STRING, 3)
      oprot.writeString(self.libSerialNo.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.cycle is not None:
      oprot.writeFieldBegin('cycle', TType.STRUCT, 4)
      self.cycle.write(oprot)
      oprot.writeFieldEnd()
    if self.driveNum is not None:
      oprot.writeFieldBegin('driveNum', TType.I32, 5)
      oprot.writeI32(self.driveNum)
      oprot.writeFieldEnd()
    if self.createTime is not None:
      oprot.writeFieldBegin('createTime', TType.STRING, 6)
      oprot.writeString(self.createTime.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.modifyTime is not None:
      oprot.writeFieldBegin('modifyTime', TType.STRING, 7)
      oprot.writeString(self.modifyTime.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.libName)
    value = (value * 31) ^ hash(self.libSerialNo)
    value = (value * 31) ^ hash(self.cycle)
    value = (value * 31) ^ hash(self.driveNum)
    value = (value * 31) ^ hash(self.createTime)
    value = (value * 31) ^ hash(self.modifyTime)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeSetInfoWeb(object):
  """
  Attributes:
   - totalNum
   - tapeSets
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'totalNum', None, None, ), # 1
    (2, TType.LIST, 'tapeSets', (TType.STRUCT,(TapeSetInfo, TapeSetInfo.thrift_spec)), None, ), # 2
  )

  def __init__(self, totalNum=None, tapeSets=None,):
    self.totalNum = totalNum
    self.tapeSets = tapeSets

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
          self.totalNum = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.tapeSets = []
          (_etype19, _size16) = iprot.readListBegin()
          for _i20 in xrange(_size16):
            _elem21 = TapeSetInfo()
            _elem21.read(iprot)
            self.tapeSets.append(_elem21)
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
    oprot.writeStructBegin('TapeSetInfoWeb')
    if self.totalNum is not None:
      oprot.writeFieldBegin('totalNum', TType.I32, 1)
      oprot.writeI32(self.totalNum)
      oprot.writeFieldEnd()
    if self.tapeSets is not None:
      oprot.writeFieldBegin('tapeSets', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.tapeSets))
      for iter22 in self.tapeSets:
        iter22.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.totalNum)
    value = (value * 31) ^ hash(self.tapeSets)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeInfo(object):
  """
  Attributes:
   - tapeLabel
   - location
   - hasData
   - usedSpace
   - lastWriteTime
   - tapeSetName
   - insideLib
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'tapeLabel', None, None, ), # 1
    (2, TType.STRING, 'location', None, None, ), # 2
    (3, TType.I16, 'hasData', None, None, ), # 3
    (4, TType.I64, 'usedSpace', None, None, ), # 4
    (5, TType.STRING, 'lastWriteTime', None, None, ), # 5
    (6, TType.STRING, 'tapeSetName', None, None, ), # 6
    (7, TType.I16, 'insideLib', None, None, ), # 7
  )

  def __init__(self, tapeLabel=None, location=None, hasData=None, usedSpace=None, lastWriteTime=None, tapeSetName=None, insideLib=None,):
    self.tapeLabel = tapeLabel
    self.location = location
    self.hasData = hasData
    self.usedSpace = usedSpace
    self.lastWriteTime = lastWriteTime
    self.tapeSetName = tapeSetName
    self.insideLib = insideLib

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
          self.tapeLabel = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.location = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.hasData = iprot.readI16()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.usedSpace = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.lastWriteTime = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.tapeSetName = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I16:
          self.insideLib = iprot.readI16()
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
    oprot.writeStructBegin('TapeInfo')
    if self.tapeLabel is not None:
      oprot.writeFieldBegin('tapeLabel', TType.STRING, 1)
      oprot.writeString(self.tapeLabel.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.location is not None:
      oprot.writeFieldBegin('location', TType.STRING, 2)
      oprot.writeString(self.location.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.hasData is not None:
      oprot.writeFieldBegin('hasData', TType.I16, 3)
      oprot.writeI16(self.hasData)
      oprot.writeFieldEnd()
    if self.usedSpace is not None:
      oprot.writeFieldBegin('usedSpace', TType.I64, 4)
      oprot.writeI64(self.usedSpace)
      oprot.writeFieldEnd()
    if self.lastWriteTime is not None:
      oprot.writeFieldBegin('lastWriteTime', TType.STRING, 5)
      oprot.writeString(self.lastWriteTime.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.tapeSetName is not None:
      oprot.writeFieldBegin('tapeSetName', TType.STRING, 6)
      oprot.writeString(self.tapeSetName.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.insideLib is not None:
      oprot.writeFieldBegin('insideLib', TType.I16, 7)
      oprot.writeI16(self.insideLib)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.tapeLabel)
    value = (value * 31) ^ hash(self.location)
    value = (value * 31) ^ hash(self.hasData)
    value = (value * 31) ^ hash(self.usedSpace)
    value = (value * 31) ^ hash(self.lastWriteTime)
    value = (value * 31) ^ hash(self.tapeSetName)
    value = (value * 31) ^ hash(self.insideLib)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeInfoWeb(object):
  """
  Attributes:
   - totalNum
   - tapes
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'totalNum', None, None, ), # 1
    (2, TType.LIST, 'tapes', (TType.STRUCT,(TapeInfo, TapeInfo.thrift_spec)), None, ), # 2
  )

  def __init__(self, totalNum=None, tapes=None,):
    self.totalNum = totalNum
    self.tapes = tapes

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
          self.totalNum = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.tapes = []
          (_etype26, _size23) = iprot.readListBegin()
          for _i27 in xrange(_size23):
            _elem28 = TapeInfo()
            _elem28.read(iprot)
            self.tapes.append(_elem28)
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
    oprot.writeStructBegin('TapeInfoWeb')
    if self.totalNum is not None:
      oprot.writeFieldBegin('totalNum', TType.I32, 1)
      oprot.writeI32(self.totalNum)
      oprot.writeFieldEnd()
    if self.tapes is not None:
      oprot.writeFieldBegin('tapes', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.tapes))
      for iter29 in self.tapes:
        iter29.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.totalNum)
    value = (value * 31) ^ hash(self.tapes)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeLibInfo(object):
  """
  Attributes:
   - name
   - serialNo
   - online
   - vendor
   - productID
   - driveNum
   - slotNum
   - accessPoint
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'serialNo', None, None, ), # 2
    (3, TType.I16, 'online', None, None, ), # 3
    (4, TType.STRING, 'vendor', None, None, ), # 4
    (5, TType.STRING, 'productID', None, None, ), # 5
    (6, TType.I32, 'driveNum', None, None, ), # 6
    (7, TType.I32, 'slotNum', None, None, ), # 7
    (8, TType.LIST, 'accessPoint', (TType.STRING,None), None, ), # 8
  )

  def __init__(self, name=None, serialNo=None, online=None, vendor=None, productID=None, driveNum=None, slotNum=None, accessPoint=None,):
    self.name = name
    self.serialNo = serialNo
    self.online = online
    self.vendor = vendor
    self.productID = productID
    self.driveNum = driveNum
    self.slotNum = slotNum
    self.accessPoint = accessPoint

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
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.serialNo = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.online = iprot.readI16()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.vendor = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.productID = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I32:
          self.driveNum = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.slotNum = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.LIST:
          self.accessPoint = []
          (_etype33, _size30) = iprot.readListBegin()
          for _i34 in xrange(_size30):
            _elem35 = iprot.readString().decode('utf-8')
            self.accessPoint.append(_elem35)
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
    oprot.writeStructBegin('TapeLibInfo')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.serialNo is not None:
      oprot.writeFieldBegin('serialNo', TType.STRING, 2)
      oprot.writeString(self.serialNo.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.online is not None:
      oprot.writeFieldBegin('online', TType.I16, 3)
      oprot.writeI16(self.online)
      oprot.writeFieldEnd()
    if self.vendor is not None:
      oprot.writeFieldBegin('vendor', TType.STRING, 4)
      oprot.writeString(self.vendor.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.productID is not None:
      oprot.writeFieldBegin('productID', TType.STRING, 5)
      oprot.writeString(self.productID.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.driveNum is not None:
      oprot.writeFieldBegin('driveNum', TType.I32, 6)
      oprot.writeI32(self.driveNum)
      oprot.writeFieldEnd()
    if self.slotNum is not None:
      oprot.writeFieldBegin('slotNum', TType.I32, 7)
      oprot.writeI32(self.slotNum)
      oprot.writeFieldEnd()
    if self.accessPoint is not None:
      oprot.writeFieldBegin('accessPoint', TType.LIST, 8)
      oprot.writeListBegin(TType.STRING, len(self.accessPoint))
      for iter36 in self.accessPoint:
        oprot.writeString(iter36.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.serialNo)
    value = (value * 31) ^ hash(self.online)
    value = (value * 31) ^ hash(self.vendor)
    value = (value * 31) ^ hash(self.productID)
    value = (value * 31) ^ hash(self.driveNum)
    value = (value * 31) ^ hash(self.slotNum)
    value = (value * 31) ^ hash(self.accessPoint)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeLibInfoWeb(object):
  """
  Attributes:
   - totalNum
   - tapeLibs
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'totalNum', None, None, ), # 1
    (2, TType.LIST, 'tapeLibs', (TType.STRUCT,(TapeLibInfo, TapeLibInfo.thrift_spec)), None, ), # 2
  )

  def __init__(self, totalNum=None, tapeLibs=None,):
    self.totalNum = totalNum
    self.tapeLibs = tapeLibs

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
          self.totalNum = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.tapeLibs = []
          (_etype40, _size37) = iprot.readListBegin()
          for _i41 in xrange(_size37):
            _elem42 = TapeLibInfo()
            _elem42.read(iprot)
            self.tapeLibs.append(_elem42)
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
    oprot.writeStructBegin('TapeLibInfoWeb')
    if self.totalNum is not None:
      oprot.writeFieldBegin('totalNum', TType.I32, 1)
      oprot.writeI32(self.totalNum)
      oprot.writeFieldEnd()
    if self.tapeLibs is not None:
      oprot.writeFieldBegin('tapeLibs', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.tapeLibs))
      for iter43 in self.tapeLibs:
        iter43.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.totalNum)
    value = (value * 31) ^ hash(self.tapeLibs)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeLibDrive(object):
  """
  Attributes:
   - serialNo
   - name
   - status
   - compress
   - protect
   - tapeLabel
   - slotID
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'serialNo', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.I32, 'status', None, None, ), # 3
    (4, TType.I16, 'compress', None, None, ), # 4
    (5, TType.I16, 'protect', None, None, ), # 5
    (6, TType.STRING, 'tapeLabel', None, None, ), # 6
    (7, TType.I32, 'slotID', None, None, ), # 7
  )

  def __init__(self, serialNo=None, name=None, status=None, compress=None, protect=None, tapeLabel=None, slotID=None,):
    self.serialNo = serialNo
    self.name = name
    self.status = status
    self.compress = compress
    self.protect = protect
    self.tapeLabel = tapeLabel
    self.slotID = slotID

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
          self.serialNo = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.status = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I16:
          self.compress = iprot.readI16()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I16:
          self.protect = iprot.readI16()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.tapeLabel = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.slotID = iprot.readI32()
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
    oprot.writeStructBegin('TapeLibDrive')
    if self.serialNo is not None:
      oprot.writeFieldBegin('serialNo', TType.STRING, 1)
      oprot.writeString(self.serialNo.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I32, 3)
      oprot.writeI32(self.status)
      oprot.writeFieldEnd()
    if self.compress is not None:
      oprot.writeFieldBegin('compress', TType.I16, 4)
      oprot.writeI16(self.compress)
      oprot.writeFieldEnd()
    if self.protect is not None:
      oprot.writeFieldBegin('protect', TType.I16, 5)
      oprot.writeI16(self.protect)
      oprot.writeFieldEnd()
    if self.tapeLabel is not None:
      oprot.writeFieldBegin('tapeLabel', TType.STRING, 6)
      oprot.writeString(self.tapeLabel.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.slotID is not None:
      oprot.writeFieldBegin('slotID', TType.I32, 7)
      oprot.writeI32(self.slotID)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.serialNo)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.compress)
    value = (value * 31) ^ hash(self.protect)
    value = (value * 31) ^ hash(self.tapeLabel)
    value = (value * 31) ^ hash(self.slotID)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeLibDriveWeb(object):
  """
  Attributes:
   - totalNum
   - tapeLibDrives
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'totalNum', None, None, ), # 1
    (2, TType.LIST, 'tapeLibDrives', (TType.STRUCT,(TapeLibDrive, TapeLibDrive.thrift_spec)), None, ), # 2
  )

  def __init__(self, totalNum=None, tapeLibDrives=None,):
    self.totalNum = totalNum
    self.tapeLibDrives = tapeLibDrives

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
          self.totalNum = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.tapeLibDrives = []
          (_etype47, _size44) = iprot.readListBegin()
          for _i48 in xrange(_size44):
            _elem49 = TapeLibDrive()
            _elem49.read(iprot)
            self.tapeLibDrives.append(_elem49)
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
    oprot.writeStructBegin('TapeLibDriveWeb')
    if self.totalNum is not None:
      oprot.writeFieldBegin('totalNum', TType.I32, 1)
      oprot.writeI32(self.totalNum)
      oprot.writeFieldEnd()
    if self.tapeLibDrives is not None:
      oprot.writeFieldBegin('tapeLibDrives', TType.LIST, 2)
      oprot.writeListBegin(TType.STRUCT, len(self.tapeLibDrives))
      for iter50 in self.tapeLibDrives:
        iter50.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.totalNum)
    value = (value * 31) ^ hash(self.tapeLibDrives)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TapeScanStatus(object):
  """
  Attributes:
   - beginTime
   - status
   - result
   - failureReason
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'beginTime', None, None, ), # 1
    (2, TType.I16, 'status', None, None, ), # 2
    (3, TType.I16, 'result', None, None, ), # 3
    (4, TType.STRING, 'failureReason', None, None, ), # 4
  )

  def __init__(self, beginTime=None, status=None, result=None, failureReason=None,):
    self.beginTime = beginTime
    self.status = status
    self.result = result
    self.failureReason = failureReason

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
          self.beginTime = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I16:
          self.status = iprot.readI16()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.result = iprot.readI16()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.failureReason = iprot.readString().decode('utf-8')
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
    oprot.writeStructBegin('TapeScanStatus')
    if self.beginTime is not None:
      oprot.writeFieldBegin('beginTime', TType.STRING, 1)
      oprot.writeString(self.beginTime.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.status is not None:
      oprot.writeFieldBegin('status', TType.I16, 2)
      oprot.writeI16(self.status)
      oprot.writeFieldEnd()
    if self.result is not None:
      oprot.writeFieldBegin('result', TType.I16, 3)
      oprot.writeI16(self.result)
      oprot.writeFieldEnd()
    if self.failureReason is not None:
      oprot.writeFieldBegin('failureReason', TType.STRING, 4)
      oprot.writeString(self.failureReason.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.beginTime)
    value = (value * 31) ^ hash(self.status)
    value = (value * 31) ^ hash(self.result)
    value = (value * 31) ^ hash(self.failureReason)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
