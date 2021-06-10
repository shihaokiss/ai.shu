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


class ncNodeStatus(object):
    OFFLINE = 0
    ONLINE = 1
    ABNORMAL = 2

    _VALUES_TO_NAMES = {
        0: "OFFLINE",
        1: "ONLINE",
        2: "ABNORMAL",
    }

    _NAMES_TO_VALUES = {
        "OFFLINE": 0,
        "ONLINE": 1,
        "ABNORMAL": 2,
    }


class ncNodeOsType(object):
    UNKNOW_TYPE = 0
    WINDOWS = 1
    LINUX = 2
    AIX = 3
    SOLARIS = 4
    HP_UX = 5
    NEOKYLIN = 6
    YHKYLIN = 7

    _VALUES_TO_NAMES = {
        0: "UNKNOW_TYPE",
        1: "WINDOWS",
        2: "LINUX",
        3: "AIX",
        4: "SOLARIS",
        5: "HP_UX",
        6: "NEOKYLIN",
        7: "YHKYLIN",
    }

    _NAMES_TO_VALUES = {
        "UNKNOW_TYPE": 0,
        "WINDOWS": 1,
        "LINUX": 2,
        "AIX": 3,
        "SOLARIS": 4,
        "HP_UX": 5,
        "NEOKYLIN": 6,
        "YHKYLIN": 7,
    }


class ncSourceType(object):
    CLIENT = 0
    VMPLAT = 1
    CLOUDPLAT = 2

    _VALUES_TO_NAMES = {
        0: "CLIENT",
        1: "VMPLAT",
        2: "CLOUDPLAT",
    }

    _NAMES_TO_VALUES = {
        "CLIENT": 0,
        "VMPLAT": 1,
        "CLOUDPLAT": 2,
    }


class ncRelationStatus(object):
    ON = 0
    OFF = 1

    _VALUES_TO_NAMES = {
        0: "ON",
        1: "OFF",
    }

    _NAMES_TO_VALUES = {
        "ON": 0,
        "OFF": 1,
    }


class ncVplatFormType(object):
    NC_V_PLATFORM_XEN = 1
    NC_V_PLATFORM_INCLOUD = 2
    NC_V_PLATFORM_VMWARE = 3
    NC_V_PLATFORM_FUSIONCOMPUTE = 4
    NC_V_PLATFORM_RHEV = 5
    NC_V_PLATFORM_HYPERV = 6
    NC_V_PLATFORM_H3CLOUD = 7
    NC_V_PLATFORM_CAS = 8
    NC_V_PLATFORM_INKVM = 9
    NC_V_PLATFORM_ACLOUD = 11

    _VALUES_TO_NAMES = {
        1: "NC_V_PLATFORM_XEN",
        2: "NC_V_PLATFORM_INCLOUD",
        3: "NC_V_PLATFORM_VMWARE",
        4: "NC_V_PLATFORM_FUSIONCOMPUTE",
        5: "NC_V_PLATFORM_RHEV",
        6: "NC_V_PLATFORM_HYPERV",
        7: "NC_V_PLATFORM_H3CLOUD",
        8: "NC_V_PLATFORM_CAS",
        9: "NC_V_PLATFORM_INKVM",
        11: "NC_V_PLATFORM_ACLOUD",
    }

    _NAMES_TO_VALUES = {
        "NC_V_PLATFORM_XEN": 1,
        "NC_V_PLATFORM_INCLOUD": 2,
        "NC_V_PLATFORM_VMWARE": 3,
        "NC_V_PLATFORM_FUSIONCOMPUTE": 4,
        "NC_V_PLATFORM_RHEV": 5,
        "NC_V_PLATFORM_HYPERV": 6,
        "NC_V_PLATFORM_H3CLOUD": 7,
        "NC_V_PLATFORM_CAS": 8,
        "NC_V_PLATFORM_INKVM": 9,
        "NC_V_PLATFORM_ACLOUD": 11,
    }


class ncCplatFormType(object):
    NC_C_PLATFORM_OPENSTACK = 0
    NC_C_PLATFORM_FUSIONCLOUD = 2

    _VALUES_TO_NAMES = {
        0: "NC_C_PLATFORM_OPENSTACK",
        2: "NC_C_PLATFORM_FUSIONCLOUD",
    }

    _NAMES_TO_VALUES = {
        "NC_C_PLATFORM_OPENSTACK": 0,
        "NC_C_PLATFORM_FUSIONCLOUD": 2,
    }


