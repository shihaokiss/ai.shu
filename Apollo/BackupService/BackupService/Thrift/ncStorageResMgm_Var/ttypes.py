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


class ncVolumeStatus(object):
    ALL = 0
    ABNORMAL = 1
    NORMAL = 2
    CREATING = 3
    DELETING = 4
    EDITING = 5
    MIRATING = 6

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "ABNORMAL",
        2: "NORMAL",
        3: "CREATING",
        4: "DELETING",
        5: "EDITING",
        6: "MIRATING",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "ABNORMAL": 1,
        "NORMAL": 2,
        "CREATING": 3,
        "DELETING": 4,
        "EDITING": 5,
        "MIRATING": 6,
    }


class ncDispatchStatus(object):
    ALL = 0
    UNASSIGN = 1
    ASSIGNING = 2
    ASSIGNED = 3

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "UNASSIGN",
        2: "ASSIGNING",
        3: "ASSIGNED",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "UNASSIGN": 1,
        "ASSIGNING": 2,
        "ASSIGNED": 3,
    }


class ncApplicationVolumeType(object):
    ALL = 0
    OFS = 1
    DDCACHE = 2
    METADATA = 3
    CLOUDINDEX = 4
    SELFBACKUP = 5
    TAPEINDEX = 6
    SFTP = 7
    BLUERAY = 8
    NAUTILUSDB = 9
    SNAPMETA = 10

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "OFS",
        2: "DDCACHE",
        3: "METADATA",
        4: "CLOUDINDEX",
        5: "SELFBACKUP",
        6: "TAPEINDEX",
        7: "SFTP",
        8: "BLUERAY",
        9: "NAUTILUSDB",
        10: "SNAPMETA",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "OFS": 1,
        "DDCACHE": 2,
        "METADATA": 3,
        "CLOUDINDEX": 4,
        "SELFBACKUP": 5,
        "TAPEINDEX": 6,
        "SFTP": 7,
        "BLUERAY": 8,
        "NAUTILUSDB": 9,
        "SNAPMETA": 10,
    }


class ncDataTransferIpType(object):
    EOSS = 0
    NAUTILUS = 1
    STORAGENAUTILUS = 2

    _VALUES_TO_NAMES = {
        0: "EOSS",
        1: "NAUTILUS",
        2: "STORAGENAUTILUS",
    }

    _NAMES_TO_VALUES = {
        "EOSS": 0,
        "NAUTILUS": 1,
        "STORAGENAUTILUS": 2,
    }


class ncFileSystemType(object):
    XFS = 0
    EXT2 = 1
    EXT3 = 2
    EXT4 = 3
    CIFS = 4
    NFS = 5
    NFS4 = 6
    CEPH = 7

    _VALUES_TO_NAMES = {
        0: "XFS",
        1: "EXT2",
        2: "EXT3",
        3: "EXT4",
        4: "CIFS",
        5: "NFS",
        6: "NFS4",
        7: "CEPH",
    }

    _NAMES_TO_VALUES = {
        "XFS": 0,
        "EXT2": 1,
        "EXT3": 2,
        "EXT4": 3,
        "CIFS": 4,
        "NFS": 5,
        "NFS4": 6,
        "CEPH": 7,
    }


class ncStorageType(object):
    SOFT = 0
    RAID = 1
    FSB = 2
    ALL = 3

    _VALUES_TO_NAMES = {
        0: "SOFT",
        1: "RAID",
        2: "FSB",
        3: "ALL",
    }

    _NAMES_TO_VALUES = {
        "SOFT": 0,
        "RAID": 1,
        "FSB": 2,
        "ALL": 3,
    }


class ncProductType(object):
    ALL = 0
    AB = 1
    HW = 2

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "AB",
        2: "HW",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "AB": 1,
        "HW": 2,
    }


class ncTaskStatus(object):
    ALL = 0
    RUNNING = 1
    SUCCEED = 2
    FAILED = 3

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "RUNNING",
        2: "SUCCEED",
        3: "FAILED",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "RUNNING": 1,
        "SUCCEED": 2,
        "FAILED": 3,
    }


class ncTaskType(object):
    ALL = 0
    CREATE_VOLUME = 1
    GET_DISK = 20
    PUT_DISK = 21
    POST_SPARE_DISK = 22
    DELETE_SPARE_DISK = 23
    GET_DATA_TRANSFER_IPS = 24
    PUT_DATA_TRANSFER_IPS = 25
    POST_DATA_TRANSFER_IPS = 26
    DELETE_DATA_TRANSFER_IPS = 27
    POST_RAID = 50
    PUT_RAID = 51
    DELETE_RAID = 52
    POST_RAID_SPARE = 53
    DELETE_RAID_SPARE = 54
    REBUILD_RAID = 55

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "CREATE_VOLUME",
        20: "GET_DISK",
        21: "PUT_DISK",
        22: "POST_SPARE_DISK",
        23: "DELETE_SPARE_DISK",
        24: "GET_DATA_TRANSFER_IPS",
        25: "PUT_DATA_TRANSFER_IPS",
        26: "POST_DATA_TRANSFER_IPS",
        27: "DELETE_DATA_TRANSFER_IPS",
        50: "POST_RAID",
        51: "PUT_RAID",
        52: "DELETE_RAID",
        53: "POST_RAID_SPARE",
        54: "DELETE_RAID_SPARE",
        55: "REBUILD_RAID",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "CREATE_VOLUME": 1,
        "GET_DISK": 20,
        "PUT_DISK": 21,
        "POST_SPARE_DISK": 22,
        "DELETE_SPARE_DISK": 23,
        "GET_DATA_TRANSFER_IPS": 24,
        "PUT_DATA_TRANSFER_IPS": 25,
        "POST_DATA_TRANSFER_IPS": 26,
        "DELETE_DATA_TRANSFER_IPS": 27,
        "POST_RAID": 50,
        "PUT_RAID": 51,
        "DELETE_RAID": 52,
        "POST_RAID_SPARE": 53,
        "DELETE_RAID_SPARE": 54,
        "REBUILD_RAID": 55,
    }


