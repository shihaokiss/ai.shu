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


class ncVolumeMappingRequest(object):
    """
    Attributes:
     - volume_uuid
     - volume_config
     - volume_wwn
     - volume_type
     - fabric_type
     - storage_object_name
     - target_wwn
     - host_wwn
     - device_ip
     - server_lun_index
     - host_lun_index
     - network_portal_ip
     - network_portal_port
     - volume_lun_id
     - volume_size
     - link_id
     - client_id
     - server_id
     - data_transfe_ip

    """


    def __init__(self, volume_uuid=None, volume_config=None, volume_wwn=None, volume_type=None, fabric_type=None, storage_object_name=None, target_wwn=None, host_wwn=None, device_ip=None, server_lun_index=None, host_lun_index=None, network_portal_ip=None, network_portal_port=None, volume_lun_id=None, volume_size=None, link_id=None, client_id=None, server_id=None, data_transfe_ip=None,):
        self.volume_uuid = volume_uuid
        self.volume_config = volume_config
        self.volume_wwn = volume_wwn
        self.volume_type = volume_type
        self.fabric_type = fabric_type
        self.storage_object_name = storage_object_name
        self.target_wwn = target_wwn
        self.host_wwn = host_wwn
        self.device_ip = device_ip
        self.server_lun_index = server_lun_index
        self.host_lun_index = host_lun_index
        self.network_portal_ip = network_portal_ip
        self.network_portal_port = network_portal_port
        self.volume_lun_id = volume_lun_id
        self.volume_size = volume_size
        self.link_id = link_id
        self.client_id = client_id
        self.server_id = server_id
        self.data_transfe_ip = data_transfe_ip

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
                    self.volume_uuid = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.volume_config = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.volume_wwn = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.volume_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.fabric_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.storage_object_name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.target_wwn = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.host_wwn = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.device_ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.server_lun_index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.host_lun_index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.STRING:
                    self.network_portal_ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.I32:
                    self.network_portal_port = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 14:
                if ftype == TType.I64:
                    self.volume_lun_id = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 15:
                if ftype == TType.I64:
                    self.volume_size = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 16:
                if ftype == TType.STRING:
                    self.link_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 17:
                if ftype == TType.STRING:
                    self.client_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 18:
                if ftype == TType.STRING:
                    self.server_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 19:
                if ftype == TType.STRING:
                    self.data_transfe_ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncVolumeMappingRequest')
        if self.volume_uuid is not None:
            oprot.writeFieldBegin('volume_uuid', TType.STRING, 1)
            oprot.writeString(self.volume_uuid.encode('utf-8') if sys.version_info[0] == 2 else self.volume_uuid)
            oprot.writeFieldEnd()
        if self.volume_config is not None:
            oprot.writeFieldBegin('volume_config', TType.STRING, 2)
            oprot.writeString(self.volume_config.encode('utf-8') if sys.version_info[0] == 2 else self.volume_config)
            oprot.writeFieldEnd()
        if self.volume_wwn is not None:
            oprot.writeFieldBegin('volume_wwn', TType.STRING, 3)
            oprot.writeString(self.volume_wwn.encode('utf-8') if sys.version_info[0] == 2 else self.volume_wwn)
            oprot.writeFieldEnd()
        if self.volume_type is not None:
            oprot.writeFieldBegin('volume_type', TType.I32, 4)
            oprot.writeI32(self.volume_type)
            oprot.writeFieldEnd()
        if self.fabric_type is not None:
            oprot.writeFieldBegin('fabric_type', TType.I32, 5)
            oprot.writeI32(self.fabric_type)
            oprot.writeFieldEnd()
        if self.storage_object_name is not None:
            oprot.writeFieldBegin('storage_object_name', TType.STRING, 6)
            oprot.writeString(self.storage_object_name.encode('utf-8') if sys.version_info[0] == 2 else self.storage_object_name)
            oprot.writeFieldEnd()
        if self.target_wwn is not None:
            oprot.writeFieldBegin('target_wwn', TType.STRING, 7)
            oprot.writeString(self.target_wwn.encode('utf-8') if sys.version_info[0] == 2 else self.target_wwn)
            oprot.writeFieldEnd()
        if self.host_wwn is not None:
            oprot.writeFieldBegin('host_wwn', TType.STRING, 8)
            oprot.writeString(self.host_wwn.encode('utf-8') if sys.version_info[0] == 2 else self.host_wwn)
            oprot.writeFieldEnd()
        if self.device_ip is not None:
            oprot.writeFieldBegin('device_ip', TType.STRING, 9)
            oprot.writeString(self.device_ip.encode('utf-8') if sys.version_info[0] == 2 else self.device_ip)
            oprot.writeFieldEnd()
        if self.server_lun_index is not None:
            oprot.writeFieldBegin('server_lun_index', TType.I32, 10)
            oprot.writeI32(self.server_lun_index)
            oprot.writeFieldEnd()
        if self.host_lun_index is not None:
            oprot.writeFieldBegin('host_lun_index', TType.I32, 11)
            oprot.writeI32(self.host_lun_index)
            oprot.writeFieldEnd()
        if self.network_portal_ip is not None:
            oprot.writeFieldBegin('network_portal_ip', TType.STRING, 12)
            oprot.writeString(self.network_portal_ip.encode('utf-8') if sys.version_info[0] == 2 else self.network_portal_ip)
            oprot.writeFieldEnd()
        if self.network_portal_port is not None:
            oprot.writeFieldBegin('network_portal_port', TType.I32, 13)
            oprot.writeI32(self.network_portal_port)
            oprot.writeFieldEnd()
        if self.volume_lun_id is not None:
            oprot.writeFieldBegin('volume_lun_id', TType.I64, 14)
            oprot.writeI64(self.volume_lun_id)
            oprot.writeFieldEnd()
        if self.volume_size is not None:
            oprot.writeFieldBegin('volume_size', TType.I64, 15)
            oprot.writeI64(self.volume_size)
            oprot.writeFieldEnd()
        if self.link_id is not None:
            oprot.writeFieldBegin('link_id', TType.STRING, 16)
            oprot.writeString(self.link_id.encode('utf-8') if sys.version_info[0] == 2 else self.link_id)
            oprot.writeFieldEnd()
        if self.client_id is not None:
            oprot.writeFieldBegin('client_id', TType.STRING, 17)
            oprot.writeString(self.client_id.encode('utf-8') if sys.version_info[0] == 2 else self.client_id)
            oprot.writeFieldEnd()
        if self.server_id is not None:
            oprot.writeFieldBegin('server_id', TType.STRING, 18)
            oprot.writeString(self.server_id.encode('utf-8') if sys.version_info[0] == 2 else self.server_id)
            oprot.writeFieldEnd()
        if self.data_transfe_ip is not None:
            oprot.writeFieldBegin('data_transfe_ip', TType.STRING, 19)
            oprot.writeString(self.data_transfe_ip.encode('utf-8') if sys.version_info[0] == 2 else self.data_transfe_ip)
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


