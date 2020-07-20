import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import*
import cdti_mainform
import socket
import datetime
from math import *
from geography_analysis import *
from a661_api import *

class Receive_661_DataThread(QThread):
    signal_a = pyqtSignal(list)
    def __init__(self):
        super(Receive_661_DataThread, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("", 8006))  # 绑定服务器的ip和端口
        #self.s.bind(("", 8001))  # 绑定服务器的ip和端口

    def run(self):
        while True:
            buffer = self.s.recv(4096)  # 一次接收最大字节长度
            receive_Data = UA_TO_CDTI_DATA()
            receive_Data.decode(buffer)
            receive_Info = []
            receive_Info.append([receive_Data.Compass_Bitmap_SET_PARAMATER.WidgetIdent,
                                 receive_Data.Compass_Bitmap_SET_PARAMATER.ParameterIdent,
                                 receive_Data.Compass_Bitmap_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Compass_Step_SET_PARAMATER.WidgetIdent,
                                 receive_Data.Compass_Step_SET_PARAMATER.ParameterIdent,
                                 receive_Data.Compass_Step_SET_PARAMATER.ParameterValueBuffer])
            # id 2-9
            receive_Info.append([receive_Data.Ownship_FlightId_SET_PARAMATER.WidgetIdent,
                                 receive_Data.Ownship_FlightId_SET_PARAMATER.ParameterIdent,
                                 receive_Data.Ownship_FlightId_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Ownship_Alt_SET_PARAMATER.WidgetIdent, receive_Data.Ownship_Alt_SET_PARAMATER.ParameterIdent,
                 receive_Data.Ownship_Alt_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Ownship_Lon_SET_PARAMATER.WidgetIdent, receive_Data.Ownship_Lon_SET_PARAMATER.ParameterIdent,
                 receive_Data.Ownship_Lon_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Ownship_Lat_SET_PARAMATER.WidgetIdent, receive_Data.Ownship_Lat_SET_PARAMATER.ParameterIdent,
                 receive_Data.Ownship_Lat_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Ownship_Alt_Range_PARAMATER.WidgetIdent,
                                 receive_Data.Ownship_Alt_Range_PARAMATER.ParameterIdent,
                                 receive_Data.Ownship_Alt_Range_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Ownship_Course_Angle_PARAMATER.WidgetIdent,
                                 receive_Data.Ownship_Course_Angle_PARAMATER.ParameterIdent,
                                 receive_Data.Ownship_Course_Angle_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Ownship_App_Status_PARAMATER.WidgetIdent,
                                 receive_Data.Ownship_App_Status_PARAMATER.ParameterIdent,
                                 receive_Data.Ownship_App_Status_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Ownship_TOA_TIME_PARAMATER.WidgetIdent,
                                 receive_Data.Ownship_TOA_TIME_PARAMATER.ParameterIdent,
                                 receive_Data.Ownship_TOA_TIME_PARAMATER.ParameterValueBuffer])
            # air1 id 11- 24
            receive_Info.append([receive_Data.Target_Lists[0].Target_Visible_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_Visible_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_Visible_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_Pic_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_Pic_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_Pic_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_RotateAngle_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_RotateAngle_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_RotateAngle_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_X_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_X_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_Y_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_Y_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_Y_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_FlightId_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_FlightId_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_Speed_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_Speed_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_Speed_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_Alt_dif_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_Alt_dif_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_Status_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_Status_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_Status_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_AppStatus_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_AppStatus_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_AppStatus_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_Lon_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_Lon_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_Lon_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_Lat_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_Lat_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_Lat_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_VSA_DIS_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_VSA_DIS_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_VSA_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_VSA_Velocity_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_VSA_Velocity_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer,
                                         receive_Data.Target_Lists[0].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer2])
            receive_Info.append([receive_Data.Target_Lists[0].Target_ITP_DIS_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_ITP_DIS_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_ITP_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_ITP_DIS_RATE_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_ITP_DIS_RATE_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_ITP_DIS_RATE_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_ITP_FORWARD_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_ITP_FORWARD_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_ITP_FORWARD_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[0].Target_ITP_Geometry_Status_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[0].Target_ITP_Geometry_Status_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[0].Target_ITP_Geometry_Status_PARAMATER.ParameterValueBuffer])
            # air2 id 31- 44
            receive_Info.append([receive_Data.Target_Lists[1].Target_Visible_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_Visible_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_Visible_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_Pic_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_Pic_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_Pic_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_RotateAngle_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_RotateAngle_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_RotateAngle_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_X_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_X_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_Y_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_Y_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_Y_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_FlightId_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_FlightId_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_Speed_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_Speed_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_Speed_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_Alt_dif_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_Alt_dif_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_Status_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_Status_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_Status_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_AppStatus_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_AppStatus_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_AppStatus_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_Lon_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_Lon_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_Lon_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_Lat_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_Lat_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_Lat_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_VSA_DIS_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_VSA_DIS_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_VSA_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_VSA_Velocity_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_VSA_Velocity_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer,
                                         receive_Data.Target_Lists[1].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer2])
            receive_Info.append([receive_Data.Target_Lists[1].Target_ITP_DIS_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_ITP_DIS_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_ITP_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_ITP_DIS_RATE_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_ITP_DIS_RATE_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_ITP_DIS_RATE_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_ITP_FORWARD_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_ITP_FORWARD_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_ITP_FORWARD_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[1].Target_ITP_Geometry_Status_PARAMATER.WidgetIdent,
                                         receive_Data.Target_Lists[1].Target_ITP_Geometry_Status_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[1].Target_ITP_Geometry_Status_PARAMATER.ParameterValueBuffer])
            # air3 id 51- 64
            receive_Info.append([receive_Data.Target_Lists[2].Target_Visible_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_Visible_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_Visible_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_Pic_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_Pic_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_Pic_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_RotateAngle_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_RotateAngle_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_RotateAngle_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_X_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_X_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_Y_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_Y_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_Y_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_FlightId_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_FlightId_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_Speed_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_Speed_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_Speed_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_Alt_dif_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_Alt_dif_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_Status_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_Status_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_Status_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_AppStatus_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_AppStatus_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_AppStatus_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_Lon_SET_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_Lon_SET_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_Lon_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_Lat_SET_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_Lat_SET_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_Lat_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_VSA_DIS_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_VSA_DIS_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_VSA_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_VSA_Velocity_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_VSA_Velocity_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer,
                                 receive_Data.Target_Lists[2].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer2])
            receive_Info.append([receive_Data.Target_Lists[2].Target_ITP_DIS_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_ITP_DIS_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_ITP_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_ITP_DIS_RATE_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_ITP_DIS_RATE_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_ITP_DIS_RATE_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_ITP_FORWARD_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_ITP_FORWARD_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_ITP_FORWARD_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[2].Target_ITP_Geometry_Status_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[2].Target_ITP_Geometry_Status_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[2].Target_ITP_Geometry_Status_PARAMATER.ParameterValueBuffer])

            # air4 id 71- 84
            receive_Info.append([receive_Data.Target_Lists[3].Target_Visible_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_Visible_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_Visible_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_Pic_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_Pic_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_Pic_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_RotateAngle_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_RotateAngle_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_RotateAngle_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_X_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_X_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_Y_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_Y_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_Y_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_FlightId_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_FlightId_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_Speed_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_Speed_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_Speed_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_Alt_dif_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_Alt_dif_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_Status_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_Status_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_Status_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_AppStatus_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_AppStatus_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_AppStatus_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_Lon_SET_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_Lon_SET_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_Lon_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_Lat_SET_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_Lat_SET_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_Lat_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_VSA_DIS_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_VSA_DIS_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_VSA_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_VSA_Velocity_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_VSA_Velocity_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer,
                                 receive_Data.Target_Lists[3].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer2])
            receive_Info.append([receive_Data.Target_Lists[3].Target_ITP_DIS_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_ITP_DIS_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_ITP_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_ITP_DIS_RATE_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_ITP_DIS_RATE_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_ITP_DIS_RATE_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_ITP_FORWARD_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_ITP_FORWARD_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_ITP_FORWARD_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[3].Target_ITP_Geometry_Status_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[3].Target_ITP_Geometry_Status_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[3].Target_ITP_Geometry_Status_PARAMATER.ParameterValueBuffer])

            # air5 id 91- 104
            receive_Info.append([receive_Data.Target_Lists[4].Target_Visible_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_Visible_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_Visible_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_Pic_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_Pic_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_Pic_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_RotateAngle_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_RotateAngle_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_RotateAngle_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_X_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_X_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_Y_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_Y_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_Y_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_FlightId_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_FlightId_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_Speed_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_Speed_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_Speed_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_Alt_dif_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_Alt_dif_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_Status_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_Status_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_Status_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_AppStatus_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_AppStatus_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_AppStatus_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_Lon_SET_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_Lon_SET_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_Lon_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_Lat_SET_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_Lat_SET_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_Lat_SET_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_VSA_DIS_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_VSA_DIS_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_VSA_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_VSA_Velocity_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_VSA_Velocity_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer,
                                 receive_Data.Target_Lists[4].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer2])
            receive_Info.append([receive_Data.Target_Lists[4].Target_ITP_DIS_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_ITP_DIS_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_ITP_DIS_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_ITP_DIS_RATE_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_ITP_DIS_RATE_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_ITP_DIS_RATE_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_ITP_FORWARD_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_ITP_FORWARD_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_ITP_FORWARD_PARAMATER.ParameterValueBuffer])
            receive_Info.append([receive_Data.Target_Lists[4].Target_ITP_Geometry_Status_PARAMATER.WidgetIdent,
                                 receive_Data.Target_Lists[4].Target_ITP_Geometry_Status_PARAMATER.ParameterIdent,
                                 receive_Data.Target_Lists[4].Target_ITP_Geometry_Status_PARAMATER.ParameterValueBuffer])

            self.signal_a.emit(receive_Info)



