# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: types.py
from types import *
MSG_KEY_PARAMS_QUERY = 65536
MSG_KEY_PARAMS_QUERY_SCHEDULER_TYPE = 65537
MSG_KEY_PARAMS_QUERY_TARGET = 65538
MSG_KEY_PARAMS_QUERY_FOLDER = 65539
MSG_KEY_PARAMS_ADD = 131072
MSG_KEY_PARAMS_ADD_SCHEDULER_TYPE = 131073
MSG_KEY_PARAMS_ADD_INTERVAL = 131074
MSG_KEY_PARAMS_ADD_TARGET = 131075
MSG_KEY_PARAMS_ADD_COMMAND = 131076
MSG_KEY_PARAMS_ADD_FOLDER = 131077
MSG_KEY_PARAMS_DELETE = 196608
MSG_KEY_PARAMS_DELETE_SCHEDULER_TYPE = 196609
MSG_KEY_PARAMS_DELETE_JOB = 196610
MSG_KEY_PARAMS_DELETE_TARGET = 196611
MSG_KEY_RESULT_ADD = 262144
MSG_KEY_RESULT_ADD_JOB_ID = 262145
MSG_KEY_RESULT_ATJOB = 327680
MSG_KEY_RESULT_ATJOB_INFO = 327681
MSG_KEY_RESULT_ATJOB_INFO_JOB_ID = 327682
MSG_KEY_RESULT_ATJOB_INFO_JOB_TIME = 327683
MSG_KEY_RESULT_ATJOB_INFO_DAYS_OF_MONTH = 327684
MSG_KEY_RESULT_ATJOB_INFO_DAYS_OF_WEEK = 327685
MSG_KEY_RESULT_ATJOB_INFO_FLAGS = 327686
MSG_KEY_RESULT_ATJOB_INFO_COMMAND = 327687
MSG_KEY_RESULT_NETJOB = 393216
MSG_KEY_RESULT_NETJOB_TRIGGER = 393217
MSG_KEY_RESULT_NETJOB_INFO = 393218
MSG_KEY_RESULT_NETJOB_INFO_NEXT_RUN = 393219
MSG_KEY_RESULT_NETJOB_INFO_FLAGS = 393220
MSG_KEY_RESULT_NETJOB_INFO_EXIT_CODE = 393221
MSG_KEY_RESULT_NETJOB_INFO_NUM_TRIGGERS = 393222
MSG_KEY_RESULT_NETJOB_INFO_JOB_NAME = 393223
MSG_KEY_RESULT_NETJOB_INFO_DISPLAY_NAME = 393224
MSG_KEY_RESULT_NETJOB_INFO_PARAMETERS = 393225
MSG_KEY_RESULT_NETJOB_INFO_ACCOUNT_NAME = 393226
MSG_KEY_RESULT_TASKSERVICE_FOLDER = 458752
MSG_KEY_RESULT_TASKSERVICE_FOLDER_INFO = 458753
MSG_KEY_RESULT_TASKSERVICE_FOLDER_INFO_NAME = 458754
MSG_KEY_RESULT_TASKSERVICE_FOLDER_INFO_PATH = 458755
MSG_KEY_RESULT_TASKSERVICEJOB = 524288
MSG_KEY_RESULT_TASKSERVICEJOB_INFO = 524289
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_FLAGS = 524290
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_NAME = 524291
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_LASTRUNTIME = 524292
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_LASTRUNRESULT = 524293
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_NEXTRUNTIME = 524294
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_PATH = 524295
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_STATE = 524296
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_XML = 524297
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_NUMMISSEDRUNS = 524298
MSG_KEY_RESULT_TASKSERVICEJOB_INFO_COMPATIBILITY = 524299
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION = 589824
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_INFO = 589825
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_INFO_ID = 589826
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_INFO_TYPE = 589827
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC = 655360
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC_ARGUMENTS = 655361
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC_PATH = 655362
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_EXEC_WORKINGDIR = 655363
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM = 720896
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM_CLASSID = 720897
MSG_KEY_RESULT_TASKSERVICEJOB_ACTION_COM_DATA = 720898
MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL = 786432
MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_DISPLAYNAME = 786433
MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_GROUPID = 786434
MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_ID = 786435
MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_LOGONTYPE = 786436
MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_RUNLEVEL = 786437
MSG_KEY_RESULT_TASKSERVICEJOB_PRINCIPAL_USERID = 786438
MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION = 851968
MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION_STOP_AT_DURATION_END = 851969
MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION_DURATION = 851970
MSG_KEY_RESULT_TASKSERVICEJOB_REPETITION_INTERVAL = 851971
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER = 917504
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_ENABLED = 917505
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_ID = 917506
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TYPE = 917507
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_START_BOUNDARY = 917508
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_END_BOUNDARY = 917509
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EXEC_TIME_LIMIT = 917510
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REPETITION = 917511
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EVENT = 983040
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_EVENT_SUBSCRIPTION = 983041
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TIME = 1048576
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_TIME_RANDOM_DELAY = 1048577
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY = 1114112
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY_RANDOM_DELAY = 1114113
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_DAILY_DAYS_INTERVAL = 1114114
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY = 1179648
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY_RANDOM_DELAY = 1179649
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_WEEKLY_DAYS_OF_WEEK = 1179650
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY = 1245184
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_RANDOM_DELAY = 1245185
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_DAYS_OF_MONTH = 1245186
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_MONTHS_OF_YEAR = 1245187
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLY_RUN_ON_LAST_DAY_OF_MONTH = 1245188
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW = 1310720
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_RANDOM_DELAY = 1310721
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_DAYS_OF_WEEK = 1310722
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_MONTHS_OF_YEAR = 1310723
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_WEEKS_OF_MONTH = 1310724
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_MONTHLYDOW_RUN_ON_LAST_WEEK_OF_MONTH = 1310725
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REGISTRATION = 1376256
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_REGISTRATION_DELAY = 1376257
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_BOOT = 1441792
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_BOOT_DELAY = 1441793
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON = 1507328
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON_DELAY = 1507329
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_LOGON_USER_ID = 1507330
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE = 1638400
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE_DELAY = 1638401
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE_USER_ID = 1638402
MSG_KEY_RESULT_TASKSERVICEJOB_TRIGGER_SESSION_STATE_CHANGE_CHANGE = 1638403