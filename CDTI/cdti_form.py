import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import*
import cdti_mainform
import cProfile
import socket
import datetime
from math import *
from geography_analysis import *
from a661_api import *
import time
class Receive_661_DataThread(QThread):
    signal_a = pyqtSignal(list)
    def __init__(self):
        super(Receive_661_DataThread, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("", 8006))  # 绑定服务器的ip和端口
        self.count_loop = 0  # 循环计数器
        self.receive_Info = []

    def run(self):
        while True:
            buffer = self.s.recv(4096)  # 一次接收最大字节长度
            receive_Data = UA_TO_CDTI_DATA()
            receive_Data.decode(buffer)
            #print(receive_Data.ContextNumber)
            len_frame = receive_Data.ContextNumber >> 8 #高8位表示帧长度  example：6
            index_frame = receive_Data.ContextNumber & 0xFF #低8位表示帧索引 example：1
            #print(len_frame,index_frame)
            if index_frame <= len_frame:
                id_addvalue = (index_frame-1)*100
                if index_frame == 1:#本机信息仅接收一次
                    self.receive_Info.append([receive_Data.Compass_Bitmap_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Compass_Bitmap_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Compass_Bitmap_SET_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Compass_Step_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Compass_Step_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Compass_Step_SET_PARAMATER.ParameterValueBuffer])
                    # id 2-9
                    self.receive_Info.append([receive_Data.Ownship_FlightId_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Ownship_FlightId_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Ownship_FlightId_SET_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Ownship_Alt_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Ownship_Alt_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Ownship_Alt_SET_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Ownship_Lon_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Ownship_Lon_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Ownship_Lon_SET_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Ownship_Lat_SET_PARAMATER.WidgetIdent,
                                         receive_Data.Ownship_Lat_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Ownship_Lat_SET_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Ownship_Alt_Range_PARAMATER.WidgetIdent,
                                         receive_Data.Ownship_Alt_Range_PARAMATER.ParameterIdent,
                                         receive_Data.Ownship_Alt_Range_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Ownship_Course_Angle_PARAMATER.WidgetIdent,
                                         receive_Data.Ownship_Course_Angle_PARAMATER.ParameterIdent,
                                         receive_Data.Ownship_Course_Angle_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Ownship_App_Status_PARAMATER.WidgetIdent,
                                         receive_Data.Ownship_App_Status_PARAMATER.ParameterIdent,
                                         receive_Data.Ownship_App_Status_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Ownship_TOA_TIME_PARAMATER.WidgetIdent,
                                         receive_Data.Ownship_TOA_TIME_PARAMATER.ParameterIdent,
                                         receive_Data.Ownship_TOA_TIME_PARAMATER.ParameterValueBuffer])
                for i in range(0,5):
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_Visible_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_Visible_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_Visible_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_Pic_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_Pic_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_Pic_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_RotateAngle_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_RotateAngle_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_RotateAngle_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_X_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_X_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_X_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_Y_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_Y_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_Y_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_FlightId_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_FlightId_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_FlightId_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_Speed_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_Speed_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_Speed_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_Alt_dif_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_Alt_dif_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_Alt_dif_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_Status_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_Status_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_Status_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_AppStatus_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_AppStatus_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_AppStatus_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_Lon_SET_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_Lon_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_Lon_SET_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_Lat_SET_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_Lat_SET_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_Lat_SET_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_VSA_DIS_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_VSA_DIS_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_VSA_DIS_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_VSA_Velocity_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_VSA_Velocity_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer,
                                         receive_Data.Target_Lists[i].Target_VSA_Velocity_PARAMATER.ParameterValueBuffer2])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_ITP_DIS_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_ITP_DIS_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_ITP_DIS_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_ITP_DIS_RATE_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_ITP_DIS_RATE_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_ITP_DIS_RATE_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_ITP_FORWARD_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_ITP_FORWARD_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_ITP_FORWARD_PARAMATER.ParameterValueBuffer])
                    self.receive_Info.append([receive_Data.Target_Lists[i].Target_ITP_Geometry_Status_PARAMATER.WidgetIdent+id_addvalue,
                                         receive_Data.Target_Lists[i].Target_ITP_Geometry_Status_PARAMATER.ParameterIdent,
                                         receive_Data.Target_Lists[i].Target_ITP_Geometry_Status_PARAMATER.ParameterValueBuffer])
                if index_frame == len_frame or self.count_loop == 20:#接收到的帧数量等于帧长度或循环20次后,发送数据给UI
                    #print(self.receive_Info)
                    self.signal_a.emit(self.receive_Info)
                    self.count_loop = 0  # 循环计数器
                    self.receive_Info = []
            self.count_loop += 1


