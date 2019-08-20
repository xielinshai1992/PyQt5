import sys
import os
import datetime
import traceback
from ctypes import *
import threading
import yaml
import time
import logging
import adsb_mainForm
from math import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from math import radians, cos, sin, asin, sqrt
from geography_analysis import Geography_Analysis
from c_api import init_ownship_data_struct

class MainWindow(QMainWindow):
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
        self.ui.btn_start.clicked.connect(self.start_takeoff)
        self.ui.btn_stop.clicked.connect(self.stop_transmitInfo)
        self.count_own = 0    # 本机定时器计数
        self.count_target = 0  # 目标机定时器计数
        self.ga = Geography_Analysis()

        #本机信息
        self.data_ownship = {}                  # 本机数据
        self.voyage_distance_ownship_list = []  # 本机航路距离列表 N个航路点有N-1条航路
        self.voyage_time_ownship_list = []      # 本机航路时间列表
        self.groundspeed_ownship = 0            # 本机地速
        self.fre_transmit_ownship = 0           # 数据发送频率 单位s
        self.delay_takeoff_ownship = 0          # 起飞延迟 单位ms
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
        self.fre_transmit_adsb_targetship_all  = []      # ADS-B数据发送频率 单位s
        self.delay_takeoff_targetship_all  = []          # 起飞延迟 单位ms
        self.Heading_Track_Angle_target_all = []  # 航向角序列  嵌套序列
        self.V_SN_target_all= []                   # 南北速度序列    嵌套序列
        self.V_EW_target_all = []                  # 东西速度序列    嵌套序列
        self.lng_target_all = []                   # 经度序列        嵌套序列
        self.lat_target_all = []                   # 纬度序列        嵌套序列
        self.lngandlat_target_all = []              # 经纬度序列      嵌套序列
        #TCAS数据
        self.tcas_enable_target_all = []            # TCAS使能序列   嵌套序列
        self.tcas_fre_transmit_target_all = []      # TCAS数据发送频率 嵌套序列

        self.ui.btn_test.clicked.connect(self.refresh_map)


    def refresh_map(self,flag):
        try:
            if self.data_ownship['basic']['Way_Point']:
                hanglu_own = self.data_ownship['basic']['Way_Point']
                speed_own = self.data_ownship['basic']['Ground_Speed']
                hanglu_own_list = [] #本机航路序列
                for i in range(1,len(hanglu_own)+1):
                    lng = hanglu_own['point'+str(i)][1]
                    lat = hanglu_own['point'+str(i)][2]
                    hanglu_own_list.append([lng,lat])
                js_string_own_init = '''init_ownship(%f,%f,'%s',%s,%d);'''%(hanglu_own['point1'][1],hanglu_own['point1'][2],self.data_ownship['basic']['Flight_ID'],hanglu_own_list,speed_own*100)
                print(js_string_own_init)
                self.browser.page().runJavaScript(js_string_own_init) #初始化本机位置、标注、航线、移动

            for target_index, info in self.data_targetship.items():
                hanglu_target = info['basic']['Way_Point']
                speed_target = info['basic']['Ground_Speed']
                hanglu_target_list = []  # 单个target机航路序列
                for i in range(1, len(hanglu_target) + 1):
                    lng = hanglu_target['point' + str(i)][1]
                    lat = hanglu_target['point' + str(i)][2]
                    hanglu_target_list.append([lng, lat])
                js_string_target_init = '''init_target(%f,%f,'%s',%s,%d);''' % (hanglu_target['point1'][1], hanglu_target['point1'][2], info['basic']['Flight_ID'], hanglu_target_list, speed_target*100)
                print(js_string_target_init)
                self.browser.page().runJavaScript(js_string_target_init)
        except:
            traceback.print_exc()

    # 本机信息区域
    def import_info_own(self):
        '''
        导入本机配置文件信息并解析
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
                    self.voyage_distance_ownship_list.append(voyage_distance)
                    self.voyage_time_ownship_list.append(int(voyage_distance/self.groundspeed_ownship * 3600))
                    interpolation_num = int(voyage_distance/self.groundspeed_ownship * 3600 /self.fre_transmit_ownship)
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
            # print(len(self.Heading_Track_Angle_own_list))
            # print(len(self.V_EW_own_list))
            # print(len(self.V_SN_own_list))
            # print(len(self.lngandlat_own_list))
            # print(len(self.lng_own_list))
        except:
            traceback.print_exc()

    # 目标机信息区域
    def import_info_target(self):
        current_targetship_index = self.ui.tabWidget.currentIndex()+1
        try:
            filename,_type = QFileDialog.getOpenFileName(self, '导入目标机信息', '','yaml(*.yaml)')
            if filename:
                with open(filename,'r',encoding='utf-8') as f:
                    file_data = f.read()
                    data_targetship = yaml.load(file_data)
                if data_targetship:
                    self.data_targetship[current_targetship_index] = data_targetship
                    self.findChild(QLineEdit, "txt_ICAO_target"+str(current_targetship_index)).setText(data_targetship['basic']['ICAO'])
                    self.findChild(QLineEdit, "txt_FlightID_target" + str(current_targetship_index)).setText(data_targetship['basic']['Flight_ID'])
                    self.findChild(QLineEdit, "txt_Altitude_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Altitude']))
                    self.findChild(QLineEdit, "txt_V_SN_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['North_South_Velocity']))
                    self.findChild(QLineEdit, "txt_V_EW_target"+ str(current_targetship_index)).setText(str(data_targetship['basic']['East_West_Velocity']))
                    self.findChild(QLineEdit, "txt_Latitude_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Way_Point']['point1'][2]))
                    self.findChild(QLineEdit, "txt_Longitude_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Way_Point']['point1'][1]))
                    self.findChild(QLineEdit, "txt_Heading_Track_Angle_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Way_Point']['point1'][3]))
                    self.findChild(QLineEdit, "txt_GroundSpeed_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Ground_Speed']))
                    self.findChild(QLineEdit, "txt_Track_ID_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Track_ID']))
                    self.findChild(QLineEdit, "txt_Tcas_Altitude_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Altitude_TCAS']))
                    self.findChild(QLineEdit, "txt_Relative_Direction_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Bearing']))
                    self.findChild(QLineEdit, "txt_Relative_Distance_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Range']))
                    fre_transmit_targetship = data_targetship['extra']['fre_transmit_adsb']
                    self.fre_transmit_adsb_targetship_all.append(fre_transmit_targetship)
                    self.delay_takeoff_targetship_all.append(data_targetship['extra']['delay_time'])
                    groundspeed_targetship = data_targetship['basic']['Ground_Speed']
                    self.groundspeed_targetship_all.append(groundspeed_targetship)
                    tcas_enable = data_targetship['extra']['TCAS']['enable']
                    tcas_transmit_fre = data_targetship['extra']['TCAS']['fre_transmit_tcas']

                    voyage_distance_targetship_list = [] #单个目标机航程距离序列
                    voyage_time_targetship_list = []   #单个目标机航程时间序列
                    lngandlat_own_list = []            #单个目标机航迹经纬度序列
                    V_EW_own_list = []                #单个目标机东西速度序列
                    V_SN_own_list = []                #单个目标机南北速度序列
                    Heading_Track_Angle_own_list = []  #单个目标机航向角序列
                    lng_own_list = []                  #单个目标机经度系列
                    lat_own_list =[]                   #单个目标机纬度系列

                    for i in range(1, len(data_targetship['basic']['Way_Point'])):
                        lng1 = data_targetship['basic']['Way_Point']['point'+str(i)][1]
                        lat1 = data_targetship['basic']['Way_Point']['point'+str(i)][2]
                        lng2 = data_targetship['basic']['Way_Point']['point'+str(i+1)][1]
                        lat2 = data_targetship['basic']['Way_Point']['point'+str(i+1)][2]
                        Heading_Track_Angle2 = data_targetship['basic']['Way_Point']['point'+str(i+1)][3]
                        voyage_distance = self.ga.geodistance(lng1,lat1,lng2,lat2)
                        voyage_distance_targetship_list.append(voyage_distance)
                        voyage_time_targetship_list.append(int(voyage_distance/groundspeed_targetship * 3600))
                        interpolation_num = int(voyage_distance/groundspeed_targetship * 3600 /fre_transmit_targetship)
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
                    self.Heading_Track_Angle_target_all.append(Heading_Track_Angle_own_list)
                    self.V_SN_target_all.append(V_SN_own_list)
                    self.V_EW_target_all.append(V_EW_own_list)
                    self.lngandlat_target_all.append(lngandlat_own_list)
                    self.lng_target_all.append(lng_own_list)
                    self.lat_target_all.append(lat_own_list)
                    self.tcas_enable_target_all.append(tcas_enable)
                    self.tcas_fre_transmit_target_all.append(tcas_transmit_fre)

        except:
            traceback.print_exc()

    def add_new_tab(self):
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
            label_Relative_Direction = QLabel('相对本机方位：',layout_tcas)
            label_Relative_Direction.setMaximumSize(QSize(16777215, 16777214))
            gridLayout_tcas.addWidget(label_Relative_Direction, 2, 1, 1, 1)
            lineEdit_Relative_Direction = QLineEdit(layout_tcas)
            lineEdit_Relative_Direction.setEnabled(False)
            lineEdit_Relative_Direction.setObjectName("txt_Relative_Direction_target"+str(target_plane_index))
            gridLayout_tcas.addWidget(lineEdit_Relative_Direction, 2, 2, 1, 1)
            #相对本机距离
            label_Relative_Distance = QLabel('相对本机距离：',layout_tcas)
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
        try:
            if self.ui.tabWidget.count() == 1:  #如果当前标签页只剩下一个则不关闭
                QMessageBox.information(self, '提示', '请保留至少一个目标机!', QMessageBox.Ok)
                return
            if self.ui.tabWidget.count() == int+1:  #仅在用户点击最后一个标签页时关闭
                self.ui.tabWidget.removeTab(int)
                self.findChild(QFrame, 'frame_target' + str(int + 1)).deleteLater()
                del self.data_targetship[self.ui.tabWidget.count()]
            else:
                QMessageBox.information(self, '提示', '请先关闭高序列目标机!', QMessageBox.Ok)
        except:
            traceback.print_exc()
    # 控制台区域
    def start_takeoff(self):
        try:
            #TODO：界面检查,确定目标机数量
            if len(self.data_targetship) == self.ui.tabWidget.count() and self.data_ownship:
                self.ui.btn_start.setEnabled(False)
                self.ui.btn_stop.setEnabled(True)
                self.ui.btn_import_info_own.setEnabled(False)
                #本机准备起飞，发送数据
                #time.sleep(self.delay_takeoff_ownship)  #起飞延迟设置

                print('本机起飞,开始发送数据...')
                logging.info('本机起飞,开始发送数据...')
                print('本机数据发送周期：'+str(self.fre_transmit_ownship)+'s')
                logging.info('本机数据发送周期：'+str(self.fre_transmit_ownship)+'s')
                own_timer = QTimer(self)
                own_timer.setObjectName('own_timer')
                own_timer.timeout.connect(self.show_own_info)
                own_timer.start(self.fre_transmit_ownship *1000)

                #目标机准备起飞，发送数据
                print('目标机起飞,开始发送数据...')
                logging.info('目标机起飞,开始发送数据...')
                self.num_targetship = self.ui.tabWidget.count()
                print('目标机数量： '+str(self.num_targetship))
                logging.info('目标机数量： '+str(self.num_targetship))
                # TODO:定时更新地图、经纬度等参数;打包数据，调用C接口
                for i in range(len(self.fre_transmit_adsb_targetship_all)):
                    self.findChild(QPushButton,'btn_import_info_target'+str(i+1)).setEnabled(False)
                    target_timer = QTimer(self)
                    target_timer.setObjectName('target_timer'+str(i+1))
                    target_timer.setProperty('target_num',i+1)
                    target_timer.timeout.connect(self.show_target_info)
                    target_timer.start(self.fre_transmit_adsb_targetship_all[i]*1000)
                    print(str(i+1)+'号目标机，TCAS数据发送周期：'+str(self.fre_transmit_adsb_targetship_all[i])+'s')
                    logging.info(str(i+1)+'号目标机，TCAS数据发送周期：'+str(self.fre_transmit_adsb_targetship_all[i])+'s')
            else:
                QMessageBox.information(self, '提示', '请检查界面参数是否齐全!', QMessageBox.Ok)
        except:
            traceback.print_exc()

    def stop_transmitInfo(self):
        try:
            #关闭所有定时器, button使能复原

            self.count_own = 0  # 本机定时器计数
            self.count_target = 0  # 目标机定时器计数
            self.findChild(QTimer,'own_timer').stop()
            self.findChild(QTimer,'own_timer').deleteLater()
            self.ui.btn_start.setEnabled(True)
            self.ui.btn_import_info_own.setEnabled(True)
            for i in range(1,self.num_targetship+1):
                print(i)
                self.findChild(QTimer,'target_timer'+str(i)).stop()
                self.findChild(QTimer,'target_timer'+str(i)).deleteLater()
                self.findChild(QPushButton,'btn_import_info_target'+str(i)).setEnabled(True)
            self.ui.btn_stop.setEnabled(False)
        except:
            traceback.print_exc()

    def show_own_info(self):
        '''显示本机信息'''
        try:
            lock = threading.Lock()
            self.ui.txt_Heading_Track_Angle_own.setText(str(self.Heading_Track_Angle_own_list[self.count_own]))
            self.ui.txt_Longitude_own.setText(str(self.lng_own_list[self.count_own]))
            self.ui.txt_Latitude_own.setText(str(self.lat_own_list[self.count_own]))
            self.ui.txt_V_EW_own.setText(str(self.V_EW_own_list[self.count_own]))
            self.ui.txt_V_SN_own.setText(str(self.V_SN_own_list[self.count_own]))
            self.count_own+=1
            lock.acquire()
            logging.info("本机当前经度："   + str(self.lng_own_list[self.count_own]))
            logging.info("本机当前纬度："   + str(self.lat_own_list[self.count_own]))
            logging.info("本机南北速度：" + str(self.V_SN_own_list[self.count_own]))
            logging.info("本机东西速度：" + str(self.V_EW_own_list[self.count_own]))
            logging.info("本机航向角：" + str(self.Heading_Track_Angle_own_list[self.count_own]))
            lock.release()
        except:
            traceback.print_exc()

    def show_target_info(self):
        '''
        显示目标机信息
        :return:
        '''
        try:
            sender = self.sender()
            target_num = sender.property('target_num')
            self.findChild(QLineEdit, "txt_Heading_Track_Angle_target" + str(target_num)).setText(str(self.Heading_Track_Angle_target_all[target_num-1][self.count_target]))
            self.findChild(QLineEdit, "txt_Longitude_target" + str(target_num)).setText(str(self.lng_target_all[target_num - 1][self.count_target]))
            self.findChild(QLineEdit, "txt_Latitude_target" + str(target_num)).setText(str(self.lat_target_all[target_num - 1][self.count_target]))
            self.findChild(QLineEdit, "txt_V_EW_target" + str(target_num)).setText(str(self.V_EW_target_all[target_num - 1][self.count_target]))
            self.findChild(QLineEdit, "txt_V_SN_target" + str(target_num)).setText(str(self.V_SN_target_all[target_num - 1][self.count_target]))
            self.count_target+=1
            lock = threading.Lock()
            lock.acquire()
            logging.info(str(target_num)+"号目标机当前经度："   + str(self.lng_target_all[target_num - 1][self.count_target]))
            logging.info(str(target_num)+"号目标机当前纬度："   + str(self.lat_target_all[target_num - 1][self.count_target]))
            logging.info(str(target_num)+"号目标机南北速度：" + str(self.V_SN_target_all[target_num - 1][self.count_target]))
            logging.info(str(target_num)+"号目标机东西速度：" + str(self.V_EW_target_all[target_num - 1][self.count_target]))
            logging.info(str(target_num)+"号目标机航向角：" + str(self.Heading_Track_Angle_target_all[target_num-1][self.count_target]))
            lock.release()
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
