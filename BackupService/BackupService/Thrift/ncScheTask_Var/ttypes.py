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


class ncScheStatus(object):
    INVALID = 0
    RUNNING = 1
    PAUSE = 2

    _VALUES_TO_NAMES = {
        0: "INVALID",
        1: "RUNNING",
        2: "PAUSE",
    }

    _NAMES_TO_VALUES = {
        "INVALID": 0,
        "RUNNING": 1,
        "PAUSE": 2,
    }


class ncPlanType(object):
    ONCE = 1
    DAILY = 2
    WEEKLY = 3
    MONTH = 4
    YEARLY = 5
    TASK = 0

    _VALUES_TO_NAMES = {
        1: "ONCE",
        2: "DAILY",
        3: "WEEKLY",
        4: "MONTH",
        5: "YEARLY",
        0: "TASK",
    }

    _NAMES_TO_VALUES = {
        "ONCE": 1,
        "DAILY": 2,
        "WEEKLY": 3,
        "MONTH": 4,
        "YEARLY": 5,
        "TASK": 0,
    }


class ncTriggerMode(object):
    TIME_MODE = 1
    TASK_MODE = 2

    _VALUES_TO_NAMES = {
        1: "TIME_MODE",
        2: "TASK_MODE",
    }

    _NAMES_TO_VALUES = {
        "TIME_MODE": 1,
        "TASK_MODE": 2,
    }


class ncTimeUnit(object):
    SECOND = 0
    MINUTE = 1
    HOUR = 2
    DAY = 3
    WEEK = 4
    MONTH = 5
    YEAR = 6
    UNLIMITED_TIME = -1

    _VALUES_TO_NAMES = {
        0: "SECOND",
        1: "MINUTE",
        2: "HOUR",
        3: "DAY",
        4: "WEEK",
        5: "MONTH",
        6: "YEAR",
        -1: "UNLIMITED_TIME",
    }

    _NAMES_TO_VALUES = {
        "SECOND": 0,
        "MINUTE": 1,
        "HOUR": 2,
        "DAY": 3,
        "WEEK": 4,
        "MONTH": 5,
        "YEAR": 6,
        "UNLIMITED_TIME": -1,
    }


class ncNeedInterval(object):
    NO = 0
    YES = 1

    _VALUES_TO_NAMES = {
        0: "NO",
        1: "YES",
    }

    _NAMES_TO_VALUES = {
        "NO": 0,
        "YES": 1,
    }
fix_spec(all_structs)
del all_structs