class MainWindow(QMainWindow):

    # 0设置显示/隐藏 1设置文本 2设置图片源 3设置symbol源 4设置旋转角 5设置X坐标 6设置Y坐标
    map_setparaId = {'46384‬': 0, '46224': 1, '45808': 2, '46272': 3, '45760': 4, '45824': 5, '45840': 6}

    map_wigdetId = {0: 'compass_bitmap', 1: 'compass_step', 2: 'ownship_id_txt',
                    3: 'ownship_alt_txt', 4: 'ownship_lon_txt', 5: 'ownship_lat_txt',
                    6: 'ownship_altrange_txt', 7: 'ownship_angle_txt', 8: 'ownship_applstatus', 9: 'ownship_toa_time',
                    11: 'target1_bitmap', 12: 'target1_id_txt', 13: 'target1_speed_txt',
                    14: 'target1_altdif_txt', 15: 'target1_airstatus_txt', 16: 'target1_applstatus_bitmap',
                    17: 'target1_lon', 18: 'target1_lat', 19: 'target1_vsa_dis', 20: 'target1_vsa_velocity',
                    21: 'target1_itp_dis', 22: 'target1_itp_dis_rate', 23: 'target1_itp_forward',
                    24: 'target1_itp_geometry_status',

                    31: 'target2_bitmap', 32: 'target2_id_txt', 33: 'target2_speed_txt',
                    34: 'target2_altdif_txt', 35: 'target2_airstatus_txt', 36: 'target2_applstatus_bitmap',
                    37: 'target2_lon', 38: 'target2_lat', 39: 'target2_vsa_dis', 40: 'target2_vsa_velocity',
                    41: 'target2_itp_dis', 42: 'target2_itp_dis_rate', 43: 'target2_itp_forward',
                    44: 'target2_itp_geometry_status',

                    51: 'target3_bitmap', 52: 'target3_id_txt', 53: 'target3_speed_txt',
                    54: 'target3_altdif_txt', 55: 'target3_airstatus_txt', 56: 'target3_applstatus_bitmap',
                    57: 'target3_lon', 58: 'target3_lat', 59: 'target3_vsa_dis', 60: 'target3_vsa_velocity',
                    61: 'target3_itp_dis', 62: 'target3_itp_dis_rate', 63: 'target3_itp_forward',
                    64: 'target3_itp_geometry_status',

                    71: 'target4_bitmap', 72: 'target4_id_txt', 73: 'target4_speed_txt',
                    74: 'target4_altdif_txt', 75: 'target4_airstatus_txt', 76: 'target4_applstatus_bitmap',
                    77: 'target4_lon', 78: 'target4_lat', 79: 'target4_vsa_dis', 80: 'target4_vsa_velocity',
                    81: 'target4_itp_dis', 82: 'target4_itp_dis_rate', 83: 'target4_itp_forward',
                    84: 'target4_itp_geometry_status',

                    91: 'target5_bitmap', 92: 'target5_id_txt', 93: 'target5_speed_txt',
                    94: 'target5_altdif_txt', 95: 'target5_airstatus_txt', 96: 'target5_applstatus_bitmap',
                    97: 'target5_lon', 98: 'target5_lat', 99: 'target5_vsa_dis', 100: 'target5_vsa_velocity',
                    101: 'target5_itp_dis', 102: 'target5_itp_dis_rate', 103: 'target5_itp_forward',
                    104: 'target5_itp_geometry_status',

                    111: 'target6_bitmap', 112: 'target6_id_txt', 113: 'target6_speed_txt',
                    114: 'target6_altdif_txt', 115: 'target6_airstatus_txt', 116: 'target6_applstatus_bitmap',
                    117: 'target6_lon', 118: 'target6_lat', 119: 'target6_vsa_dis', 120: 'target6_vsa_velocity',
                    121: 'target6_itp_dis', 122: 'target6_itp_dis_rate', 123: 'target6_itp_forward',
                    124: 'target6_itp_geometry_status',

                    131: 'target7_bitmap', 132: 'target7_id_txt', 133: 'target7_speed_txt',
                    134: 'target7_altdif_txt', 135: 'target7_airstatus_txt', 136: 'target7_applstatus_bitmap',
                    137: 'target7_lon', 138: 'target7_lat', 139: 'target2_vsa_dis', 140: 'target7_vsa_velocity',
                    141: 'target7_itp_dis', 142: 'target7_itp_dis_rate', 143: 'target7_itp_forward',
                    144: 'target7_itp_geometry_status',

                    151: 'target8_bitmap', 152: 'target8_id_txt', 153: 'target8_speed_txt',
                    154: 'target8_altdif_txt', 155: 'target8_airstatus_txt', 156: 'target8_applstatus_bitmap',
                    157: 'target8_lon', 158: 'target8_lat', 159: 'target8_vsa_dis', 160: 'target8_vsa_velocity',
                    161: 'target8_itp_dis', 162: 'target8_itp_dis_rate', 163: 'target8_itp_forward',
                    164: 'target8_itp_geometry_status',

                    171: 'target9_bitmap', 172: 'target9_id_txt', 173: 'target9_speed_txt',
                    174: 'target9_altdif_txt', 175: 'target9_airstatus_txt', 176: 'target9_applstatus_bitmap',
                    177: 'target9_lon', 178: 'target9_lat', 179: 'target9_vsa_dis', 180: 'target9_vsa_velocity',
                    181: 'target9_itp_dis', 182: 'target9_itp_dis_rate', 183: 'target9_itp_forward',
                    184: 'target9_itp_geometry_status',

                    191: 'target10_bitmap', 192: 'target10_id_txt', 193: 'target10_speed_txt',
                    194: 'target10_altdif_txt', 195: 'target10_airstatus_txt', 196: 'target10_applstatus_bitmap',
                    197: 'target10_lon', 198: 'target10_lat', 199: 'target10_vsa_dis', 200: 'target10_vsa_velocity',
                    201: 'target10_itp_dis', 202: 'target10_itp_dis_rate', 203: 'target10_itp_forward',
                    204: 'target10_itp_geometry_status',

                    211: 'target11_bitmap', 212: 'target11_id_txt', 213: 'target11_speed_txt',
                    214: 'target11_altdif_txt', 215: 'target11_airstatus_txt', 216: 'target11_applstatus_bitmap',
                    217: 'target11_lon', 218: 'target11_lat', 219: 'target11_vsa_dis', 220: 'target11_vsa_velocity',
                    221: 'target11_itp_dis', 222: 'target11_itp_dis_rate', 223: 'target11_itp_forward',
                    224: 'target11_itp_geometry_status',

                    231: 'target12_bitmap', 232: 'target12_id_txt', 233: 'target12_speed_txt',
                    234: 'target12_altdif_txt', 235: 'target12_airstatus_txt', 236: 'target12_applstatus_bitmap',
                    237: 'target12_lon', 238: 'target12_lat', 239: 'target12_vsa_dis', 240: 'target12_vsa_velocity',
                    241: 'target12_itp_dis', 242: 'target12_itp_dis_rate', 243: 'target12_itp_forward',
                    244: 'target12_itp_geometry_status',

                    251: 'target13_bitmap', 252: 'target13_id_txt', 253: 'target13_speed_txt',
                    254: 'target13_altdif_txt', 255: 'target13_airstatus_txt', 256: 'target13_applstatus_bitmap',
                    257: 'target13_lon', 258: 'target13_lat', 259: 'target13_vsa_dis', 260: 'target13_vsa_velocity',
                    261: 'target13_itp_dis', 262: 'target13_itp_dis_rate', 263: 'target13_itp_forward',
                    264: 'target13_itp_geometry_status',

                    271: 'target14_bitmap', 272: 'target14_id_txt', 273: 'target14_speed_txt',
                    274: 'target14_altdif_txt', 275: 'target14_airstatus_txt', 276: 'target14_applstatus_bitmap',
                    277: 'target14_lon', 278: 'target14_lat', 279: 'target14_vsa_dis', 280: 'target14_vsa_velocity',
                    281: 'target14_itp_dis', 282: 'target14_itp_dis_rate', 283: 'target14_itp_forward',
                    284: 'target14_itp_geometry_status',

                    291: 'target15_bitmap', 292: 'target15_id_txt', 293: 'target15_speed_txt',
                    294: 'target15_altdif_txt', 295: 'target15_airstatus_txt', 296: 'target15_applstatus_bitmap',
                    297: 'target15_lon', 298: 'target15_lat', 299: 'target15_vsa_dis', 300: 'target15_vsa_velocity',
                    301: 'target15_itp_dis', 302: 'target15_itp_dis_rate', 303: 'target15_itp_forward',
                    304: 'target15_itp_geometry_status',

                    311: 'target16_bitmap', 312: 'target16_id_txt', 313: 'target16_speed_txt',
                    314: 'target16_altdif_txt', 315: 'target16_airstatus_txt', 316: 'target16_applstatus_bitmap',
                    317: 'target16_lon', 318: 'target16_lat', 319: 'target16_vsa_dis', 320: 'target16_vsa_velocity',
                    321: 'target16_itp_dis', 322: 'target16_itp_dis_rate', 323: 'target16_itp_forward',
                    324: 'target16_itp_geometry_status',

                    331: 'target17_bitmap', 332: 'target17_id_txt', 333: 'target17_speed_txt',
                    334: 'target17_altdif_txt', 335: 'target17_airstatus_txt', 336: 'target17_applstatus_bitmap',
                    337: 'target17_lon', 338: 'target17_lat', 339: 'target17_vsa_dis', 340: 'target17_vsa_velocity',
                    341: 'target17_itp_dis', 342: 'target17_itp_dis_rate', 343: 'target17_itp_forward',
                    344: 'target17_itp_geometry_status',

                    351: 'target18_bitmap', 352: 'target18_id_txt', 353: 'target18_speed_txt',
                    354: 'target18_altdif_txt', 355: 'target18_airstatus_txt', 356: 'target18_applstatus_bitmap',
                    357: 'target18_lon', 358: 'target18_lat', 359: 'target18_vsa_dis', 360: 'target18_vsa_velocity',
                    361: 'target18_itp_dis', 362: 'target18_itp_dis_rate', 363: 'target18_itp_forward',
                    364: 'target18_itp_geometry_status',

                    371: 'target19_bitmap', 372: 'target19_id_txt', 373: 'target19_speed_txt',
                    374: 'target19_altdif_txt', 375: 'target19_airstatus_txt', 376: 'target19_applstatus_bitmap',
                    377: 'target19_lon', 378: 'target19_lat', 379: 'target19_vsa_dis', 380: 'target19_vsa_velocity',
                    381: 'target19_itp_dis', 382: 'target19_itp_dis_rate', 383: 'target19_itp_forward',
                    384: 'target19_itp_geometry_status',

                    391: 'target20_bitmap', 392: 'target20_id_txt', 393: 'target20_speed_txt',
                    394: 'target20_altdif_txt', 395: 'target20_airstatus_txt', 396: 'target20_applstatus_bitmap',
                    397: 'target20_lon', 398: 'target20_lat', 399: 'target20_vsa_dis', 400: 'target20_vsa_velocity',
                    401: 'target20_itp_dis', 402: 'target20_itp_dis_rate', 403: 'target20_itp_forward',
                    404: 'target20_itp_geometry_status',

                    411: 'target21_bitmap', 412: 'target21_id_txt', 413: 'target21_speed_txt',
                    414: 'target21_altdif_txt', 415: 'target21_airstatus_txt', 416: 'target21_applstatus_bitmap',
                    417: 'target21_lon', 418: 'target21_lat', 419: 'target21_vsa_dis', 420: 'target21_vsa_velocity',
                    421: 'target21_itp_dis', 422: 'target21_itp_dis_rate', 423: 'target21_itp_forward',
                    424: 'target21_itp_geometry_status',

                    431: 'target22_bitmap', 432: 'target22_id_txt', 433: 'target22_speed_txt',
                    434: 'target22_altdif_txt', 435: 'target22_airstatus_txt', 436: 'target22_applstatus_bitmap',
                    437: 'target22_lon', 438: 'target22_lat', 439: 'target22_vsa_dis', 440: 'target22_vsa_velocity',
                    441: 'target22_itp_dis', 442: 'target22_itp_dis_rate', 443: 'target22_itp_forward',
                    444: 'target22_itp_geometry_status',

                    451: 'target23_bitmap', 452: 'target23_id_txt', 453: 'target23_speed_txt',
                    454: 'target23_altdif_txt', 455: 'target23_airstatus_txt', 456: 'target23_applstatus_bitmap',
                    457: 'target23_lon', 458: 'target23_lat', 459: 'target23_vsa_dis', 460: 'target23_vsa_velocity',
                    461: 'target23_itp_dis', 462: 'target23_itp_dis_rate', 463: 'target23_itp_forward',
                    464: 'target23_itp_geometry_status',

                    471: 'target24_bitmap', 472: 'target24_id_txt', 473: 'target24_speed_txt',
                    474: 'target24_altdif_txt', 475: 'target24_airstatus_txt', 476: 'target24_applstatus_bitmap',
                    477: 'target24_lon', 478: 'target24_lat', 479: 'target24_vsa_dis', 480: 'target24_vsa_velocity',
                    481: 'target24_itp_dis', 482: 'target24_itp_dis_rate', 483: 'target24_itp_forward',
                    484: 'target24_itp_geometry_status',

                    491: 'target25_bitmap', 492: 'target25_id_txt', 493: 'target25_speed_txt',
                    494: 'target25_altdif_txt', 495: 'target25_airstatus_txt', 496: 'target25_applstatus_bitmap',
                    497: 'target25_lon', 498: 'target25_lat', 499: 'target25_vsa_dis', 500: 'target25_vsa_velocity',
                    501: 'target25_itp_dis', 502: 'target25_itp_dis_rate', 503: 'target25_itp_forward',
                    504: 'target25_itp_geometry_status',

                    511: 'target26_bitmap', 512: 'target26_id_txt', 513: 'target26_speed_txt',
                    514: 'target26_altdif_txt', 515: 'target26_airstatus_txt', 516: 'target26_applstatus_bitmap',
                    517: 'target26_lon', 518: 'target26_lat', 519: 'target26_vsa_dis', 520: 'target26_vsa_velocity',
                    521: 'target26_itp_dis', 522: 'target26_itp_dis_rate', 523: 'target26_itp_forward',
                    524: 'target26_itp_geometry_status',

                    531: 'target27_bitmap', 532: 'target27_id_txt', 533: 'target27_speed_txt',
                    534: 'target27_altdif_txt', 535: 'target27_airstatus_txt', 536: 'target27_applstatus_bitmap',
                    537: 'target27_lon', 538: 'target27_lat', 539: 'target27_vsa_dis', 540: 'target27_vsa_velocity',
                    541: 'target27_itp_dis', 542: 'target27_itp_dis_rate', 543: 'target27_itp_forward',
                    544: 'target27_itp_geometry_status',

                    551: 'target28_bitmap', 552: 'target28_id_txt', 553: 'target28_speed_txt',
                    554: 'target28_altdif_txt', 555: 'target28_airstatus_txt', 556: 'target28_applstatus_bitmap',
                    557: 'target28_lon', 558: 'target28_lat', 559: 'target28_vsa_dis', 560: 'target28_vsa_velocity',
                    561: 'target28_itp_dis', 562: 'target28_itp_dis_rate', 563: 'target28_itp_forward',
                    564: 'target28_itp_geometry_status',

                    571: 'target29_bitmap', 572: 'target29_id_txt', 573: 'target29_speed_txt',
                    574: 'target29_altdif_txt', 575: 'target29_airstatus_txt', 576: 'target29_applstatus_bitmap',
                    577: 'target29_lon', 578: 'target29_lat', 579: 'target29_vsa_dis', 580: 'target29_vsa_velocity',
                    581: 'target29_itp_dis', 582: 'target29_itp_dis_rate', 583: 'target29_itp_forward',
                    584: 'target29_itp_geometry_status',

                    591: 'target30_bitmap', 592: 'target30_id_txt', 593: 'target30_speed_txt',
                    594: 'target30_altdif_txt', 595: 'target30_airstatus_txt', 596: 'target30_applstatus_bitmap',
                    597: 'target30_lon', 598: 'target30_lat', 599: 'target30_vsa_dis', 600: 'target30_vsa_velocity',
                    601: 'target30_itp_dis', 602: 'target30_itp_dis_rate', 603: 'target30_itp_forward',
                    604: 'target30_itp_geometry_status',

                    611: 'target31_bitmap', 612: 'target31_id_txt', 613: 'target31_speed_txt',
                    614: 'target31_altdif_txt', 615: 'target31_airstatus_txt', 616: 'target31_applstatus_bitmap',
                    617: 'target31_lon', 618: 'target31_lat', 619: 'target31_vsa_dis', 620: 'target31_vsa_velocity',
                    621: 'target31_itp_dis', 622: 'target31_itp_dis_rate', 623: 'target31_itp_forward',
                    624: 'target31_itp_geometry_status',

                    631: 'target32_bitmap', 632: 'target32_id_txt', 633: 'target32_speed_txt',
                    634: 'target32_altdif_txt', 635: 'target32_airstatus_txt', 636: 'target32_applstatus_bitmap',
                    637: 'target32_lon', 638: 'target32_lat', 639: 'target32_vsa_dis', 640: 'target32_vsa_velocity',
                    641: 'target32_itp_dis', 642: 'target32_itp_dis_rate', 643: 'target32_itp_forward',
                    644: 'target32_itp_geometry_status',

                    651: 'target33_bitmap', 652: 'target33_id_txt', 653: 'target33_speed_txt',
                    654: 'target33_altdif_txt', 655: 'target33_airstatus_txt', 656: 'target33_applstatus_bitmap',
                    657: 'target33_lon', 658: 'target33_lat', 659: 'target33_vsa_dis', 660: 'target33_vsa_velocity',
                    661: 'target33_itp_dis', 662: 'target33_itp_dis_rate', 663: 'target33_itp_forward',
                    664: 'target33_itp_geometry_status',

                    671: 'target34_bitmap', 672: 'target34_id_txt', 673: 'target34_speed_txt',
                    674: 'target34_altdif_txt', 675: 'target34_airstatus_txt', 676: 'target34_applstatus_bitmap',
                    677: 'target34_lon', 678: 'target34_lat', 679: 'target34_vsa_dis', 680: 'target34_vsa_velocity',
                    681: 'target34_itp_dis', 682: 'target34_itp_dis_rate', 683: 'target34_itp_forward',
                    684: 'target34_itp_geometry_status',

                    691: 'target35_bitmap', 692: 'target35_id_txt', 693: 'target35_speed_txt',
                    694: 'target35_altdif_txt', 695: 'target35_airstatus_txt', 696: 'target35_applstatus_bitmap',
                    697: 'target35_lon', 698: 'target35_lat', 699: 'target35_vsa_dis', 700: 'target35_vsa_velocity',
                    701: 'target35_itp_dis', 702: 'target35_itp_dis_rate', 703: 'target35_itp_forward',
                    704: 'target35_itp_geometry_status',
                    }

    tabWidget_Name = {'0':'airb','1':'surf','2':'vsa','3':'itp'}


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
        self.surf_map_zoom = 9 #surf地图当前等级为9 不能小于7
        self.initUI()

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
        self.ui.btn_close.clicked.connect(self.closeUI)

    def closeUI(self):

        self.myWorker.terminate()
        print("线程终止")
        app =  QApplication.instance()
        app.quit()

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
        # =========================================#
        #surf
        #通用部分开始
        self.ui.horizontalLayoutWidget.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_surf = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_surf.setStyleSheet("padding: 0px; border: 0px;")
        self.ui.graphicsView_surf.setRenderHint(QPainter.Antialiasing)
        self.ui.graphicsView_surf.setCacheMode(QGraphicsView.CacheBackground)
        self.ui.graphicsView_surf.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
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
        self.surf_compass_Item.setPos(0, 45)
        self.surf_ownship_item = self.surf_scene.addPixmap(pixmap_ownship)    #本机图标
        self.surf_ownship_item.setPos(320-15, 320+17.5)
        self.surf_air_heading_txt = QLabel("23.5")
        self.surf_air_heading_txt.setStyleSheet("color:white;background-color:transparent")
        surf_air_heading = self.surf_scene.addWidget(self.surf_air_heading_txt)  # 本机航向角
        surf_air_heading.setPos(315, 20)
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
        self.ui.graphicsView_itp.setScene(self.itp_scene)
        self.ui.graphicsView_itp.setSceneRect(1, 1, 715, 715)
        self.target_air_init_UI()
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

        appl_list = ['airb','vsa','surf']
        for appl_name in appl_list:
            eval("self.ui.tableWidget_" + appl_name + ".setEditTriggers(QTableView.NoEditTriggers)")
            eval("self.ui.tableWidget_" + appl_name + ".horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)")
            eval("self.ui.tableWidget_" + appl_name + ".horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)")
            eval("self.ui.tableWidget_" + appl_name + ".horizontalHeader()").setStyleSheet("QHeaderView::section{"
                                                                  "background-color:black; color:white}")
            eval("self.ui.tableWidget_" + appl_name + ".verticalHeader().setVisible(False)")

    def target_air_init_UI(self):
        pixmap_type1_targetship = QPixmap("pic/air1.png")  # 1号类型目标机图标
        appl_name_list = ['airb','surf','vsa','itp']
        for i in range(1,41):
            for appl_name in appl_name_list:
                # 定义目标机占据的formlayout
                exec("self.formLayout_"+appl_name+"_targetair"+str(i)+" = QFormLayout()")
                eval("self.formLayout_"+appl_name+"_targetair"+str(i) + ".setContentsMargins(0, 0, 0, 0)")
                eval("self.formLayout_"+appl_name+"_targetair"+str(i) + ".setSpacing(1)")
                #目标机ID
                exec("self."+appl_name+"_target" +str(i) + "_id_txt = QLabel()")
                eval("self."+appl_name+"_target" +str(i) + "_id_txt").setStyleSheet("color:white")
                eval("self.formLayout_"+appl_name+"_targetair"+str(i)+".setWidget(0, QFormLayout.LabelRole, self."+appl_name+"_target"+str(i)+"_id_txt)")
                #目标机高度差
                exec("self."+appl_name+"_target" +str(i) + "_altdif_txt = QLabel()")
                eval("self."+appl_name+"_target" +str(i) + "_altdif_txt").setStyleSheet("color:white")
                eval("self.formLayout_"+appl_name+"_targetair"+str(i)+".setWidget(1, QFormLayout.LabelRole, self."+appl_name+"_target"+str(i)+"_altdif_txt)")
                #目标机地空状态
                exec("self."+appl_name+"_target" +str(i) + "_airstatus_txt = QLabel()")
                eval("self."+appl_name+"_target" +str(i) + "_airstatus_txt").setText("AIR")
                eval("self."+appl_name+"_target" +str(i) + "_airstatus_txt").setStyleSheet("color:white")
                eval("self.formLayout_"+appl_name+"_targetair"+str(i)+".setWidget(2, QFormLayout.LabelRole, self."+appl_name+"_target"+str(i)+"_airstatus_txt)")
                #目标机应用状态
                label_appl = QLabel("APPL:")
                label_appl.setStyleSheet("color:white")
                eval("self.formLayout_"+appl_name+"_targetair" + str(i) + ".setWidget(3, QFormLayout.LabelRole, label_appl)")
                exec("self."+appl_name+"_target" + str(i) + "_applstatus_bitmap = QLabel()")
                eval("self."+appl_name+"_target" + str(i) + "_applstatus_bitmap").setPixmap(QPixmap("C:/Users/Administrator/.designer/backup/pic/appstatus1.png"))
                eval("self."+appl_name+"_target" + str(i) + "_applstatus_bitmap").setScaledContents(True)
                eval("self.formLayout_"+appl_name+"_targetair"+str(i)+".setWidget(3, QFormLayout.FieldRole, self."+appl_name+"_target"+str(i)+"_applstatus_bitmap)")

                #sence中的控件初始化
                #目标机图标
                exec("self."+appl_name+"_targetair"+str(i)+"_PixItem = self."+appl_name+"_scene.addPixmap(pixmap_type1_targetship)")
                centerPos = eval("self."+appl_name+"_targetair"+str(i)+"_PixItem.boundingRect().center()")
                eval("self."+appl_name+"_targetair"+str(i)+"_PixItem.setTransformOriginPoint(centerPos)")
                #目标机文本
                exec("self."+appl_name+"_frametxt_targetAir"+str(i)+"=QFrame()")
                eval("self."+appl_name+"_frametxt_targetAir"+str(i)).setStyleSheet("background-color:transparent")
                eval("self."+appl_name+"_frametxt_targetAir"+str(i)+".setLayout(self.formLayout_"+appl_name+"_targetair"+str(i)+")")
                exec("self."+appl_name+"_air"+str(i)+"_text_Item=self."+appl_name+"_scene.addWidget(self."+appl_name+"_frametxt_targetAir"+str(i)+")")
                eval("self."+appl_name+"_air"+str(i)+"_text_Item.setOpacity(0.9)")
                eval("self."+appl_name+"_targetair"+str(i)+"_PixItem.setPos(100, 500)")
                eval("self."+appl_name+"_air" + str(i) + "_text_Item.setPos(100, 520)")
                # 设置item图层位置
                eval("self."+appl_name+"_targetair"+str(i)+"_PixItem.stackBefore(self."+appl_name+"_ownship_item)")
                eval("self."+appl_name+"_air"+str(i)+"_text_Item.stackBefore(self."+appl_name+"_ownship_item)")
                eval("self."+appl_name+"_targetair"+str(i)+"_PixItem.stackBefore(self."+appl_name+"_border_Item)")
                eval("self."+appl_name+"_air"+str(i)+"_text_Item.stackBefore(self."+appl_name+"_border_Item)")
                if appl_name == 'itp':
                    exec("self.frame_itp_target"+str(i)+"=QFrame(self.ui.frame_5)")
                    eval("self.frame_itp_target"+str(i)+".setGeometry(QRect(70, 280, 121, 81))")
                    eval("self.frame_itp_target"+str(i)).setStyleSheet("background-color:transparent")
                    # eval("self.frame_itp_target" + str(i)+".setFrameShape(QFrame.StyledPanel)")
                    # eval("self.frame_itp_target" + str(i) + ".setFrameShadow(QFrame.Raised)")
                    #itp目标机id
                    exec("self.itp_alt_target"+str(i)+"_id=QLabel(self.frame_itp_target"+str(i)+")")
                    eval("self.itp_alt_target"+str(i)+"_id.setGeometry(QRect(40, 30, 64, 15))")
                    eval("self.itp_alt_target" + str(i) + "_id").setStyleSheet("color:white")
                    #目标机itp距离
                    exec("self.itp_alt_target" + str(i) + "_dis=QLabel(self.frame_itp_target" + str(i) + ")")
                    eval("self.itp_alt_target" + str(i) + "_dis.setGeometry(QRect(20, 50, 51, 21))")
                    eval("self.itp_alt_target" + str(i) + "_dis").setStyleSheet("color:white")
                    #目标机itp图标
                    exec("self.itp_bitmap_target" + str(i) + "=QLabel(self.frame_itp_target" + str(i) + ")")
                    eval("self.itp_bitmap_target" + str(i) + ".setGeometry(QRect(40, 10, 31, 16))")
                    eval("self.itp_bitmap_target" + str(i)).setStyleSheet("color:rgb(255, 255, 255)")
                    eval("self.itp_bitmap_target" + str(i)).setPixmap(QPixmap("C:/Users/Administrator/.designer/backup/pic/itp_air1.png"))
                    eval("self.itp_bitmap_target" + str(i)).setScaledContents(True)
                    #目标机itp距离变化率
                    exec("self.itp_alt_target" + str(i) + "_dis_rate=QLabel(self.frame_itp_target" + str(i) + ")")
                    eval("self.itp_alt_target" + str(i) + "_dis_rate.setGeometry(QRect(80, 50, 31, 20))")
                    eval("self.itp_alt_target" + str(i) + "_dis_rate").setStyleSheet("color:white")

            eval("self.frame_itp_target" + str(i) + ".setVisible(False)")
            # 初始化目标机不可见
            eval("self.airb_targetair" + str(i) + "_PixItem.setVisible(False)")
            eval("self.airb_air" + str(i) + "_text_Item.setVisible(False)")
            eval("self.surf_targetair" + str(i) + "_PixItem.setVisible(False)")
            eval("self.surf_air" + str(i) + "_text_Item.setVisible(False)")
            eval("self.vsa_targetair" + str(i) + "_PixItem.setVisible(False)")
            eval("self.vsa_air" + str(i) + "_text_Item.setVisible(False)")
            eval("self.itp_targetair" + str(i) + "_PixItem.setVisible(False)")
            eval("self.itp_air" + str(i) + "_text_Item.setVisible(False)")
        pass

    def map_zoom_in(self):
        # 放大一级视图
        js_string_map_zoom_in = 'map.zoomIn();'
        self.browser.page().runJavaScript(js_string_map_zoom_in)  # 初始化本机位置、标注、航线、移动
        self.surf_map_zoom += 1

    def map_zoom_out(self):
        # 缩小一级视图
        if self.surf_map_zoom >= 8:
            js_string_map_zoom_in = 'map.zoomOut();'
            self.browser.page().runJavaScript(js_string_map_zoom_in)  # 初始化本机位置、标注、航线、移动
            self.surf_map_zoom -= 1

    def update_cdti_ui(self,info):
        '''

        :param info:
        :return:
        '''
        target_id_list = [] # 目标机id序列
        target_dif_speed = [] #目标机地速差序列
        target_vsa_dis = [] #目标机vsa距离序列
        target_vsa_v = []  #目标机vsa速度序列
        target_x_list = []  # 目标机x轴坐标序列
        target_y_list = []  # 目标机y轴坐标序列
        target_lon_list = [] #目标机经度序列
        target_lat_list = []  #目标机纬度序列
        target_pic_surf_type = [] #目标机SURF类型序列
        target_itp_x = []    # itp目标机横坐标序列
        target_itp_x_forward = [] # itp相对本机前后位置
        target_itp_y = []      # itp目标机纵坐标序列
        one_pixel_itp_x = 0.0  # itp一坐标单位代表的距离
        target_alt_dif_list=[]          #目标机高度差
        target_air_ground_status_list=[]#目标机空地状态
        target_surf_app_status_list = []#目标机SURF应用状态
        target_angle_list = []  #目标机旋转角
        ownship_angle = 0 #本机航向角
        compass_step = 0 #罗盘步长 单位海里
        num_target = 0  # 目标机架数

        if info:
           print("接收到UA发送数据，开始解析...")
           current_index = self.ui.tabWidget.currentIndex()
           current_app_name = self.tabWidget_Name[str(current_index)]
           print("current_app_name: "+current_app_name)
           break_flag = 0
           temp = []
           for item in info:
               temp.append(item[0])
           num_target = int(max(temp)/20)
           print(str(num_target)+"架目标机")

           if num_target == 0:#仅绘制本机信息
               if current_app_name == 'airb':
                   for item in info:
                       if item[1] == 46224:  # 设置文本
                           if 'ownship_toa_time' == self.map_wigdetId[item[0]]:
                               self.ui.airb_time_txt.setText(str(round(item[2], 3)))
                           if 'ownship_id_txt' == self.map_wigdetId[item[0]]:  # 本机ID
                               self.ui.airb_ownship_id_txt.setText(str(item[2].decode()))
                           if 'ownship_lon_txt' == self.map_wigdetId[item[0]]:  # 本机经度
                               self.ui.airb_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_lat_txt' == self.map_wigdetId[item[0]]:  # 本机纬度
                               self.ui.airb_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_altrange_txt' == self.map_wigdetId[item[0]]:
                               self.ui.airb_ownship_altrange_txt.setText(str(item[2]) + "ft")
                           if 'ownship_alt_txt' == self.map_wigdetId[item[0]]:
                               self.ui.airb_ownship_alt_txt.setText(str(item[2]))
                           if 'ownship_angle_txt' == self.map_wigdetId[item[0]]:  # 设置本机航向角
                               self.airb_air_heading_txt.setText(str(item[2]))
                           if 'compass_step' == self.map_wigdetId[item[0]]:
                               compass_step = int(item[2])
                               self.ui.airb_compass_step.setText(str(compass_step))
                               self.ui.airb_compass_step1.setText(str(-2 * compass_step))
                               self.ui.airb_compass_step2.setText(str(-1 * compass_step))
                               self.ui.airb_compass_step3.setText(str(1 * compass_step))
                               self.ui.airb_compass_step4.setText(str(2 * compass_step))
                               self.ui.airb_compass_step5.setText(str(-1 * compass_step))
                               self.ui.airb_compass_step6.setText(str(-2 * compass_step))
                       if item[1] == 45808:  # 设置飞机应用状态图片
                           airb_app_status = '{:04b}'.format(item[2])[-1]
                           if 'ownship_applstatus' == self.map_wigdetId[item[0]]:
                               self.ui.airb_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(airb_app_status) + ".png"))
                       if item[1] == 45760:  # 设置旋转角
                           if 'compass_bitmap' == self.map_wigdetId[item[0]]:
                               self.airb_compass_Item.setRotation(360 - int(item[2]))
               if current_app_name == 'surf':
                   for item in info:
                       if item[1] == 46224:  # 设置文本
                           if 'ownship_toa_time' == self.map_wigdetId[item[0]]:
                               self.ui.surf_time_txt.setText(str(round(item[2], 3)))
                           if 'ownship_id_txt' == self.map_wigdetId[item[0]]:  # 本机ID
                               self.ui.surf_ownship_id_txt.setText(str(item[2].decode()))
                           if 'ownship_lon_txt' == self.map_wigdetId[item[0]]:  # 本机经度
                               self.ui.surf_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_lat_txt' == self.map_wigdetId[item[0]]:  # 本机纬度
                               self.ui.surf_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_altrange_txt' == self.map_wigdetId[item[0]]:
                               self.ui.surf_ownship_altrange_txt.setText(str(item[2]) + "ft")
                           if 'ownship_alt_txt' == self.map_wigdetId[item[0]]:
                               self.ui.surf_ownship_alt_txt.setText(str(item[2]))
                           if 'ownship_angle_txt' == self.map_wigdetId[item[0]]:  # 设置本机航向角
                               self.surf_air_heading_txt.setText(str(item[2]))
                           if 'compass_step' == self.map_wigdetId[item[0]]:
                               compass_step = int(item[2])
                               self.ui.surf_compass_step.setText(str(compass_step))
                               self.ui.surf_compass_step1.setText(str(-2 * compass_step))
                               self.ui.surf_compass_step2.setText(str(-1 * compass_step))
                               self.ui.surf_compass_step3.setText(str(1 * compass_step))
                               self.ui.surf_compass_step4.setText(str(2 * compass_step))
                               self.ui.surf_compass_step5.setText(str(-1 * compass_step))
                               self.ui.surf_compass_step6.setText(str(-2 * compass_step))
                       if item[1] == 45808:  # 设置飞机应用状态图片
                           surf_app_status = '{:04b}'.format(item[2])[-2]
                           if 'ownship_applstatus' == self.map_wigdetId[item[0]]:
                               self.ui.surf_ownship_applstatus_bitmap.setPixmap(
                                   QPixmap("pic/appstatus" + str(surf_app_status) + ".png"))
                       if item[1] == 45760:  # 设置旋转角
                           if 'compass_bitmap' == self.map_wigdetId[item[0]]:
                               self.surf_compass_Item.setRotation(360 - int(item[2]))
               if current_app_name == 'vsa':
                   for item in info:
                       if item[1] == 46224:  # 设置文本
                           if 'ownship_toa_time' == self.map_wigdetId[item[0]]:
                               self.ui.vsa_time_txt.setText(str(round(item[2], 3)))
                           if 'ownship_id_txt' == self.map_wigdetId[item[0]]:  # 本机ID
                               self.ui.vsa_ownship_id_txt.setText(str(item[2].decode()))
                           if 'ownship_lon_txt' == self.map_wigdetId[item[0]]:  # 本机经度
                               self.ui.vsa_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_lat_txt' == self.map_wigdetId[item[0]]:  # 本机纬度
                               self.ui.vsa_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_altrange_txt' == self.map_wigdetId[item[0]]:
                               self.ui.vsa_ownship_altrange_txt.setText(str(item[2]) + "ft")
                           if 'ownship_alt_txt' == self.map_wigdetId[item[0]]:
                               self.ui.vsa_ownship_alt_txt.setText(str(item[2]))
                           if 'ownship_angle_txt' == self.map_wigdetId[item[0]]:  # 设置本机航向角
                               self.vsa_air_heading_txt.setText(str(item[2]))
                           if 'compass_step' == self.map_wigdetId[item[0]]:
                               compass_step = int(item[2])
                               self.ui.vsa_compass_step.setText(str(compass_step))
                               self.ui.vsa_compass_step1.setText(str(-2 * compass_step))
                               self.ui.vsa_compass_step2.setText(str(-1 * compass_step))
                               self.ui.vsa_compass_step3.setText(str(1 * compass_step))
                               self.ui.vsa_compass_step4.setText(str(2 * compass_step))
                               self.ui.vsa_compass_step5.setText(str(-1 * compass_step))
                               self.ui.vsa_compass_step6.setText(str(-2 * compass_step))
                       if item[1] == 45808:  # 设置飞机应用状态图片
                           vsa_app_status = '{:04b}'.format(item[2])[-3]
                           if 'ownship_applstatus' == self.map_wigdetId[item[0]]:
                               self.ui.vsa_ownship_applstatus_bitmap.setPixmap(
                                   QPixmap("pic/appstatus" + str(vsa_app_status) + ".png"))
                       if item[1] == 45760:  # 设置旋转角
                           if 'compass_bitmap' == self.map_wigdetId[item[0]]:
                               self.vsa_compass_Item.setRotation(360 - int(item[2]))
               if current_app_name == 'itp':
                   for item in info:
                       if item[1] == 46224:  # 设置文本
                           if 'ownship_toa_time' == self.map_wigdetId[item[0]]:
                               self.ui.itp_time_txt.setText(str(round(item[2], 3)))
                           if 'ownship_id_txt' == self.map_wigdetId[item[0]]:  # 本机ID
                               self.ui.itp_ownship_id_txt.setText(str(item[2].decode()))
                           if 'ownship_lon_txt' == self.map_wigdetId[item[0]]:  # 本机经度
                               self.ui.itp_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_lat_txt' == self.map_wigdetId[item[0]]:  # 本机纬度
                               self.ui.itp_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                           if 'ownship_altrange_txt' == self.map_wigdetId[item[0]]:
                               self.ui.itp_ownship_altrange_txt.setText(str(item[2]) + "ft")
                           if 'ownship_alt_txt' == self.map_wigdetId[item[0]]:
                               self.ui.itp_ownship_alt_txt.setText(str(item[2]))
                           if 'ownship_angle_txt' == self.map_wigdetId[item[0]]:  # 设置本机航向角
                               self.itp_air_heading_txt.setText(str(item[2]))
                           if 'compass_step' == self.map_wigdetId[item[0]]:
                               compass_step = int(item[2])
                               self.ui.itp_compass_step.setText(str(compass_step))
                               self.ui.itp_compass_step1.setText(str(-2 * compass_step))
                               self.ui.itp_compass_step2.setText(str(-1 * compass_step))
                               self.ui.itp_compass_step3.setText(str(1 * compass_step))
                               self.ui.itp_compass_step4.setText(str(2 * compass_step))
                               self.ui.itp_compass_step5.setText(str(-1 * compass_step))
                               self.ui.itp_compass_step6.setText(str(-2 * compass_step))
                       if item[1] == 45808:  # 设置飞机应用状态图片
                           itp_app_status = '{:04b}'.format(item[2])[-4]
                           if 'ownship_applstatus' == self.map_wigdetId[item[0]]:
                               self.ui.itp_ownship_applstatus_bitmap.setPixmap(
                                   QPixmap("pic/appstatus" + str(itp_app_status) + ".png"))
                       if item[1] == 45760:  # 设置旋转角
                           if 'compass_bitmap' == self.map_wigdetId[item[0]]:
                               self.itp_compass_Item.setRotation(360 - int(item[2]))
           if num_target >= 1: #存在目标机
               if current_app_name == 'airb':
                   #初始化airb页面
                   self.ui.tableWidget_airb.setRowCount(0)
                   self.ui.tableWidget_airb.clearContents()
                   self.ui.tableWidget_airb.setRowCount(num_target)
                   for j in range(1, 41):
                       # 罗盘飞机图标和飞机文本 隐藏
                       eval("self.airb_targetair" + str(j) + "_PixItem.setVisible(False)")
                       eval("self.airb_air" + str(j) + "_text_Item.setVisible(False)")
                   for i in range(1, num_target + 1):
                       # 罗盘飞机图标和飞机文本 显示
                       eval("self.airb_targetair" + str(i) + "_PixItem.setVisible(True)")
                       eval("self.airb_air" + str(i) + "_text_Item.setVisible(True)")
                   for item in info:
                       break_flag += 1
                       try:
                           if break_flag > 1 and item[0] == 0:
                               break
                           if item[1] == 46224:  # 设置文本
                               if 'ownship_toa_time' == self.map_wigdetId[item[0]]:
                                   self.ui.airb_time_txt.setText(str(round(item[2], 3)))
                               if 'ownship_id_txt' == self.map_wigdetId[item[0]]:  # 本机ID
                                   self.ui.airb_ownship_id_txt.setText(str(item[2].decode()))
                               if 'ownship_lon_txt' == self.map_wigdetId[item[0]]:  # 本机经度
                                   self.ui.airb_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                               if 'ownship_lat_txt' == self.map_wigdetId[item[0]]:  # 本机纬度
                                   self.ui.airb_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                               if 'ownship_altrange_txt' == self.map_wigdetId[item[0]]:
                                   self.ui.airb_ownship_altrange_txt.setText(str(item[2]) + "ft")
                               if 'ownship_alt_txt' == self.map_wigdetId[item[0]]:
                                   self.ui.airb_ownship_alt_txt.setText(str(item[2]))
                               if 'ownship_angle_txt' == self.map_wigdetId[item[0]]:  # 设置本机航向角
                                   self.airb_air_heading_txt.setText(str(item[2]))
                               if 'compass_step' == self.map_wigdetId[item[0]]:
                                   compass_step = int(item[2])
                                   self.ui.airb_compass_step1.setText(str(-2 * compass_step))
                                   self.ui.airb_compass_step2.setText(str(-1 * compass_step))
                                   self.ui.airb_compass_step3.setText(str(1 * compass_step))
                                   self.ui.airb_compass_step4.setText(str(2 * compass_step))
                                   self.ui.airb_compass_step5.setText(str(-1 * compass_step))
                                   self.ui.airb_compass_step6.setText(str(-2 * compass_step))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_lon'") == self.map_wigdetId[item[0]]:  # 目标机经纬度
                                       target_lon_list.append(item[2])
                                   if eval("'target" + str(i) + "_lat'") == self.map_wigdetId[item[0]]:  # 目标机经纬度
                                       target_lat_list.append(item[2])
                                   if eval("'target" + str(i) + "_id_txt'") == self.map_wigdetId[item[0]]:  # 设置目标机id
                                       target_id_list.append(str(item[2].decode()))
                                       eval("self.airb_target" + str(i) + "_id_txt").setText(str(item[2].decode()))
                                   if eval("'target" + str(i) + "_altdif_txt'") == self.map_wigdetId[item[0]]:  # 目标机高度差
                                       target_alt_dif_list.append(item[2])
                                       if item[2] > 0:
                                           eval("self.airb_target" + str(i) + "_altdif_txt").setText("+" + str(item[2]))
                                       else:
                                           eval("self.airb_target" + str(i) + "_altdif_txt").setText(str(item[2]))
                                   if eval("'target" + str(i) + "_airstatus_txt'") == self.map_wigdetId[item[0]]:  # 目标机空地状态
                                       if item[2] == 2:  # GROUND
                                           eval("self.airb_target" + str(i) + "_airstatus_txt").setText("GROUND")
                                   if eval("'target" + str(i) + "_speed_txt'") == self.map_wigdetId[item[0]]:  # 目标机地速差
                                       temp = str(round(item[2], 6))
                                       if temp == '-10000.0':
                                           temp = '0'
                                       target_dif_speed.append(temp)
                           if item[1] == 45808:  # 设置飞机应用状态图片
                               airb_app_status = '{:04b}'.format(item[2])[-1]
                               if 'ownship_applstatus' == self.map_wigdetId[item[0]]:
                                   self.ui.airb_ownship_applstatus_bitmap.setPixmap(
                                       QPixmap("pic/appstatus" + str(airb_app_status) + ".png"))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_applstatus_bitmap'") == self.map_wigdetId[item[0]]:
                                       eval("self.airb_target" + str(i) + "_applstatus_bitmap").setPixmap(
                                           QPixmap("pic/appstatus" + str(airb_app_status) + ".png"))
                           if item[1] == 46272:  # 设置目标机图标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       airb_value = item[2] & int('0xf', 16)
                                       pixmap_airb_targetship = QPixmap("pic/air" + str(airb_value) + ".png")  # 1号类型目标机图标
                                       eval("self.airb_targetair" + str(i) + "_PixItem.setPixmap(pixmap_airb_targetship)")
                           if item[1] == 45760:  # 设置旋转角
                               if 'compass_bitmap' == self.map_wigdetId[item[0]]:
                                   ownship_angle = item[2]
                                   self.airb_compass_Item.setRotation(360 - int(item[2]))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_angle_list.append(item[2])
                                       eval("self.airb_targetair" + str(i) + "_PixItem").setRotation(int(item[2]))
                           if item[1] == 45824:  # 设置目标机X轴坐标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_x_list.append(int(item[2]))
                           if item[1] == 45840:  # 设置目标机Y轴坐标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_y_list.append(int(item[2]))
                       except:
                           import traceback
                           traceback.print_exc()
                           print("更新AIRB界面有错误，请检查~")
                           continue
                   temp_list_A = []
                   for i in range(len(target_id_list)):
                       temp_list_A.append([target_id_list[i], target_dif_speed[i]])
                   for i in range(len(temp_list_A)):
                       item = temp_list_A[i]
                       for j in range(len(item)):
                           item_airb = QTableWidgetItem(str(temp_list_A[i][j]))
                           item_airb.setForeground(QBrush(QColor(255, 255, 255)))
                           item_airb.setBackground(QBrush(QColor(0, 0, 0)))
                           item_airb.setTextAlignment(Qt.AlignCenter)
                           self.ui.tableWidget_airb.setItem(i, j, item_airb)
                   for i in range(0, num_target):
                       # 绘制罗盘中目标机图标和文本位置
                       eval('self.airb_targetair' + str(i + 1) + '_PixItem.setPos(target_x_list[i], target_y_list[i])')
                       eval('self.airb_air' + str(i + 1) + '_text_Item.setPos(target_x_list[i], target_y_list[i]+20)')
               if current_app_name == 'surf':
                   #初始化surf页面
                   self.browser.page().runJavaScript("remove_overlay();")  # 移除surf机场绘制的飞机图标
                   self.ui.tableWidget_surf.setRowCount(0)
                   self.ui.tableWidget_surf.clearContents()
                   self.ui.tableWidget_surf.setRowCount(num_target)
                   for item in info:
                       break_flag += 1
                       try:
                           if break_flag > 1 and item[0] == 0:
                               break
                           if item[1] == 46224:  # 设置文本
                               if 'ownship_toa_time' == self.map_wigdetId[item[0]]:
                                   self.ui.surf_time_txt.setText(str(round(item[2], 3)))
                               if 'ownship_id_txt' == self.map_wigdetId[item[0]]:  # 本机ID
                                   self.ui.surf_ownship_id_txt.setText(str(item[2].decode()))
                               if 'ownship_lon_txt' == self.map_wigdetId[item[0]]:  # 本机经度
                                   self.ui.surf_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                               if 'ownship_lat_txt' == self.map_wigdetId[item[0]]:  # 本机纬度
                                   self.ui.surf_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                               if 'ownship_altrange_txt' == self.map_wigdetId[item[0]]:
                                   self.ui.surf_ownship_altrange_txt.setText(str(item[2]) + "ft")
                               if 'ownship_alt_txt' == self.map_wigdetId[item[0]]:
                                   self.ui.surf_ownship_alt_txt.setText(str(item[2]))
                               if 'ownship_angle_txt' == self.map_wigdetId[item[0]]:  # 设置本机航向角
                                   self.surf_air_heading_txt.setText(str(item[2]))
                               if 'compass_step' == self.map_wigdetId[item[0]]:
                                   compass_step = int(item[2])
                                   self.ui.surf_compass_step1.setText(str(-2 * compass_step))
                                   self.ui.surf_compass_step2.setText(str(-1 * compass_step))
                                   self.ui.surf_compass_step3.setText(str(1 * compass_step))
                                   self.ui.surf_compass_step4.setText(str(2 * compass_step))
                                   self.ui.surf_compass_step5.setText(str(-1 * compass_step))
                                   self.ui.surf_compass_step6.setText(str(-2 * compass_step))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_lon'") == self.map_wigdetId[item[0]]:  # 目标机经纬度
                                       target_lon_list.append(item[2])
                                   if eval("'target" + str(i) + "_lat'") == self.map_wigdetId[item[0]]:  # 目标机经纬度
                                       target_lat_list.append(item[2])
                                   if eval("'target" + str(i) + "_id_txt'") == self.map_wigdetId[item[0]]:  # 设置目标机id
                                       target_id_list.append(str(item[2].decode()))
                                       eval("self.surf_target" + str(i) + "_id_txt").setText(str(item[2].decode()))
                                   if eval("'target" + str(i) + "_altdif_txt'") == self.map_wigdetId[item[0]]:  # 目标机高度差
                                       target_alt_dif_list.append(item[2])
                                       if item[2] > 0:
                                           eval("self.surf_target" + str(i) + "_altdif_txt").setText("+" + str(item[2]))
                                       else:
                                           eval("self.surf_target" + str(i) + "_altdif_txt").setText(str(item[2]))
                                   if eval("'target" + str(i) + "_airstatus_txt'") == self.map_wigdetId[item[0]]:  # 目标机空地状态
                                       if item[2] == 1:  # AIR
                                           target_air_ground_status_list.append("AIR")
                                       elif item[2] == 2:  # GROUND
                                           target_air_ground_status_list.append("GROUND")
                                           eval("self.surf_target" + str(i) + "_airstatus_txt").setText("GROUND")
                                   if eval("'target" + str(i) + "_speed_txt'") == self.map_wigdetId[item[0]]:  # 目标机地速差
                                       temp = str(round(item[2], 6))
                                       if temp == '-10000.0':
                                           temp = '0'
                                       target_dif_speed.append(temp)
                           if item[1] == 45808:  # 设置飞机应用状态图片
                               surf_app_status = '{:04b}'.format(item[2])[-2]
                               if 'ownship_applstatus' == self.map_wigdetId[item[0]]:
                                   self.ui.surf_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(surf_app_status) + ".png"))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_applstatus_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_surf_app_status_list.append(surf_app_status)
                                       eval("self.surf_target" + str(i) + "_applstatus_bitmap").setPixmap(QPixmap("pic/appstatus" + str(surf_app_status) + ".png"))
                           if item[1] == 46272:  # 设置目标机图标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       surf_value = (item[2] >> 4) & int('0xf', 16)
                                       pixmap_surf_targetship = QPixmap("pic/air" + str(surf_value) + ".png")  # 1号类型目标机图标
                                       eval("self.surf_targetair" + str(i) + "_PixItem.setPixmap(pixmap_surf_targetship)")
                                       target_pic_surf_type.append(surf_value)
                           if item[1] == 45760:  # 设置旋转角
                               if 'compass_bitmap' == self.map_wigdetId[item[0]]:
                                   ownship_angle = item[2]
                                   self.surf_compass_Item.setRotation(360 - int(item[2]))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_angle_list.append(item[2])
                                       eval("self.surf_targetair" + str(i) + "_PixItem").setRotation(int(item[2]))
                           if item[1] == 45824:  # 设置目标机X轴坐标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_x_list.append(int(item[2]))
                           if item[1] == 45840:  # 设置目标机Y轴坐标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_y_list.append(int(item[2]))
                       except:
                           import traceback
                           traceback.print_exc()
                           print("更新AIRB界面有错误，请检查~")
                           continue
                   temp_list_A = []
                   for i in range(len(target_id_list)):
                       temp_list_A.append([target_id_list[i], target_dif_speed[i]])
                   for i in range(len(temp_list_A)):
                       item = temp_list_A[i]
                       for j in range(len(item)):
                           item_surf = QTableWidgetItem(str(temp_list_A[i][j]))
                           item_surf.setForeground(QBrush(QColor(255, 255, 255)))
                           item_surf.setBackground(QBrush(QColor(0, 0, 0)))
                           item_surf.setTextAlignment(Qt.AlignCenter)
                           self.ui.tableWidget_surf.setItem(i, j, item_surf)
                   # 绘制surf区域
                   # step1: 移动地图,将地图中心点变更为本机坐标点
                   own_lon = round(float(self.ui.surf_ownship_lon_txt.text()), 6)
                   own_lat = round(float(self.ui.surf_ownship_lat_txt.text()), 6)
                   js_string_move_map = '''move_map(%f,%f);''' % (own_lon, own_lat)
                   self.browser.page().runJavaScript(js_string_move_map)  # 初始化本机位置、标注、航线、移动
                   # step2: 地图角度旋转 按照本机航向旋转
                   ownship_angle = float(self.surf_air_heading_txt.text())
                   self.map_widgetItem.setRotation(-ownship_angle)
                   for i in range(0, num_target):
                       if target_pic_surf_type and target_lon_list and target_lat_list:
                           if target_lon_list[i] == 0.0 and target_lat_list[i] == 0.0:  # 仅tcas surf无法显示目标机
                               pass
                               # angle_temp = 0.0  # 方位角
                               # dis_temp = 0.0  # 相对距离 km
                               # dx = abs(target_x_list[i] - 305)
                               # dy = abs(target_y_list[i] - 337.5)
                               # dxy = sqrt(dx ** 2 + dy ** 2)
                               # angle_temp = atan(dx / dy) * 180 / pi
                               # dis_temp = compass_step * 1.852 * dxy / 800
                               # own_lon = float(self.ui.surf_ownship_lon_txt.text())
                               # own_lat = float(self.ui.surf_ownship_lat_txt.text())
                               # ga = Geography_Analysis()
                               # target_lon, target_lat = ga.get_lngAndlat(own_lon, own_lat, angle_temp, dis_temp)
                               # js_string1 = '''update_target_pic(%d,%d,%f,%f,%d);''' % (
                               #     i + 1, target_pic_surf_type[i], target_lon, target_lat,
                               #     ownship_angle + target_angle_list[i])
                               # self.browser.page().runJavaScript(js_string1)  # 更新目标机目标
                               # if target_alt_dif_list and target_air_ground_status_list and target_surf_app_status_list:
                               #     js_string2 = '''update_target_info(%d,'%s','%s','%s',%d,%f,%f,%d);''' % (
                               #     i + 1, target_id_list[i], str(target_alt_dif_list[i]),
                               #     target_air_ground_status_list[i], int(target_surf_app_status_list[i]),
                               #     target_lon, target_lat, ownship_angle)
                               #     self.browser.page().runJavaScript(js_string2)  # 更新目标机航班号...
                           else:  # 正常情况
                               js_string1 = '''update_target_pic(%d,%d,%f,%f,%d);''' % (
                               i + 1, target_pic_surf_type[i], target_lon_list[i], target_lat_list[i],
                               ownship_angle + target_angle_list[i])
                               self.browser.page().runJavaScript(js_string1)  # 更新目标机目标
                               if target_alt_dif_list and target_air_ground_status_list and target_surf_app_status_list:
                                   js_string2 = '''update_target_info(%d,'%s','%s','%s',%d,%f,%f,%d);''' % (
                                   i + 1, target_id_list[i], str(target_alt_dif_list[i]),
                                   target_air_ground_status_list[i], int(target_surf_app_status_list[i]),
                                   target_lon_list[i], target_lat_list[i], ownship_angle)
                                   self.browser.page().runJavaScript(js_string2)  # 更新目标机航班号、空地状态、应用状态
               if current_app_name == 'vsa':
                   # 初始化vsa页面
                   self.ui.tableWidget_vsa.setRowCount(0)
                   self.ui.tableWidget_vsa.clearContents()
                   self.ui.tableWidget_vsa.setRowCount(num_target)
                   for j in range(1, 41):
                       # 罗盘飞机图标和飞机文本 隐藏
                       eval("self.vsa_targetair" + str(j) + "_PixItem.setVisible(False)")
                       eval("self.vsa_air" + str(j) + "_text_Item.setVisible(False)")
                   for i in range(1, num_target + 1):
                       # 罗盘飞机图标和飞机文本 显示
                       eval("self.vsa_targetair" + str(i) + "_PixItem.setVisible(True)")
                       eval("self.vsa_air" + str(i) + "_text_Item.setVisible(True)")
                   for item in info:
                       break_flag += 1
                       try:
                           if break_flag > 1 and item[0] == 0:
                               break
                           if item[1] == 46224:  # 设置文本
                               if 'ownship_toa_time' == self.map_wigdetId[item[0]]:
                                   self.ui.vsa_time_txt.setText(str(round(item[2], 3)))
                               if 'ownship_id_txt' == self.map_wigdetId[item[0]]:  # 本机ID
                                   self.ui.vsa_ownship_id_txt.setText(str(item[2].decode()))
                               if 'ownship_lon_txt' == self.map_wigdetId[item[0]]:  # 本机经度
                                   self.ui.vsa_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                               if 'ownship_lat_txt' == self.map_wigdetId[item[0]]:  # 本机纬度
                                   self.ui.vsa_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                               if 'ownship_altrange_txt' == self.map_wigdetId[item[0]]:
                                   self.ui.vsa_ownship_altrange_txt.setText(str(item[2]) + "ft")
                               if 'ownship_alt_txt' == self.map_wigdetId[item[0]]:
                                   self.ui.vsa_ownship_alt_txt.setText(str(item[2]))
                               if 'ownship_angle_txt' == self.map_wigdetId[item[0]]:  # 设置本机航向角
                                   self.vsa_air_heading_txt.setText(str(item[2]))
                               if 'compass_step' == self.map_wigdetId[item[0]]:
                                   compass_step = int(item[2])
                                   self.ui.vsa_compass_step1.setText(str(-2 * compass_step))
                                   self.ui.vsa_compass_step2.setText(str(-1 * compass_step))
                                   self.ui.vsa_compass_step3.setText(str(1 * compass_step))
                                   self.ui.vsa_compass_step4.setText(str(2 * compass_step))
                                   self.ui.vsa_compass_step5.setText(str(-1 * compass_step))
                                   self.ui.vsa_compass_step6.setText(str(-2 * compass_step))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_lon'") == self.map_wigdetId[item[0]]:  # 目标机经纬度
                                       target_lon_list.append(item[2])
                                   if eval("'target" + str(i) + "_lat'") == self.map_wigdetId[item[0]]:  # 目标机经纬度
                                       target_lat_list.append(item[2])
                                   if eval("'target" + str(i) + "_id_txt'") == self.map_wigdetId[item[0]]:  # 设置目标机id
                                       target_id_list.append(str(item[2].decode()))
                                       eval("self.vsa_target" + str(i) + "_id_txt").setText(str(item[2].decode()))
                                   if eval("'target" + str(i) + "_altdif_txt'") == self.map_wigdetId[item[0]]:  # 目标机高度差
                                       target_alt_dif_list.append(item[2])
                                       if item[2] > 0:
                                           eval("self.vsa_target" + str(i) + "_altdif_txt").setText("+" + str(item[2]))
                                       else:
                                           eval("self.vsa_target" + str(i) + "_altdif_txt").setText(str(item[2]))
                                   if eval("'target" + str(i) + "_airstatus_txt'") == self.map_wigdetId[item[0]]:  # 目标机空地状态
                                       if item[2] == 2:  # GROUND
                                           eval("self.vsa_target" + str(i) + "_airstatus_txt").setText("GROUND")
                                   if eval("'target" + str(i) + "_speed_txt'") == self.map_wigdetId[item[0]]:  # 目标机地速差
                                       temp = str(round(item[2], 6))
                                       if temp == '-10000.0':
                                           temp = '0'
                                       target_dif_speed.append(temp)
                                   if eval("'target" + str(i) + "_vsa_dis'") == self.map_wigdetId[item[0]]:  # VSA距离
                                       target_vsa_dis.append(str(round(item[2], 3)))
                                   if eval("'target" + str(i) + "_vsa_velocity'") == self.map_wigdetId[item[0]]:  # VSA速度
                                       target_vsa_v.append(str(round(item[2], 3)) + " " + str(round(item[2], 4)))
                           if item[1] == 45808:  # 设置飞机应用状态图片
                               vsa_app_status = '{:04b}'.format(item[2])[-3]
                               if 'ownship_applstatus' == self.map_wigdetId[item[0]]:
                                   self.ui.vsa_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(vsa_app_status) + ".png"))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_applstatus_bitmap'") == self.map_wigdetId[item[0]]:
                                       eval("self.vsa_target" + str(i) + "_applstatus_bitmap").setPixmap(QPixmap("pic/appstatus" + str(vsa_app_status) + ".png"))
                           if item[1] == 46272:  # 设置目标机图标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       vsa_value = (item[2] >> 8) & int('0xf', 16)
                                       pixmap_vsa_targetship = QPixmap("pic/air" + str(vsa_value) + ".png")  # 1号类型目标机图标
                                       eval("self.vsa_targetair" + str(i) + "_PixItem.setPixmap(pixmap_vsa_targetship)")
                           if item[1] == 45760:  # 设置旋转角
                               if 'compass_bitmap' == self.map_wigdetId[item[0]]:
                                   self.vsa_compass_Item.setRotation(360 - int(item[2]))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_angle_list.append(item[2])
                                       eval("self.vsa_targetair" + str(i) + "_PixItem").setRotation(int(item[2]))
                           if item[1] == 45824:  # 设置目标机X轴坐标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_x_list.append(int(item[2]))
                           if item[1] == 45840:  # 设置目标机Y轴坐标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_y_list.append(int(item[2]))
                       except:
                           import traceback
                           traceback.print_exc()
                           print("更新VSA界面有错误，请检查~")
                           continue
                   temp_list_B = []
                   for j in range(len(target_id_list)):
                       temp_list_B.append([target_id_list[j], target_dif_speed[j], target_vsa_dis[j], target_vsa_v[j]])
                   for i in range(len(temp_list_B)):
                       item = temp_list_B[i]
                       for j in range(len(item)):
                           item = QTableWidgetItem(str(temp_list_B[i][j]))
                           item.setForeground(QBrush(QColor(255, 255, 255)))
                           item.setBackground(QBrush(QColor(0, 0, 0)))
                           item.setTextAlignment(Qt.AlignCenter)
                           self.ui.tableWidget_vsa.setItem(i, j, item)
                   for i in range(0, num_target):
                       # 绘制罗盘中目标机图标和文本位置
                       eval('self.vsa_targetair' + str(i + 1) + '_PixItem.setPos(target_x_list[i], target_y_list[i])')
                       eval('self.vsa_air' + str(i + 1) + '_text_Item.setPos(target_x_list[i], target_y_list[i]+20)')
               if current_app_name == 'itp':
                   #初始化itp页面
                   for j in range(1, 41):
                       # 罗盘飞机图标和飞机文本 隐藏
                       eval("self.itp_targetair" + str(j) + "_PixItem.setVisible(False)")
                       eval("self.itp_air" + str(j) + "_text_Item.setVisible(False)")
                       # Itp区域 隐藏
                       eval("self.frame_itp_target" + str(j) + ".setVisible(False)")
                   for i in range(1, num_target + 1):
                       # 罗盘飞机图标和飞机文本 显示
                       eval("self.itp_targetair" + str(i) + "_PixItem.setVisible(True)")
                       eval("self.itp_air" + str(i) + "_text_Item.setVisible(True)")
                       # Itp区域 显示
                       eval("self.frame_itp_target" + str(i) + ".setVisible(True)")
                   for item in info:
                       break_flag += 1
                       try:
                           if break_flag > 1 and item[0] == 0:
                               break
                           if item[1] == 46224:  # 设置文本
                               if 'ownship_toa_time' == self.map_wigdetId[item[0]]:
                                   self.ui.itp_time_txt.setText(str(round(item[2], 3)))
                               if 'ownship_id_txt' == self.map_wigdetId[item[0]]:  # 本机ID
                                   self.ui.itp_ownship_id_txt.setText(str(item[2].decode()))
                               if 'ownship_lon_txt' == self.map_wigdetId[item[0]]:  # 本机经度
                                   self.ui.itp_ownship_lon_txt.setText(str(round(float(item[2]), 6)))
                               if 'ownship_lat_txt' == self.map_wigdetId[item[0]]:  # 本机纬度
                                   self.ui.itp_ownship_lat_txt.setText(str(round(float(item[2]), 6)))
                               if 'ownship_altrange_txt' == self.map_wigdetId[item[0]]:
                                   self.ui.itp_ownship_altrange_txt.setText(str(item[2]) + "ft")
                               if 'ownship_alt_txt' == self.map_wigdetId[item[0]]:
                                   self.ui.itp_ownship_alt_txt.setText(str(item[2]))
                               if 'ownship_angle_txt' == self.map_wigdetId[item[0]]:  # 设置本机航向角
                                   self.itp_air_heading_txt.setText(str(item[2]))
                               if 'compass_step' == self.map_wigdetId[item[0]]:
                                   compass_step = int(item[2])
                                   one_pixel_itp_x = float(compass_step / 115)
                                   self.ui.itp_compass_step1.setText(str(-2 * compass_step))
                                   self.ui.itp_compass_step2.setText(str(-1 * compass_step))
                                   self.ui.itp_compass_step3.setText(str(1 * compass_step))
                                   self.ui.itp_compass_step4.setText(str(2 * compass_step))
                                   self.ui.itp_compass_step5.setText(str(-1 * compass_step))
                                   self.ui.itp_compass_step6.setText(str(-2 * compass_step))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_lon'") == self.map_wigdetId[item[0]]:  # 目标机经纬度
                                       target_lon_list.append(item[2])
                                   if eval("'target" + str(i) + "_lat'") == self.map_wigdetId[item[0]]:  # 目标机经纬度
                                       target_lat_list.append(item[2])
                                   if eval("'target" + str(i) + "_id_txt'") == self.map_wigdetId[item[0]]:  # 设置目标机id
                                       target_id_list.append(str(item[2].decode()))
                                       eval("self.itp_target" + str(i) + "_id_txt").setText(str(item[2].decode()))
                                       eval("self.itp_alt_target" + str(i) + "_id").setText(str(item[2].decode()))
                                   if eval("'target" + str(i) + "_altdif_txt'") == self.map_wigdetId[item[0]]:  # 目标机高度差
                                       current_alt = int(self.ui.itp_ownship_alt_txt.text()) + item[2] * 100
                                       print("alt_dif"+str(item[2]))
                                       target_itp_y.append(int(current_alt / 100))
                                       target_alt_dif_list.append(item[2])
                                       if item[2] > 0:
                                           eval("self.itp_target" + str(i) + "_altdif_txt").setText("+" + str(item[2]))
                                       else:
                                           eval("self.itp_target" + str(i) + "_altdif_txt").setText(str(item[2]))
                                   if eval("'target" + str(i) + "_airstatus_txt'") == self.map_wigdetId[item[0]]:  # 目标机空地状态
                                       if item[2] == 2:  # GROUND
                                           eval("self.airb_target" + str(i) + "_airstatus_txt").setText("GROUND")
                                   if eval("'target" + str(i) + "_speed_txt'") == self.map_wigdetId[item[0]]:  # 目标机地速差
                                       target_dif_speed.append(str(round(item[2], 6)))
                                   if eval("'target" + str(i) + "_itp_dis'") == self.map_wigdetId[item[0]]:  # ITP距离
                                       eval("self.itp_alt_target" + str(i) + "_dis").setText(str(round(item[2], 1)) + "NM")
                                       target_itp_x.append(round(item[2], 1))
                                   if eval("'target" + str(i) + "_itp_dis_rate'") == self.map_wigdetId[item[0]]:  # ITP距离变化率
                                       eval("self.itp_alt_target" + str(i) + "_dis_rate").setText(str(int(item[2])) + "KT")
                                       target_itp_x.append(round(item[2], 1))
                                   if eval("'target" + str(i) + "_itp_geometry_status'") == self.map_wigdetId[item[0]]:  # itp有效
                                       if item[2] == 1:  # ITP有效
                                           eval("self.ui.itp_bitmap_target" + str(i)).setPixmap(QPixmap("pic/itp_air2.png"))
                                           eval("self.ui.itp_alt_target" + str(i) + "_id").setStyleSheet("color:rgb(0, 255, 255)")
                                           eval("self.ui.itp_alt_target" + str(i) + "_dis").setStyleSheet("color:rgb(0, 255, 255)")
                                           eval("self.ui.itp_alt_target" + str(i) + "_dis_rate").setStyleSheet("color:rgb(0, 255, 255)")
                                       else:
                                           eval("self.itp_bitmap_target" + str(i)).setPixmap(QPixmap("pic/itp_air1.png"))
                                   if eval("'target" + str(i) + "_itp_forward'") == self.map_wigdetId[item[0]]:  # 1相对本机前 2相对本机后
                                       target_itp_x_forward.append(item[2])
                           if item[1] == 45808:  # 设置飞机应用状态图片
                               itp_app_status = '{:04b}'.format(item[2])[-4]
                               if 'ownship_applstatus' == self.map_wigdetId[item[0]]:
                                   self.ui.itp_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(itp_app_status) + ".png"))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_applstatus_bitmap'") == self.map_wigdetId[item[0]]:
                                       eval("self.itp_target" + str(i) + "_applstatus_bitmap").setPixmap(QPixmap("pic/appstatus" + str(itp_app_status) + ".png"))
                           if item[1] == 46272:  # 设置目标机图标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       itp_value = (item[2] >> 12) & int('0xf', 16)
                                       pixmap_itp_targetship = QPixmap("pic/air" + str(itp_value) + ".png")  # 1号类型目标机图标
                                       eval("self.itp_targetair" + str(i) + "_PixItem.setPixmap(pixmap_itp_targetship)")
                           if item[1] == 45760:  # 设置旋转角
                               if 'compass_bitmap' == self.map_wigdetId[item[0]]:
                                   ownship_angle = item[2]
                                   self.itp_compass_Item.setRotation(360 - int(item[2]))
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_angle_list.append(item[2])
                                       eval("self.itp_targetair" + str(i) + "_PixItem").setRotation(int(item[2]))
                           if item[1] == 45824:  # 设置目标机X轴坐标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_x_list.append(int(item[2]))
                           if item[1] == 45840:  # 设置目标机Y轴坐标
                               for i in range(1, num_target + 1):
                                   if eval("'target" + str(i) + "_bitmap'") == self.map_wigdetId[item[0]]:
                                       target_y_list.append(int(item[2]))
                       except:
                           import traceback
                           traceback.print_exc()
                           print("更新AIRB界面有错误，请检查~")
                           continue
                   one_pixel_itp_y = 1 / 7
                   own_alt = int(int(self.ui.itp_ownship_alt_txt.text()) / 100)
                   print("target_itp_y:"+str(target_itp_y))
                   for i in range(0, num_target):
                       # 绘制罗盘中目标机图标和文本位置
                       eval('self.itp_targetair' + str(i + 1) + '_PixItem.setPos(target_x_list[i], target_y_list[i])')
                       eval('self.itp_air' + str(i + 1) + '_text_Item.setPos(target_x_list[i], target_y_list[i]+20)')
                       # 绘制Itp区域
                       if target_itp_x_forward[i] == 1:  # 相对本机前
                           eval("self.frame_itp_target" + str(i + 1) + ".setGeometry(QRect(275 + int( target_itp_x[i]/one_pixel_itp_x), 380 - int((target_itp_y[i]- own_alt) / one_pixel_itp_y),121, 81))")
                       else:  # 相对本机后
                           eval("self.frame_itp_target" + str(i + 1) + ".setGeometry(QRect(275 - int( target_itp_x[i]/one_pixel_itp_x), 380 - int((target_itp_y[i] - own_alt) / one_pixel_itp_y),121, 81))")


    def send_data1_to_ua(self):
        try:
            self.pack_CDTI_TO_UA_DATA(self.cdti_to_ua_in_data,0)
            buf = bytes(168)
            buf = self.cdti_to_ua_in_data.encode()
            socket_661 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
            socket_661.sendto(buf, self.ip_port_toUA)
        except:
            print("发送数据出错")

    def send_data2_to_ua(self):
        try:
            self.pack_CDTI_TO_UA_DATA(self.cdti_to_ua_out_data,1)
            buf = bytes(168)
            buf = self.cdti_to_ua_out_data.encode()
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