class ncVolumeMappingReply(object):
    """
    Attributes:
     - storage_object_type
     - storage_object_config
     - storage_object_name
     - storage_object_wwn
     - fabric_type
     - target_wwn
     - host_wwn
     - server_lun_index
     - host_lun_index
     - network_portal_ip
     - network_portal_port
     - tpg_tag
     - link_id

    """


    def __init__(self, storage_object_type=None, storage_object_config=None, storage_object_name=None, storage_object_wwn=None, fabric_type=None, target_wwn=None, host_wwn=None, server_lun_index=None, host_lun_index=None, network_portal_ip=None, network_portal_port=None, tpg_tag=None, link_id=None,):
        self.storage_object_type = storage_object_type
        self.storage_object_config = storage_object_config
        self.storage_object_name = storage_object_name
        self.storage_object_wwn = storage_object_wwn
        self.fabric_type = fabric_type
        self.target_wwn = target_wwn
        self.host_wwn = host_wwn
        self.server_lun_index = server_lun_index
        self.host_lun_index = host_lun_index
        self.network_portal_ip = network_portal_ip
        self.network_portal_port = network_portal_port
        self.tpg_tag = tpg_tag
        self.link_id = link_id

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
                    self.storage_object_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.storage_object_config = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.storage_object_name = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.storage_object_wwn = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.fabric_type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.target_wwn = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.host_wwn = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.server_lun_index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.host_lun_index = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.network_portal_ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.I32:
                    self.network_portal_port = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.I32:
                    self.tpg_tag = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 13:
                if ftype == TType.STRING:
                    self.link_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
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
        oprot.writeStructBegin('ncVolumeMappingReply')
        if self.storage_object_type is not None:
            oprot.writeFieldBegin('storage_object_type', TType.I32, 1)
            oprot.writeI32(self.storage_object_type)
            oprot.writeFieldEnd()
        if self.storage_object_config is not None:
            oprot.writeFieldBegin('storage_object_config', TType.STRING, 2)
            oprot.writeString(self.storage_object_config.encode('utf-8') if sys.version_info[0] == 2 else self.storage_object_config)
            oprot.writeFieldEnd()
        if self.storage_object_name is not None:
            oprot.writeFieldBegin('storage_object_name', TType.STRING, 3)
            oprot.writeString(self.storage_object_name.encode('utf-8') if sys.version_info[0] == 2 else self.storage_object_name)
            oprot.writeFieldEnd()
        if self.storage_object_wwn is not None:
            oprot.writeFieldBegin('storage_object_wwn', TType.STRING, 4)
            oprot.writeString(self.storage_object_wwn.encode('utf-8') if sys.version_info[0] == 2 else self.storage_object_wwn)
            oprot.writeFieldEnd()
        if self.fabric_type is not None:
            oprot.writeFieldBegin('fabric_type', TType.I32, 5)
            oprot.writeI32(self.fabric_type)
            oprot.writeFieldEnd()
        if self.target_wwn is not None:
            oprot.writeFieldBegin('target_wwn', TType.STRING, 6)
            oprot.writeString(self.target_wwn.encode('utf-8') if sys.version_info[0] == 2 else self.target_wwn)
            oprot.writeFieldEnd()
        if self.host_wwn is not None:
            oprot.writeFieldBegin('host_wwn', TType.STRING, 7)
            oprot.writeString(self.host_wwn.encode('utf-8') if sys.version_info[0] == 2 else self.host_wwn)
            oprot.writeFieldEnd()
        if self.server_lun_index is not None:
            oprot.writeFieldBegin('server_lun_index', TType.I32, 8)
            oprot.writeI32(self.server_lun_index)
            oprot.writeFieldEnd()
        if self.host_lun_index is not None:
            oprot.writeFieldBegin('host_lun_index', TType.I32, 9)
            oprot.writeI32(self.host_lun_index)
            oprot.writeFieldEnd()
        if self.network_portal_ip is not None:
            oprot.writeFieldBegin('network_portal_ip', TType.STRING, 10)
            oprot.writeString(self.network_portal_ip.encode('utf-8') if sys.version_info[0] == 2 else self.network_portal_ip)
            oprot.writeFieldEnd()
        if self.network_portal_port is not None:
            oprot.writeFieldBegin('network_portal_port', TType.I32, 11)
            oprot.writeI32(self.network_portal_port)
            oprot.writeFieldEnd()
        if self.tpg_tag is not None:
            oprot.writeFieldBegin('tpg_tag', TType.I32, 12)
            oprot.writeI32(self.tpg_tag)
            oprot.writeFieldEnd()
        if self.link_id is not None:
            oprot.writeFieldBegin('link_id', TType.STRING, 13)
            oprot.writeString(self.link_id.encode('utf-8') if sys.version_info[0] == 2 else self.link_id)
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