class ncThirdPartyStorageStatus(object):
    ALL = 0
    ABNORMAL = 1
    NORMAL = 2

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "ABNORMAL",
        2: "NORMAL",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "ABNORMAL": 1,
        "NORMAL": 2,
    }


class ncPoolStatus(object):
    ALL = 0
    ABNORMAL = 1
    NORMAL = 2
    STOPPED = 3
    UNKNOW = 4
    DEGRADATION = 5
    CREATING = 6
    DELETING = 7

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "ABNORMAL",
        2: "NORMAL",
        3: "STOPPED",
        4: "UNKNOW",
        5: "DEGRADATION",
        6: "CREATING",
        7: "DELETING",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "ABNORMAL": 1,
        "NORMAL": 2,
        "STOPPED": 3,
        "UNKNOW": 4,
        "DEGRADATION": 5,
        "CREATING": 6,
        "DELETING": 7,
    }


class ncRedundancyPolicy(object):
    ALL = 0
    REPLICATION = 1
    EC = 2

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "REPLICATION",
        2: "EC",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "REPLICATION": 1,
        "EC": 2,
    }


class ncSecurityLevel(object):
    ALL = 0
    RACK = 1
    SERVER = 2

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "RACK",
        2: "SERVER",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "RACK": 1,
        "SERVER": 2,
    }


class ncStorageMediaType(object):
    ALL = 0
    SATA = 1

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "SATA",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "SATA": 1,
    }


class ncCacheMediaType(object):
    ALL = 0
    SSD_CARD = 1
    SSD_DISK = 2

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "SSD_CARD",
        2: "SSD_DISK",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "SSD_CARD": 1,
        "SSD_DISK": 2,
    }


class ncDiskStatus(object):
    HOT_SPARE = 0
    UNCONFIGURE_GOOD = 1
    UNCONFIGURE_BAD = 2
    ONLINE = 3
    REBUILDING = 4
    FAILED = 5
    MISSING = 6
    OFFLINE = 7
    COPYBACK = 8
    INITIALIZATION = 9
    CREATING_HOTSPARE = 10
    DELETING_HOTSPARE = 11

    _VALUES_TO_NAMES = {
        0: "HOT_SPARE",
        1: "UNCONFIGURE_GOOD",
        2: "UNCONFIGURE_BAD",
        3: "ONLINE",
        4: "REBUILDING",
        5: "FAILED",
        6: "MISSING",
        7: "OFFLINE",
        8: "COPYBACK",
        9: "INITIALIZATION",
        10: "CREATING_HOTSPARE",
        11: "DELETING_HOTSPARE",
    }

    _NAMES_TO_VALUES = {
        "HOT_SPARE": 0,
        "UNCONFIGURE_GOOD": 1,
        "UNCONFIGURE_BAD": 2,
        "ONLINE": 3,
        "REBUILDING": 4,
        "FAILED": 5,
        "MISSING": 6,
        "OFFLINE": 7,
        "COPYBACK": 8,
        "INITIALIZATION": 9,
        "CREATING_HOTSPARE": 10,
        "DELETING_HOTSPARE": 11,
    }


class ncRaidStatus(object):
    NORMAL = 1
    DEGRADATION = 2
    ABNORMAL = 3
    REBUILDING = 4
    CREATING = 5
    PART_DEGRADATION = 6
    EDITING = 7
    SETTING_SPARE_DISK = 8
    CANCEL_SPARE_DISK = 9
    DELETING = 10

    _VALUES_TO_NAMES = {
        1: "NORMAL",
        2: "DEGRADATION",
        3: "ABNORMAL",
        4: "REBUILDING",
        5: "CREATING",
        6: "PART_DEGRADATION",
        7: "EDITING",
        8: "SETTING_SPARE_DISK",
        9: "CANCEL_SPARE_DISK",
        10: "DELETING",
    }

    _NAMES_TO_VALUES = {
        "NORMAL": 1,
        "DEGRADATION": 2,
        "ABNORMAL": 3,
        "REBUILDING": 4,
        "CREATING": 5,
        "PART_DEGRADATION": 6,
        "EDITING": 7,
        "SETTING_SPARE_DISK": 8,
        "CANCEL_SPARE_DISK": 9,
        "DELETING": 10,
    }


class ncDeleteSpareDiskSystemLogType(object):
    GLOBAL_SPARE_DISK = 0
    SPECIFIC_SPARE_DISK = 1

    _VALUES_TO_NAMES = {
        0: "GLOBAL_SPARE_DISK",
        1: "SPECIFIC_SPARE_DISK",
    }

    _NAMES_TO_VALUES = {
        "GLOBAL_SPARE_DISK": 0,
        "SPECIFIC_SPARE_DISK": 1,
    }


class ncNASStatus(object):
    ALL = 0
    ABNORMAL = 1
    NORMAL = 2
    CREATING = 3
    DELETING = 4

    _VALUES_TO_NAMES = {
        0: "ALL",
        1: "ABNORMAL",
        2: "NORMAL",
        3: "CREATING",
        4: "DELETING",
    }

    _NAMES_TO_VALUES = {
        "ALL": 0,
        "ABNORMAL": 1,
        "NORMAL": 2,
        "CREATING": 3,
        "DELETING": 4,
    }
fix_spec(all_structs)
del all_structs
