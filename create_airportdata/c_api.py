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
                ("Ground_Speed", c_uint16),
                ("Seconds", c_uint8),
                ("Mintes", c_uint8),
                ("Hours", c_uint8),
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
                ("Warning_Status", c_uint8)]

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
                ("NACV", c_uint8),
                ("NACp", c_uint8)]


def init_adsb_data_struct():
    adsb_data_struct = ADSB_Data_Struct()
    adsb_data_struct.ICAO = "9543c1".encode(encoding='utf-8')
    adsb_data_struct.Flight_ID = "9C6187".encode(encoding='utf-8')
    adsb_data_struct.Flight_24bit_addr = 0
    adsb_data_struct.Aircraft_Category = 1
    adsb_data_struct.Altitude = 12500
    adsb_data_struct.Radio_Altitude = 0
    adsb_data_struct.North_South_Velocity = 0
    adsb_data_struct.East_West_Velocity = 0
    adsb_data_struct.Vertical_Speed = 0
    adsb_data_struct.Latitude = 32.5
    adsb_data_struct.Longitude = 40.7
    adsb_data_struct.Heading_Track_Angle = 78.1
    adsb_data_struct.Ground_Speed = 900
    adsb_data_struct.Seconds = 32
    adsb_data_struct.Mintes = 5
    adsb_data_struct.Hours = 7
    adsb_data_struct.NACV = 6
    adsb_data_struct.NACp = 0
    adsb_data_struct.NIC = 1
    adsb_data_struct.SIL = 1
    adsb_data_struct.SDA = 1
    adsb_data_struct.emergency_priority_sta = 0
    adsb_data_struct.data_link_version = 2
    return adsb_data_struct

def init_tcas_data_struct():
    tcas_data_struct = TCAS_Data_Struct()
    tcas_data_struct.Track_ID = "3".encode(encoding='utf-8')
    tcas_data_struct.Flight_24bit_address = 0
    tcas_data_struct.Altitude = 0
    tcas_data_struct.Vertical_Speed = 1
    tcas_data_struct.Bearing = 71.5
    tcas_data_struct.Range = 630.6
    tcas_data_struct.Warning_Status = 0
    return tcas_data_struct

def init_ownship_data_struct(icao,flight_id,filght_24bit_addr,altitude,radio_altitude,north_south_veloctity, \
                             east_west_velocity,vertical_speed,latitude,longitude,heading_track_angle,ground_speed,flight_length, \
                             flight_width,seconds,mintes,hours,NACV,NACp):
    ownship_data_struct = Ownship_Data_Struct()
    ownship_data_struct.ICAO = icao.encode(encoding='utf-8')
    ownship_data_struct.Flight_ID = flight_id.encode(encoding='utf-8')
    ownship_data_struct.Flight_24bit_addr = filght_24bit_addr
    ownship_data_struct.Altitude = altitude
    ownship_data_struct.Radio_Altitude = radio_altitude
    ownship_data_struct.North_South_Velocity = north_south_veloctity
    ownship_data_struct.East_West_Velocity = east_west_velocity
    ownship_data_struct.Vertical_Speed = vertical_speed
    ownship_data_struct.Latitude = latitude
    ownship_data_struct.Longitude = longitude
    ownship_data_struct.Heading_Track_Angle = heading_track_angle
    ownship_data_struct.Ground_Speed = ground_speed
    ownship_data_struct.Flight_Length = flight_length
    ownship_data_struct.Flight_Width = flight_width
    ownship_data_struct.Seconds = seconds
    ownship_data_struct.Mintes = mintes
    ownship_data_struct.Hours = hours
    ownship_data_struct.NACV = NACV
    ownship_data_struct.NACp = NACp
    return ownship_data_struct

# try:
#     dll = cdll.LoadLibrary("data_interface_pro.dll")
#
#     # adsb_data_struct = init_adsb_data_struct()
#     # a = c_char()
#     # print(dll.Pack_ADSB_data(byref(adsb_data_struct), 1, byref(a), 1024*4))
#     # print(byref(a))
#
#     # tcas_data_struct = init_tcas_data_struct()
#     # b = c_char()
#     # print(dll.Pack_TCAS_data(byref(tcas_data_struct), 1, byref(b), 1024*4))
#     # print(byref(b))
#
#     ownship_data_struct = init_ownship_data_struct(icao='5843be',flight_id='3U8894',filght_24bit_addr=0,altitude=0,radio_altitude=0,north_south_veloctity=0, \
#                                                    east_west_velocity=0,vertical_speed=0,latitude=0,longitude=0,heading_track_angle=0,ground_speed=0,flight_length=0, \
#                                                    flight_width=0,seconds=0,mintes=0,hours=0,NACV=0,NACp=0)
#     c = c_char()
#     print(dll.Pack_TCAS_data(byref(ownship_data_struct), 1, byref(c), 1024*4))
#     print(byref(c))
# except:
#     traceback.print_exc()