class ncServiceType(object):
    ALL = 0
    BACKUP = 1
    DEDUPE = 2
    TAPE = 3
    COMMON = 4
    AUTH = 5
    LOG = 6
    STORAGE = 7
    UPDATE = 8
    CDP = 9
    DR = 10
    CDR = 11
    DATACP = 12
    ARCHIVE = 13
    CDMDISPATCH = 14
    CDMSTOREMGM = 15
    CLUSTERMGM = 16
    ESSSS = 17
    EOSSMGM = 18
    CLIENT = 19
    DB = 20
    KAD = 21
    WEB = 22
    EOSS = 23
    AMS = 24
    CDPSTORE = 25
    SNAPSYNC = 26
    EOSSMeta = 27
    EOSSData = 28
    KEY = 29
    ECSS = 30
    DEPLOY = 31
    EBSS_ARCHIVE = 32
    ETSS = 33
    STORAGERESMGM = 34
    VCS = 35
    KMC = 36
    LINKMGM = 37
    KMS = 38
    ProxyMgr = 39
    Proxy = 40
    SNMP = 41
    NautilusData = 42
    NautilusMeta = 43
    NautilusTask = 45

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "BACKUP",
        2: "DEDUPE",
        3: "TAPE",
        4: "COMMON",
        5: "AUTH",
        6: "LOG",
        7: "STORAGE",
        8: "UPDATE",
        9: "CDP",
        10: "DR",
        11: "CDR",
        12: "DATACP",
        13: "ARCHIVE",
        14: "CDMDISPATCH",
        15: "CDMSTOREMGM",
        16: "CLUSTERMGM",
        17: "ESSSS",
        18: "EOSSMGM",
        19: "CLIENT",
        20: "DB",
        21: "KAD",
        22: "WEB",
        23: "EOSS",
        24: "AMS",
        25: "CDPSTORE",
        26: "SNAPSYNC",
        27: "EOSSMeta",
        28: "EOSSData",
        29: "KEY",
        30: "ECSS",
        31: "DEPLOY",
        32: "EBSS_ARCHIVE",
        33: "ETSS",
        34: "STORAGERESMGM",
        35: "VCS",
        36: "KMC",
        37: "LINKMGM",
        38: "KMS",
        39: "ProxyMgr",
        40: "Proxy",
        41: "SNMP",
        42: "NautilusData",
        43: "NautilusMeta",
        45: "NautilusTask",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "BACKUP": 1,
        "DEDUPE": 2,
        "TAPE": 3,
        "COMMON": 4,
        "AUTH": 5,
        "LOG": 6,
        "STORAGE": 7,
        "UPDATE": 8,
        "CDP": 9,
        "DR": 10,
        "CDR": 11,
        "DATACP": 12,
        "ARCHIVE": 13,
        "CDMDISPATCH": 14,
        "CDMSTOREMGM": 15,
        "CLUSTERMGM": 16,
        "ESSSS": 17,
        "EOSSMGM": 18,
        "CLIENT": 19,
        "DB": 20,
        "KAD": 21,
        "WEB": 22,
        "EOSS": 23,
        "AMS": 24,
        "CDPSTORE": 25,
        "SNAPSYNC": 26,
        "EOSSMeta": 27,
        "EOSSData": 28,
        "KEY": 29,
        "ECSS": 30,
        "DEPLOY": 31,
        "EBSS_ARCHIVE": 32,
        "ETSS": 33,
        "STORAGERESMGM": 34,
        "VCS": 35,
        "KMC": 36,
        "LINKMGM": 37,
        "KMS": 38,
        "ProxyMgr": 39,
        "Proxy": 40,
        "SNMP": 41,
        "NautilusData": 42,
        "NautilusMeta": 43,
        "NautilusTask": 45,
    }


class ncExecLogLevel(object):
    INFO_LOG = 1
    WARNING_LOG = 2
    ERROR_LOG = 3
    FATAL_LOG = 4

    _VALUES_TO_NAMES = {
        1: "INFO_LOG",
        2: "WARNING_LOG",
        3: "ERROR_LOG",
        4: "FATAL_LOG",
    }

    _NAMES_TO_VALUES = {
        "INFO_LOG": 1,
        "WARNING_LOG": 2,
        "ERROR_LOG": 3,
        "FATAL_LOG": 4,
    }


