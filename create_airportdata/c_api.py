# -*- coding: utf-8 -*-
import traceback
from ctypes import *
class ADSB_Data_Struct(Structure):
    _fields_ = [("ICAO", c_char*16),
                ("Flight_ID", c_char*16),
                ("Flight_24bit_addr",c_int32),
                ("Aircraft_Category", c_uint8),
                ("Altitude", c_int16),
                ("Radio_Altitude", c_int16),
                ("North_South_Velocity", c_int16),
                ("East_West_Velocity", c_int16),
                ("Vertical_Speed", c_int16),
                ("Latitude", c_float),
                ("Longitude", c_float),
                ("Heading_Track_Angle", c_float),
                ("Air_Ground_Sta", c_uint8),
                ("Ground_Speed", c_uint16),
                ("Seconds", c_uint8),
                ("Mintes", c_uint8),
                ("Hours", c_uint8),
                ("p_Seconds", c_uint8),
                ("p_Mintes", c_uint8),
                ("p_Hours", c_uint8),
                ("v_Seconds", c_uint8),
                ("v_Mintes", c_uint8),
                ("v_Hours", c_uint8),
                ("s_Seconds", c_uint8),
                ("s_Mintes", c_uint8),
                ("s_Hours", c_uint8),
                ("NACV", c_uint8),
                ("NACp", c_uint8),
                ("NIC", c_uint8),
                ("SIL", c_uint8),
                ("SDA", c_uint8),
                ("emergency_priority_sta", c_uint8),
                ("data_link_version", c_uint8)]

class TCAS_Data_Struct(Structure):
    _fields_ = [("Track_ID", c_char*16),
                ("Flight_24bit_address", c_uint32),
                ("Altitude", c_int16),
                ("Vertical_Speed", c_int16),
                ("Bearing", c_float),
                ("Range", c_float),
                ("Warning_Status", c_uint8),
                ("Seconds", c_uint8),
                ("Mintes", c_uint8),
                ("Hours", c_uint8),
                ("p_Seconds", c_uint8),
                ("p_Mintes", c_uint8),
                ("p_Hours", c_uint8),
                ("v_Seconds", c_uint8),
                ("v_Mintes", c_uint8),
                ("v_Hours", c_uint8),
                ("s_Seconds", c_uint8),
                ("s_Mintes", c_uint8),
                ("s_Hours", c_uint8),
                ]

class Ownship_Data_Struct(Structure):
    _fields_ = [("ICAO", c_char*16),
                ("Flight_ID", c_char*16),
                ("Flight_24bit_addr",c_int32),
                ("Altitude", c_int16),
                ("Radio_Altitude", c_int16),
                ("North_South_Velocity", c_int16),
                ("East_West_Velocity", c_int16),
                ("Vertical_Speed", c_int16),
                ("Latitude", c_float),
                ("Longitude", c_float),
                ("Heading_Track_Angle", c_float),
                ("Ground_Speed", c_uint16),
                ("Flight_Length", c_uint16),
                ("Flight_Width", c_uint16),
                ("Seconds", c_uint8),
                ("Mintes", c_uint8),
                ("Hours", c_uint8),
                ("p_Seconds", c_uint8),
                ("p_Mintes", c_uint8),
                ("p_Hours", c_uint8),
                ("v_Seconds", c_uint8),
                ("v_Mintes", c_uint8),
                ("v_Hours", c_uint8),
                ("s_Seconds", c_uint8),
                ("s_Mintes", c_uint8),
                ("s_Hours", c_uint8),
                ("NACV", c_uint8),
                ("NACp", c_uint8)]