class MainWindow(QMainWindow):



    # 0设置显示/隐藏 1设置文本 2设置图片源 3设置symbol源 4设置旋转角 5设置X坐标 6设置Y坐标
    map_setparaId = {'46384‬': 0, '46224': 1, '45808': 2, '46272': 3, '45760': 4, '45824': 5, '45840': 6}


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.rotateAngle = 0  # 每次旋转角度
        self.count = 0
        self.map_widgetItem = 0
        self.surf_compass_Item = 0
        self.airb_compass_Item = 0
        self.vsa_compass_Item = 0
        self.targetAir1_Item = 0
        self.surf_air1_text_Item = 0
        self.ip_port_toUA = ('127.0.0.1', 8010)
        #self.ip_port_toUA = ('192.168.253.2', 8010)

        self.initUI()

        # timer_a = QTimer(self)
        # timer_a.timeout.connect(self.update_time)
        # timer_a.start()
        self.myWorker = Receive_661_DataThread()
        self.myWorker.signal_a.connect(self.update_cdti_ui)
        self.myWorker.start()
        print("打开UDP通信端口，开始接收UA发送数据...")
        self.cdti_to_ua_in_data = CDTI_TO_UA_WIDGET_EVENT_DATA()
        self.cdti_to_ua_out_data = CDTI_TO_UA_WIDGET_EVENT_DATA()
        self.ui.btn_zoom_in_airb.clicked.connect(self.send_data1_to_ua)
        self.ui.btn_zoom_out_airb.clicked.connect(self.send_data2_to_ua)
        self.ui.btn_zoom_in_vsa.clicked.connect(self.send_data1_to_ua)
        self.ui.btn_zoom_out_vsa.clicked.connect(self.send_data2_to_ua)
        self.ui.btn_zoom_in_itp.clicked.connect(self.send_data1_to_ua)
        self.ui.btn_zoom_out_itp.clicked.connect(self.send_data2_to_ua)

    def update_time(self):
        Seconds = int(datetime.datetime.now().strftime('%H:%M:%S:%f').split(':')[2])  #
        Mintes = int(datetime.datetime.now().strftime('%H:%M:%S:%f').split(':')[1])  #
        Hours = int(datetime.datetime.now().strftime('%H:%M:%S:%f').split(':')[0])  #
        sec = round(float(datetime.datetime.now().strftime('%H:%M:%S:%f').split(':')[-1]) / 1000000, 1)
        time = Hours * 3600 + Mintes * 60 + Seconds + sec
        self.ui.airb_time_txt.setText(str(time))
        self.ui.surf_time_txt.setText(str(time))
        self.ui.vsa_time_txt.setText(str(time))
        self.ui.itp_time_txt.setText(str(time))

    def initUI(self):
        self.ui = cdti_mainform.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_zoom_in_surf.clicked.connect(self.map_zoom_in)
        self.ui.btn_zoom_out_surf.clicked.connect(self.map_zoom_out)
        self.ui.widget_itp.setVisible(False)
        self.ui.widget_airb.setVisible(False)
        self.ui.widget_surf.setVisible(False)
        self.ui.widget_vsa.setVisible(False)


        self.ui.btn_zoom_in_surf.setIcon(QIcon("pic/+.png"))
        self.ui.btn_zoom_in_airb.setIcon(QIcon("pic/+.png"))
        self.ui.btn_zoom_in_vsa.setIcon(QIcon("pic/+.png"))
        self.ui.btn_zoom_in_itp.setIcon(QIcon("pic/+.png"))
        self.ui.btn_zoom_out_surf.setIcon(QIcon("pic/-.png"))
        self.ui.btn_zoom_out_airb.setIcon(QIcon("pic/-.png"))
        self.ui.btn_zoom_out_vsa.setIcon(QIcon("pic/-.png"))
        self.ui.btn_zoom_out_itp.setIcon(QIcon("pic/-.png"))
        self.ui.img_itp_alt.setPixmap(QPixmap("pic/ITP.png"))

        #通用图片初始化
        pixmap_ownship =  QPixmap("pic/ownship.png") #本机图标
        pixmap_border = QPixmap("pic/b.png") #罗盘外轮廓
        scaledPixmap_border = pixmap_border.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatioByExpanding)
        pixmap_compass_transparent = QPixmap("pic/罗盘-透明背景.png") #透明罗盘
        scaledPixmap_compass_transparent = pixmap_compass_transparent.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatio)

        pixmap_type1_targetship = QPixmap("pic/air1.png")  # 1号类型目标机图标
        pixmap_type2_targetship = QPixmap("pic/air2.png")  # 2号类型目标机图标
        pixmap_type3_targetship = QPixmap("pic/air3.png")  # 3号类型目标机图标
        pixmap_type4_targetship = QPixmap("pic/air4.png")  # 4号类型目标机图标
        pixmap_type5_targetship = QPixmap("pic/air5.png")  # 5号类型目标机图标
        pixmap_type6_targetship = QPixmap("pic/air6.png")  # 6号类型目标机图标
        pixmap_type7_targetship = QPixmap("pic/air7.png")  # 7号类型目标机图标
        pixmap_type8_targetship = QPixmap("pic/air8.png")  # 8号类型目标机图标
        pixmap_type9_targetship = QPixmap("pic/air9.png")  # 9号类型目标机图标
        pixmap_type10_targetship = QPixmap("pic/air10.png")  # 10号类型目标机图标
        pixmap_type11_targetship = QPixmap("pic/air11.png")  # 11号类型目标机图标
        pixmap_type12_targetship = QPixmap("pic/air12.png")  # 12号类型目标机图标

        from PyQt5.QtGui import QPainter
        #surf
        #通用部分开始
        self.ui.horizontalLayoutWidget.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_surf = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_surf.setStyleSheet("padding: 0px; border: 0px;")
        self.ui.graphicsView_surf.setRenderHint(QPainter.TextAntialiasing)
        self.ui.horizontalLayout.addWidget(self.ui.graphicsView_surf)
        url = os.getcwd() + '/map_surf.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.browser.resize(640,640)
        self.surf_scene = QGraphicsScene(self)

        #scene场景增加条目并设置位置
        self.map_widgetItem = self.surf_scene.addWidget(self.browser) # 地图条目
        surf_compass_centerPos3 = self.map_widgetItem.boundingRect().center()
        self.map_widgetItem.setTransformOriginPoint(surf_compass_centerPos3)
        self.map_widgetItem.setPos(0, 45)
        self.surf_border_Item = self.surf_scene.addPixmap(scaledPixmap_border) #罗盘边框条目
        self.surf_compass_Item = self.surf_scene.addPixmap(scaledPixmap_compass_transparent) #罗盘条目
        surf_compass_centerPos1 = self.surf_compass_Item.boundingRect().center()
        self.surf_compass_Item.setTransformOriginPoint(surf_compass_centerPos1)
        self.surf_compass_Item.setPos(0,45)
        self.surf_ownship_item = self.surf_scene.addPixmap(pixmap_ownship)    #本机图标
        self.surf_ownship_item.setPos(320-15,320+17.5)
        self.surf_air_heading_txt = QLabel("23.5")
        self.surf_air_heading_txt.setStyleSheet("color:white;background-color:transparent")
        surf_air_heading = self.surf_scene.addWidget(self.surf_air_heading_txt)  # 本机航向角
        surf_air_heading.setPos(315, 20)
        #初始化五架目标飞机
        self.surf_targetair1_PixItem = self.surf_scene.addPixmap(pixmap_type1_targetship) #1号目标机图标
        surf_centerPos1 = self.surf_targetair1_PixItem.boundingRect().center()
        self.surf_targetair1_PixItem.setTransformOriginPoint(surf_centerPos1)
        self.surf_frametxt_targetAir1 = QFrame() #1号目标机文本
        self.surf_frametxt_targetAir1.setStyleSheet("background-color:transparent")
        self.surf_frametxt_targetAir1.setLayout(self.ui.formLayout_surf_targetair1)
        self.surf_air1_text_Item = self.surf_scene.addWidget(self.surf_frametxt_targetAir1)
        self.surf_air1_text_Item.setOpacity(0.9)
        self.surf_targetair1_PixItem.setPos(100, 500)
        self.surf_air1_text_Item.setPos(100, 520)


        self.surf_targetair2_PixItem = self.surf_scene.addPixmap(pixmap_type2_targetship)
        surf_centerPos2 = self.surf_targetair2_PixItem.boundingRect().center()
        self.surf_targetair2_PixItem.setTransformOriginPoint(surf_centerPos2)
        self.surf_frametxt_targetAir2 = QFrame() #2号目标机文本
        self.surf_frametxt_targetAir2.setStyleSheet("background-color:transparent")
        self.surf_frametxt_targetAir2.setLayout(self.ui.formLayout_surf_targetair2)
        self.surf_air2_text_Item = self.surf_scene.addWidget(self.surf_frametxt_targetAir2)
        self.surf_air2_text_Item.setOpacity(0.9)
        self.surf_targetair2_PixItem.setPos(200, 500)
        self.surf_air2_text_Item.setPos(200, 520)


        self.surf_targetair3_PixItem = self.surf_scene.addPixmap(pixmap_type3_targetship)
        surf_centerPos3 = self.surf_targetair3_PixItem.boundingRect().center()
        self.surf_targetair3_PixItem.setTransformOriginPoint(surf_centerPos3)
        self.surf_frametxt_targetAir3 = QFrame() #3号目标机文本
        self.surf_frametxt_targetAir3.setStyleSheet("background-color:transparent")
        self.surf_frametxt_targetAir3.setLayout(self.ui.formLayout_surf_targetair3)
        self.surf_air3_text_Item = self.surf_scene.addWidget(self.surf_frametxt_targetAir3)
        self.surf_air3_text_Item.setOpacity(0.9)
        self.surf_targetair3_PixItem.setPos(300, 500)
        self.surf_air3_text_Item.setPos(300, 520)

        self.surf_targetair4_PixItem = self.surf_scene.addPixmap(pixmap_type4_targetship)
        surf_centerPos4 = self.surf_targetair4_PixItem.boundingRect().center()
        self.surf_targetair4_PixItem.setTransformOriginPoint(surf_centerPos4)
        self.surf_frametxt_targetAir4 = QFrame() #4号目标机文本
        self.surf_frametxt_targetAir4.setStyleSheet("background-color:transparent")
        self.surf_frametxt_targetAir4.setLayout(self.ui.formLayout_surf_targetair4)
        self.surf_air4_text_Item = self.surf_scene.addWidget(self.surf_frametxt_targetAir4)
        self.surf_air4_text_Item.setOpacity(0.9)
        self.surf_targetair4_PixItem.setPos(400, 500)
        self.surf_air4_text_Item.setPos(400, 520)

        self.surf_targetair5_PixItem = self.surf_scene.addPixmap(pixmap_type5_targetship)
        surf_centerPos5 = self.surf_targetair5_PixItem.boundingRect().center()
        self.surf_targetair5_PixItem.setTransformOriginPoint(surf_centerPos5)
        self.surf_frametxt_targetAir5 = QFrame() #5号目标机文本
        self.surf_frametxt_targetAir5.setStyleSheet("background-color:transparent")
        self.surf_frametxt_targetAir5.setLayout(self.ui.formLayout_surf_targetair5)
        self.surf_air5_text_Item = self.surf_scene.addWidget(self.surf_frametxt_targetAir5)
        self.surf_air5_text_Item.setOpacity(0.9)
        self.surf_targetair5_PixItem.setPos(500, 500)
        self.surf_air5_text_Item.setPos(500, 520)

        #设置item图层位置
        self.map_widgetItem.stackBefore(self.surf_border_Item)
        self.surf_targetair1_PixItem.stackBefore(self.surf_ownship_item)
        self.surf_air1_text_Item.stackBefore(self.surf_ownship_item)
        self.surf_targetair1_PixItem.stackBefore(self.surf_border_Item)
        self.surf_air1_text_Item.stackBefore(self.surf_border_Item)

        self.surf_targetair2_PixItem.stackBefore(self.surf_ownship_item)
        self.surf_air2_text_Item.stackBefore(self.surf_ownship_item)
        self.surf_targetair2_PixItem.stackBefore(self.surf_border_Item)
        self.surf_air2_text_Item.stackBefore(self.surf_border_Item)

        self.surf_targetair3_PixItem.stackBefore(self.surf_ownship_item)
        self.surf_air3_text_Item.stackBefore(self.surf_ownship_item)
        self.surf_targetair3_PixItem.stackBefore(self.surf_border_Item)
        self.surf_air3_text_Item.stackBefore(self.surf_border_Item)

        self.surf_targetair4_PixItem.stackBefore(self.surf_ownship_item)
        self.surf_air4_text_Item.stackBefore(self.surf_ownship_item)
        self.surf_targetair4_PixItem.stackBefore(self.surf_border_Item)
        self.surf_air4_text_Item.stackBefore(self.surf_border_Item)

        self.surf_targetair5_PixItem.stackBefore(self.surf_ownship_item)
        self.surf_air5_text_Item.stackBefore(self.surf_ownship_item)
        self.surf_targetair5_PixItem.stackBefore(self.surf_border_Item)
        self.surf_air5_text_Item.stackBefore(self.surf_border_Item)
        self.ui.graphicsView_surf.setScene(self.surf_scene)
        self.ui.graphicsView_surf.setSceneRect(1, 1, 715, 715)


        #=========================================#
        # airb
        # 通用部分开始
        self.ui.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_airb = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_airb.setStyleSheet("padding: 0px; border: 0px;")
        self.ui.horizontalLayout_2.addWidget(self.ui.graphicsView_airb)
        self.airb_scene = QGraphicsScene(self)

        # scene场景增加条目并设置位置
        self.airb_border_Item = self.airb_scene.addPixmap(scaledPixmap_border)  # 罗盘边框条目
        self.airb_compass_Item = self.airb_scene.addPixmap(scaledPixmap_compass_transparent)  # 罗盘条目
        airb_compass_centerPos1 = self.airb_compass_Item.boundingRect().center()
        self.airb_compass_Item.setTransformOriginPoint(airb_compass_centerPos1)
        self.airb_compass_Item.setPos(0, 45)
        self.airb_ownship_item = self.airb_scene.addPixmap(pixmap_ownship)  # 本机图标
        self.airb_ownship_item.setPos(320 - 15, 320 + 17.5)
        self.airb_air_heading_txt = QLabel("23.5")
        self.airb_air_heading_txt.setStyleSheet("color:white;background-color:transparent")
        airb_air_heading = self.airb_scene.addWidget(self.airb_air_heading_txt)  # 本机航向角
        airb_air_heading.setPos(315, 20)


        # 初始化五架目标飞机
        self.airb_targetair1_PixItem = self.airb_scene.addPixmap(pixmap_type1_targetship)  # 1号目标机图标
        airb_centerPos1 = self.airb_targetair1_PixItem.boundingRect().center()
        self.airb_targetair1_PixItem.setTransformOriginPoint(airb_centerPos1)
        self.airb_frametxt_targetAir1 = QFrame()  # 1号目标机文本
        self.airb_frametxt_targetAir1.setStyleSheet("background-color:transparent")
        self.airb_frametxt_targetAir1.setLayout(self.ui.formLayout_airb_targetair1)
        self.airb_air1_text_Item = self.airb_scene.addWidget(self.airb_frametxt_targetAir1)
        self.airb_air1_text_Item.setOpacity(0.9)
        self.airb_targetair1_PixItem.setPos(100, 500)
        self.airb_air1_text_Item.setPos(100, 520)

        self.airb_targetair2_PixItem = self.airb_scene.addPixmap(pixmap_type2_targetship)
        airb_centerPos2 = self.airb_targetair2_PixItem.boundingRect().center()
        self.airb_targetair2_PixItem.setTransformOriginPoint(airb_centerPos2)
        self.airb_frametxt_targetAir2 = QFrame()  # 2号目标机文本
        self.airb_frametxt_targetAir2.setStyleSheet("background-color:transparent")
        self.airb_frametxt_targetAir2.setLayout(self.ui.formLayout_airb_targetair2)
        self.airb_air2_text_Item = self.airb_scene.addWidget(self.airb_frametxt_targetAir2)
        self.airb_air2_text_Item.setOpacity(0.9)
        self.airb_targetair2_PixItem.setPos(200, 500)
        self.airb_air2_text_Item.setPos(200, 520)

        self.airb_targetair3_PixItem = self.airb_scene.addPixmap(pixmap_type3_targetship)
        airb_centerPos3 = self.airb_targetair3_PixItem.boundingRect().center()
        self.airb_targetair3_PixItem.setTransformOriginPoint(airb_centerPos3)
        self.airb_frametxt_targetAir3 = QFrame()  # 3号目标机文本
        self.airb_frametxt_targetAir3.setStyleSheet("background-color:transparent")
        self.airb_frametxt_targetAir3.setLayout(self.ui.formLayout_airb_targetair3)
        self.airb_air3_text_Item = self.airb_scene.addWidget(self.airb_frametxt_targetAir3)
        self.airb_air3_text_Item.setOpacity(0.9)
        self.airb_targetair3_PixItem.setPos(300, 500)
        self.airb_air3_text_Item.setPos(300, 520)

        self.airb_targetair4_PixItem = self.airb_scene.addPixmap(pixmap_type4_targetship)
        airb_centerPos4 = self.airb_targetair4_PixItem.boundingRect().center()
        self.airb_targetair4_PixItem.setTransformOriginPoint(airb_centerPos4)
        self.airb_frametxt_targetAir4 = QFrame()  # 4号目标机文本
        self.airb_frametxt_targetAir4.setStyleSheet("background-color:transparent")
        self.airb_frametxt_targetAir4.setLayout(self.ui.formLayout_airb_targetair4)
        self.airb_air4_text_Item = self.airb_scene.addWidget(self.airb_frametxt_targetAir4)
        self.airb_air4_text_Item.setOpacity(0.9)
        self.airb_targetair4_PixItem.setPos(400, 500)
        self.airb_air4_text_Item.setPos(400, 520)

        self.airb_targetair5_PixItem = self.airb_scene.addPixmap(pixmap_type5_targetship)
        airb_centerPos5 = self.airb_targetair5_PixItem.boundingRect().center()
        self.airb_targetair5_PixItem.setTransformOriginPoint(airb_centerPos5)
        self.airb_frametxt_targetAir5 = QFrame()  # 5号目标机文本
        self.airb_frametxt_targetAir5.setStyleSheet("background-color:transparent")
        self.airb_frametxt_targetAir5.setLayout(self.ui.formLayout_airb_targetair5)
        self.airb_air5_text_Item = self.airb_scene.addWidget(self.airb_frametxt_targetAir5)
        self.airb_air5_text_Item.setOpacity(0.9)
        self.airb_targetair5_PixItem.setPos(500, 500)
        self.airb_air5_text_Item.setPos(500, 520)

        # 设置item图层位置
        self.airb_targetair1_PixItem.stackBefore(self.airb_ownship_item)
        self.airb_air1_text_Item.stackBefore(self.airb_ownship_item)
        self.airb_targetair1_PixItem.stackBefore(self.airb_border_Item)
        self.airb_air1_text_Item.stackBefore(self.airb_border_Item)
        self.airb_targetair2_PixItem.stackBefore(self.airb_ownship_item)
        self.airb_air2_text_Item.stackBefore(self.airb_ownship_item)
        self.airb_targetair2_PixItem.stackBefore(self.airb_border_Item)
        self.airb_air2_text_Item.stackBefore(self.airb_border_Item)

        self.airb_targetair3_PixItem.stackBefore(self.airb_ownship_item)
        self.airb_air3_text_Item.stackBefore(self.airb_ownship_item)
        self.airb_targetair3_PixItem.stackBefore(self.airb_border_Item)
        self.airb_air3_text_Item.stackBefore(self.airb_border_Item)

        self.airb_targetair4_PixItem.stackBefore(self.airb_ownship_item)
        self.airb_air4_text_Item.stackBefore(self.airb_ownship_item)
        self.airb_targetair4_PixItem.stackBefore(self.airb_border_Item)
        self.airb_air4_text_Item.stackBefore(self.airb_border_Item)

        self.airb_targetair5_PixItem.stackBefore(self.airb_ownship_item)
        self.airb_air5_text_Item.stackBefore(self.airb_ownship_item)
        self.airb_targetair5_PixItem.stackBefore(self.airb_border_Item)
        self.airb_air5_text_Item.stackBefore(self.airb_border_Item)
        self.ui.graphicsView_airb.setScene(self.airb_scene)
        self.ui.graphicsView_airb.setSceneRect(1, 1, 715, 715)

        # =========================================#
        # vsa
        # 通用部分开始
        self.ui.horizontalLayoutWidget_3.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_vsa = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_vsa.setStyleSheet("padding: 0px; border: 0px;")
        self.ui.horizontalLayout_3.addWidget(self.ui.graphicsView_vsa)
        self.vsa_scene = QGraphicsScene(self)

        # scene场景增加条目并设置位置
        self.vsa_border_Item = self.vsa_scene.addPixmap(scaledPixmap_border)  # 罗盘边框条目
        self.vsa_compass_Item = self.vsa_scene.addPixmap(scaledPixmap_compass_transparent)  # 罗盘条目
        vsa_compass_centerPos1 = self.vsa_compass_Item.boundingRect().center()
        self.vsa_compass_Item.setTransformOriginPoint(vsa_compass_centerPos1)
        self.vsa_compass_Item.setPos(0, 45)
        self.vsa_ownship_item = self.vsa_scene.addPixmap(pixmap_ownship)  # 本机图标
        self.vsa_ownship_item.setPos(320 - 15, 320 + 17.5)
        self.vsa_air_heading_txt = QLabel("23.5")
        self.vsa_air_heading_txt.setStyleSheet("color:white;background-color:transparent")
        vsa_air_heading = self.vsa_scene.addWidget(self.vsa_air_heading_txt)  # 本机航向角
        vsa_air_heading.setPos(315, 20)

        # 初始化五架目标飞机
        self.vsa_targetair1_PixItem = self.vsa_scene.addPixmap(pixmap_type1_targetship)  # 1号目标机图标
        vsa_centerPos1 = self.vsa_targetair1_PixItem.boundingRect().center()
        self.vsa_targetair1_PixItem.setTransformOriginPoint(vsa_centerPos1)
        self.vsa_frametxt_targetAir1 = QFrame()  # 1号目标机文本
        self.vsa_frametxt_targetAir1.setStyleSheet("background-color:transparent")
        self.vsa_frametxt_targetAir1.setLayout(self.ui.formLayout_vsa_targetair1)
        self.vsa_air1_text_Item = self.vsa_scene.addWidget(self.vsa_frametxt_targetAir1)
        self.vsa_air1_text_Item.setOpacity(0.9)
        self.vsa_targetair1_PixItem.setPos(100, 500)
        self.vsa_air1_text_Item.setPos(100, 520)

        self.vsa_targetair2_PixItem = self.vsa_scene.addPixmap(pixmap_type2_targetship)
        vsa_centerPos2 = self.vsa_targetair2_PixItem.boundingRect().center()
        self.vsa_targetair2_PixItem.setTransformOriginPoint(vsa_centerPos2)
        self.vsa_frametxt_targetAir2 = QFrame()  # 2号目标机文本
        self.vsa_frametxt_targetAir2.setStyleSheet("background-color:transparent")
        self.vsa_frametxt_targetAir2.setLayout(self.ui.formLayout_vsa_targetair2)
        self.vsa_air2_text_Item = self.vsa_scene.addWidget(self.vsa_frametxt_targetAir2)
        self.vsa_air2_text_Item.setOpacity(0.9)
        self.vsa_targetair2_PixItem.setPos(200, 500)
        self.vsa_air2_text_Item.setPos(200, 520)

        self.vsa_targetair3_PixItem = self.vsa_scene.addPixmap(pixmap_type3_targetship)
        vsa_centerPos3 = self.vsa_targetair3_PixItem.boundingRect().center()
        self.vsa_targetair3_PixItem.setTransformOriginPoint(vsa_centerPos3)
        self.vsa_frametxt_targetAir3 = QFrame()  # 3号目标机文本
        self.vsa_frametxt_targetAir3.setStyleSheet("background-color:transparent")
        self.vsa_frametxt_targetAir3.setLayout(self.ui.formLayout_vsa_targetair3)
        self.vsa_air3_text_Item = self.vsa_scene.addWidget(self.vsa_frametxt_targetAir3)
        self.vsa_air3_text_Item.setOpacity(0.9)
        self.vsa_targetair3_PixItem.setPos(300, 500)
        self.vsa_air3_text_Item.setPos(300, 520)

        self.vsa_targetair4_PixItem = self.vsa_scene.addPixmap(pixmap_type4_targetship)
        vsa_centerPos4 = self.vsa_targetair4_PixItem.boundingRect().center()
        self.vsa_targetair4_PixItem.setTransformOriginPoint(vsa_centerPos4)
        self.vsa_frametxt_targetAir4 = QFrame()  # 4号目标机文本
        self.vsa_frametxt_targetAir4.setStyleSheet("background-color:transparent")
        self.vsa_frametxt_targetAir4.setLayout(self.ui.formLayout_vsa_targetair4)
        self.vsa_air4_text_Item = self.vsa_scene.addWidget(self.vsa_frametxt_targetAir4)
        self.vsa_air4_text_Item.setOpacity(0.9)
        self.vsa_targetair4_PixItem.setPos(400, 500)
        self.vsa_air4_text_Item.setPos(400, 520)

        self.vsa_targetair5_PixItem = self.vsa_scene.addPixmap(pixmap_type5_targetship)
        vsa_centerPos5 = self.vsa_targetair5_PixItem.boundingRect().center()
        self.vsa_targetair5_PixItem.setTransformOriginPoint(vsa_centerPos5)
        self.vsa_frametxt_targetAir5 = QFrame()  # 5号目标机文本
        self.vsa_frametxt_targetAir5.setStyleSheet("background-color:transparent")
        self.vsa_frametxt_targetAir5.setLayout(self.ui.formLayout_vsa_targetair5)
        self.vsa_air5_text_Item = self.vsa_scene.addWidget(self.vsa_frametxt_targetAir5)
        self.vsa_air5_text_Item.setOpacity(0.9)
        self.vsa_targetair5_PixItem.setPos(500, 500)
        self.vsa_air5_text_Item.setPos(500, 520)

        # 设置item图层位置
        self.vsa_targetair1_PixItem.stackBefore(self.vsa_ownship_item)
        self.vsa_air1_text_Item.stackBefore(self.vsa_ownship_item)
        self.vsa_targetair1_PixItem.stackBefore(self.vsa_border_Item)
        self.vsa_air1_text_Item.stackBefore(self.vsa_border_Item)
        self.vsa_targetair2_PixItem.stackBefore(self.vsa_ownship_item)
        self.vsa_air2_text_Item.stackBefore(self.vsa_ownship_item)
        self.vsa_targetair2_PixItem.stackBefore(self.vsa_border_Item)
        self.vsa_air2_text_Item.stackBefore(self.vsa_border_Item)

        self.vsa_targetair3_PixItem.stackBefore(self.vsa_ownship_item)
        self.vsa_air3_text_Item.stackBefore(self.vsa_ownship_item)
        self.vsa_targetair3_PixItem.stackBefore(self.vsa_border_Item)
        self.vsa_air3_text_Item.stackBefore(self.vsa_border_Item)

        self.vsa_targetair4_PixItem.stackBefore(self.vsa_ownship_item)
        self.vsa_air4_text_Item.stackBefore(self.vsa_ownship_item)
        self.vsa_targetair4_PixItem.stackBefore(self.vsa_border_Item)
        self.vsa_air4_text_Item.stackBefore(self.vsa_border_Item)

        self.vsa_targetair5_PixItem.stackBefore(self.vsa_ownship_item)
        self.vsa_air5_text_Item.stackBefore(self.vsa_ownship_item)
        self.vsa_targetair5_PixItem.stackBefore(self.vsa_border_Item)
        self.vsa_air5_text_Item.stackBefore(self.vsa_border_Item)
        self.ui.graphicsView_vsa.setScene(self.vsa_scene)
        self.ui.graphicsView_vsa.setSceneRect(1, 1, 715, 715)

        # =========================================#
        # itp
        # 通用部分开始
        self.ui.horizontalLayoutWidget_4.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_itp = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_itp.setStyleSheet("padding: 0px; border: 0px;")
        self.ui.horizontalLayout_4.addWidget(self.ui.graphicsView_itp)
        self.itp_scene = QGraphicsScene(self)

        # scene场景增加条目并设置位置
        self.itp_border_Item = self.itp_scene.addPixmap(scaledPixmap_border)  # 罗盘边框条目
        self.itp_compass_Item = self.itp_scene.addPixmap(scaledPixmap_compass_transparent)  # 罗盘条目
        itp_compass_centerPos1 = self.itp_compass_Item.boundingRect().center()
        self.itp_compass_Item.setTransformOriginPoint(itp_compass_centerPos1)
        self.itp_compass_Item.setPos(0, 45)
        self.itp_ownship_item = self.itp_scene.addPixmap(pixmap_ownship)  # 本机图标
        self.itp_ownship_item.setPos(320 - 15, 320 + 17.5)
        self.itp_air_heading_txt = QLabel("23.5")
        self.itp_air_heading_txt.setStyleSheet("color:white;background-color:transparent")
        itp_air_heading = self.itp_scene.addWidget(self.itp_air_heading_txt)  # 本机航向角
        itp_air_heading.setPos(315, 20)
        # 初始化五架目标飞机
        self.itp_targetair1_PixItem = self.itp_scene.addPixmap(pixmap_type1_targetship)  # 1号目标机图标
        itp_centerPos1 = self.itp_targetair1_PixItem.boundingRect().center()
        self.itp_targetair1_PixItem.setTransformOriginPoint(itp_centerPos1)
        self.itp_frametxt_targetAir1 = QFrame()  # 1号目标机文本
        self.itp_frametxt_targetAir1.setStyleSheet("background-color:transparent")
        self.itp_frametxt_targetAir1.setLayout(self.ui.formLayout_itp_targetair1)
        self.itp_air1_text_Item = self.itp_scene.addWidget(self.itp_frametxt_targetAir1)
        self.itp_air1_text_Item.setOpacity(0.9)
        self.itp_targetair1_PixItem.setPos(100, 500)
        self.itp_air1_text_Item.setPos(100, 520)

        self.itp_targetair2_PixItem = self.itp_scene.addPixmap(pixmap_type2_targetship)
        itp_centerPos2 = self.itp_targetair2_PixItem.boundingRect().center()
        self.itp_targetair2_PixItem.setTransformOriginPoint(itp_centerPos2)
        self.itp_frametxt_targetAir2 = QFrame()  # 2号目标机文本
        self.itp_frametxt_targetAir2.setStyleSheet("background-color:transparent")
        self.itp_frametxt_targetAir2.setLayout(self.ui.formLayout_itp_targetair2)
        self.itp_air2_text_Item = self.itp_scene.addWidget(self.itp_frametxt_targetAir2)
        self.itp_air2_text_Item.setOpacity(0.9)
        self.itp_targetair2_PixItem.setPos(200, 500)
        self.itp_air2_text_Item.setPos(200, 520)

        self.itp_targetair3_PixItem = self.itp_scene.addPixmap(pixmap_type3_targetship)
        itp_centerPos3 = self.itp_targetair3_PixItem.boundingRect().center()
        self.itp_targetair3_PixItem.setTransformOriginPoint(itp_centerPos3)
        self.itp_frametxt_targetAir3 = QFrame()  # 3号目标机文本
        self.itp_frametxt_targetAir3.setStyleSheet("background-color:transparent")
        self.itp_frametxt_targetAir3.setLayout(self.ui.formLayout_itp_targetair3)
        self.itp_air3_text_Item = self.itp_scene.addWidget(self.itp_frametxt_targetAir3)
        self.itp_air3_text_Item.setOpacity(0.9)
        self.itp_targetair3_PixItem.setPos(300, 500)
        self.itp_air3_text_Item.setPos(300, 520)

        self.itp_targetair4_PixItem = self.itp_scene.addPixmap(pixmap_type4_targetship)
        itp_centerPos4 = self.itp_targetair4_PixItem.boundingRect().center()
        self.itp_targetair4_PixItem.setTransformOriginPoint(itp_centerPos4)
        self.itp_frametxt_targetAir4 = QFrame()  # 4号目标机文本
        self.itp_frametxt_targetAir4.setStyleSheet("background-color:transparent")
        self.itp_frametxt_targetAir4.setLayout(self.ui.formLayout_itp_targetair4)
        self.itp_air4_text_Item = self.itp_scene.addWidget(self.itp_frametxt_targetAir4)
        self.itp_air4_text_Item.setOpacity(0.9)
        self.itp_targetair4_PixItem.setPos(400, 500)
        self.itp_air4_text_Item.setPos(400, 520)

        self.itp_targetair5_PixItem = self.itp_scene.addPixmap(pixmap_type5_targetship)
        itp_centerPos5 = self.itp_targetair5_PixItem.boundingRect().center()
        self.itp_targetair5_PixItem.setTransformOriginPoint(itp_centerPos5)
        self.itp_frametxt_targetAir5 = QFrame()  # 5号目标机文本
        self.itp_frametxt_targetAir5.setStyleSheet("background-color:transparent")
        self.itp_frametxt_targetAir5.setLayout(self.ui.formLayout_itp_targetair5)
        self.itp_air5_text_Item = self.itp_scene.addWidget(self.itp_frametxt_targetAir5)
        self.itp_air5_text_Item.setOpacity(0.9)
        self.itp_targetair5_PixItem.setPos(500, 500)
        self.itp_air5_text_Item.setPos(500, 520)

        # 设置item图层位置
        self.itp_targetair1_PixItem.stackBefore(self.itp_ownship_item)
        self.itp_air1_text_Item.stackBefore(self.itp_ownship_item)
        self.itp_targetair1_PixItem.stackBefore(self.itp_border_Item)
        self.itp_air1_text_Item.stackBefore(self.itp_border_Item)
        self.itp_targetair2_PixItem.stackBefore(self.itp_ownship_item)
        self.itp_air2_text_Item.stackBefore(self.itp_ownship_item)
        self.itp_targetair2_PixItem.stackBefore(self.itp_border_Item)
        self.itp_air2_text_Item.stackBefore(self.itp_border_Item)

        self.itp_targetair3_PixItem.stackBefore(self.itp_ownship_item)
        self.itp_air3_text_Item.stackBefore(self.itp_ownship_item)
        self.itp_targetair3_PixItem.stackBefore(self.itp_border_Item)
        self.itp_air3_text_Item.stackBefore(self.itp_border_Item)

        self.itp_targetair4_PixItem.stackBefore(self.itp_ownship_item)
        self.itp_air4_text_Item.stackBefore(self.itp_ownship_item)
        self.itp_targetair4_PixItem.stackBefore(self.itp_border_Item)
        self.itp_air4_text_Item.stackBefore(self.itp_border_Item)

        self.itp_targetair5_PixItem.stackBefore(self.itp_ownship_item)
        self.itp_air5_text_Item.stackBefore(self.itp_ownship_item)
        self.itp_targetair5_PixItem.stackBefore(self.itp_border_Item)
        self.itp_air5_text_Item.stackBefore(self.itp_border_Item)
        self.ui.graphicsView_itp.setScene(self.itp_scene)
        self.ui.graphicsView_itp.setSceneRect(1, 1, 715, 715)

        for i in range(1, 6):
            eval("self.ui.frame_itp_target" + str(i) + ".setVisible(False)")
            eval("self.ui.airb_targetair" + str(i) + "_id_info.setVisible(False)")
            eval("self.ui.airb_target" + str(i) + "_speed_txt.setVisible(False)")
            eval("self.ui.surf_targetair" + str(i) + "_id_info.setVisible(False)")
            eval("self.ui.surf_target" + str(i) + "_speed_txt.setVisible(False)")
            eval("self.ui.vsa_targetair" + str(i) + "_id_info.setVisible(False)")
            eval("self.ui.vsa_target" + str(i) + "_speed_txt.setVisible(False)")
            eval("self.ui.vsa_target" + str(i) + "_dis_txt.setVisible(False)")
            eval("self.ui.vsa_target" + str(i) + "_v1_txt.setVisible(False)")
            eval("self.ui.vsa_target" + str(i) + "_v2_txt.setVisible(False)")
            # 初始化五架目标机不可见
            eval("self.airb_targetair" + str(i) + "_PixItem.setVisible(False)")
            eval("self.airb_air" + str(i) + "_text_Item.setVisible(False)")
            eval("self.surf_targetair" + str(i) + "_PixItem.setVisible(False)")
            eval("self.surf_air" + str(i) + "_text_Item.setVisible(False)")
            eval("self.vsa_targetair" + str(i) + "_PixItem.setVisible(False)")
            eval("self.vsa_air" + str(i) + "_text_Item.setVisible(False)")
            eval("self.itp_targetair" + str(i) + "_PixItem.setVisible(False)")
            eval("self.itp_air" + str(i) + "_text_Item.setVisible(False)")

        self.ui.airb_ownship_lon_txt.setText("")
        self.ui.airb_ownship_lat_txt.setText("")
        self.ui.airb_ownship_altrange_txt.setText("")
        self.ui.vsa_ownship_lon_txt.setText("")
        self.ui.vsa_ownship_lat_txt.setText("")
        self.ui.vsa_ownship_altrange_txt.setText("")
        self.ui.surf_ownship_lon_txt.setText("")
        self.ui.surf_ownship_lat_txt.setText("")
        self.ui.surf_ownship_altrange_txt.setText("")
        self.ui.itp_ownship_lon_txt.setText("")
        self.ui.itp_ownship_lat_txt.setText("")
        self.ui.itp_ownship_altrange_txt.setText("")

    def map_zoom_in(self):
        # 放大一级视图
        js_string_map_zoom_in = 'map.zoomIn();'
        self.browser.page().runJavaScript(js_string_map_zoom_in)  # 初始化本机位置、标注、航线、移动

    def map_zoom_out(self):
        # 缩小一级视图
        js_string_map_zoom_in = 'map.zoomOut();'
        self.browser.page().runJavaScript(js_string_map_zoom_in)  # 初始化本机位置、标注、航线、移动


    def update_cdti_ui(self,info):
        '''

        :param info:
        :return:
        '''
        target_x_list = []  # 目标机x轴坐标序列
        target_y_list = []  # 目标机y轴坐标序列
        target_lon_list = [] #目标机经度序列
        target_lat_list = []  #目标机纬度序列
        target_pic_surf_type = [] #目标机SURF类型序列
        target_itp_x = []    # itp目标机横坐标序列
        target_itp_x_forward = [] # itp相对本机前后位置
        target_itp_y = []     # itp目标机纵坐标序列
        one_pixel_itp_x = 0.0 # itp一坐标单位代表的距离
        target_alt_dif_list=[]          #目标机高度差
        target_air_ground_status_list=[]#目标机空地状态
        target_surf_app_status_list = []#目标机SURF应用状态
        target_angle_list = []  #目标机旋转角
        ownship_angle = 0 #本机航向角
        compass_step = 0 #罗盘步长 单位海里

        map_wigdetId = {0: 'compass_bitmap', 1: 'compass_step', 2: 'ownship_id_txt',
                        3: 'ownship_alt_txt', 4: 'ownship_lon_txt', 5: 'ownship_lat_txt',
                        6: 'ownship_altrange_txt', 7: 'ownship_angle_txt', 8: 'ownship_applstatus',9:'ownship_toa_time',
                        11: 'target1_bitmap', 12: 'target1_id_txt',13: 'target1_speed_txt',
                        14: 'target1_altdif_txt', 15: 'target1_airstatus_txt',16: 'target1_applstatus_bitmap',
                        17: 'target1_lon', 18:'target1_lat',19:'target1_vsa_dis',20:'target1_vsa_velocity',
                        21: 'target1_itp_dis',22:'target1_itp_dis_rate',23:'target1_itp_forward',24:'target1_itp_geometry_status',

                        31: 'target2_bitmap', 32: 'target2_id_txt', 33: 'target2_speed_txt',
                        34: 'target2_altdif_txt', 35: 'target2_airstatus_txt', 36: 'target2_applstatus_bitmap',
                        37: 'target2_lon', 38: 'target2_lat', 39: 'target2_vsa_dis', 40: 'target2_vsa_velocity',
                        41: 'target2_itp_dis', 42: 'target2_itp_dis_rate', 43: 'target2_itp_forward',44: 'target2_itp_geometry_status',

                        51: 'target3_bitmap', 52: 'target3_id_txt', 53: 'target3_speed_txt',
                        54: 'target3_altdif_txt', 55: 'target3_airstatus_txt', 56: 'target3_applstatus_bitmap',
                        57: 'target3_lon', 58: 'target3_lat', 59: 'target3_vsa_dis', 60: 'target3_vsa_velocity',
                        61: 'target3_itp_dis', 62: 'target3_itp_dis_rate', 63: 'target3_itp_forward',64: 'target3_itp_geometry_status',

                        71: 'target4_bitmap', 72: 'target4_id_txt', 73: 'target4_speed_txt',
                        74: 'target4_altdif_txt', 75: 'target4_airstatus_txt', 76: 'target4_applstatus_bitmap',
                        77: 'target4_lon', 78: 'target4_lat', 79: 'target4_vsa_dis', 80: 'target4_vsa_velocity',
                        81: 'target4_itp_dis', 82: 'target4_itp_dis_rate', 83: 'target4_itp_forward',84: 'target4_itp_geometry_status',

                        91: 'target5_bitmap', 92: 'target5_id_txt', 93: 'target5_speed_txt',
                        94: 'target5_altdif_txt', 95: 'target5_airstatus_txt', 96: 'target5_applstatus_bitmap',
                        97: 'target5_lon', 98: 'target5_lat', 99: 'target5_vsa_dis', 100: 'target5_vsa_velocity',
                        101: 'target5_itp_dis', 102: 'target5_itp_dis_rate', 103: 'target5_itp_forward',104: 'target5_itp_geometry_status',
                      }


        if info:
           print("接收到UA发送数据，开始解析")
           print(info)
           break_flag = 0
           max_id_index = 0  #最大id索引，以确定目标机有几架
           num_target = 0 #目标机架数
           temp = []
           self.browser.page().runJavaScript("remove_overlay();")  # 移除surf机场绘制的飞机图标
           for j in range(1, 6):
               # 罗盘飞机图标和飞机文本 隐藏
               eval("self.airb_targetair" + str(j) + "_PixItem.setVisible(False)")
               eval("self.airb_air" + str(j) + "_text_Item.setVisible(False)")
               eval("self.vsa_targetair" + str(j) + "_PixItem.setVisible(False)")
               eval("self.vsa_air" + str(j) + "_text_Item.setVisible(False)")
               eval("self.itp_targetair" + str(j) + "_PixItem.setVisible(False)")
               eval("self.itp_air" + str(j) + "_text_Item.setVisible(False)")
               # Target Info 隐藏
               eval("self.ui.airb_targetair" + str(j) + "_id_info.setVisible(False)")
               eval("self.ui.airb_target" + str(j) + "_speed_txt.setVisible(False)")
               eval("self.ui.surf_targetair" + str(j) + "_id_info.setVisible(False)")
               eval("self.ui.surf_target" + str(j) + "_speed_txt.setVisible(False)")
               eval("self.ui.vsa_targetair" + str(j) + "_id_info.setVisible(False)")
               eval("self.ui.vsa_target" + str(j) + "_speed_txt.setVisible(False)")
               eval("self.ui.vsa_target" + str(j) + "_dis_txt.setVisible(False)")
               eval("self.ui.vsa_target" + str(j) + "_v1_txt.setVisible(False)")
               eval("self.ui.vsa_target" + str(j) + "_v2_txt.setVisible(False)")
               # Itp区域 隐藏
               eval("self.ui.frame_itp_target" + str(j) + ".setVisible(False)")
           for item in info:
               temp.append(item[0])
           max_id_index = max(temp)
           num_target = int(max_id_index/20)
           print(str(num_target)+"架目标机")
           if num_target == 0:#仅绘制本机信息
               for item in info:
                   if item[1] == 46224:  # 设置文本
                       if 'ownship_toa_time' == map_wigdetId[item[0]]:
                           self.ui.airb_time_txt.setText(str(round(item[2], 3)))
                           self.ui.surf_time_txt.setText(str(round(item[2], 3)))
                           self.ui.vsa_time_txt.setText(str(round(item[2], 3)))
                           self.ui.itp_time_txt.setText(str(round(item[2], 3)))
                       if 'ownship_id_txt' == map_wigdetId[item[0]]:  # 本机ID
                           self.ui.surf_ownship_id_txt.setText(str(item[2].decode()))
                           self.ui.airb_ownship_id_txt.setText(str(item[2].decode()))
                           self.ui.vsa_ownship_id_txt.setText(str(item[2].decode()))
                           self.ui.itp_ownship_id_txt.setText(str(item[2].decode()))
                       if 'ownship_lon_txt' == map_wigdetId[item[0]]:  # 本机经度
                           self.ui.airb_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                           self.ui.surf_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                           self.ui.vsa_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                           self.ui.itp_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                       if 'ownship_lat_txt' == map_wigdetId[item[0]]:  # 本机纬度
                           self.ui.airb_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                           self.ui.surf_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                           self.ui.vsa_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                           self.ui.itp_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                       if 'ownship_altrange_txt' == map_wigdetId[item[0]]:
                           self.ui.airb_ownship_altrange_txt.setText(str(item[2]) + "ft")
                           self.ui.surf_ownship_altrange_txt.setText(str(item[2]) + "ft")
                           self.ui.vsa_ownship_altrange_txt.setText(str(item[2]) + "ft")
                           self.ui.itp_ownship_altrange_txt.setText(str(item[2]) + "ft")
                       if 'ownship_alt_txt' == map_wigdetId[item[0]]:
                           self.ui.airb_ownship_alt_txt.setText(str(item[2]))
                           self.ui.surf_ownship_alt_txt.setText(str(item[2]))
                           self.ui.vsa_ownship_alt_txt.setText(str(item[2]))
                           self.ui.itp_ownship_alt_txt.setText(str(item[2]))
                           itp_own_alt = int((item[2] + 500) / 1000) * 10
                           self.ui.itp_own_alt.setText(str(itp_own_alt))
                           self.ui.itp_own_alt1.setText(str(itp_own_alt - 30))
                           self.ui.itp_own_alt2.setText(str(itp_own_alt - 20))
                           self.ui.itp_own_alt3.setText(str(itp_own_alt - 10))
                           self.ui.itp_own_alt4.setText(str(itp_own_alt + 10))
                           self.ui.itp_own_alt5.setText(str(itp_own_alt + 20))
                           self.ui.itp_own_alt6.setText(str(itp_own_alt + 30))
                       if 'ownship_angle_txt' == map_wigdetId[item[0]]:  # 设置本机航向角
                           self.surf_air_heading_txt.setText(str(item[2]))
                           self.airb_air_heading_txt.setText(str(item[2]))
                           self.vsa_air_heading_txt.setText(str(item[2]))
                           self.itp_air_heading_txt.setText(str(item[2]))
                       if 'compass_step' == map_wigdetId[item[0]]:
                           compass_step = int(item[2])
                           one_pixel_itp_x = float(compass_step / 115)
                           self.ui.itp_own_dis1.setText(str(2 * compass_step))
                           self.ui.itp_own_dis2.setText(str(compass_step))
                           self.ui.itp_own_dis3.setText(str(compass_step))
                           self.ui.itp_own_dis4.setText(str(2 * compass_step))
                           self.ui.surf_compass_step.setText(str(compass_step))
                           self.ui.airb_compass_step.setText(str(compass_step))
                           self.ui.vsa_compass_step.setText(str(compass_step))
                           self.ui.itp_compass_step.setText(str(compass_step))
                           self.ui.surf_compass_step1.setText(str(-2 * compass_step))
                           self.ui.surf_compass_step2.setText(str(-1 * compass_step))
                           self.ui.surf_compass_step3.setText(str(1 * compass_step))
                           self.ui.surf_compass_step4.setText(str(2 * compass_step))
                           self.ui.surf_compass_step5.setText(str(-1 * compass_step))
                           self.ui.surf_compass_step6.setText(str(-2 * compass_step))
                           self.ui.airb_compass_step1.setText(str(-2 * compass_step))
                           self.ui.airb_compass_step2.setText(str(-1 * compass_step))
                           self.ui.airb_compass_step3.setText(str(1 * compass_step))
                           self.ui.airb_compass_step4.setText(str(2 * compass_step))
                           self.ui.airb_compass_step5.setText(str(-1 * compass_step))
                           self.ui.airb_compass_step6.setText(str(-2 * compass_step))
                           self.ui.vsa_compass_step1.setText(str(-2 * compass_step))
                           self.ui.vsa_compass_step2.setText(str(-1 * compass_step))
                           self.ui.vsa_compass_step3.setText(str(1 * compass_step))
                           self.ui.vsa_compass_step4.setText(str(2 * compass_step))
                           self.ui.vsa_compass_step5.setText(str(-1 * compass_step))
                           self.ui.vsa_compass_step6.setText(str(-2 * compass_step))
                           self.ui.itp_compass_step1.setText(str(-2 * compass_step))
                           self.ui.itp_compass_step2.setText(str(-1 * compass_step))
                           self.ui.itp_compass_step3.setText(str(1 * compass_step))
                           self.ui.itp_compass_step4.setText(str(2 * compass_step))
                           self.ui.itp_compass_step5.setText(str(-1 * compass_step))
                           self.ui.itp_compass_step6.setText(str(-2 * compass_step))
                   if item[1] == 45808:  # 设置飞机应用状态图片
                       airb_app_status = '{:04b}'.format(item[2])[-1]
                       surf_app_status = '{:04b}'.format(item[2])[-2]
                       vsa_app_status = '{:04b}'.format(item[2])[-3]
                       itp_app_status = '{:04b}'.format(item[2])[-4]
                       if 'ownship_applstatus' == map_wigdetId[item[0]]:
                           self.ui.airb_ownship_applstatus_bitmap.setPixmap(
                               QPixmap("pic/appstatus" + str(airb_app_status) + ".png"))
                           self.ui.surf_ownship_applstatus_bitmap.setPixmap(
                               QPixmap("pic/appstatus" + str(surf_app_status) + ".png"))
                           self.ui.vsa_ownship_applstatus_bitmap.setPixmap(
                               QPixmap("pic/appstatus" + str(vsa_app_status) + ".png"))
                           self.ui.itp_ownship_applstatus_bitmap.setPixmap(
                               QPixmap("pic/appstatus" + str(itp_app_status) + ".png"))
                   if item[1] == 45760: # 设置旋转角
                       if 'compass_bitmap' == map_wigdetId[item[0]]:
                           ownship_angle = item[2]
                           self.surf_compass_Item.setRotation(360 - int(item[2]))
                           self.airb_compass_Item.setRotation(360 - int(item[2]))
                           self.vsa_compass_Item.setRotation(360 - int(item[2]))
                           self.itp_compass_Item.setRotation(360 - int(item[2]))
           if num_target >=1: #存在目标机
               for i in range(1,num_target+1):
                   #罗盘飞机图标和飞机文本 显示
                   eval("self.airb_targetair"+str(i)+"_PixItem.setVisible(True)")
                   eval("self.airb_air" + str(i) + "_text_Item.setVisible(True)")
                   eval("self.vsa_targetair"+str(i)+"_PixItem.setVisible(True)")
                   eval("self.vsa_air" + str(i) + "_text_Item.setVisible(True)")
                   eval("self.itp_targetair"+str(i)+"_PixItem.setVisible(True)")
                   eval("self.itp_air" + str(i) + "_text_Item.setVisible(True)")
                   # Target Info 显示
                   eval("self.ui.airb_targetair"+str(i)+"_id_info.setVisible(True)")
                   eval("self.ui.airb_target" + str(i) + "_speed_txt.setVisible(True)")
                   eval("self.ui.surf_targetair"+str(i)+"_id_info.setVisible(True)")
                   eval("self.ui.surf_target" + str(i) + "_speed_txt.setVisible(True)")
                   eval("self.ui.vsa_targetair"+str(i)+"_id_info.setVisible(True)")
                   eval("self.ui.vsa_target" + str(i) + "_speed_txt.setVisible(True)")
                   eval("self.ui.vsa_target"+str(i)+"_dis_txt.setVisible(True)")
                   eval("self.ui.vsa_target" + str(i) + "_v1_txt.setVisible(True)")
                   eval("self.ui.vsa_target" + str(i) + "_v2_txt.setVisible(True)")
                   # Itp区域 显示
                   eval("self.ui.frame_itp_target" + str(i) + ".setVisible(True)")
               for item in info:
                   break_flag += 1
                   try:
                       if break_flag >1 and item[0] == 0:
                           break
                       if item[1] == 46224:  # 设置文本
                           if 'ownship_toa_time' == map_wigdetId[item[0]]:
                               self.ui.airb_time_txt.setText(str(round(item[2], 3)))
                               self.ui.surf_time_txt.setText(str(round(item[2], 3)))
                               self.ui.vsa_time_txt.setText(str(round(item[2], 3)))
                               self.ui.itp_time_txt.setText(str(round(item[2], 3)))
                           if 'ownship_id_txt' == map_wigdetId[item[0]]: #本机ID
                               self.ui.surf_ownship_id_txt.setText(str(item[2].decode()))
                               self.ui.airb_ownship_id_txt.setText(str(item[2].decode()))
                               self.ui.vsa_ownship_id_txt.setText(str(item[2].decode()))
                               self.ui.itp_ownship_id_txt.setText(str(item[2].decode()))
                           if 'ownship_lon_txt' == map_wigdetId[item[0]]: #本机经度
                               self.ui.airb_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                               self.ui.surf_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                               self.ui.vsa_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                               self.ui.itp_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_lat_txt' == map_wigdetId[item[0]]: #本机纬度
                               self.ui.airb_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                               self.ui.surf_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                               self.ui.vsa_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                               self.ui.itp_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_altrange_txt' == map_wigdetId[item[0]]:
                               self.ui.airb_ownship_altrange_txt.setText(str(item[2])+ "ft")
                               self.ui.surf_ownship_altrange_txt.setText(str(item[2])+ "ft")
                               self.ui.vsa_ownship_altrange_txt.setText(str(item[2]) + "ft")
                               self.ui.itp_ownship_altrange_txt.setText(str(item[2]) + "ft")
                           if 'ownship_alt_txt' == map_wigdetId[item[0]]:
                               self.ui.airb_ownship_alt_txt.setText(str(item[2]))
                               self.ui.surf_ownship_alt_txt.setText(str(item[2]))
                               self.ui.vsa_ownship_alt_txt.setText(str(item[2]))
                               self.ui.itp_ownship_alt_txt.setText(str(item[2]))
                               itp_own_alt =  int((item[2]+500)/1000)*10
                               self.ui.itp_own_alt.setText(str(itp_own_alt))
                               self.ui.itp_own_alt1.setText(str(itp_own_alt - 30))
                               self.ui.itp_own_alt2.setText(str(itp_own_alt - 20))
                               self.ui.itp_own_alt3.setText(str(itp_own_alt - 10))
                               self.ui.itp_own_alt4.setText(str(itp_own_alt + 10))
                               self.ui.itp_own_alt5.setText(str(itp_own_alt + 20))
                               self.ui.itp_own_alt6.setText(str(itp_own_alt + 30))
                           if 'ownship_angle_txt' == map_wigdetId[item[0]]:#设置本机航向角
                               self.surf_air_heading_txt.setText(str(item[2]))
                               self.airb_air_heading_txt.setText(str(item[2]))
                               self.vsa_air_heading_txt.setText(str(item[2]))
                               self.itp_air_heading_txt.setText(str(item[2]))
                           for i in range(1,6):
                               if eval("'target"+str(i)+"_lon'") == map_wigdetId[item[0]]:#目标机经纬度
                                   target_lon_list.append(item[2])
                               if eval("'target"+str(i)+"_lat'") == map_wigdetId[item[0]]:#目标机经纬度
                                   target_lat_list.append(item[2])
                               if eval("'target"+str(i)+"_id_txt'") == map_wigdetId[item[0]]:#设置目标机id
                                   eval("self.ui.airb_target"+str(i)+"_id_txt").setText(str(item[2].decode()))
                                   eval("self.ui.surf_target" + str(i) + "_id_txt").setText(str(item[2].decode()))
                                   eval("self.ui.vsa_target" + str(i) + "_id_txt").setText(str(item[2].decode()))
                                   eval("self.ui.itp_target" + str(i) + "_id_txt").setText(str(item[2].decode()))
                                   eval("self.ui.surf_targetair"+str(i)+"_id_info").setText(str(item[2].decode()))
                                   eval("self.ui.airb_targetair" + str(i) + "_id_info").setText(str(item[2].decode()))
                                   eval("self.ui.vsa_targetair" + str(i) + "_id_info").setText(str(item[2].decode()))
                                   eval("self.ui.itp_alt_target" + str(i) + "_id").setText(str(item[2].decode()))
                               if eval("'target"+str(i)+"_altdif_txt'") == map_wigdetId[item[0]]: #目标机高度差
                                   current_alt = int(self.ui.itp_ownship_alt_txt.text())+ item[2]*100
                                   target_itp_y.append(int(current_alt / 100))
                                   target_alt_dif_list.append(item[2])
                                   if item[2]>0:
                                       eval("self.ui.airb_target"+ str(i) + "_altdif_txt").setText("+"+str(item[2]))
                                       eval("self.ui.surf_target"+ str(i) + "_altdif_txt").setText("+"+str(item[2]))
                                       eval("self.ui.vsa_target" + str(i) + "_altdif_txt").setText("+"+str(item[2]))
                                       eval("self.ui.itp_target" + str(i) + "_altdif_txt").setText("+"+str(item[2]))
                                   else:
                                       eval("self.ui.airb_target" + str(i) + "_altdif_txt").setText(str(item[2]))
                                       eval("self.ui.surf_target" + str(i) + "_altdif_txt").setText(str(item[2]))
                                       eval("self.ui.vsa_target" + str(i) + "_altdif_txt").setText(str(item[2]))
                                       eval("self.ui.itp_target" + str(i) + "_altdif_txt").setText(str(item[2]))
                               if eval("'target"+str(i)+"_airstatus_txt'") == map_wigdetId[item[0]]:#目标机空地状态
                                   if item[2] == 1:#AIR
                                       target_air_ground_status_list.append("AIR")
                                   elif item[2] == 2:#GROUND
                                       target_air_ground_status_list.append("GROUND")
                                       eval("self.ui.airb_target"+ str(i) + "_airstatus_txt").setText("GROUND")
                                       eval("self.ui.vsa_target" + str(i) + "_airstatus_txt").setText("GROUND")
                                       eval("self.ui.itp_target" + str(i) + "_airstatus_txt").setText("GROUND")
                               if eval("'target"+str(i)+"_speed_txt'") == map_wigdetId[item[0]]: #目标机地速差
                                   eval("self.ui.surf_target"+ str(i) + "_speed_txt").setText(str(round(item[2],6)))
                                   eval("self.ui.airb_target"+ str(i) + "_speed_txt").setText(str(round(item[2],6)))
                                   eval("self.ui.vsa_target" + str(i) + "_speed_txt").setText(str(round(item[2],6)))
                               if eval("'target"+str(i)+"_vsa_dis'")== map_wigdetId[item[0]]:#VSA距离
                                   eval("self.ui.vsa_target"+str(i)+"_dis_txt").setText(str(round(item[2],3)))
                               if eval("'target"+str(i)+"_vsa_velocity'")== map_wigdetId[item[0]]:#VSA速度
                                   eval("self.ui.vsa_target"+str(i)+"_v1_txt").setText(str(round(item[2], 3)))
                                   eval("self.ui.vsa_target"+str(i)+"_v2_txt").setText(str(round(item[2], 3)))
                               if eval("'target"+str(i)+"_itp_dis'")== map_wigdetId[item[0]]:#ITP距离
                                   eval("self.ui.itp_alt_target"+str(i)+"_dis").setText(str(round(item[2],1))+"NM")
                                   target_itp_x.append(round(item[2], 1))
                               if eval("'target"+str(i)+"_itp_dis_rate'")== map_wigdetId[item[0]]:#ITP距离变化率
                                   eval("self.ui.itp_alt_target"+str(i)+"_dis_rate").setText(str(int(item[2]))+"KT")
                                   target_itp_x.append(round(item[2], 1))
                               if eval("'target" + str(i) + "_itp_geometry_status'") == map_wigdetId[item[0]]:#itp有效
                                   if item[2] == 1:  # ITP有效
                                       eval("self.ui.itp_bitmap_target"+str(i)).setPixmap(QPixmap("pic/itp_air2.png"))
                                       eval("self.ui.itp_alt_target"+str(i)+"_id").setStyleSheet("color:rgb(0, 255, 255)")
                                       eval("self.ui.itp_alt_target"+str(i)+"_dis").setStyleSheet("color:rgb(0, 255, 255)")
                                       eval("self.ui.itp_alt_target" + str(i) + "_dis_rate").setStyleSheet("color:rgb(0, 255, 255)")
                                   else:
                                       eval("self.ui.itp_bitmap_target" + str(i)).setPixmap(QPixmap("pic/itp_air1.png"))
                               if eval("'target" + str(i) + "_itp_forward'") == map_wigdetId[item[0]]:#1相对本机前 2相对本机后
                                   target_itp_x_forward.append(item[2])
                           if 'compass_step' == map_wigdetId[item[0]]:
                               compass_step = int(item[2])
                               one_pixel_itp_x = float(compass_step/115)
                               self.ui.itp_own_dis1.setText(str(2 *compass_step))
                               self.ui.itp_own_dis2.setText(str(compass_step))
                               self.ui.itp_own_dis3.setText(str(compass_step))
                               self.ui.itp_own_dis4.setText(str(2 *compass_step))
                               self.ui.surf_compass_step.setText(str(compass_step))
                               self.ui.airb_compass_step.setText(str(compass_step))
                               self.ui.vsa_compass_step.setText(str(compass_step))
                               self.ui.itp_compass_step.setText(str(compass_step))
                               self.ui.surf_compass_step1.setText(str(-2 * compass_step))
                               self.ui.surf_compass_step2.setText(str(-1 * compass_step))
                               self.ui.surf_compass_step3.setText(str(1 * compass_step))
                               self.ui.surf_compass_step4.setText(str(2 * compass_step))
                               self.ui.surf_compass_step5.setText(str(-1 * compass_step))
                               self.ui.surf_compass_step6.setText(str(-2 * compass_step))
                               self.ui.airb_compass_step1.setText(str(-2 * compass_step))
                               self.ui.airb_compass_step2.setText(str(-1 * compass_step))
                               self.ui.airb_compass_step3.setText(str(1 * compass_step))
                               self.ui.airb_compass_step4.setText(str(2 * compass_step))
                               self.ui.airb_compass_step5.setText(str(-1 * compass_step))
                               self.ui.airb_compass_step6.setText(str(-2 * compass_step))
                               self.ui.vsa_compass_step1.setText(str(-2 * compass_step))
                               self.ui.vsa_compass_step2.setText(str(-1 * compass_step))
                               self.ui.vsa_compass_step3.setText(str(1 * compass_step))
                               self.ui.vsa_compass_step4.setText(str(2 * compass_step))
                               self.ui.vsa_compass_step5.setText(str(-1 * compass_step))
                               self.ui.vsa_compass_step6.setText(str(-2 * compass_step))
                               self.ui.itp_compass_step1.setText(str(-2 * compass_step))
                               self.ui.itp_compass_step2.setText(str(-1 * compass_step))
                               self.ui.itp_compass_step3.setText(str(1 * compass_step))
                               self.ui.itp_compass_step4.setText(str(2 * compass_step))
                               self.ui.itp_compass_step5.setText(str(-1 * compass_step))
                               self.ui.itp_compass_step6.setText(str(-2 * compass_step))
                       if item[1] == 45808:  # 设置飞机应用状态图片
                           airb_app_status = '{:04b}'.format(item[2])[-1]
                           surf_app_status = '{:04b}'.format(item[2])[-2]
                           vsa_app_status = '{:04b}'.format(item[2])[-3]
                           itp_app_status = '{:04b}'.format(item[2])[-4]
                           if 'ownship_applstatus' == map_wigdetId[item[0]]:
                               self.ui.airb_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(airb_app_status) + ".png"))
                               self.ui.surf_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(surf_app_status) + ".png"))
                               self.ui.vsa_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(vsa_app_status) + ".png"))
                               self.ui.itp_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(itp_app_status) + ".png"))
                           for i in range(1, 6):
                               if eval("'target"+str(i)+"_applstatus_bitmap'") == map_wigdetId[item[0]]:
                                   target_surf_app_status_list.append(surf_app_status)
                                   eval("self.ui.airb_target"+str(i)+"_applstatus_bitmap").setPixmap(QPixmap("pic/appstatus" + str(airb_app_status) + ".png"))
                                   eval("self.ui.surf_target" + str(i) + "_applstatus_bitmap").setPixmap(
                                       QPixmap("pic/appstatus" + str(surf_app_status) + ".png"))
                                   eval("self.ui.vsa_target" + str(i) + "_applstatus_bitmap").setPixmap(
                                       QPixmap("pic/appstatus" + str(vsa_app_status) + ".png"))
                                   eval("self.ui.itp_target" + str(i) + "_applstatus_bitmap").setPixmap(
                                       QPixmap("pic/appstatus" + str(itp_app_status) + ".png"))
                       if item[1] == 46272: #设置目标机图标
                           for i in range(1, 6):
                               if eval("'target"+str(i)+"_bitmap'") == map_wigdetId[item[0]]:
                                   airb_value = item[2] & int('0xf',16)
                                   surf_value = (item[2] >> 4) & int('0xf',16)
                                   vsa_value = (item[2] >> 8) & int('0xf',16)
                                   itp_value  = (item[2] >> 12) & int('0xf',16)
                                   print(str(i)+"号目标机飞机图标依次为："+str(airb_value)+str(surf_value)+str(vsa_value)+str(itp_value))

                                   pixmap_airb_targetship = QPixmap("pic/air" + str(airb_value) + ".png")  # 1号类型目标机图标
                                   pixmap_surf_targetship = QPixmap("pic/air" + str(surf_value) + ".png")  # 1号类型目标机图标
                                   pixmap_vsa_targetship = QPixmap("pic/air" + str(vsa_value) + ".png")  # 1号类型目标机图标
                                   pixmap_itp_targetship = QPixmap("pic/air" + str(itp_value) + ".png")  # 1号类型目标机图标
                                   eval("self.airb_targetair"+  str(i)+"_PixItem.setPixmap(pixmap_airb_targetship)")
                                   eval("self.surf_targetair" + str(i) + "_PixItem.setPixmap(pixmap_surf_targetship)")
                                   eval("self.vsa_targetair" + str(i) + "_PixItem.setPixmap(pixmap_vsa_targetship)")
                                   eval("self.itp_targetair" + str(i) + "_PixItem.setPixmap(pixmap_itp_targetship)")
                                   target_pic_surf_type.append(surf_value)
                       if item[1] == 45760: # 设置旋转角
                           if 'compass_bitmap' == map_wigdetId[item[0]]:
                               ownship_angle = item[2]
                               self.surf_compass_Item.setRotation(360 - int(item[2]))
                               self.airb_compass_Item.setRotation(360 - int(item[2]))
                               self.vsa_compass_Item.setRotation(360 - int(item[2]))
                               self.itp_compass_Item.setRotation(360 - int(item[2]))
                           for i in range(1, 6):
                               if eval("'target"+str(i)+"_bitmap'") == map_wigdetId[item[0]]:
                                   target_angle_list.append(item[2])
                                   eval("self.airb_targetair" + str(i) + "_PixItem").setRotation(int(item[2]))
                                   eval("self.surf_targetair" + str(i) + "_PixItem").setRotation(int(item[2]))
                                   eval("self.vsa_targetair" + str(i) + "_PixItem").setRotation(int(item[2]))
                                   eval("self.itp_targetair" + str(i) + "_PixItem").setRotation(int(item[2]))
                       if item[1] == 45824: # 设置目标机X轴坐标
                           for i in range(1, 6):
                               if eval("'target" + str(i) + "_bitmap'") == map_wigdetId[item[0]]:
                                   target_x_list.append(int(item[2]))
                       if item[1] == 45840: # 设置目标机Y轴坐标
                           for i in range(1, 6):
                               if eval("'target" + str(i) + "_bitmap'") == map_wigdetId[item[0]]:
                                   target_y_list.append(int(item[2]))
                   except:
                       import traceback
                       traceback.print_exc()
                       print("更新界面UI有错误，请检查~")
                       continue
               #设置目标机位置
               print(target_x_list)
               print(target_y_list)
               one_pixel_itp_y = 1 / 7
               own_alt = int(int(self.ui.itp_ownship_alt_txt.text()) / 100)
               for i in range(0,num_target):
                   # 绘制罗盘中目标机图标和文本位置
                   eval('self.airb_targetair'+str(i+1)+'_PixItem.setPos(target_x_list[i], target_y_list[i])')
                   eval('self.airb_air' + str(i+1) + '_text_Item.setPos(target_x_list[i], target_y_list[i]+20)')
                   eval('self.vsa_targetair'+str(i+1)+'_PixItem.setPos(target_x_list[i], target_y_list[i])')
                   eval('self.vsa_air' + str(i+1) + '_text_Item.setPos(target_x_list[i], target_y_list[i]+20)')
                   eval('self.itp_targetair'+str(i+1)+'_PixItem.setPos(target_x_list[i], target_y_list[i])')
                   eval('self.itp_air' + str(i+1) + '_text_Item.setPos(target_x_list[i], target_y_list[i]+20)')
                   # 绘制Itp区域
                   if target_itp_x_forward[i] == 1:#相对本机前
                       eval("self.ui.frame_itp_target"+str(i+1) + ".setGeometry(QRect(275 + int( target_itp_x[i]/one_pixel_itp_x), 380 - int((target_itp_y[i]- own_alt) / one_pixel_itp_y),121, 81))")
                   else: #相对本机后
                       eval("self.ui.frame_itp_target" + str(i+1) + ".setGeometry(QRect(275 - int( target_itp_x[i]/one_pixel_itp_x), 380 - int((target_itp_y[i] - own_alt) / one_pixel_itp_y),121, 81))")
               #绘制surf区域
               # step1: 移动地图,将地图中心点变更为本机坐标点
               own_lon = round(float(self.ui.surf_ownship_lon_txt.text()), 6)
               own_lat = round(float(self.ui.surf_ownship_lat_txt.text()), 6)
               js_string_move_map = '''move_map(%f,%f);''' % (own_lon, own_lat)
               self.browser.page().runJavaScript(js_string_move_map)  # 初始化本机位置、标注、航线、移动
               #step2: 地图角度旋转 按照本机航向旋转
               ownship_angle =   float(self.surf_air_heading_txt.text())
               self.map_widgetItem.setRotation(-ownship_angle)
               print(target_pic_surf_type)
               print(target_lon_list)
               print(target_lat_list)
               print(target_alt_dif_list)
               print(target_air_ground_status_list)
               print(target_surf_app_status_list)
               print(target_angle_list)
               for i in range(0, num_target):
                   if target_pic_surf_type and target_lon_list and target_lat_list:
                       if target_lon_list[i] == 0.0 and target_lat_list[i] == 0.0:#仅tcas surf无法显示目标机
                           angle_temp = 0.0 #方位角
                           dis_temp = 0.0 #相对距离 km
                           #(320 - 15, 320 + 17.5)
                           dx = abs(target_x_list[i] - 305)
                           dy = abs(target_y_list[i] - 337.5)
                           dxy = sqrt(dx**2+dy**2)
                           angle_temp = atan(dx/dy)* 180 / pi
                           dis_temp = compass_step * 1.852 * dxy/800
                           own_lon = float(self.ui.surf_ownship_lon_txt.text())
                           own_lat = float(self.ui.surf_ownship_lat_txt.text())
                           print("angle_temp：" + str(angle_temp))
                           print("dis_temp：" + str(dis_temp))
                           ga = Geography_Analysis()
                           target_lon,target_lat = ga.get_lngAndlat(own_lon,own_lat,angle_temp,dis_temp)
                           print(target_lon,target_lat)
                           js_string1 = '''update_target_pic(%d,%d,%f,%f,%d);''' % (
                           i + 1, target_pic_surf_type[i], target_lon, target_lat,ownship_angle+target_angle_list[i])
                           print(js_string1)
                           self.browser.page().runJavaScript(js_string1)  # 更新目标机目标
                           if target_alt_dif_list and target_air_ground_status_list and target_surf_app_status_list:
                               js_string2 = '''update_target_info(%d,'%s','%s','%s',%d,%f,%f,%d);'''%(i+1,eval('self.ui.surf_targetair'+str(i+1)+'_id_info.text()'),str(target_alt_dif_list[i]),target_air_ground_status_list[i],int(target_surf_app_status_list[i]),target_lon, target_lat,ownship_angle)
                               print(js_string2)
                               self.browser.page().runJavaScript(js_string2)  # 更新目标机航班号...
                       else: #正常情况
                           js_string1 = '''update_target_pic(%d,%d,%f,%f,%d);'''%(i+1,target_pic_surf_type[i],target_lon_list[i], target_lat_list[i],ownship_angle+target_angle_list[i])
                           print(js_string1)
                           self.browser.page().runJavaScript(js_string1)  # 更新目标机目标
                           if target_alt_dif_list and target_air_ground_status_list and target_surf_app_status_list:
                               js_string2 = '''update_target_info(%d,'%s','%s','%s',%d,%f,%f,%d);'''%(i+1,eval('self.ui.surf_targetair'+str(i+1)+'_id_info.text()'),str(target_alt_dif_list[i]),target_air_ground_status_list[i],int(target_surf_app_status_list[i]),target_lon_list[i], target_lat_list[i],ownship_angle)
                               print(js_string2)
                               self.browser.page().runJavaScript(js_string2)  # 更新目标机航班号、空地状态、应用状态

    def send_data1_to_ua(self):
        try:
            self.pack_CDTI_TO_UA_DATA(self.cdti_to_ua_in_data,0)
            buf = bytes(168)
            buf = self.cdti_to_ua_in_data.encode()
            print("待发送的字节:" + str(buf))
            socket_661 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
            socket_661.sendto(buf, self.ip_port_toUA)
        except:
            print("发送数据出错")

    def send_data2_to_ua(self):
        try:
            self.pack_CDTI_TO_UA_DATA(self.cdti_to_ua_out_data,1)
            buf = bytes(168)
            buf = self.cdti_to_ua_out_data.encode()
            print("待发送的字节:" + str(buf))
            socket_661 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
            socket_661.sendto(buf, self.ip_port_toUA)
        except:
            print("发送数据出错")

    def pack_CDTI_TO_UA_DATA(self,data,event_id):
        try:
            data.A661_BEGIN_BLOCK = int('B0', 16)
            data.LayerIdent = 2
            data.ContextNumber = 1
            data.BlockSize = 24
            surf_map_in_widget_event_paramater = A661_NOTIFY_WIDGET_EVENT_12BYTE()
            surf_map_in_widget_event_paramater.A661_NOTIFY_WIDGET_EVENT = int('CC01',16)
            surf_map_in_widget_event_paramater.CommandSize = 12
            surf_map_in_widget_event_paramater.WidgetIdent = 1
            surf_map_in_widget_event_paramater.EventOrigin = int('CCD1 ',16)
            surf_map_in_widget_event_paramater.EventID =  event_id  #button按钮点击
            surf_map_in_widget_event_paramater.UnusedPad = '00'.encode()
            data.Compass_InOut_Click_Envent = surf_map_in_widget_event_paramater
            data.A661_END_BLOCK = int('D0', 16)
            data.Unused1 = '000'.encode()
            return data
        except:
            print("数据打包出错~")


if __name__=='__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())