class ncClientType(object):
    NC_CLIENT_TYPE_PYSICAL = 1
    NC_CLIENT_TYPE_COUPLE = 2
    NC_CLIENT_TYPE_RAC = 3
    NC_CLIENT_TYPE_HYPERV = 4
    NC_CLIENT_TYPE_VMWARE = 5
    NC_CLIENT_TYPE_FUSIONCOMPUTE = 6
    NC_CLIENT_TYPE_DAG = 7
    NC_CLIENT_TYPE_CAS = 8
    NC_CLIENT_TYPE_NAS = 9
    NC_CLIENT_TYPE_CNware = 10
    NC_CLIENT_TYPE_OpenStack = 11
    NC_CLIENT_TYPE_H3Cloud = 12
    NC_CLIENT_TYPE_RHEV = 13
    NC_CLIENT_TYPE_INCLOUD = 14
    NC_CLIENT_TYPE_XEN = 15
    NC_CLIENT_TYPE_HANA = 16
    NC_CLIENT_TYPE_HADOOP = 17
    NC_CLIENT_TYPE_MONGODB = 18
    NC_CLIENT_TYPE_ALWAYSON = 19
    NC_CLIENT_TYPE_GAUSSDB = 20
    NC_CLIENT_TYPE_ACLOUD = 21
    NC_CLIENT_TYPE_VMWARE_ACCURATE = 22
    NC_CLIENT_TYPE_MYSQL = 23
    NC_CLIENT_TYPE_FILE_CLUSTER = 24
    NC_CLIENT_TYPE_SQLSERVER_DOUBLE = 25
    NC_CLIENT_TYPE_POSTGRESQL = 26

    _VALUES_TO_NAMES = {
        1: "NC_CLIENT_TYPE_PYSICAL",
        2: "NC_CLIENT_TYPE_COUPLE",
        3: "NC_CLIENT_TYPE_RAC",
        4: "NC_CLIENT_TYPE_HYPERV",
        5: "NC_CLIENT_TYPE_VMWARE",
        6: "NC_CLIENT_TYPE_FUSIONCOMPUTE",
        7: "NC_CLIENT_TYPE_DAG",
        8: "NC_CLIENT_TYPE_CAS",
        9: "NC_CLIENT_TYPE_NAS",
        10: "NC_CLIENT_TYPE_CNware",
        11: "NC_CLIENT_TYPE_OpenStack",
        12: "NC_CLIENT_TYPE_H3Cloud",
        13: "NC_CLIENT_TYPE_RHEV",
        14: "NC_CLIENT_TYPE_INCLOUD",
        15: "NC_CLIENT_TYPE_XEN",
        16: "NC_CLIENT_TYPE_HANA",
        17: "NC_CLIENT_TYPE_HADOOP",
        18: "NC_CLIENT_TYPE_MONGODB",
        19: "NC_CLIENT_TYPE_ALWAYSON",
        20: "NC_CLIENT_TYPE_GAUSSDB",
        21: "NC_CLIENT_TYPE_ACLOUD",
        22: "NC_CLIENT_TYPE_VMWARE_ACCURATE",
        23: "NC_CLIENT_TYPE_MYSQL",
        24: "NC_CLIENT_TYPE_FILE_CLUSTER",
        25: "NC_CLIENT_TYPE_SQLSERVER_DOUBLE",
        26: "NC_CLIENT_TYPE_POSTGRESQL",
    }

    _NAMES_TO_VALUES = {
        "NC_CLIENT_TYPE_PYSICAL": 1,
        "NC_CLIENT_TYPE_COUPLE": 2,
        "NC_CLIENT_TYPE_RAC": 3,
        "NC_CLIENT_TYPE_HYPERV": 4,
        "NC_CLIENT_TYPE_VMWARE": 5,
        "NC_CLIENT_TYPE_FUSIONCOMPUTE": 6,
        "NC_CLIENT_TYPE_DAG": 7,
        "NC_CLIENT_TYPE_CAS": 8,
        "NC_CLIENT_TYPE_NAS": 9,
        "NC_CLIENT_TYPE_CNware": 10,
        "NC_CLIENT_TYPE_OpenStack": 11,
        "NC_CLIENT_TYPE_H3Cloud": 12,
        "NC_CLIENT_TYPE_RHEV": 13,
        "NC_CLIENT_TYPE_INCLOUD": 14,
        "NC_CLIENT_TYPE_XEN": 15,
        "NC_CLIENT_TYPE_HANA": 16,
        "NC_CLIENT_TYPE_HADOOP": 17,
        "NC_CLIENT_TYPE_MONGODB": 18,
        "NC_CLIENT_TYPE_ALWAYSON": 19,
        "NC_CLIENT_TYPE_GAUSSDB": 20,
        "NC_CLIENT_TYPE_ACLOUD": 21,
        "NC_CLIENT_TYPE_VMWARE_ACCURATE": 22,
        "NC_CLIENT_TYPE_MYSQL": 23,
        "NC_CLIENT_TYPE_FILE_CLUSTER": 24,
        "NC_CLIENT_TYPE_SQLSERVER_DOUBLE": 25,
        "NC_CLIENT_TYPE_POSTGRESQL": 26,
    }


