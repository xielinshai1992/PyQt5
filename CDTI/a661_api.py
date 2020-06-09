# -*- coding: utf-8 -*-
from ctypes import *


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

class UA_TO_CDTI_DATA(Structure):
    _pack_ = 1  #1字节对齐
    _fields_ = [("A661_BEGIN_BLOCK", c_char),
                ("LayerIdent", c_char),
                ("ContextNumber",c_ushort),
                ("BlockSize",c_ulong),
                ("Compass_Bitmap_SET_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Compass_Step_SET_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Ownship_FlightId_SET_PARAMATER",A661_CMD_SET_PARAMATER_16BYTE),
                ("Ownship_Alt_SET_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Ownship_Lon_SET_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Ownship_Lat_SET_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Ownship_Alt_Range_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Ownship_Course_Angle_PARAMATER",A661_CMD_SET_PARAMATER_16BYTE),
                ("Ownship_App_Status_PARAMATER",A661_CMD_SET_PARAMATER_12BYTE),
                ("Airport_Map_PARAMATER",A661_CMD_SET_PARAMATER_16BYTE),
                ("Target1_Visible_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target1_Pic_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target1_RotateAngle_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target1_X_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target1_Y_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target1_FlightId_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target1_Speed_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target1_Alt_dif_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target1_Status_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target1_AppStatus_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target2_Visible_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target2_Pic_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target2_RotateAngle_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target2_X_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target2_Y_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target2_FlightId_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target2_Speed_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target2_Alt_dif_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target2_Status_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target2_AppStatus_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target3_Visible_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target3_Pic_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target3_RotateAngle_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target3_X_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target3_Y_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target3_FlightId_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target3_Speed_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target3_Alt_dif_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target3_Status_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target3_AppStatus_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target4_Visible_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target4_Pic_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target4_RotateAngle_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target4_X_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target4_Y_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target4_FlightId_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target4_Speed_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target4_Alt_dif_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target4_Status_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target4_AppStatus_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target5_Visible_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target5_Pic_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("Target5_RotateAngle_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target5_X_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target5_Y_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target5_FlightId_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target5_Speed_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target5_Alt_dif_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target5_Status_PARAMATER", A661_CMD_SET_PARAMATER_16BYTE),
                ("Target5_AppStatus_PARAMATER", A661_CMD_SET_PARAMATER_12BYTE),
                ("A661_END_BLOCK",c_uint8),
                ("Unused1",c_char*3)
                ]
    def encode(self):
        return string_at(addressof(self), sizeof(self))

    def decode(self, data):
        memmove(addressof(self), data, sizeof(self))
        return len(data)
