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
from ttypes import *

EEF_STOP_EXECUTE = "msg://eef/server/stopexecute"
EEF_CHECK_EXEC = "msg://eef/server/checkexec"
EEF_WATCH_EXEC = "msg://eef/server/watchexec"
EEF_START_EXECUTE = "msg://eef/server/startexecute"
EEF_REPLY_CHECK = "msg://eef/client/replycheck"
EEF_BODY_CONNECT_MSG = "msg://eef/client/connect"
EEF_BODY_RECONNECT_CHECK_MSG = "msg://eef/client/reconnectcheck"
EEF_EXEC_MESSAGE = "msg://eef/client/execmessage"
EEF_EXEC_EXCEPTION = "msg://eef/client/execerror"
EEF_EXEC_STATUS = "msg://eef/client/execstatus"
EEF_EXEC_PROGRESS = "msg://eef/client/execprogress"
EEF_EXEC_REPORT = "msg://eef/client/execreport"
EEF_EXEC_START = "msg://eef/client/execstart"
EEF_EXEC_ALARM = "msg://eef/client/execalarm"
EEF_EXEC_TASK = "msg://eef/client/exectaskinfo"
EEF_CDM_EXEC_TASK = "msg://eef/client/execcdmtaskinfo"
EEF_EXEC_OBJECT = "msg://eef/client/execobjectinfo"
EEF_EXEC_ALL_OBJECT = "msg://eef/client/execallobjectinfo"
EEF_HAS_CONNECTED_WITH_CLIENT_SOCKET = "msg://eef/client/hasconnectedwithclientsocket"
EEF_PAUSE_EXECUTE = "msg://eef/server/pauseexecute"
EEF_TASK_EXCEPTION = "msg://eef/client/taskerror"
EEE_GAUSSDB_METADATA_RESTORE_OVER = "msg://eef/client/gaussdbmetadatarestoreover"
EEF_GAUSSDB_REPLY_STATUS = "msg://eef/client/gaussdbreplystatus"
EEF_OPENSTACK_ACTION = "msg://eef/client/openstackaction"
EEF_BODY_CREATE_BACKUP_LUN_MAPPING_MSG = "msg://eef/client/createbackuplunmapping"
EEF_BODY_DELETE_BACKUP_LUN_MAPPING_MSG = "msg://eef/client/deletebackuplunmapping"
EEE_VCP_UPDATE_DATASOURCE = "msg://eef/client/vcpdatasourceupdate"
EEF_RESTART_EXECUTE = "msg://eef/server/restartexecute"
EEF_ABORT_RESTART_EXECUTE = "msg://eef/server/abortrestartexecute"
EEF_RECOVER_EXECUTE = "msg://eef/server/recoverexecute"
EEF_RESET_JOBINFO = "msg://eef/server/resetjobinfo"
EEF_EXEC_WAITING_RECOVER = "msg://eef/client/execwaitrecover"
EEF_UPDATE_JOB_TIMEPINTS_REPORTS = "msg://eef/client/updatejobtpreports"
EEF_BODY_SET_EXTRA_METADATA_MSG = "msg://eef/client/setextrametadata"
EEF_BODY_GET_EXTRA_METADATA_MSG = "msg://eef/client/getextrametadata"
EEF_BODY_CREATE_CDM_LUN_MSG = "msg://eef/client/createcdmlun"
EEF_BODY_CREATE_CDM_LUN_MAPPING_MSG = "msg://eef/client/createcdmlunmapping"
EEF_BODY_CHECK_CDM_LUN_MAPPING_MSG = "msg://eef/client/checkcdmlunmapping"
EEF_BODY_GET_JOB_CDM_LUN_INFO_MSG = "msg://eef/client/getcdmluninfo"
EEF_BODY_UPDATE_CDM_LUN_INFO_MSG = "msg://eef/client/updatecdmluninfo"
EEF_BODY_CDM_VM_RECORED_RESTORED_VMS = "msg://eef/client/recoredrestoredvms"
EEF_BODY_DELETE_CDM_LUN_MAPPING_MSG = "msg://eef/client/deletecdmlunmapping"
EEF_BODY_CHECK_DELETE_CDM_LUN_MAPPING_MSG = "msg://eef/client/checkdeletecdmlunmapping"
EEF_BODY_CDM_UPDATE_IMAGE_CUSTOMER = "msg://eef/client/updateimagecustomer"
EEE_BODY_VCP_UPDATE_DATASOURCE = "msg://eef/client/vmwaredatasourceupdate"
EEF_BODY_TIMEPOINTS_INFO_MSG = "msg://eef/client/timepiontinfo"
EEF_BODY_GET_MONGODBBACKUP_INFO_MSG = "msg://eef/client/getmongodbbackupinfo"
EEF_BODY_UPDATE_MONGODBBACKUP_INFO_MSG = "msg://eef/client/updatemongodbbackupinfo"
EEF_BODY_REDUNDANCY_GET_MSG = "msg://eef/client/getredundancy"
EEF_BODY_REDUNDANCY_CREATE_MSG = "msg://eef/client/createredundancy"
