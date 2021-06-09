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
import ncScheTask_Var.ttypes
import ncCommonType_Var.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class ncJobInfo(object):
  """
  Attributes:
   - jobId
   - svcType
   - execType
   - depJobId
   - customer
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'jobId', None, None, ), # 1
    (2, TType.I32, 'svcType', None, None, ), # 2
    (3, TType.I32, 'execType', None, None, ), # 3
    (4, TType.STRING, 'depJobId', None, None, ), # 4
    (5, TType.STRING, 'customer', None, None, ), # 5
  )

  def __init__(self, jobId=None, svcType=None, execType=None, depJobId=None, customer=None,):
    self.jobId = jobId
    self.svcType = svcType
    self.execType = execType
    self.depJobId = depJobId
    self.customer = customer

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
          self.jobId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.svcType = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.execType = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.depJobId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.customer = iprot.readString().decode('utf-8')
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
    oprot.writeStructBegin('ncJobInfo')
    if self.jobId is not None:
      oprot.writeFieldBegin('jobId', TType.STRING, 1)
      oprot.writeString(self.jobId.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.svcType is not None:
      oprot.writeFieldBegin('svcType', TType.I32, 2)
      oprot.writeI32(self.svcType)
      oprot.writeFieldEnd()
    if self.execType is not None:
      oprot.writeFieldBegin('execType', TType.I32, 3)
      oprot.writeI32(self.execType)
      oprot.writeFieldEnd()
    if self.depJobId is not None:
      oprot.writeFieldBegin('depJobId', TType.STRING, 4)
      oprot.writeString(self.depJobId.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.customer is not None:
      oprot.writeFieldBegin('customer', TType.STRING, 5)
      oprot.writeString(self.customer.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.jobId)
    value = (value * 31) ^ hash(self.svcType)
    value = (value * 31) ^ hash(self.execType)
    value = (value * 31) ^ hash(self.depJobId)
    value = (value * 31) ^ hash(self.customer)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncScheExtendInfo(object):
  """
  Attributes:
   - scheDesc
   - scheCustomer
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'scheDesc', None, None, ), # 1
    (2, TType.STRING, 'scheCustomer', None, None, ), # 2
  )

  def __init__(self, scheDesc=None, scheCustomer=None,):
    self.scheDesc = scheDesc
    self.scheCustomer = scheCustomer

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
          self.scheDesc = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.scheCustomer = iprot.readString().decode('utf-8')
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
    oprot.writeStructBegin('ncScheExtendInfo')
    if self.scheDesc is not None:
      oprot.writeFieldBegin('scheDesc', TType.STRING, 1)
      oprot.writeString(self.scheDesc.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.scheCustomer is not None:
      oprot.writeFieldBegin('scheCustomer', TType.STRING, 2)
      oprot.writeString(self.scheCustomer.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.scheDesc)
    value = (value * 31) ^ hash(self.scheCustomer)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncTScheTaskInfo(object):
  """
  Attributes:
   - id
   - state
   - job
   - type
   - beignRunTime
   - nextRunTime
   - duration
   - frequency
   - params
   - mode
   - durationUnit
   - frequencyUnit
   - needInterval
   - nodeIp
   - nodeStatus
   - extendInfo
   - strategyId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.I32, 'state', None,     1, ), # 2
    (3, TType.STRUCT, 'job', (ncJobInfo, ncJobInfo.thrift_spec), None, ), # 3
    (4, TType.I32, 'type', None, None, ), # 4
    (5, TType.I64, 'beignRunTime', None, None, ), # 5
    (6, TType.I64, 'nextRunTime', None, None, ), # 6
    (7, TType.I64, 'duration', None, None, ), # 7
    (8, TType.I64, 'frequency', None, None, ), # 8
    (9, TType.LIST, 'params', (TType.I32,None), None, ), # 9
    (10, TType.I32, 'mode', None,     1, ), # 10
    (11, TType.I32, 'durationUnit', None, None, ), # 11
    (12, TType.I32, 'frequencyUnit', None, None, ), # 12
    (13, TType.I32, 'needInterval', None,     0, ), # 13
    (14, TType.STRING, 'nodeIp', None, None, ), # 14
    (15, TType.I32, 'nodeStatus', None,     1, ), # 15
    (16, TType.STRUCT, 'extendInfo', (ncScheExtendInfo, ncScheExtendInfo.thrift_spec), None, ), # 16
    (17, TType.STRING, 'strategyId', None, None, ), # 17
  )

  def __init__(self, id=None, state=thrift_spec[2][4], job=None, type=None, beignRunTime=None, nextRunTime=None, duration=None, frequency=None, params=None, mode=thrift_spec[10][4], durationUnit=None, frequencyUnit=None, needInterval=thrift_spec[13][4], nodeIp=None, nodeStatus=thrift_spec[15][4], extendInfo=None, strategyId=None,):
    self.id = id
    self.state = state
    self.job = job
    self.type = type
    self.beignRunTime = beignRunTime
    self.nextRunTime = nextRunTime
    self.duration = duration
    self.frequency = frequency
    self.params = params
    self.mode = mode
    self.durationUnit = durationUnit
    self.frequencyUnit = frequencyUnit
    self.needInterval = needInterval
    self.nodeIp = nodeIp
    self.nodeStatus = nodeStatus
    self.extendInfo = extendInfo
    self.strategyId = strategyId

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
          self.id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.state = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.job = ncJobInfo()
          self.job.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.type = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.beignRunTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.nextRunTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.duration = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.frequency = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.LIST:
          self.params = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readI32()
            self.params.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I32:
          self.mode = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I32:
          self.durationUnit = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I32:
          self.frequencyUnit = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.I32:
          self.needInterval = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.STRING:
          self.nodeIp = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.I32:
          self.nodeStatus = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 16:
        if ftype == TType.STRUCT:
          self.extendInfo = ncScheExtendInfo()
          self.extendInfo.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 17:
        if ftype == TType.STRING:
          self.strategyId = iprot.readString().decode('utf-8')
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
    oprot.writeStructBegin('ncTScheTaskInfo')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I32, 2)
      oprot.writeI32(self.state)
      oprot.writeFieldEnd()
    if self.job is not None:
      oprot.writeFieldBegin('job', TType.STRUCT, 3)
      self.job.write(oprot)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 4)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.beignRunTime is not None:
      oprot.writeFieldBegin('beignRunTime', TType.I64, 5)
      oprot.writeI64(self.beignRunTime)
      oprot.writeFieldEnd()
    if self.nextRunTime is not None:
      oprot.writeFieldBegin('nextRunTime', TType.I64, 6)
      oprot.writeI64(self.nextRunTime)
      oprot.writeFieldEnd()
    if self.duration is not None:
      oprot.writeFieldBegin('duration', TType.I64, 7)
      oprot.writeI64(self.duration)
      oprot.writeFieldEnd()
    if self.frequency is not None:
      oprot.writeFieldBegin('frequency', TType.I64, 8)
      oprot.writeI64(self.frequency)
      oprot.writeFieldEnd()
    if self.params is not None:
      oprot.writeFieldBegin('params', TType.LIST, 9)
      oprot.writeListBegin(TType.I32, len(self.params))
      for iter6 in self.params:
        oprot.writeI32(iter6)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.mode is not None:
      oprot.writeFieldBegin('mode', TType.I32, 10)
      oprot.writeI32(self.mode)
      oprot.writeFieldEnd()
    if self.durationUnit is not None:
      oprot.writeFieldBegin('durationUnit', TType.I32, 11)
      oprot.writeI32(self.durationUnit)
      oprot.writeFieldEnd()
    if self.frequencyUnit is not None:
      oprot.writeFieldBegin('frequencyUnit', TType.I32, 12)
      oprot.writeI32(self.frequencyUnit)
      oprot.writeFieldEnd()
    if self.needInterval is not None:
      oprot.writeFieldBegin('needInterval', TType.I32, 13)
      oprot.writeI32(self.needInterval)
      oprot.writeFieldEnd()
    if self.nodeIp is not None:
      oprot.writeFieldBegin('nodeIp', TType.STRING, 14)
      oprot.writeString(self.nodeIp.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.nodeStatus is not None:
      oprot.writeFieldBegin('nodeStatus', TType.I32, 15)
      oprot.writeI32(self.nodeStatus)
      oprot.writeFieldEnd()
    if self.extendInfo is not None:
      oprot.writeFieldBegin('extendInfo', TType.STRUCT, 16)
      self.extendInfo.write(oprot)
      oprot.writeFieldEnd()
    if self.strategyId is not None:
      oprot.writeFieldBegin('strategyId', TType.STRING, 17)
      oprot.writeString(self.strategyId.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.state)
    value = (value * 31) ^ hash(self.job)
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.beignRunTime)
    value = (value * 31) ^ hash(self.nextRunTime)
    value = (value * 31) ^ hash(self.duration)
    value = (value * 31) ^ hash(self.frequency)
    value = (value * 31) ^ hash(self.params)
    value = (value * 31) ^ hash(self.mode)
    value = (value * 31) ^ hash(self.durationUnit)
    value = (value * 31) ^ hash(self.frequencyUnit)
    value = (value * 31) ^ hash(self.needInterval)
    value = (value * 31) ^ hash(self.nodeIp)
    value = (value * 31) ^ hash(self.nodeStatus)
    value = (value * 31) ^ hash(self.extendInfo)
    value = (value * 31) ^ hash(self.strategyId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncTScheTaskInfoResult(object):
  """
  Attributes:
   - index
   - count
   - scheSet
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'index', None, None, ), # 1
    (2, TType.I32, 'count', None, None, ), # 2
    (3, TType.LIST, 'scheSet', (TType.STRUCT,(ncTScheTaskInfo, ncTScheTaskInfo.thrift_spec)), None, ), # 3
  )

  def __init__(self, index=None, count=None, scheSet=None,):
    self.index = index
    self.count = count
    self.scheSet = scheSet

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
          self.index = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.count = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.scheSet = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = ncTScheTaskInfo()
            _elem12.read(iprot)
            self.scheSet.append(_elem12)
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
    oprot.writeStructBegin('ncTScheTaskInfoResult')
    if self.index is not None:
      oprot.writeFieldBegin('index', TType.I32, 1)
      oprot.writeI32(self.index)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I32, 2)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    if self.scheSet is not None:
      oprot.writeFieldBegin('scheSet', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.scheSet))
      for iter13 in self.scheSet:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.index)
    value = (value * 31) ^ hash(self.count)
    value = (value * 31) ^ hash(self.scheSet)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncTScheTaskResult(object):
  """
  Attributes:
   - id
   - state
   - job
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.I32, 'state', None, None, ), # 2
    (3, TType.STRUCT, 'job', (ncJobInfo, ncJobInfo.thrift_spec), None, ), # 3
  )

  def __init__(self, id=None, state=None, job=None,):
    self.id = id
    self.state = state
    self.job = job

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
          self.id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.state = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.job = ncJobInfo()
          self.job.read(iprot)
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
    oprot.writeStructBegin('ncTScheTaskResult')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I32, 2)
      oprot.writeI32(self.state)
      oprot.writeFieldEnd()
    if self.job is not None:
      oprot.writeFieldBegin('job', TType.STRUCT, 3)
      self.job.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.state)
    value = (value * 31) ^ hash(self.job)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncNextSche(object):
  """
  Attributes:
   - jobId
   - svcType
   - scheCount
   - nextRunTime
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'jobId', None, None, ), # 1
    (2, TType.I32, 'svcType', None, None, ), # 2
    (3, TType.I64, 'scheCount', None, None, ), # 3
    (4, TType.I64, 'nextRunTime', None, None, ), # 4
  )

  def __init__(self, jobId=None, svcType=None, scheCount=None, nextRunTime=None,):
    self.jobId = jobId
    self.svcType = svcType
    self.scheCount = scheCount
    self.nextRunTime = nextRunTime

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
          self.jobId = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.svcType = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.scheCount = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.nextRunTime = iprot.readI64()
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
    oprot.writeStructBegin('ncNextSche')
    if self.jobId is not None:
      oprot.writeFieldBegin('jobId', TType.STRING, 1)
      oprot.writeString(self.jobId.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.svcType is not None:
      oprot.writeFieldBegin('svcType', TType.I32, 2)
      oprot.writeI32(self.svcType)
      oprot.writeFieldEnd()
    if self.scheCount is not None:
      oprot.writeFieldBegin('scheCount', TType.I64, 3)
      oprot.writeI64(self.scheCount)
      oprot.writeFieldEnd()
    if self.nextRunTime is not None:
      oprot.writeFieldBegin('nextRunTime', TType.I64, 4)
      oprot.writeI64(self.nextRunTime)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.jobId)
    value = (value * 31) ^ hash(self.svcType)
    value = (value * 31) ^ hash(self.scheCount)
    value = (value * 31) ^ hash(self.nextRunTime)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncNextScheResult(object):
  """
  Attributes:
   - sches
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'sches', (TType.STRUCT,(ncNextSche, ncNextSche.thrift_spec)), None, ), # 1
  )

  def __init__(self, sches=None,):
    self.sches = sches

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
          self.sches = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = ncNextSche()
            _elem19.read(iprot)
            self.sches.append(_elem19)
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
    oprot.writeStructBegin('ncNextScheResult')
    if self.sches is not None:
      oprot.writeFieldBegin('sches', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.sches))
      for iter20 in self.sches:
        iter20.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.sches)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ncScheTaskInfo(object):
  """
  Attributes:
   - id
   - state
   - job
   - type
   - beignRunTime
   - nextRunTime
   - duration
   - frequency
   - params
   - mode
   - durationUnit
   - frequencyUnit
   - needInterval
   - nodeIp
   - nodeStatus
   - extendInfo
   - strategyId
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.I32, 'state', None,     1, ), # 2
    (3, TType.STRUCT, 'job', (ncJobInfo, ncJobInfo.thrift_spec), None, ), # 3
    (4, TType.I32, 'type', None, None, ), # 4
    (5, TType.I64, 'beignRunTime', None, None, ), # 5
    (6, TType.I64, 'nextRunTime', None, None, ), # 6
    (7, TType.I64, 'duration', None, None, ), # 7
    (8, TType.I64, 'frequency', None, None, ), # 8
    (9, TType.STRING, 'params', None, None, ), # 9
    (10, TType.I32, 'mode', None,     1, ), # 10
    (11, TType.I32, 'durationUnit', None, None, ), # 11
    (12, TType.I32, 'frequencyUnit', None, None, ), # 12
    (13, TType.I32, 'needInterval', None,     0, ), # 13
    (14, TType.STRING, 'nodeIp', None, None, ), # 14
    (15, TType.I32, 'nodeStatus', None,     1, ), # 15
    (16, TType.STRUCT, 'extendInfo', (ncScheExtendInfo, ncScheExtendInfo.thrift_spec), None, ), # 16
    (17, TType.STRING, 'strategyId', None, None, ), # 17
  )

  def __init__(self, id=None, state=thrift_spec[2][4], job=None, type=None, beignRunTime=None, nextRunTime=None, duration=None, frequency=None, params=None, mode=thrift_spec[10][4], durationUnit=None, frequencyUnit=None, needInterval=thrift_spec[13][4], nodeIp=None, nodeStatus=thrift_spec[15][4], extendInfo=None, strategyId=None,):
    self.id = id
    self.state = state
    self.job = job
    self.type = type
    self.beignRunTime = beignRunTime
    self.nextRunTime = nextRunTime
    self.duration = duration
    self.frequency = frequency
    self.params = params
    self.mode = mode
    self.durationUnit = durationUnit
    self.frequencyUnit = frequencyUnit
    self.needInterval = needInterval
    self.nodeIp = nodeIp
    self.nodeStatus = nodeStatus
    self.extendInfo = extendInfo
    self.strategyId = strategyId

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
          self.id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.state = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.job = ncJobInfo()
          self.job.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.type = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.beignRunTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.nextRunTime = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I64:
          self.duration = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.I64:
          self.frequency = iprot.readI64()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.params = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I32:
          self.mode = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.I32:
          self.durationUnit = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.I32:
          self.frequencyUnit = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.I32:
          self.needInterval = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.STRING:
          self.nodeIp = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.I32:
          self.nodeStatus = iprot.readI32()
        else:
          iprot.skip(ftype)
      elif fid == 16:
        if ftype == TType.STRUCT:
          self.extendInfo = ncScheExtendInfo()
          self.extendInfo.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 17:
        if ftype == TType.STRING:
          self.strategyId = iprot.readString().decode('utf-8')
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
    oprot.writeStructBegin('ncScheTaskInfo')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.state is not None:
      oprot.writeFieldBegin('state', TType.I32, 2)
      oprot.writeI32(self.state)
      oprot.writeFieldEnd()
    if self.job is not None:
      oprot.writeFieldBegin('job', TType.STRUCT, 3)
      self.job.write(oprot)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 4)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.beignRunTime is not None:
      oprot.writeFieldBegin('beignRunTime', TType.I64, 5)
      oprot.writeI64(self.beignRunTime)
      oprot.writeFieldEnd()
    if self.nextRunTime is not None:
      oprot.writeFieldBegin('nextRunTime', TType.I64, 6)
      oprot.writeI64(self.nextRunTime)
      oprot.writeFieldEnd()
    if self.duration is not None:
      oprot.writeFieldBegin('duration', TType.I64, 7)
      oprot.writeI64(self.duration)
      oprot.writeFieldEnd()
    if self.frequency is not None:
      oprot.writeFieldBegin('frequency', TType.I64, 8)
      oprot.writeI64(self.frequency)
      oprot.writeFieldEnd()
    if self.params is not None:
      oprot.writeFieldBegin('params', TType.STRING, 9)
      oprot.writeString(self.params.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.mode is not None:
      oprot.writeFieldBegin('mode', TType.I32, 10)
      oprot.writeI32(self.mode)
      oprot.writeFieldEnd()
    if self.durationUnit is not None:
      oprot.writeFieldBegin('durationUnit', TType.I32, 11)
      oprot.writeI32(self.durationUnit)
      oprot.writeFieldEnd()
    if self.frequencyUnit is not None:
      oprot.writeFieldBegin('frequencyUnit', TType.I32, 12)
      oprot.writeI32(self.frequencyUnit)
      oprot.writeFieldEnd()
    if self.needInterval is not None:
      oprot.writeFieldBegin('needInterval', TType.I32, 13)
      oprot.writeI32(self.needInterval)
      oprot.writeFieldEnd()
    if self.nodeIp is not None:
      oprot.writeFieldBegin('nodeIp', TType.STRING, 14)
      oprot.writeString(self.nodeIp.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.nodeStatus is not None:
      oprot.writeFieldBegin('nodeStatus', TType.I32, 15)
      oprot.writeI32(self.nodeStatus)
      oprot.writeFieldEnd()
    if self.extendInfo is not None:
      oprot.writeFieldBegin('extendInfo', TType.STRUCT, 16)
      self.extendInfo.write(oprot)
      oprot.writeFieldEnd()
    if self.strategyId is not None:
      oprot.writeFieldBegin('strategyId', TType.STRING, 17)
      oprot.writeString(self.strategyId.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.id)
    value = (value * 31) ^ hash(self.state)
    value = (value * 31) ^ hash(self.job)
    value = (value * 31) ^ hash(self.type)
    value = (value * 31) ^ hash(self.beignRunTime)
    value = (value * 31) ^ hash(self.nextRunTime)
    value = (value * 31) ^ hash(self.duration)
    value = (value * 31) ^ hash(self.frequency)
    value = (value * 31) ^ hash(self.params)
    value = (value * 31) ^ hash(self.mode)
    value = (value * 31) ^ hash(self.durationUnit)
    value = (value * 31) ^ hash(self.frequencyUnit)
    value = (value * 31) ^ hash(self.needInterval)
    value = (value * 31) ^ hash(self.nodeIp)
    value = (value * 31) ^ hash(self.nodeStatus)
    value = (value * 31) ^ hash(self.extendInfo)
    value = (value * 31) ^ hash(self.strategyId)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