class ncCheckLinkReply(object):
    """
    Attributes:
     - link_num
     - link_check

    """


    def __init__(self, link_num=None, link_check=None,):
        self.link_num = link_num
        self.link_check = link_check

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
                    self.link_num = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BOOL:
                    self.link_check = iprot.readBool()
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
        oprot.writeStructBegin('ncCheckLinkReply')
        if self.link_num is not None:
            oprot.writeFieldBegin('link_num', TType.I32, 1)
            oprot.writeI32(self.link_num)
            oprot.writeFieldEnd()
        if self.link_check is not None:
            oprot.writeFieldBegin('link_check', TType.BOOL, 2)
            oprot.writeBool(self.link_check)
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


class ncLinkMappingRequest(object):
    """
    Attributes:
     - link_id
     - fabric_type
     - server_wwn
     - client_wwn
     - server_id
     - client_id
     - portal_ip
     - portal_port
     - pool_id
     - tpg_tag

    """


    def __init__(self, link_id=None, fabric_type=None, server_wwn=None, client_wwn=None, server_id=None, client_id=None, portal_ip=None, portal_port=None, pool_id=None, tpg_tag=None,):
        self.link_id = link_id
        self.fabric_type = fabric_type
        self.server_wwn = server_wwn
        self.client_wwn = client_wwn
        self.server_id = server_id
        self.client_id = client_id
        self.portal_ip = portal_ip
        self.portal_port = portal_port
        self.pool_id = pool_id
        self.tpg_tag = tpg_tag

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
                    self.portal_ip = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.portal_port = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.pool_id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I32:
                    self.tpg_tag = iprot.readI32()
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
        oprot.writeStructBegin('ncLinkMappingRequest')
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
        if self.portal_ip is not None:
            oprot.writeFieldBegin('portal_ip', TType.STRING, 7)
            oprot.writeString(self.portal_ip.encode('utf-8') if sys.version_info[0] == 2 else self.portal_ip)
            oprot.writeFieldEnd()
        if self.portal_port is not None:
            oprot.writeFieldBegin('portal_port', TType.I32, 8)
            oprot.writeI32(self.portal_port)
            oprot.writeFieldEnd()
        if self.pool_id is not None:
            oprot.writeFieldBegin('pool_id', TType.STRING, 9)
            oprot.writeString(self.pool_id.encode('utf-8') if sys.version_info[0] == 2 else self.pool_id)
            oprot.writeFieldEnd()
        if self.tpg_tag is not None:
            oprot.writeFieldBegin('tpg_tag', TType.I32, 10)
            oprot.writeI32(self.tpg_tag)
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
all_structs.append(ncVolumeMappingRequest)
ncVolumeMappingRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'volume_uuid', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'volume_config', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'volume_wwn', 'UTF8', None, ),  # 3
    (4, TType.I32, 'volume_type', None, None, ),  # 4
    (5, TType.I32, 'fabric_type', None, None, ),  # 5
    (6, TType.STRING, 'storage_object_name', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'target_wwn', 'UTF8', None, ),  # 7
    (8, TType.STRING, 'host_wwn', 'UTF8', None, ),  # 8
    (9, TType.STRING, 'device_ip', 'UTF8', None, ),  # 9
    (10, TType.I32, 'server_lun_index', None, None, ),  # 10
    (11, TType.I32, 'host_lun_index', None, None, ),  # 11
    (12, TType.STRING, 'network_portal_ip', 'UTF8', None, ),  # 12
    (13, TType.I32, 'network_portal_port', None, None, ),  # 13
    (14, TType.I64, 'volume_lun_id', None, None, ),  # 14
    (15, TType.I64, 'volume_size', None, None, ),  # 15
    (16, TType.STRING, 'link_id', 'UTF8', None, ),  # 16
    (17, TType.STRING, 'client_id', 'UTF8', None, ),  # 17
    (18, TType.STRING, 'server_id', 'UTF8', None, ),  # 18
    (19, TType.STRING, 'data_transfe_ip', 'UTF8', None, ),  # 19
)
all_structs.append(ncVolumeMappingReply)
ncVolumeMappingReply.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'storage_object_type', None, None, ),  # 1
    (2, TType.STRING, 'storage_object_config', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'storage_object_name', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'storage_object_wwn', 'UTF8', None, ),  # 4
    (5, TType.I32, 'fabric_type', None, None, ),  # 5
    (6, TType.STRING, 'target_wwn', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'host_wwn', 'UTF8', None, ),  # 7
    (8, TType.I32, 'server_lun_index', None, None, ),  # 8
    (9, TType.I32, 'host_lun_index', None, None, ),  # 9
    (10, TType.STRING, 'network_portal_ip', 'UTF8', None, ),  # 10
    (11, TType.I32, 'network_portal_port', None, None, ),  # 11
    (12, TType.I32, 'tpg_tag', None, None, ),  # 12
    (13, TType.STRING, 'link_id', 'UTF8', None, ),  # 13
)
all_structs.append(ncCheckLinkReply)
ncCheckLinkReply.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'link_num', None, None, ),  # 1
    (2, TType.BOOL, 'link_check', None, None, ),  # 2
)
all_structs.append(ncLinkMappingRequest)
ncLinkMappingRequest.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'link_id', 'UTF8', None, ),  # 1
    (2, TType.I32, 'fabric_type', None, None, ),  # 2
    (3, TType.STRING, 'server_wwn', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'client_wwn', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'server_id', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'client_id', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'portal_ip', 'UTF8', None, ),  # 7
    (8, TType.I32, 'portal_port', None, None, ),  # 8
    (9, TType.STRING, 'pool_id', 'UTF8', None, ),  # 9
    (10, TType.I32, 'tpg_tag', None, None, ),  # 10
)
fix_spec(all_structs)
del all_structs