class ncEngineType(object):
    NORMAL_BACKUP_ENGINE = 1001
    NORMAL_RESTORE_ENGINE = 1002
    ACCURATE_RESTORE_ENGINE = 1003
    MOUNTED_RESTORE_ENGINE = 1004
    NORMAL_CLEAN_ENGINE = 2001
    NORMAL_DATA_SYNC_ENGINE = 2101
    CDP_REPLICATION_ENGINE = 3001
    LOGSOURCE_CDP_ENGINE = 3002
    LOGTARGET_CDP_ENGINE = 3003
    CDP_DATA_SYNC_ENGINE = 3004
    DG_PRIMARY_ENGINE = 3005
    DG_STANDBY_ENGINE = 3006
    HOST_BACKUP_ENGINE = 3007
    HOST_RESTORE_ENGINE = 3008
    HOST_MOUNT_RESTORE_ENGINE = 3009
    HOST_ACCURATE_RESTORE_ENGINE = 3010
    HOST_DRILL_ENGINE = 3011
    CDP_REPLICATIONSOURCE_ENGINE = 3012
    HOST_MOUNT_RESTORE_ENGINE_SECOND = 3013
    DRAAS_REPLICATIONSOURCE_ENGINE = 3014
    DRAAS_REPLICATION_ENGINE = 3015
    CDP_FILEREPLICATIONSOURCE_ENGINE = 3016
    CDP_FILEREPLICATIONTARGET_ENGINE = 3017
    CDM_NORMAL_BACKUP_ENGINE = 4001
    CDM_NORMAL_MOUNT_ENGINE = 4002
    CDM_NORMAL_CLONE_ENGINE = 4003
    CDM_NORMAL_RESTORE_ENGINE = 4004
    CDM_ACCURATE_RESTORE_ENGINE = 4005
    CDM_LIVE_CLONE_ENGINE = 4006
    CDM_NORMAL_UMOUNT_ENGINE = 4007
    CDM_SNAP_SYNC_ENGINE = 4008
    FI_HADOOP_BACKUP_ENGINE = 6001
    FI_HADOOP_RESTORE_ENGINE = 6002
    CDM_NORMAL_BROWSE_TASK_RESTORE = 4008
    CDM_NORMAL_BROWSE_IMAGE_RESTORE = 4009
    PHY_NORMAL_BACKUP_ENGINE = 5001
    PHY_NORMAL_RESTORE_ENGINE = 5002
    V2V_FUSION_VMWARE_ENGINE = 7001

    _VALUES_TO_NAMES = {
        1001: "NORMAL_BACKUP_ENGINE",
        1002: "NORMAL_RESTORE_ENGINE",
        1003: "ACCURATE_RESTORE_ENGINE",
        1004: "MOUNTED_RESTORE_ENGINE",
        2001: "NORMAL_CLEAN_ENGINE",
        2101: "NORMAL_DATA_SYNC_ENGINE",
        3001: "CDP_REPLICATION_ENGINE",
        3002: "LOGSOURCE_CDP_ENGINE",
        3003: "LOGTARGET_CDP_ENGINE",
        3004: "CDP_DATA_SYNC_ENGINE",
        3005: "DG_PRIMARY_ENGINE",
        3006: "DG_STANDBY_ENGINE",
        3007: "HOST_BACKUP_ENGINE",
        3008: "HOST_RESTORE_ENGINE",
        3009: "HOST_MOUNT_RESTORE_ENGINE",
        3010: "HOST_ACCURATE_RESTORE_ENGINE",
        3011: "HOST_DRILL_ENGINE",
        3012: "CDP_REPLICATIONSOURCE_ENGINE",
        3013: "HOST_MOUNT_RESTORE_ENGINE_SECOND",
        3014: "DRAAS_REPLICATIONSOURCE_ENGINE",
        3015: "DRAAS_REPLICATION_ENGINE",
        3016: "CDP_FILEREPLICATIONSOURCE_ENGINE",
        3017: "CDP_FILEREPLICATIONTARGET_ENGINE",
        4001: "CDM_NORMAL_BACKUP_ENGINE",
        4002: "CDM_NORMAL_MOUNT_ENGINE",
        4003: "CDM_NORMAL_CLONE_ENGINE",
        4004: "CDM_NORMAL_RESTORE_ENGINE",
        4005: "CDM_ACCURATE_RESTORE_ENGINE",
        4006: "CDM_LIVE_CLONE_ENGINE",
        4007: "CDM_NORMAL_UMOUNT_ENGINE",
        4008: "CDM_SNAP_SYNC_ENGINE",
        6001: "FI_HADOOP_BACKUP_ENGINE",
        6002: "FI_HADOOP_RESTORE_ENGINE",
        4008: "CDM_NORMAL_BROWSE_TASK_RESTORE",
        4009: "CDM_NORMAL_BROWSE_IMAGE_RESTORE",
        5001: "PHY_NORMAL_BACKUP_ENGINE",
        5002: "PHY_NORMAL_RESTORE_ENGINE",
        7001: "V2V_FUSION_VMWARE_ENGINE",
    }

    _NAMES_TO_VALUES = {
        "NORMAL_BACKUP_ENGINE": 1001,
        "NORMAL_RESTORE_ENGINE": 1002,
        "ACCURATE_RESTORE_ENGINE": 1003,
        "MOUNTED_RESTORE_ENGINE": 1004,
        "NORMAL_CLEAN_ENGINE": 2001,
        "NORMAL_DATA_SYNC_ENGINE": 2101,
        "CDP_REPLICATION_ENGINE": 3001,
        "LOGSOURCE_CDP_ENGINE": 3002,
        "LOGTARGET_CDP_ENGINE": 3003,
        "CDP_DATA_SYNC_ENGINE": 3004,
        "DG_PRIMARY_ENGINE": 3005,
        "DG_STANDBY_ENGINE": 3006,
        "HOST_BACKUP_ENGINE": 3007,
        "HOST_RESTORE_ENGINE": 3008,
        "HOST_MOUNT_RESTORE_ENGINE": 3009,
        "HOST_ACCURATE_RESTORE_ENGINE": 3010,
        "HOST_DRILL_ENGINE": 3011,
        "CDP_REPLICATIONSOURCE_ENGINE": 3012,
        "HOST_MOUNT_RESTORE_ENGINE_SECOND": 3013,
        "DRAAS_REPLICATIONSOURCE_ENGINE": 3014,
        "DRAAS_REPLICATION_ENGINE": 3015,
        "CDP_FILEREPLICATIONSOURCE_ENGINE": 3016,
        "CDP_FILEREPLICATIONTARGET_ENGINE": 3017,
        "CDM_NORMAL_BACKUP_ENGINE": 4001,
        "CDM_NORMAL_MOUNT_ENGINE": 4002,
        "CDM_NORMAL_CLONE_ENGINE": 4003,
        "CDM_NORMAL_RESTORE_ENGINE": 4004,
        "CDM_ACCURATE_RESTORE_ENGINE": 4005,
        "CDM_LIVE_CLONE_ENGINE": 4006,
        "CDM_NORMAL_UMOUNT_ENGINE": 4007,
        "CDM_SNAP_SYNC_ENGINE": 4008,
        "FI_HADOOP_BACKUP_ENGINE": 6001,
        "FI_HADOOP_RESTORE_ENGINE": 6002,
        "CDM_NORMAL_BROWSE_TASK_RESTORE": 4008,
        "CDM_NORMAL_BROWSE_IMAGE_RESTORE": 4009,
        "PHY_NORMAL_BACKUP_ENGINE": 5001,
        "PHY_NORMAL_RESTORE_ENGINE": 5002,
        "V2V_FUSION_VMWARE_ENGINE": 7001,
    }


