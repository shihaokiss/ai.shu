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


class ncEEFEventType(object):
    NOTIFY_EVENT = 1
    TAKEOVER_EVENT = 2
    EXERCISE_EVENT = 3

    _VALUES_TO_NAMES = {
        1: "NOTIFY_EVENT",
        2: "TAKEOVER_EVENT",
        3: "EXERCISE_EVENT",
    }

    _NAMES_TO_VALUES = {
        "NOTIFY_EVENT": 1,
        "TAKEOVER_EVENT": 2,
        "EXERCISE_EVENT": 3,
    }
fix_spec(all_structs)
del all_structs
