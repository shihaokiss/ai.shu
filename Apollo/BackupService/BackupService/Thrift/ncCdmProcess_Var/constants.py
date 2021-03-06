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
from .ttypes import *
EEE_JOB_NAME = "EEE_JOB_NAME"
EEE_JOB_ID = "EEE_JOB_ID"
EEE_NODE_ID = "EEE_NODE_ID"
EEE_CLIENT_ID = "EEE_CLIENT_ID"
EEE_CLIENT_MAC = "EEE_CLIENT_MAC"
EEE_ENGINE_TYPE = "EEE_ENGINE_TYPE"
EEE_CLIENT_TYPE = "EEE_CLIENT_TYPE"
EEE_DATA_SOURCE = "EEE_DATA_SOURCE"
EEE_VOLUME_MAPPING_IP = "EEE_VOLUME_MAPPING_IP"
EEE_VOLUME_MAPPING_PORT = "EEE_VOLUME_MAPPING_PORT"
EEE_VOLUME_WWN = "EEE_VOLUME_WWN"
EEE_CDM_ALL_TARGET_WWNS = "EEE_CDM_ALL_TARGET_WWNS"
EEE_CDM_BACKUP_POOL_TYPE = "EEE_CDM_BACKUP_POOL_TYPE"
EEE_CLIENT_WWN = "EEE_CLIENT_WWN"
EEE_LINK_TYPE = "EEE_LINK_TYPE"
EEE_BACKUP_TYPE = "EEE_BACKUP_TYPE"
EEE_IS_ALWAYS_ONLINE = "EEE_IS_ALWAYS_ONLINE"
EEE_DATA_RETENTION_POLICY = "EEE_DATA_RETENTION_POLICY"
EEE_DATA_RETENTION_TYPE = "EEE_DATA_RETENTION_TYPE"
EEE_DATA_RETENTION_CYCLE_NUM = "EEE_DATA_RETENTION_CYCLE_NUM"
EEE_DATA_RETENTION_CYCLE_UNIT = "EEE_DATA_RETENTION_CYCLE_UNIT"
EEE_STOREPOOL_TYPE = "EEE_STOREPOOL_TYPE"
EEE_MAPPING_LUN_UUID = "EEE_MAPPING_LUN_UUID"
EEE_LUN_BIND_RELATIONSHIP = "EEE_LUN_BIND_RELATIONSHIP"
EEE_RESTORE_TIMESTAMP = "EEE_RESTORE_TIMESTAMP"
EEE_RESTORE_DEST_PATH = "EEE_RESTORE_PATH"
EEE_IS_FIRST_TIME = "EEE_IS_FIRST_TIME"
EEE_IS_RESTORE_TO_NEW_NAME = "EEE_IS_RESTORE_TO_NEW_NAME"
EEE_RESTORE_TO_NEW_NAME = "EEE_RESTORE_TO_NEW_NAME"
EEE_RESTORE_COVER_OLD = "EEE_RESTORE_COVER_OLD"
EEE_IS_POWER_ON_AFTER_RESTORE = "EEE_IS_POWER_ON_AFTER_RESTORE"
EEE_IS_DELETE_ARCHIVE_LOG = "EEE_IS_DELETE_ARCHIVE_LOG"
EEE_DELETE_ARCHIVE_LOG_TIME = "EEE_DELETE_ARCHIVE_LOG_TIME"
EEE_UNIT_OF_TIME_FOR_DELETE_ARCH = "EEE_UNIT_OF_TIME_FOR_DELETE_ARCH"
EEE_IS_BACKUP_ARCHIVE_LOG_BY_TIME = "EEE_IS_BACKUP_ARCHIVE_LOG_BY_TIME"
EEE_BACKUP_ARCHIVE_LOG_TIME = "EEE_BACKUP_ARCHIVE_LOG_TIME"
EEE_UNIT_OF_TIME_FOR_BACKUP_ARCHIVE_LOG = "EEE_UNIT_OF_TIME_FOR_BACKUP_ARCHIVE_LOG"
EEE_ORACLE_RMAN_MULTI_CHANNEL_TYPE = "EEE_ORACLE_RMAN_MULTI_CHANNEL_TYPE"
EEE_ORACLE_RMAN_MULTI_CHANNEL_DATA = "EEE_ORACLE_RMAN_MULTI_CHANNEL_DATA"
EEE_ORACLE_RMAN_MULTI_CHANNEL_LOG = "EEE_ORACLE_RMAN_MULTI_CHANNEL_LOG"
EEE_ORACLE_RMAN_BCT_TYPE = "EEE_ORACLE_RMAN_BCT_TYPE"
EEE_ORACLE_RMAN_BCT_PATH = "EEE_ORACLE_RMAN_BCT_PATH"
EEE_DATA_VOLUME_UUID = "EEE_DATA_VOLUME_UUID"
EEE_DATA_VOLUME_MOUNT_POINT = "EEE_DATA_VOLUME_MOUNT_POINT"
EEE_DATA_VOLUME_CONFIG = "EEE_DATA_VOLUME_CONFIG"
EEE_LOG_VOLUME_UUID = "EEE_LOG_VOLUME_UUID"
EEE_LOG_VOLUME_MOUNT_POINT = "EEE_LOG_VOLUME_MOUNT_POINT"
EEE_LOG_VOLUME_CONFIG = "EEE_LOG_VOLUME_CONFIG"
EEE_VOLUME_POOL_UUID = "EEE_VOLUME_POOL_UUID"
EEE_VOLUME_VENDOR_ID = "EEE_VOLUME_VENDOR_ID"
EEE_RAC_ARCHIVELOG_IS_ON_NODE = "EEE_RAC_ARCHIVELOG_IS_ON_NODE"
EEE_IS_SOURCE_MACHINE = "EEE_IS_SOURCE_MACHINE"
EEE_REAL_PATH = "EEE_REAL_PATH"