class ncDataSourceNodeType(object):
    NT_FILE_ROOT = 1000
    NT_DIR = 1001
    NT_FILE = 1002
    NT_ORA_ROOT = 2000
    NT_ORA_INST = 2001
    NT_ORA_TP = 2002
    NT_ORA_SCHEMA = 2003
    NT_ORA_TABLE = 2004
    NT_ORA_CONT = 2005
    NT_MSSQL_ROOT = 3000
    NT_MSSQL_INST = 3001
    NT_MSSQL_DB = 3002
    NT_MSSQL_AG = 3003
    NT_EXCHANGE_VSS_ROOT = 4000
    NT_EXCHANGE_VSS_INST = 4001
    NT_EXCHANGE_VSS_DB = 4002
    NT_EXCHANGE_MAIL_ROOT = 4050
    NT_EXCHANGE_MAIL_INST = 4051
    NT_EXCHANGE_MAIL_USER = 4052
    NT_EXCHANGE_MAIL_DIR = 4053
    NT_EXCHANGE_MAIL_FILE = 4054
    NT_AD_ROOT = 5000
    NT_AD_INST = 5001
    NT_DB2_ROOT = 6000
    NT_DB2_INST = 6001
    NT_DB2_DB = 6002
    NT_DB2_TP = 6003
    NT_SYB_ROOT = 7000
    NT_SYB_INST = 7001
    NT_SYB_DB = 7002
    NT_MYSQL_ROOT = 8000
    NT_MYSQL_INST = 8001
    NT_MYSQL_DB = 8002
    NT_DOMINO_ROOT = 10000
    NT_DOMINO_INST = 10001
    NT_DOMINO_INI = 10002
    NT_DOMINO_DATA = 10003
    NT_DOMINO_DAOS = 10004
    NT_DOMINO_DIR = 10005
    NT_DOMINO_FILE = 10006
    NT_DOMINO_LINK_DIR = 10007
    NT_GBASE_ROOT = 11000
    NT_GBASE_INST = 11001
    NT_VMWARE_ROOT = 12000
    NT_VMWARE_ESXI = 12001
    NT_VMWARE_DC = 12002
    NT_VMWARE_DIR = 12003
    NT_VMWARE_CLU = 12004
    NT_VMWARE_HOST = 12005
    NT_VMWARE_POOL = 12006
    NT_VMWARE_VM = 12007
    NT_VMWARE_VAPP = 12008
    NT_VMWARE_PLATFORM = 12009
    NT_VMWARE_FOLDER = 12010
    NT_VMWARE_DATACENTER = 12011
    NT_VMWARE_VMFOLDER = 12012
    NT_HYPERV_ROOT = 13000
    NT_HYPERV_PLAT = 13001
    NT_HYPERV_VM = 13002
    NT_MAIL_ROOT = 14000
    NT_MAIL_USER = 14001
    NT_MAIL_CLIENT = 14002
    NT_CAS_ROOT = 15000
    NT_CAS_PLAT = 15001
    NT_CAS_HOSTPOOL = 15002
    NT_CAS_CLUSTER = 15003
    NT_CAS_HOST = 15004
    NT_CAS_VM = 15005
    NT_CAS_CLUSTER_VM = 15006
    NT_OPENSTACK_PLATE = 16000
    NT_OPENSTACK_PROJECT = 16001
    NT_OPENSTACK_REGION = 16002
    NT_OPENSTACK_USER = 16003
    NT_OPENSTACK_VM = 16004
    NT_VOLCDP_ROOT = 20000
    NT_VOLCDP_VOL = 20001
    NT_FUSION_UNDEFINE = 21000
    NT_FUSION_ROOT = 21001
    NT_FUSION_SITE = 21002
    NT_FUSION_CLUSTER_FOLDER = 21003
    NT_FUSION_CLUSTER = 21004
    NT_FUSION_HOST = 21005
    NT_FUSION_VM = 21006
    NT_WINCENTER_ROOT = 23000
    NT_WINCENTER_RSC = 23001
    NT_WINCENTER_HOST = 23002
    NT_WINCENTER_VM = 23003
    NT_INSPUR_POOL = 26000
    NT_INSPUR_HOST = 26001
    NT_INSPUR_VM = 26002
    NT_INSPUR_UNDEFINE = 26003
    NT_VOLUME = 27000
    NC_HWCLOUD_TENANT = 28001
    NC_HWCLOUD_REGION = 28002
    NC_HWCLOUD_PROJECT = 28003
    NC_HWCLOUD_VM = 28004
    NT_ACLOUD_ROOT = 30000
    NT_ACLOUD_PLAT = 30001
    NT_ACLOUD_GROUP = 30002
    NT_ACLOUD_VM = 30003
    NT_POSTGRESQL_ROOT = 31000
    NT_POSTGRESQL_INST = 31001
    NT_MONGODB_ROOT = 8000
    NT_MONGODB_INST = 8001
    NT_MONGODB_DB = 8002
    NT_KINGBASE_ROOT = 31000
    NT_KINGBASE_INST = 31001

    _VALUES_TO_NAMES = {
        1000: "NT_FILE_ROOT",
        1001: "NT_DIR",
        1002: "NT_FILE",
        2000: "NT_ORA_ROOT",
        2001: "NT_ORA_INST",
        2002: "NT_ORA_TP",
        2003: "NT_ORA_SCHEMA",
        2004: "NT_ORA_TABLE",
        2005: "NT_ORA_CONT",
        3000: "NT_MSSQL_ROOT",
        3001: "NT_MSSQL_INST",
        3002: "NT_MSSQL_DB",
        3003: "NT_MSSQL_AG",
        4000: "NT_EXCHANGE_VSS_ROOT",
        4001: "NT_EXCHANGE_VSS_INST",
        4002: "NT_EXCHANGE_VSS_DB",
        4050: "NT_EXCHANGE_MAIL_ROOT",
        4051: "NT_EXCHANGE_MAIL_INST",
        4052: "NT_EXCHANGE_MAIL_USER",
        4053: "NT_EXCHANGE_MAIL_DIR",
        4054: "NT_EXCHANGE_MAIL_FILE",
        5000: "NT_AD_ROOT",
        5001: "NT_AD_INST",
        6000: "NT_DB2_ROOT",
        6001: "NT_DB2_INST",
        6002: "NT_DB2_DB",
        6003: "NT_DB2_TP",
        7000: "NT_SYB_ROOT",
        7001: "NT_SYB_INST",
        7002: "NT_SYB_DB",
        8000: "NT_MYSQL_ROOT",
        8001: "NT_MYSQL_INST",
        8002: "NT_MYSQL_DB",
        10000: "NT_DOMINO_ROOT",
        10001: "NT_DOMINO_INST",
        10002: "NT_DOMINO_INI",
        10003: "NT_DOMINO_DATA",
        10004: "NT_DOMINO_DAOS",
        10005: "NT_DOMINO_DIR",
        10006: "NT_DOMINO_FILE",
        10007: "NT_DOMINO_LINK_DIR",
        11000: "NT_GBASE_ROOT",
        11001: "NT_GBASE_INST",
        12000: "NT_VMWARE_ROOT",
        12001: "NT_VMWARE_ESXI",
        12002: "NT_VMWARE_DC",
        12003: "NT_VMWARE_DIR",
        12004: "NT_VMWARE_CLU",
        12005: "NT_VMWARE_HOST",
        12006: "NT_VMWARE_POOL",
        12007: "NT_VMWARE_VM",
        12008: "NT_VMWARE_VAPP",
        12009: "NT_VMWARE_PLATFORM",
        12010: "NT_VMWARE_FOLDER",
        12011: "NT_VMWARE_DATACENTER",
        12012: "NT_VMWARE_VMFOLDER",
        13000: "NT_HYPERV_ROOT",
        13001: "NT_HYPERV_PLAT",
        13002: "NT_HYPERV_VM",
        14000: "NT_MAIL_ROOT",
        14001: "NT_MAIL_USER",
        14002: "NT_MAIL_CLIENT",
        15000: "NT_CAS_ROOT",
        15001: "NT_CAS_PLAT",
        15002: "NT_CAS_HOSTPOOL",
        15003: "NT_CAS_CLUSTER",
        15004: "NT_CAS_HOST",
        15005: "NT_CAS_VM",
        15006: "NT_CAS_CLUSTER_VM",
        16000: "NT_OPENSTACK_PLATE",
        16001: "NT_OPENSTACK_PROJECT",
        16002: "NT_OPENSTACK_REGION",
        16003: "NT_OPENSTACK_USER",
        16004: "NT_OPENSTACK_VM",
        20000: "NT_VOLCDP_ROOT",
        20001: "NT_VOLCDP_VOL",
        21000: "NT_FUSION_UNDEFINE",
        21001: "NT_FUSION_ROOT",
        21002: "NT_FUSION_SITE",
        21003: "NT_FUSION_CLUSTER_FOLDER",
        21004: "NT_FUSION_CLUSTER",
        21005: "NT_FUSION_HOST",
        21006: "NT_FUSION_VM",
        23000: "NT_WINCENTER_ROOT",
        23001: "NT_WINCENTER_RSC",
        23002: "NT_WINCENTER_HOST",
        23003: "NT_WINCENTER_VM",
        26000: "NT_INSPUR_POOL",
        26001: "NT_INSPUR_HOST",
        26002: "NT_INSPUR_VM",
        26003: "NT_INSPUR_UNDEFINE",
        27000: "NT_VOLUME",
        28001: "NC_HWCLOUD_TENANT",
        28002: "NC_HWCLOUD_REGION",
        28003: "NC_HWCLOUD_PROJECT",
        28004: "NC_HWCLOUD_VM",
        30000: "NT_ACLOUD_ROOT",
        30001: "NT_ACLOUD_PLAT",
        30002: "NT_ACLOUD_GROUP",
        30003: "NT_ACLOUD_VM",
        31000: "NT_POSTGRESQL_ROOT",
        31001: "NT_POSTGRESQL_INST",
        8000: "NT_MONGODB_ROOT",
        8001: "NT_MONGODB_INST",
        8002: "NT_MONGODB_DB",
        31000: "NT_KINGBASE_ROOT",
        31001: "NT_KINGBASE_INST",
    }

    _NAMES_TO_VALUES = {
        "NT_FILE_ROOT": 1000,
        "NT_DIR": 1001,
        "NT_FILE": 1002,
        "NT_ORA_ROOT": 2000,
        "NT_ORA_INST": 2001,
        "NT_ORA_TP": 2002,
        "NT_ORA_SCHEMA": 2003,
        "NT_ORA_TABLE": 2004,
        "NT_ORA_CONT": 2005,
        "NT_MSSQL_ROOT": 3000,
        "NT_MSSQL_INST": 3001,
        "NT_MSSQL_DB": 3002,
        "NT_MSSQL_AG": 3003,
        "NT_EXCHANGE_VSS_ROOT": 4000,
        "NT_EXCHANGE_VSS_INST": 4001,
        "NT_EXCHANGE_VSS_DB": 4002,
        "NT_EXCHANGE_MAIL_ROOT": 4050,
        "NT_EXCHANGE_MAIL_INST": 4051,
        "NT_EXCHANGE_MAIL_USER": 4052,
        "NT_EXCHANGE_MAIL_DIR": 4053,
        "NT_EXCHANGE_MAIL_FILE": 4054,
        "NT_AD_ROOT": 5000,
        "NT_AD_INST": 5001,
        "NT_DB2_ROOT": 6000,
        "NT_DB2_INST": 6001,
        "NT_DB2_DB": 6002,
        "NT_DB2_TP": 6003,
        "NT_SYB_ROOT": 7000,
        "NT_SYB_INST": 7001,
        "NT_SYB_DB": 7002,
        "NT_MYSQL_ROOT": 8000,
        "NT_MYSQL_INST": 8001,
        "NT_MYSQL_DB": 8002,
        "NT_DOMINO_ROOT": 10000,
        "NT_DOMINO_INST": 10001,
        "NT_DOMINO_INI": 10002,
        "NT_DOMINO_DATA": 10003,
        "NT_DOMINO_DAOS": 10004,
        "NT_DOMINO_DIR": 10005,
        "NT_DOMINO_FILE": 10006,
        "NT_DOMINO_LINK_DIR": 10007,
        "NT_GBASE_ROOT": 11000,
        "NT_GBASE_INST": 11001,
        "NT_VMWARE_ROOT": 12000,
        "NT_VMWARE_ESXI": 12001,
        "NT_VMWARE_DC": 12002,
        "NT_VMWARE_DIR": 12003,
        "NT_VMWARE_CLU": 12004,
        "NT_VMWARE_HOST": 12005,
        "NT_VMWARE_POOL": 12006,
        "NT_VMWARE_VM": 12007,
        "NT_VMWARE_VAPP": 12008,
        "NT_VMWARE_PLATFORM": 12009,
        "NT_VMWARE_FOLDER": 12010,
        "NT_VMWARE_DATACENTER": 12011,
        "NT_VMWARE_VMFOLDER": 12012,
        "NT_HYPERV_ROOT": 13000,
        "NT_HYPERV_PLAT": 13001,
        "NT_HYPERV_VM": 13002,
        "NT_MAIL_ROOT": 14000,
        "NT_MAIL_USER": 14001,
        "NT_MAIL_CLIENT": 14002,
        "NT_CAS_ROOT": 15000,
        "NT_CAS_PLAT": 15001,
        "NT_CAS_HOSTPOOL": 15002,
        "NT_CAS_CLUSTER": 15003,
        "NT_CAS_HOST": 15004,
        "NT_CAS_VM": 15005,
        "NT_CAS_CLUSTER_VM": 15006,
        "NT_OPENSTACK_PLATE": 16000,
        "NT_OPENSTACK_PROJECT": 16001,
        "NT_OPENSTACK_REGION": 16002,
        "NT_OPENSTACK_USER": 16003,
        "NT_OPENSTACK_VM": 16004,
        "NT_VOLCDP_ROOT": 20000,
        "NT_VOLCDP_VOL": 20001,
        "NT_FUSION_UNDEFINE": 21000,
        "NT_FUSION_ROOT": 21001,
        "NT_FUSION_SITE": 21002,
        "NT_FUSION_CLUSTER_FOLDER": 21003,
        "NT_FUSION_CLUSTER": 21004,
        "NT_FUSION_HOST": 21005,
        "NT_FUSION_VM": 21006,
        "NT_WINCENTER_ROOT": 23000,
        "NT_WINCENTER_RSC": 23001,
        "NT_WINCENTER_HOST": 23002,
        "NT_WINCENTER_VM": 23003,
        "NT_INSPUR_POOL": 26000,
        "NT_INSPUR_HOST": 26001,
        "NT_INSPUR_VM": 26002,
        "NT_INSPUR_UNDEFINE": 26003,
        "NT_VOLUME": 27000,
        "NC_HWCLOUD_TENANT": 28001,
        "NC_HWCLOUD_REGION": 28002,
        "NC_HWCLOUD_PROJECT": 28003,
        "NC_HWCLOUD_VM": 28004,
        "NT_ACLOUD_ROOT": 30000,
        "NT_ACLOUD_PLAT": 30001,
        "NT_ACLOUD_GROUP": 30002,
        "NT_ACLOUD_VM": 30003,
        "NT_POSTGRESQL_ROOT": 31000,
        "NT_POSTGRESQL_INST": 31001,
        "NT_MONGODB_ROOT": 8000,
        "NT_MONGODB_INST": 8001,
        "NT_MONGODB_DB": 8002,
        "NT_KINGBASE_ROOT": 31000,
        "NT_KINGBASE_INST": 31001,
    }


