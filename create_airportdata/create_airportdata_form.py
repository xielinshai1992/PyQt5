import sys
import os
import datetime
import traceback
from ctypes import *
import threading
import yaml
import time
import socket
import logging
import adsb_mainForm
from math import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from math import radians, cos, sin, asin, sqrt
from geography_analysis import Geography_Analysis
from c_api import Ownship_Data_Struct,ADSB_Data_Struct,TCAS_Data_Struct

class MainWindow(QMainWindow):

    own_takeoff_signal = pyqtSignal()
    target_takeoff_signal = pyqtSignal(int)
    dll = cdll.LoadLibrary("data_interface_pro.dll")
    own_example = Ownship_Data_Struct()



    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = adsb_mainForm.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1540, 880)
        #装载更多控件
        url = os.getcwd() + '/tt.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.ui.horizontalLayout_3.addWidget(self.browser)
        # 允许关闭标签
        self.ui.tabWidget.setTabsClosable(True)
        # 设置关闭按钮的槽
        self.ui.tabWidget.tabCloseRequested.connect(self.close_current_tab)
        btn = QToolButton( )
        btn.setIcon(QIcon('pic/add2.jpg'))
        btn.clicked.connect(self.add_new_tab)
        self.ui.tabWidget.setCornerWidget(btn, Qt.TopRightCorner)
        self.time_label= QLabel('')
        self.statusBar().addPermanentWidget(self.time_label,stretch=1)
        timer_a = QTimer(self)
        timer_a.timeout.connect(self.update_time)
        timer_a.start()
        self.ui.btn_import_info_own.clicked.connect(self.import_info_own)
        self.ui.btn_import_info_target1.clicked.connect(self.import_info_target)
        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_stop.clicked.connect(self.stop)

        self.ga = Geography_Analysis()

        #本机信息
        self.data_ownship = {}                  # 本机数据
        self.voyage_distance_ownship_list = []  # 本机航路距离列表 N个航路点有N-1条航路
        self.voyage_time_ownship_list = []      # 本机航路时间列表
        self.groundspeed_ownship = 0            # 本机地速
        self.fre_transmit_ownship = 0           # 数据发送频率 单位s
        self.delay_takeoff_ownship = 0          # 起飞延迟 单位s
        self.Heading_Track_Angle_own_list = []  # 本机航向角序列
        self.V_SN_own_list = []                 # 南北速度序列
        self.V_EW_own_list = []                 # 东西速度序列
        self.lng_own_list = []                  # 经度序列
        self.lat_own_list = []                  # 纬度序列
        self.lngandlat_own_list = []            # 经纬度序列

        #目标机信息
        self.num_targetship = 0     #目标机数量
        self.data_targetship = {}   #目标机携带的所有信息 嵌套字典的字典
        self.groundspeed_targetship_all  = []            # 目标机地速
        self.Altitude_targetship_all = []                # 目标机压强高度
        self.Altitude_targetship_Tcas_all = []               #  目标机Tcas压强高度
        self.fre_transmit_adsb_targetship_all  = []      # ADS-B数据发送频率 单位s
        self.delay_takeoff_targetship_all  = []          # 起飞延迟 单位ms
        self.Heading_Track_Angle_target_all = []  # 航向角序列  嵌套序列
        self.V_SN_target_all= []                   # 南北速度序列    嵌套序列
        self.V_EW_target_all = []                  # 东西速度序列    嵌套序列
        self.lng_target_all = []                   # 经度序列        嵌套序列
        self.lat_target_all = []                   # 纬度序列        嵌套序列
        self.lngandlat_target_all = []              # 经纬度序列      嵌套序列
        #TCAS数据
        self.tcas_fre_transmit_target_all = {}     # TCAS数据发送频率

        #全局
        self.own_takeoff_signal.connect(self.own_takeoff)
        self.target_takeoff_signal.connect(self.target_takeoff)

        #定时器
        self.count_own = 0    # 本机定时器计数
        self.timer_own_show = QTimer()
        self.timer_own_transmit = QTimer()

        self.timer_adsb_transmit = QTimer()
        self.timer_tcas_transmit = QTimer()

        self.variable = locals()
        self.ui.btn_test.clicked.connect(self.test)

    def test(self):
        js_string= '''refreshmarker_ownship(%f,%f);'''%(123.640000,29.72)
        print(js_string)
        self.browser.page().runJavaScript(js_string)
        pass

    def refresh_map(self):
        try:
            if self.data_ownship['basic']['Way_Point']:
                hanglu_own = self.data_ownship['basic']['Way_Point']
                speed_own = self.data_ownship['basic']['Ground_Speed']
                hanglu_own_list = [] #本机航路序列
                for i in range(1,len(hanglu_own)+1):
                    lng = hanglu_own['point'+str(i)][1]
                    lat = hanglu_own['point'+str(i)][2]
                    hanglu_own_list.append([lng,lat])
                js_string_own_init = '''init_ownship(%f,%f,'%s',%s,%d);'''%(hanglu_own['point1'][1],hanglu_own['point1'][2],self.data_ownship['basic']['Flight_ID'],hanglu_own_list,speed_own)
                print(js_string_own_init)
                self.browser.page().runJavaScript(js_string_own_init) #初始化本机位置、标注、航线、移动
            for target_index, info in self.data_targetship.items():
                hanglu_target = info['ADS-B']['Way_Point']
                speed_target = info['ADS-B']['Ground_Speed']
                hanglu_target_list = []  # 单个target机航路序列
                for i in range(1, len(hanglu_target) + 1):
                    lng = hanglu_target['point' + str(i)][1]
                    lat = hanglu_target['point' + str(i)][2]
                    hanglu_target_list.append([lng, lat])
                js_string_target_init = '''init_target(%f,%f,'%s',%s,%d);''' % (hanglu_target['point1'][1], hanglu_target['point1'][2], info['ADS-B']['Flight_ID'], hanglu_target_list, speed_target)
                print(js_string_target_init)
                self.browser.page().runJavaScript(js_string_target_init)
        except:
            traceback.print_exc()

    # 本机信息区域
    def import_info_own(self):
        '''
        导入本机配置文件并解析
        :return:
        '''
        try:
            filename,_type = QFileDialog.getOpenFileName(self, '导入本机信息', '','yaml(*.yaml)')
            if filename:
                with open(filename,'r',encoding='utf-8') as f:
                    file_data = f.read()
                    self.data_ownship = yaml.load(file_data)
            if self.data_ownship:
                self.ui.txt_ICAO_own.setText(self.data_ownship['basic']['ICAO'])
                self.ui.txt_FlightID_own.setText(self.data_ownship['basic']['Flight_ID'])
                self.ui.txt_Altitude_own.setText(str(self.data_ownship['basic']['Altitude']))
                self.ui.txt_V_SN_own.setText(str(self.data_ownship['basic']['North_South_Velocity']))
                self.ui.txt_V_EW_own.setText(str(self.data_ownship['basic']['East_West_Velocity']))
                self.ui.txt_Latitude_own.setText(str(self.data_ownship['basic']['Way_Point']['point1'][2]))
                self.ui.txt_Longitude_own.setText(str(self.data_ownship['basic']['Way_Point']['point1'][1]))
                self.ui.txt_Heading_Track_Angle_own.setText(str(self.data_ownship['basic']['Way_Point']['point1'][3]))
                self.groundspeed_ownship = self.data_ownship['basic']['Ground_Speed']
                self.ui.txt_GroundSpeed_own.setText(str(self.groundspeed_ownship))
                self.fre_transmit_ownship = self.data_ownship['extra']['fre_transmit_data']
                self.delay_takeoff_ownship = self.data_ownship['extra']['delay_time']
                for i in range(1, len(self.data_ownship['basic']['Way_Point'])):
                    lng1 = self.data_ownship['basic']['Way_Point']['point'+str(i)][1]
                    lat1 = self.data_ownship['basic']['Way_Point']['point'+str(i)][2]
                    lng2 = self.data_ownship['basic']['Way_Point']['point'+str(i+1)][1]
                    lat2 = self.data_ownship['basic']['Way_Point']['point'+str(i+1)][2]
                    Heading_Track_Angle2 = self.data_ownship['basic']['Way_Point']['point'+str(i+1)][3]
                    voyage_distance = self.ga.geodistance(lng1,lat1,lng2,lat2)
                    self.voyage_distance_ownship_list.append(voyage_distance)  #距离 km
                    self.voyage_time_ownship_list.append(int(voyage_distance/self.groundspeed_ownship * 3600)) #时间 s
                    interpolation_num = int(voyage_distance/self.groundspeed_ownship * 3600 * 2)
                    interpolation_dis = [voyage_distance/interpolation_num * x for x in range(1,interpolation_num+1)]
                    self.lngandlat_own_list += [self.ga.get_lngAndlat(lng1,lat1,Heading_Track_Angle2,x) for x in interpolation_dis]
                    V_SN = round(self.groundspeed_ownship * cos(Heading_Track_Angle2 * pi / 180.0), 3)
                    V_EW = round(self.groundspeed_ownship * sin(Heading_Track_Angle2 * pi / 180.0), 3)
                    self.V_EW_own_list += [V_EW]*interpolation_num
                    self.V_SN_own_list += [V_SN]*interpolation_num
                    self.Heading_Track_Angle_own_list += [Heading_Track_Angle2] * interpolation_num
                for item in self.lngandlat_own_list:
                    self.lng_own_list.append(item[0])
                    self.lat_own_list.append(item[1])
            # print(self.voyage_distance_ownship_list)
            # print(self.voyage_time_ownship_list)  #单位s
            # print(self.Heading_Track_Angle_own_list)
            print("本机数据量："+ str(len(self.Heading_Track_Angle_own_list)))
            print("本机数据量：" + str(len(self.lngandlat_own_list)))
            # print(len(self.V_EW_own_list))
            # print(len(self.V_SN_own_list))
            # print(len(self.lngandlat_own_list))
            # print(len(self.lng_own_list))

        except:
            traceback.print_exc()
    # 目标机信息区域
    def import_info_target(self):
        '''
        导入目标机配置文件并解析
        :return:
        '''
        current_targetship_index = self.ui.tabWidget.currentIndex()+1
        try:
            filename,_type = QFileDialog.getOpenFileName(self, '导入目标机信息', '','yaml(*.yaml)')
            if filename:
                with open(filename,'r',encoding='utf-8') as f:
                    file_data = f.read()
                    data_targetship = yaml.load(file_data)
                if data_targetship:
                    self.data_targetship[current_targetship_index] = data_targetship
                    self.findChild(QLineEdit, "txt_ICAO_target"+str(current_targetship_index)).setText(data_targetship['ADS-B']['ICAO'])
                    self.findChild(QLineEdit, "txt_FlightID_target" + str(current_targetship_index)).setText(data_targetship['ADS-B']['Flight_ID'])
                    self.findChild(QLineEdit, "txt_Altitude_target" + str(current_targetship_index)).setText(str(data_targetship['ADS-B']['Altitude']))
                    self.findChild(QLineEdit, "txt_V_SN_target" + str(current_targetship_index)).setText(str(data_targetship['ADS-B']['North_South_Velocity']))
                    self.findChild(QLineEdit, "txt_V_EW_target"+ str(current_targetship_index)).setText(str(data_targetship['ADS-B']['East_West_Velocity']))
                    self.findChild(QLineEdit, "txt_Latitude_target" + str(current_targetship_index)).setText(str(data_targetship['ADS-B']['Way_Point']['point1'][2]))
                    self.findChild(QLineEdit, "txt_Longitude_target" + str(current_targetship_index)).setText(str(data_targetship['ADS-B']['Way_Point']['point1'][1]))
                    self.findChild(QLineEdit, "txt_Heading_Track_Angle_target" + str(current_targetship_index)).setText(str(data_targetship['ADS-B']['Way_Point']['point1'][3]))
                    self.findChild(QLineEdit, "txt_GroundSpeed_target" + str(current_targetship_index)).setText(str(data_targetship['ADS-B']['Ground_Speed']))
                    self.findChild(QLineEdit, "txt_Track_ID_target" + str(current_targetship_index)).setText(str(data_targetship['TCAS']['Track_ID']))
                    self.findChild(QLineEdit, "txt_Tcas_Altitude_target" + str(current_targetship_index)).setText(str(data_targetship['TCAS']['Altitude_TCAS']))
                    self.findChild(QLineEdit, "txt_Relative_Direction_target" + str(current_targetship_index)).setText(str(data_targetship['TCAS']['Bearing']))
                    self.findChild(QLineEdit, "txt_Relative_Distance_target" + str(current_targetship_index)).setText(str(data_targetship['TCAS']['Range']))
                    fre_transmit_targetship = data_targetship['ADS-B']['fre_transmit_adsb']
                    self.fre_transmit_adsb_targetship_all.append(fre_transmit_targetship)
                    self.delay_takeoff_targetship_all.append(data_targetship['extra']['delay_time'])
                    groundspeed_targetship = data_targetship['ADS-B']['Ground_Speed']
                    self.groundspeed_targetship_all.append(groundspeed_targetship)
                    altitude_target =  data_targetship['ADS-B']['Altitude']
                    self.Altitude_targetship_all.append(altitude_target)
                    tcas_altitude = data_targetship['TCAS']['Altitude_TCAS']
                    self.Altitude_targetship_Tcas_all.append(tcas_altitude)
                    tcas_enable = data_targetship['TCAS']['enable']
                    if tcas_enable == 1:
                        tcas_transmit_fre = data_targetship['TCAS']['fre_transmit_tcas']
                        self.tcas_fre_transmit_target_all[current_targetship_index]= tcas_transmit_fre
                    voyage_distance_targetship_list = [] #单个目标机航程距离序列
                    voyage_time_targetship_list = []   #单个目标机航程时间序列
                    lngandlat_own_list = []            #单个目标机航迹经纬度序列
                    V_EW_own_list = []                #单个目标机东西速度序列
                    V_SN_own_list = []                #单个目标机南北速度序列
                    Heading_Track_Angle_own_list = []  #单个目标机航向角序列
                    lng_own_list = []                  #单个目标机经度系列
                    lat_own_list =[]                   #单个目标机纬度系列

                    for i in range(1, len(data_targetship['ADS-B']['Way_Point'])):
                        lng1 = data_targetship['ADS-B']['Way_Point']['point'+str(i)][1]
                        lat1 = data_targetship['ADS-B']['Way_Point']['point'+str(i)][2]
                        lng2 = data_targetship['ADS-B']['Way_Point']['point'+str(i+1)][1]
                        lat2 = data_targetship['ADS-B']['Way_Point']['point'+str(i+1)][2]
                        Heading_Track_Angle2 = data_targetship['ADS-B']['Way_Point']['point'+str(i+1)][3]
                        voyage_distance = self.ga.geodistance(lng1,lat1,lng2,lat2)
                        voyage_distance_targetship_list.append(voyage_distance)
                        voyage_time_targetship_list.append(int(voyage_distance/groundspeed_targetship * 3600))
                        interpolation_num = int(voyage_distance/groundspeed_targetship * 3600 *2 )
                        interpolation_dis = [voyage_distance/interpolation_num * x for x in range(1,interpolation_num+1)]
                        lngandlat_own_list += [self.ga.get_lngAndlat(lng1,lat1,Heading_Track_Angle2,x) for x in interpolation_dis]
                        V_SN = round(groundspeed_targetship * cos(Heading_Track_Angle2 * pi / 180.0), 3)
                        V_EW = round(groundspeed_targetship * sin(Heading_Track_Angle2 * pi / 180.0), 3)
                        V_EW_own_list += [V_EW]*interpolation_num
                        V_SN_own_list += [V_SN]*interpolation_num
                        Heading_Track_Angle_own_list += [Heading_Track_Angle2] * interpolation_num
                    for item in lngandlat_own_list:
                        lng_own_list.append(item[0])
                        lat_own_list.append(item[1])
                    print("目标机数据量：" + str(len(lng_own_list)))
                    self.Heading_Track_Angle_target_all.append(Heading_Track_Angle_own_list)
                    self.V_SN_target_all.append(V_SN_own_list)
                    self.V_EW_target_all.append(V_EW_own_list)
                    self.lngandlat_target_all.append(lngandlat_own_list)
                    self.lng_target_all.append(lng_own_list)
                    self.lat_target_all.append(lat_own_list)


        except:
            traceback.print_exc()

    def add_new_tab(self):
        '''
        创建新的目标机标签页
        :return:
        '''
        try:
            target_plane_index = self.ui.tabWidget.count()+1
            frame_copy = QFrame()
            frame_copy.setObjectName('frame_target'+str(target_plane_index))
            btn_import_info_target = QPushButton(frame_copy)
            btn_import_info_target.setObjectName('btn_import_info_target'+str(target_plane_index))
            btn_import_info_target.setText('导入飞机信息')
            btn_import_info_target.setGeometry(QRect(10, 15, 241, 28))
            btn_import_info_target.clicked.connect(self.import_info_target)
            # ADS-B布局
            groupBox_adsb = QGroupBox(frame_copy)
            groupBox_adsb.setTitle('ADS-B')
            groupBox_adsb.setGeometry(QRect(10, 50, 291, 361))
            layout_adsb = QWidget(groupBox_adsb)
            layout_adsb.setGeometry(QRect(9, 34, 271, 318))
            gridLayout_adsb = QGridLayout(layout_adsb)
            gridLayout_adsb.setContentsMargins(0, 0, 0, 0)
            # ICAO码
            label_ICAO = QLabel('ICAO码：',layout_adsb)
            label_ICAO.setMaximumSize(QSize(90, 16777215))
            label_ICAO.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_ICAO, 0, 1, 1, 1)
            lineEdit_ICAO = QLineEdit(layout_adsb)
            lineEdit_ICAO.setEnabled(False)
            lineEdit_ICAO.setMaximumSize(QSize(150, 16777215))
            lineEdit_ICAO.setObjectName("txt_ICAO_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_ICAO, 0, 2, 1, 1)
            # 航班号
            label_Flight_No = QLabel('航班号：',layout_adsb)
            label_Flight_No.setMaximumSize(QSize(90, 16777215))
            label_Flight_No.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Flight_No, 1, 1, 1, 1)
            lineEdit_Flight_No = QLineEdit(layout_adsb)
            lineEdit_Flight_No.setEnabled(False)
            lineEdit_Flight_No.setMaximumSize(QSize(150, 16777215))
            lineEdit_Flight_No.setObjectName("txt_FlightID_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Flight_No, 1, 2, 1, 1)
            #压强高度
            label_Press_Height = QLabel('压强高度(m)：',layout_adsb)
            label_Press_Height.setMaximumSize(QSize(90, 16777215))
            label_Press_Height.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Press_Height, 2, 1, 1, 1)
            lineEdit_Press_Height = QLineEdit(layout_adsb)
            lineEdit_Press_Height.setEnabled(False)
            lineEdit_Press_Height.setMaximumSize(QSize(150, 16777215))
            lineEdit_Press_Height.setObjectName("txt_Altitude_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Press_Height, 2, 2, 1, 1)
            #南北速度
            label_V_SN= QLabel('南北速度(km/h)：',layout_adsb)
            label_V_SN.setMaximumSize(QSize(16777215, 16777214))
            label_V_SN.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_V_SN, 3, 1, 1, 1)
            lineEdit_V_SN = QLineEdit(layout_adsb)
            lineEdit_V_SN.setEnabled(False)
            lineEdit_V_SN.setMaximumSize(QSize(150, 16777215))
            lineEdit_V_SN.setObjectName("txt_V_SN_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_V_SN, 3, 2, 1, 1)
            #东西速度
            label_V_EW= QLabel('东西速度(km/h)：',layout_adsb)
            label_V_EW.setMaximumSize(QSize(16777215, 16777214))
            label_V_EW.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_V_EW, 4, 1, 1, 1)
            lineEdit_V_EW = QLineEdit(layout_adsb)
            lineEdit_V_EW.setEnabled(False)
            lineEdit_V_EW.setMaximumSize(QSize(150, 16777215))
            lineEdit_V_EW.setObjectName("txt_V_EW_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_V_EW, 4, 2, 1, 1)
            #纬度
            label_Latitude= QLabel('纬度(deg)：',layout_adsb)
            label_Latitude.setMaximumSize(QSize(90, 16777215))
            label_Latitude.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Latitude, 5, 1, 1, 1)
            lineEdit_Latitude = QLineEdit(layout_adsb)
            lineEdit_Latitude.setEnabled(False)
            lineEdit_Latitude.setMaximumSize(QSize(150, 16777215))
            lineEdit_Latitude.setObjectName("txt_Latitude_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Latitude, 5, 2, 1, 1)
            #经度
            label_Longitude= QLabel('经度(deg)：',layout_adsb)
            label_Longitude.setMaximumSize(QSize(90, 16777215))
            label_Longitude.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Longitude, 6, 1, 1, 1)
            lineEdit_Longitude = QLineEdit(layout_adsb)
            lineEdit_Longitude.setEnabled(False)
            lineEdit_Longitude.setMaximumSize(QSize(150, 16777215))
            lineEdit_Longitude.setObjectName("txt_Longitude_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Longitude, 6, 2, 1, 1)
            #航向角
            label_Heading_Track_Angle= QLabel('航向角(deg)：',layout_adsb)
            label_Heading_Track_Angle.setMaximumSize(QSize(90, 16777215))
            label_Heading_Track_Angle.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Heading_Track_Angle, 7, 1, 1, 1)
            lineEdit_Heading_Track_Angle = QLineEdit(layout_adsb)
            lineEdit_Heading_Track_Angle.setEnabled(False)
            lineEdit_Heading_Track_Angle.setMaximumSize(QSize(150, 16777215))
            lineEdit_Heading_Track_Angle.setObjectName("txt_Heading_Track_Angle_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Heading_Track_Angle, 7, 2, 1, 1)
            #地速
            label_Ground_Speed= QLabel('地速(km/h)：',layout_adsb)
            label_Ground_Speed.setMaximumSize(QSize(90, 16777215))
            label_Ground_Speed.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Ground_Speed, 8, 1, 1, 1)
            lineEdit_Ground_Speed = QLineEdit(layout_adsb)
            lineEdit_Ground_Speed.setEnabled(False)
            lineEdit_Ground_Speed.setMaximumSize(QSize(150, 16777215))
            lineEdit_Ground_Speed.setObjectName("txt_GroundSpeed_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Ground_Speed, 8, 2, 1, 1)
            #"停止发送ADS-B数据"button
            btn_stop_sending_adsb = QPushButton('停止发送ADS-B数据', layout_adsb)
            btn_stop_sending_adsb.setObjectName("btn_stopsend_adsb_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(btn_stop_sending_adsb, 9, 1, 1, 2)
            # T-CAS布局
            groupBox_tcas = QGroupBox(frame_copy)
            groupBox_tcas.setTitle('TCAS')
            groupBox_tcas.setGeometry(QRect(310, 50, 271, 361))
            layout_tcas = QWidget(groupBox_tcas)
            layout_tcas.setGeometry(QRect(10, 40, 251, 261))
            gridLayout_tcas = QGridLayout(layout_tcas)
            gridLayout_tcas.setContentsMargins(0, 0, 0, 0)
            #Track_ID
            label_Track_ID= QLabel('Track_ID：',layout_tcas)
            gridLayout_tcas.addWidget(label_Track_ID, 0, 1, 1, 1)
            lineEdit_Track_ID = QLineEdit(layout_tcas)
            lineEdit_Track_ID.setEnabled(False)
            lineEdit_Track_ID.setObjectName("txt_Track_ID_target"+str(target_plane_index))
            gridLayout_tcas.addWidget(lineEdit_Track_ID, 0, 2, 1, 1)
            #压强高度
            label_Press_Height_TCAS = QLabel('压强高度(m)：',layout_tcas)
            gridLayout_tcas.addWidget(label_Press_Height_TCAS, 1, 1, 1, 1)
            lineEdit_Press_Height_TCAS = QLineEdit(layout_tcas)
            lineEdit_Press_Height_TCAS.setEnabled(False)
            lineEdit_Press_Height_TCAS.setObjectName("txt_Tcas_Altitude_target"+str(target_plane_index))
            gridLayout_tcas.addWidget(lineEdit_Press_Height_TCAS, 1, 2, 1, 1)
            #相对本机方位
            label_Relative_Direction = QLabel('相对本机方位(deg)：',layout_tcas)
            label_Relative_Direction.setMaximumSize(QSize(16777215, 16777214))
            gridLayout_tcas.addWidget(label_Relative_Direction, 2, 1, 1, 1)
            lineEdit_Relative_Direction = QLineEdit(layout_tcas)
            lineEdit_Relative_Direction.setEnabled(False)
            lineEdit_Relative_Direction.setObjectName("txt_Relative_Direction_target"+str(target_plane_index))
            gridLayout_tcas.addWidget(lineEdit_Relative_Direction, 2, 2, 1, 1)
            #相对本机距离
            label_Relative_Distance = QLabel('相对本机距离(km)：',layout_tcas)
            label_Relative_Distance.setMaximumSize(QSize(16777215, 16777214))
            gridLayout_tcas.addWidget(label_Relative_Distance, 3, 1, 1, 1)
            lineEdit_Relative_Distance = QLineEdit(layout_tcas)
            lineEdit_Relative_Distance.setEnabled(False)
            lineEdit_Relative_Distance.setObjectName("txt_Relative_Distance_target"+str(target_plane_index))
            gridLayout_tcas.addWidget(lineEdit_Relative_Distance, 3, 2, 1, 1)
            #"停止发送TCAS数据"button
            btn_stop_sending_tcas = QPushButton('停止发送TCAS数据',groupBox_tcas)
            #gridLayout_tcas.addWidget(btn_stop_sending_tcas,4,1,1,2)
            btn_stop_sending_tcas.setGeometry(QRect(10, 318, 251, 28))
            btn_stop_sending_tcas.setObjectName("btn_stopsend_tcas_target"+str(target_plane_index))
            i = self.ui.tabWidget.addTab(frame_copy,  str(target_plane_index)+'号目标机')
            self.ui.tabWidget.setCurrentIndex(i)
        except:
            traceback.print_exc()

    def close_current_tab(self,int):
        '''
        删除当前目标机标签页
        :param int:
        :return:
        '''
        try:
            if self.ui.tabWidget.count() == 1:  #如果当前标签页只剩下一个则不关闭
                QMessageBox.information(self, '提示', '请保留至少一个目标机!', QMessageBox.Ok)
                return
            if self.ui.tabWidget.count() == int+1:  #仅在用户点击最后一个标签页时关闭
                if self.data_targetship.get(self.ui.tabWidget.count()):
                    del self.data_targetship[self.ui.tabWidget.count()]
                self.ui.tabWidget.removeTab(int)
                self.findChild(QFrame, 'frame_target' + str(int + 1)).deleteLater()
            else:
                QMessageBox.information(self, '提示', '请先关闭高序列目标机!', QMessageBox.Ok)
        except:
            traceback.print_exc()

    # 控制台区域
    def start(self):
        try:
            #TODO：界面检查,确定目标机数量
            if len(self.data_targetship) == self.ui.tabWidget.count() and self.data_ownship:
                #创建socket
                #'192.168.100.128', 8000
                self.ip_port_own = ('127.0.0.1', 8000)
                self.socket_own = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
                self.ip_port_tcas = ('127.0.0.1', 8001)
                self.socket_tcas = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
                self.ip_port_adsb = ('127.0.0.1', 8002)
                self.socket_adsb = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
                # 界面btn使能
                self.ui.btn_start.setEnabled(False)
                self.ui.btn_stop.setEnabled(True)
                self.ui.btn_import_info_own.setEnabled(False)
                # 本机起飞延时
                print("本机起飞延时"+str(self.delay_takeoff_ownship)+'s')
                timer_own = threading.Timer(self.delay_takeoff_ownship,self.own_takeoff_signal.emit)
                timer_own.start()

                # 确定目标机数量
                self.num_targetship = self.ui.tabWidget.count()
                for i in range(self.num_targetship):
                    self.variable['target_count' + str(i+1)] = 0
                print('目标机数量： ' + str(self.num_targetship))
                logging.info('目标机数量： '+str(self.num_targetship))
                for i in range(self.num_targetship):
                    self.findChild(QPushButton, 'btn_import_info_target' + str(i + 1)).setEnabled(False)
                    print(str(i+1)+"号目标机起飞延时" + str(self.delay_takeoff_targetship_all[i]) + 's')
                    def emit_signal():
                        self.target_takeoff_signal.emit(i+1)
                    timer_target = threading.Timer(self.delay_takeoff_targetship_all[i],emit_signal)
                    timer_target.start()

                #设置发送ads-b和tcas的timer
                self.count_timer_adsb_transmit = 0
                self.timer_adsb_transmit.timeout.connect(self.target_ads_b_transmit)
                self.timer_adsb_transmit.start(1000)

                self.count_timer_tcas_transmit = 0
                self.timer_tcas_transmit.timeout.connect(self.target_tcas_transmit)
                self.timer_tcas_transmit.start(1000)

            else:
                QMessageBox.information(self, '提示', '请检查界面参数是否齐全!', QMessageBox.Ok)
        except:
            traceback.print_exc()

    def stop(self):
        try:
            #地图标识删除，button使能复原
            self.browser.page().runJavaScript("removeMarkers();")
            self.ui.btn_start.setEnabled(True)
            self.ui.btn_import_info_own.setEnabled(True)
            self.ui.btn_stop.setEnabled(False)
            self.count_own = 0  # 本机定时器计数
            #定时器关闭
            self.timer_own_show.stop()
            self.timer_own_transmit.stop()
            self.timer_adsb_transmit.stop()
            self.timer_tcas_transmit.stop()
            for i in range(1,self.num_targetship+1):
                self.variable['target_count' + str(i)] = 0
                if self.findChild(QTimer,'target_timer'+str(i)):
                    self.findChild(QTimer,'target_timer'+str(i)).stop()
                    self.findChild(QTimer,'target_timer'+str(i)).deleteLater()
                self.findChild(QPushButton,'btn_import_info_target'+str(i)).setEnabled(True)
            # socket关闭
            self.socket_tcas.close()
            self.socket_own.close()
            self.socket_adsb.close()
        except:
            traceback.print_exc()

    # 本机相关函数
    def own_takeoff(self):
        '''
        模拟本机起飞过程,动态刷新地图、界面,仅执行一次
        :return:
        '''
        try:
            # 本机准备起飞
            print('本机起飞,开始发送数据...')
            logging.info('本机起飞,开始发送数据...')
            # 开启定时器动态显示本机信息、发送数据
            self.timer_own_show.timeout.connect(self.own_showinfo)
            self.timer_own_show.start(500)
            self.timer_own_transmit.timeout.connect(self.own_transmit)
            self.timer_own_transmit.start(self.fre_transmit_ownship * 1000)
            # 地图模拟飞行
            if self.data_ownship['basic']['Way_Point']:
                hanglu_own = self.data_ownship['basic']['Way_Point']
                speed_own = self.data_ownship['basic']['Ground_Speed']
                hanglu_own_list = []  # 本机航路序列
                for i in range(1, len(hanglu_own) + 1):
                    lng = hanglu_own['point' + str(i)][1]
                    lat = hanglu_own['point' + str(i)][2]
                    hanglu_own_list.append([lng, lat])
                js_string_own_init = '''init_ownship(%f,%f,'%s',%s,%d);''' % (
                hanglu_own['point1'][1], hanglu_own['point1'][2], self.data_ownship['basic']['Flight_ID'], hanglu_own_list,
                speed_own)
                print(js_string_own_init)
                self.browser.page().runJavaScript(js_string_own_init)  # 初始化本机位置、标注、航线、移动
        except:
            traceback.print_exc()

    def own_showinfo(self):
        '''显示本机信息,主要为经纬度、飞行速度,地图数据更新'''
        try:
            if self.count_own >= len(self.Heading_Track_Angle_own_list):
                self.timer_own_show.stop()
            else:
                current_Heading_Track_Angle = self.Heading_Track_Angle_own_list[self.count_own]
                current_lng = self.lng_own_list[self.count_own]
                current_lat = self.lat_own_list[self.count_own]
                current_v_ew = self.V_EW_own_list[self.count_own]
                current_v_sn =  self.V_SN_own_list[self.count_own]
                self.ui.txt_Heading_Track_Angle_own.setText(str(current_Heading_Track_Angle))
                self.ui.txt_Longitude_own.setText(str(current_lng))
                self.ui.txt_Latitude_own.setText(str(current_lat))
                self.ui.txt_V_EW_own.setText(str(current_v_ew))
                self.ui.txt_V_SN_own.setText(str(current_v_sn))
                self.count_own += 1
        except:
            traceback.print_exc()

    def own_transmit(self):
        '''
        发送本机数据
        :return:
        '''
        try:
            own_data_struct = Ownship_Data_Struct()
            own_data_struct.ICAO = self.data_ownship['basic']['ICAO'].encode()                           #ICAO码
            own_data_struct.Flight_ID = self.data_ownship['basic']['Flight_ID'].encode()                 #航班号
            own_data_struct.Flight_24bit_addr = self.data_ownship['basic']['Flight_24bit_addr']
            own_data_struct.Altitude = self.data_ownship['basic']['Altitude']                            #几何高度
            own_data_struct.Radio_Altitude = self.data_ownship['basic']['Radio_Altitude']
            own_data_struct.North_South_Velocity = int(float(self.ui.txt_V_SN_own.text()) * 1000/3600)    #南北速度
            own_data_struct.East_West_Velocity = int(float(self.ui.txt_V_EW_own.text()) * 1000/3600)      #东西速度
            own_data_struct.Vertical_Speed = int(float(self.data_ownship['basic']['Vertical_Speed'] * 1000/3600))
            own_data_struct.Latitude  = self.ga.degTorad(float(self.ui.txt_Latitude_own.text()))    #纬度
            own_data_struct.Longitude = self.ga.degTorad(float(self.ui.txt_Longitude_own.text()))   #经度
            Heading_own = self.ga.degTorad(float(self.ui.txt_Heading_Track_Angle_own.text()))
            own_data_struct.Heading_Track_Angle = Heading_own #航向角
            own_data_struct.Ground_Speed = int(float(self.data_ownship['basic']['Ground_Speed'] * 1000/3600)) #
            own_data_struct.Flight_Length = int(self.data_ownship['basic']['Flight_Length'] * 1000)
            own_data_struct.Flight_Width = int(self.data_ownship['basic']['Flight_Width'] * 1000)
            own_data_struct.Seconds = int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[-1])  #
            own_data_struct.Mintes  = int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[1])   #
            own_data_struct.Hours   = int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[0])   #
            own_data_struct.p_Seconds =  0
            own_data_struct.p_Mintes  =  0
            own_data_struct.p_Hours   =  0
            own_data_struct.v_Seconds =  0
            own_data_struct.v_Mintes  =  0
            own_data_struct.v_Hours   =  0
            own_data_struct.s_Seconds =  0
            own_data_struct.s_Mintes  =  0
            own_data_struct.s_Hours   =  0
            own_data_struct.NACV = int(self.data_ownship['basic']['NACV'])                 # 0-4
            own_data_struct.NACp = int(self.data_ownship['basic']['NACp'])                 # 0-11
            temp_byte = bytes(2048)
            lenth = self.dll.Pack_Ownship_data(own_data_struct, temp_byte, 2048)
            print('本机数据打包长度：'+ str(lenth))
            #print(temp_byte.strip(b'\x00'))
            self.socket_own.sendto(temp_byte.strip(b'\x00'), self.ip_port_own)
            #写入日志
            lock = threading.Lock()
            lock.acquire()
            logging.info("本机发送数据：" + str(temp_byte.strip(b'\x00')))
            lock.release()
        except:
            traceback.print_exc()

    #  目标机相关函数
    def target_takeoff(self,target_index):
        '''
        模拟目标机起飞过程，动态刷新地图、界面，需要执行与目标机数量相同次
        :param target_index:目标机编号
        :return:
        '''
        try:
            print(str(target_index)+'号目标机起飞,开始发送数据...')
            logging.info(str(target_index)+'号目标机起飞,开始发送数据...')
            print(str(target_index)+'号目标机，adsb数据发送周期：'+str(self.fre_transmit_adsb_targetship_all[target_index-1])+'s')
            logging.info(str(target_index)+'号目标机，adsb数据发送周期：'+str(self.fre_transmit_adsb_targetship_all[target_index-1])+'s')
            # 开启定时器动态显示本机信息、发送数据
            target_timer = QTimer(self)
            target_timer.setObjectName('target_timer'+str(target_index))
            target_timer.setProperty('target_num',target_index)
            target_timer.timeout.connect(self.target_showinfo)
            target_timer.start(500)
            # 地图模拟飞行
            hanglu_target = self.data_targetship[target_index]['ADS-B']['Way_Point']
            speed_target = self.data_targetship[target_index]['ADS-B']['Ground_Speed']
            hanglu_target_list = []  # 单个target机航路序列
            for i in range(1, len(hanglu_target) + 1):
                lng = hanglu_target['point' + str(i)][1]
                lat = hanglu_target['point' + str(i)][2]
                hanglu_target_list.append([lng, lat])
            js_string_target_init = '''init_target(%f,%f,'%s',%s,%d);''' % (
                hanglu_target['point1'][1], hanglu_target['point1'][2], self.data_targetship[target_index]['ADS-B']['Flight_ID'],
                hanglu_target_list,
                speed_target)
            print(js_string_target_init)
            self.browser.page().runJavaScript(js_string_target_init)
        except:
            traceback.print_exc()

    def target_showinfo(self):
        '''
        显示目标机信息 主要为ADS-B速度、经纬度和TCAS相对位置和相对方位
        '''
        try:
            sender = self.sender() #获取连接槽函数的信号源
            target_num = sender.property('target_num')
            if self.variable['target_count' + str(target_num)] >= len(self.lng_target_all[target_num-1]):
                self.findChild(QTimer,'target_timer'+str(target_num)).stop()
                self.findChild(QTimer,'target_timer'+str(target_num)).deleteLater()
            else:
                current_adsb_lng = self.lng_target_all[target_num-1][self.variable['target_count' + str(target_num)]]
                current_adsb_lat = self.lat_target_all[target_num-1][self.variable['target_count' + str(target_num)]]
                current_Heading_Track_Angle = self.Heading_Track_Angle_target_all[target_num-1][self.variable['target_count' + str(target_num)]]
                current_tcas_height = self.Altitude_targetship_Tcas_all[target_num-1]
                self.findChild(QLineEdit, "txt_Heading_Track_Angle_target" + str(target_num)).setText(str(current_Heading_Track_Angle))
                self.findChild(QLineEdit, "txt_Longitude_target" + str(target_num)).setText(str(current_adsb_lng))
                self.findChild(QLineEdit, "txt_Latitude_target" + str(target_num)).setText(str(current_adsb_lat))
                self.findChild(QLineEdit, "txt_V_EW_target" + str(target_num)).setText(str(self.V_EW_target_all[target_num - 1][self.variable['target_count' + str(target_num)]]))
                self.findChild(QLineEdit, "txt_V_SN_target" + str(target_num)).setText(str(self.V_SN_target_all[target_num - 1][self.variable['target_count' + str(target_num)]]))
                self.variable['target_count' + str(target_num)] +=1
                # 本机坐标信息
                current_own_lng = self.ui.txt_Longitude_own.text()
                current_own_lat = self.ui.txt_Latitude_own.text()
                current_own_Heading_Track_Angle = self.ui.txt_Heading_Track_Angle_own.text()
                current_own_height = self.ui.txt_Altitude_own.text()

                # 相对本机方位角
                relative_direction = 0 # 目标机相对本机方位角 单位deg
                if float(current_Heading_Track_Angle) > float(current_own_Heading_Track_Angle):
                    relative_direction = float(current_Heading_Track_Angle) - float(current_own_Heading_Track_Angle)
                else:
                    relative_direction =  float(current_Heading_Track_Angle)+ 360 - float(current_own_Heading_Track_Angle)
                # print(relative_direction)
                self.findChild(QLineEdit, "txt_Relative_Direction_target" + str(target_num)).setText(str(relative_direction))
                # ads-b相对本机距离
                relative_distance_xy = self.ga.geodistance(float(current_adsb_lng), float(current_adsb_lat), float(current_own_lng),float(current_own_lat))
                #获取NIC和SIL数据 确定是否为Tcas关联的最佳源
                tcas_lng = current_adsb_lng   #TCAS经度坐标
                tcas_lat = current_adsb_lat   #TCAS纬度坐标
                relative_distance_tcas = 0 #tcas相对本机距离
                if relative_distance_xy >= 4.649 and relative_distance_xy<=18.52: #tcas取ads-b为圆心半径2324内任意点
                    print('a')
                    tcas_lng =  current_adsb_lng
                    tcas_lat =  current_adsb_lat
                elif relative_distance_xy >2.324 and  relative_distance_xy <4.649:
                    print('b')
                    tcas_lng, tcas_lat = self.ga.get_lngAndlat(current_own_lng,current_own_lat,relative_direction,relative_distance_xy-2.324)
                elif relative_distance_xy <2.324:
                    print('c')
                    tcas_lng =  current_adsb_lng
                    tcas_lat =  current_adsb_lat
                relative_distance_tcas = round(self.ga.geodistance_with_height(float(tcas_lng), float(tcas_lat),
                                                                    float(current_tcas_height)/1000, float(current_own_lng),
                                                                    float(current_own_lat),
                                                                    float(current_own_height)/1000),3)
                self.findChild(QLineEdit, "txt_Relative_Distance_target" + str(target_num)).setText(str(relative_distance_tcas))
        except:
            traceback.print_exc()

    def target_ads_b_transmit(self):
        try:
            #确定一个ads_b发送周期内的ADSB_Data_Struct数量
            num = 0
            target_index_list = []
            for index in range(self.num_targetship):
                if self.count_timer_adsb_transmit% self.fre_transmit_adsb_targetship_all[index] == 0:
                    num += 1
                    target_index_list.append(index+1)
            # 开始打包ADS-B数据
            lock = threading.Lock()
            lock.acquire()
            logging.info("开始打包"+str(num)+"个目标机ADS-B数据....")
            print("开始打包"+str(num)+"个目标机ADS-B数据....")
            ArrayType = ADSB_Data_Struct * num
            array = ArrayType()
            j = 0
            for target_index in target_index_list:
                adsb_data_struct = ADSB_Data_Struct()
                adsb_data_struct.ICAO = self.data_targetship[target_index]['ADS-B']['ICAO'].encode()            #ICAO码
                adsb_data_struct.Flight_ID = self.data_targetship[target_index]['ADS-B']['Flight_ID'].encode()  #航班号
                adsb_data_struct.Flight_24bit_addr = self.data_targetship[target_index]['ADS-B']['Flight_24bit_addr']
                adsb_data_struct.Aircraft_Category =  self.data_targetship[target_index]['ADS-B']['Aircraft_Category']
                adsb_data_struct.Altitude = self.data_targetship[target_index]['ADS-B']['Altitude']             #几何高度
                adsb_data_struct.Radio_Altitude = self.data_targetship[target_index]['ADS-B']['Radio_Altitude']
                adsb_data_struct.North_South_Velocity = int(float(self.findChild(QLineEdit, "txt_V_SN_target" + str(target_index)).text()) * 1000 / 3600)  # 南北速度m/s
                adsb_data_struct.East_West_Velocity = int(float(self.findChild(QLineEdit, "txt_V_EW_target" + str(target_index)).text()) * 1000 / 3600)    # 东西速度m/s
                adsb_data_struct.Vertical_Speed = int(float(self.data_targetship[target_index]['ADS-B']['Vertical_Speed'] * 1000 / 3600))
                adsb_data_struct.Latitude = self.ga.degTorad(float(self.findChild(QLineEdit, "txt_Latitude_target" + str(target_index)).text()))  # 纬度 弧度
                adsb_data_struct.Longitude =self.ga.degTorad(float(self.findChild(QLineEdit, "txt_Longitude_target" + str(target_index)).text())) # 经度 弧度
                adsb_data_struct.Heading_Track_Angle = self.ga.degTorad(float(self.findChild(QLineEdit, "txt_Heading_Track_Angle_target" + str(target_index)).text()))  # 航向角
                adsb_data_struct.Air_Ground_Sta = self.data_targetship[target_index]['ADS-B']['Air_Ground_Sta']
                adsb_data_struct.Ground_Speed = int(float(self.data_targetship[target_index]['ADS-B']['Ground_Speed'] * 1000/3600))    #地速
                adsb_data_struct.Seconds = int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[-1])    #
                adsb_data_struct.Mintes = int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[1])      #
                adsb_data_struct.Hours = int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[0])       #
                adsb_data_struct.p_Seconds = int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[-1])  #
                adsb_data_struct.p_Mintes = int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[1])    #
                adsb_data_struct.p_Hours = int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[0])     #
                adsb_data_struct.v_Seconds = 0
                adsb_data_struct.v_Mintes = 0
                adsb_data_struct.v_Hours = 0
                adsb_data_struct.s_Seconds = 0
                adsb_data_struct.s_Mintes = 0
                adsb_data_struct.s_Hours = 0
                adsb_data_struct.NACV = self.data_targetship[target_index]['ADS-B']['NACV']
                adsb_data_struct.NACp = self.data_targetship[target_index]['ADS-B']['NACp']
                adsb_data_struct.NIC =  self.data_targetship[target_index]['ADS-B']['NIC']
                adsb_data_struct.SIL =  self.data_targetship[target_index]['ADS-B']['SIL']
                adsb_data_struct.SAD =  self.data_targetship[target_index]['ADS-B']['SDA']
                adsb_data_struct.emergency_priority_sta = self.data_targetship[target_index]['ADS-B']['emergency_priority_sta']
                adsb_data_struct.data_link_version = self.data_targetship[target_index]['ADS-B']['data_link_version']
                array[j] = adsb_data_struct
                j+=1
            temp_byte = bytes(2048)
            lenth = self.dll.Pack_ADSB_data(array,num, temp_byte, 2048)
            print('目标机ADS-B数据打包长度：' + str(lenth))
            logging.info('目标机ADS-B数据打包长度：' + str(lenth))
            print(temp_byte.strip(b'\x00'))
            #UDP发送数据
            #self.socket_adsb.sendto(temp_byte.strip(b'\x00'), self.ip_port_adsb)
            # logging.info("目标机发送ADS-B数据：" + str(temp_byte.strip(b'\x00')))
            # lock.release()
            # self.count_timer_adsb_transmit +=1
        except:
            traceback.print_exc()

    def target_tcas_transmit(self):
        try:
            # 确定一个tcas发送周期内的TCAS_Data_Struct数量
            target_index_list = []
            for target_index, fre in self.tcas_fre_transmit_target_all.items():
                if self.count_timer_tcas_transmit % fre == 0:
                    target_index_list.append(target_index)
            num = 0
            target_tcas_index_list = []
            for target_index in target_index_list:
                relative_distance = float(self.findChild(QLineEdit, "txt_Relative_Distance_target" + str(target_index)).text())
                print(str(target_index)+'号目标机相对本机距离：'+ str(relative_distance))
                if relative_distance <= 18.52:# 当相对本机位置小于18.52km时，开始发送TCAS数据
                    target_tcas_index_list.append(target_index)
                    num +=1
            # 开始打包TCAS数据
            if num > 0:
                lock = threading.Lock()
                lock.acquire()
                logging.info("开始打包" + str(num) + "个目标机TCAS数据....")
                print("开始打包" + str(num) + "个目标机TCAS数据....")
                ArrayType = TCAS_Data_Struct * num
                array = ArrayType()
                j = 0
                for target_index in target_tcas_index_list:
                    tcas_data_struct = TCAS_Data_Struct()
                    tcas_data_struct.Track_ID = self.data_targetship[target_index]['TCAS']['Track_ID']
                    tcas_data_struct.Flight_24bit_addr = self.data_targetship[target_index]['TCAS']['Flight_24bit_addr_TCAS']
                    tcas_data_struct.Altitude = self.data_targetship[target_index]['TCAS']['Altitude_TCAS']
                    tcas_data_struct.Vertical_Speed = self.data_targetship[target_index]['TCAS']['Vertical_Speed_TCAS']
                    tcas_data_struct.Bearing = c_float(self.ga.degTorad(float(self.findChild(QLineEdit, "txt_Relative_Direction_target" + str(target_index)).text())))  # 单位弧度#
                    tcas_data_struct.Range = c_float(float(self.findChild(QLineEdit, "txt_Relative_Distance_target" + str(target_index)).text())*1000) #相对本机距离 单位m
                    tcas_data_struct.Warning_Status = self.data_targetship[target_index]['TCAS']['Warning_Status']
                    tcas_data_struct.Seconds = c_uint8(int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[-1]))  #
                    tcas_data_struct.Mintes = c_uint8(int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[1]))  #
                    tcas_data_struct.Hours = c_uint8(int(datetime.datetime.now().strftime('%H:%M:%S').split(':')[0]))  #
                    tcas_data_struct.p_Seconds = 0  #
                    tcas_data_struct.p_Mintes = 0  #
                    tcas_data_struct.p_Hours = 0 #
                    tcas_data_struct.v_Seconds = 0
                    tcas_data_struct.v_Mintes = 0
                    tcas_data_struct.v_Hours = 0
                    tcas_data_struct.s_Seconds = 0
                    tcas_data_struct.s_Mintes = 0
                    tcas_data_struct.s_Hours = 0
                    array[j] = tcas_data_struct
                    j+=1
                temp_byte = bytes(2048)
                print('目标机TCAS数据打包长度：' + str(self.dll.Pack_TCAS_data(array,num, temp_byte, 2048)))
                logging.info('目标机TCAS数据打包长度：' + str(self.dll.Pack_TCAS_data(array,num, temp_byte, 2048)))
                print(temp_byte.strip(b'\x00'))
                # UDP发送数据
               # self.socket_tcas.sendto(temp_byte.strip(b'\x00'), self.ip_port_tcas)
                logging.info("目标机发送ADS-B数据：" + str(temp_byte.strip(b'\x00')))
                lock.release()
            self.count_timer_tcas_transmit += 1
        except:
            traceback.print_exc()

    def update_time(self):
        current_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time_label.setText(current_Time)


if __name__=='__main__':
    app = QApplication(sys.argv)
    logging.basicConfig(filename='own_data.log', format='%(asctime)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',level=logging.INFO)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
