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


class ncStrategyType(object):
    PTOS = 1
    STOD = 2
    DTOC = 3

    _VALUES_TO_NAMES = {
        1: "PTOS",
        2: "STOD",
        3: "DTOC",
    }

    _NAMES_TO_VALUES = {
        "PTOS": 1,
        "STOD": 2,
        "DTOC": 3,
    }
fix_spec(all_structs)
del all_structs