class ncPathType(object):
    NP_FILE_ATR = 1
    NP_DIRE_ATR = 2
    NP_LOGICAL_ATR = 3

    _VALUES_TO_NAMES = {
        1: "NP_FILE_ATR",
        2: "NP_DIRE_ATR",
        3: "NP_LOGICAL_ATR",
    }

    _NAMES_TO_VALUES = {
        "NP_FILE_ATR": 1,
        "NP_DIRE_ATR": 2,
        "NP_LOGICAL_ATR": 3,
    }


class ncBackupType(object):
    FULL_BACKUP = 1
    INCRE_BACKUP = 2
    DIFF_BACKUP = 3
    LOG_BACKUP = 4
    FORE_INCRE_BACKUP = 5
    CHEAT_FULL_BACKUP = 6

    _VALUES_TO_NAMES = {
        1: "FULL_BACKUP",
        2: "INCRE_BACKUP",
        3: "DIFF_BACKUP",
        4: "LOG_BACKUP",
        5: "FORE_INCRE_BACKUP",
        6: "CHEAT_FULL_BACKUP",
    }

    _NAMES_TO_VALUES = {
        "FULL_BACKUP": 1,
        "INCRE_BACKUP": 2,
        "DIFF_BACKUP": 3,
        "LOG_BACKUP": 4,
        "FORE_INCRE_BACKUP": 5,
        "CHEAT_FULL_BACKUP": 6,
    }


