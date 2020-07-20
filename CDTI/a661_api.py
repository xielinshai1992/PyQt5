# -*- coding: utf-8 -*-
from ctypes import *


class A661_NOTIFY_WIDGET_EVENT_12BYTE(Structure):
    _pack_ = 1
    _fields_ = [("A661_NOTIFY_WIDGET_EVENT", c_ushort),
                ("CommandSize", c_ushort),
                ("WidgetIdent", c_ushort),
                ("EventOrigin", c_ushort),
                ("EventID", c_ushort),
                ("UnusedPad", c_char * 146)]

class CDTI_TO_UA_WIDGET_EVENT_DATA(Structure):
    _pack_ = 1  #1字节对齐
    _fields_ = [("A661_BEGIN_BLOCK", c_char),
                ("LayerIdent", c_char),
                ("ContextNumber",c_ushort),
                ("BlockSize",c_ulong),
                ("Compass_InOut_Click_Envent",A661_NOTIFY_WIDGET_EVENT_12BYTE),
                ("A661_END_BLOCK", c_char),
                ("Unused1", c_char * 3)]
    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)


class A661_CMD_SET_PARAMATER_12BYTE(Structure):
    _pack_ = 1
    _fields_ = [("A661_CMD_SET_PARAMETER", c_ushort),
                ("CommandSize", c_ushort),
                ("WidgetIdent", c_ushort),
                ("UnusedPad", c_ushort),
                ("ParameterIdent",c_ushort),
                ("ParameterValueBuffer",c_ushort)]

class A661_CMD_SET_PARAMATER_16BYTE(Structure):
    _pack_ = 1
    _fields_ = [("A661_CMD_SET_PARAMETER", c_ushort),
                ("CommandSize", c_ushort),
                ("WidgetIdent", c_ushort),
                ("UnusedPad", c_ushort),
                ("ParameterIdent",c_ushort),
                ("ParameterValueBuffer",c_char*6)]

class A661_CMD_SET_PARAMATER_16BYTE_FLOAT(Structure):
    _pack_ = 1
    _fields_ = [("A661_CMD_SET_PARAMETER", c_ushort),
                ("CommandSize", c_ushort),
                ("WidgetIdent", c_ushort),
                ("UnusedPad1", c_ushort),
                ("ParameterIdent",c_ushort),
                ("ParameterValueBuffer",c_float),
                ("UnusedPad2", c_ushort)]

class A661_CMD_SET_PARAMATER_20BYTE_2FLOAT(Structure):
    _pack_ = 1
    _fields_ = [("A661_CMD_SET_PARAMETER", c_ushort),
                ("CommandSize", c_ushort),
                ("WidgetIdent", c_ushort),
                ("UnusedPad1", c_ushort),
                ("ParameterIdent", c_ushort),
                ("ParameterValueBuffer", c_float),#南北速度
                ("ParameterValueBuffer2", c_float),#东西速度
                ("UnusedPad2", c_ushort)]

class A661_CMD_SET_PARAMATER_16BYTE_INT(Structure):
    _pack_ = 1
    _fields_ = [("A661_CMD_SET_PARAMETER", c_ushort),
                ("CommandSize", c_ushort),
                ("WidgetIdent", c_ushort),
                ("UnusedPad1", c_ushort),
                ("ParameterIdent",c_ushort),
                ("ParameterValueBuffer",c_int),
                ("UnusedPad2", c_ushort)]

class TARGET_INFO(Structure):
    _pack_ = 1
    _fields_ = [("Target_Visible_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE), #short 1可见 0不可见
                ("Target_Pic_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),      #short 飞机图标类型
                ("Target_RotateAngle_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_FLOAT),#float deg
                ("Target_X_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE), #short 640*640
                ("Target_Y_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE), #short
                ("Target_FlightId_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),#string
                ("Target_Speed_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_FLOAT),#short ft
                ("Target_Alt_dif_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_INT),#short feet
                ("Target_Status_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),#short 1=AIR 2=GROUND
                ("Target_AppStatus_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),#short 第0位 AIRB应用有效状态 第1位SURF应用有效状态 第2位VSA应用有效状态 第3位ITP应用有效状态，0无效1有效
                ("Target_Lon_SET_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_FLOAT),#float
                ("Target_Lat_SET_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_FLOAT),#float
                ("Target_VSA_DIS_PARAMATER",A661_CMD_SET_PARAMATER_16BYTE_FLOAT),#float nm
                ("Target_VSA_Velocity_PARAMATER", A661_CMD_SET_PARAMATER_20BYTE_2FLOAT),#float ft
                ("Target_ITP_DIS_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_FLOAT),#float nm
                ("Target_ITP_DIS_RATE_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_FLOAT), #float ft
                ("Target_ITP_FORWARD_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE), #short 1相对本机前 2相对本机后
                ("Target_ITP_Geometry_Status_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE)]#short 1有效 0无效

class UA_TO_CDTI_DATA(Structure):
    _pack_ = 1  #1字节对齐
    _fields_ = [("A661_BEGIN_BLOCK", c_char),
                ("LayerIdent", c_char),
                ("ContextNumber",c_ushort),
                ("BlockSize",c_ulong),
                ("Ownship_TOA_TIME_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_FLOAT),  # float deg
                ("Compass_Bitmap_SET_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),  #short deg
                ("Compass_Step_SET_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),  #short  nm
                ("Ownship_FlightId_SET_PARAMATER",A661_CMD_SET_PARAMATER_16BYTE),  #string
                ("Ownship_Alt_SET_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),  #short feet
                ("Ownship_Lon_SET_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_FLOAT),  #float
                ("Ownship_Lat_SET_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE_FLOAT),  #float
                ("Ownship_Alt_Range_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),  #short feet
                ("Ownship_Course_Angle_PARAMATER",A661_CMD_SET_PARAMATER_16BYTE_FLOAT),  #float deg
                ("Ownship_App_Status_PARAMATER",A661_CMD_SET_PARAMATER_12BYTE),  #short 1有效 0无效
                ("Target_Lists", TARGET_INFO*5),
                ("A661_END_BLOCK",c_char),
                ("Unused1",c_char*3)]
    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)
print(sizeof(UA_TO_CDTI_DATA))
print(sizeof(CDTI_TO_UA_WIDGET_EVENT_DATA))