class ncBackupMediaTypeEnum(object):
    OFS = 1
    CLOUD_STORAGE = 2
    TAPE = 3

    _VALUES_TO_NAMES = {
        1: "OFS",
        2: "CLOUD_STORAGE",
        3: "TAPE",
    }

    _NAMES_TO_VALUES = {
        "OFS": 1,
        "CLOUD_STORAGE": 2,
        "TAPE": 3,
    }


class ncRetentionUnitType(object):
    NT_DAY_TYPE = 0
    NT_WEEK_TYPE = 1
    NT_MONTH_TYPE = 2
    NT_YEAR_TYPE = 3

    _VALUES_TO_NAMES = {
        0: "NT_DAY_TYPE",
        1: "NT_WEEK_TYPE",
        2: "NT_MONTH_TYPE",
        3: "NT_YEAR_TYPE",
    }

    _NAMES_TO_VALUES = {
        "NT_DAY_TYPE": 0,
        "NT_WEEK_TYPE": 1,
        "NT_MONTH_TYPE": 2,
        "NT_YEAR_TYPE": 3,
    }


class ncFingerPrintTypeEnum(object):
    COMMON = 0
    DATABASE = 1
    VIRTUAL = 2
    VOLUME = 3

    _VALUES_TO_NAMES = {
        0: "COMMON",
        1: "DATABASE",
        2: "VIRTUAL",
        3: "VOLUME",
    }

    _NAMES_TO_VALUES = {
        "COMMON": 0,
        "DATABASE": 1,
        "VIRTUAL": 2,
        "VOLUME": 3,
    }


class ncTaskType(object):
    BACKUP = 1
    CDM = 2
    CDP = 3

    _VALUES_TO_NAMES = {
        1: "BACKUP",
        2: "CDM",
        3: "CDP",
    }

    _NAMES_TO_VALUES = {
        "BACKUP": 1,
        "CDM": 2,
        "CDP": 3,
    }


class ncPublicCloudType(object):
    HWCloud = 1

    _VALUES_TO_NAMES = {
        1: "HWCloud",
    }

    _NAMES_TO_VALUES = {
        "HWCloud": 1,
    }


class ncLoadBalanceType(object):
    SINGLE = 0
    ALL = 1
    CHECK = 2

    _VALUES_TO_NAMES = {
        0: "SINGLE",
        1: "ALL",
        2: "CHECK",
    }

    _NAMES_TO_VALUES = {
        "SINGLE": 0,
        "ALL": 1,
        "CHECK": 2,
    }


class ncLoadBalanceDatabaseStatusType(object):
    FAILED = 0
    SUCCESS = 1
    RUNNING = 2
    READY = 3

    _VALUES_TO_NAMES = {
        0: "FAILED",
        1: "SUCCESS",
        2: "RUNNING",
        3: "READY",
    }

    _NAMES_TO_VALUES = {
        "FAILED": 0,
        "SUCCESS": 1,
        "RUNNING": 2,
        "READY": 3,
    }


class ncLoadBalanceStatusType(object):
    FAILED = 0
    SUCCESS = 1
    PARTIAL = 2
    RUNNING = 3
    NOTHING = 4

    _VALUES_TO_NAMES = {
        0: "FAILED",
        1: "SUCCESS",
        2: "PARTIAL",
        3: "RUNNING",
        4: "NOTHING",
    }

    _NAMES_TO_VALUES = {
        "FAILED": 0,
        "SUCCESS": 1,
        "PARTIAL": 2,
        "RUNNING": 3,
        "NOTHING": 4,
    }


class ncClientLoadBalanceStatusType(object):
    NORMAL = 0
    LOADING = 1

    _VALUES_TO_NAMES = {
        0: "NORMAL",
        1: "LOADING",
    }

    _NAMES_TO_VALUES = {
        "NORMAL": 0,
        "LOADING": 1,
    }
fix_spec(all_structs)
del all_structs
