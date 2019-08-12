import sys
import os
import datetime
import traceback
import yaml
import time
import adsb_mainForm
from math import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from math import radians, cos, sin, asin, sqrt
from geography_analysis import Geography_Analysis
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = adsb_mainForm.Ui_MainWindow()
        self.ui.setupUi(self)
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
        self.data_ownship    = {}    #本机数据
        self.voyage_distance_ownship_list = []    #本机航路距离列表 N个航路点有N-1条航路
        self.voyage_time_ownship_list = []    # 本机航路时间列表
        self.groundspeed_ownship = 0   #本机地速
        self.fre_transmit_ownship = 0  #数据发送频率 单位s
        self.delay_takeoff = 0   #起飞延迟 单位ms
        self.count = 0

        self.Heading_Track_Angle_own_list = []#本机航向角序列
        self.V_SN_own_list = [] #南北速度序列
        self.V_EW_own_list = [] #东西速度序列
        self.lng_own_list = [] #经度序列
        self.lat_own_list = [] #纬度序列
        self.lngandlat_own_list = [] #经纬度序列

    # 本机信息区域
    def import_info_own(self):
        try:
            ga = Geography_Analysis()
            filename,_type = QFileDialog.getOpenFileName(self, '导入本机信息', '','yaml(*.yaml)')
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
                self.delay_takeoff = self.data_ownship['extra']['delay_time']

            for i in range(1, len(self.data_ownship['basic']['Way_Point'])):
                lng1 = self.data_ownship['basic']['Way_Point']['point'+str(i)][1]
                lat1 = self.data_ownship['basic']['Way_Point']['point'+str(i)][2]
                lng2 = self.data_ownship['basic']['Way_Point']['point'+str(i+1)][1]
                lat2 = self.data_ownship['basic']['Way_Point']['point'+str(i+1)][2]
                Heading_Track_Angle2 = self.data_ownship['basic']['Way_Point']['point'+str(i+1)][3]
                voyage_distance = self.geodistance(lng1,lat1,lng2,lat2)
                self.voyage_distance_ownship_list.append(voyage_distance)
                self.voyage_time_ownship_list.append(int(voyage_distance/self.groundspeed_ownship * 3600))
                interpolation_num = int(voyage_distance/self.groundspeed_ownship * 3600 /self.fre_transmit_ownship)
                interpolation_dis = [voyage_distance/interpolation_num * x for x in range(1,interpolation_num+1)]
                self.lngandlat_own_list += [ga.get_lngAndlat(lng1,lat1,Heading_Track_Angle2,x) for x in interpolation_dis]
                V_SN = round(self.groundspeed_ownship * cos(Heading_Track_Angle2 * pi / 180.0), 3)
                V_EW = round(self.groundspeed_ownship * sin(Heading_Track_Angle2 * pi / 180.0), 3)
                self.V_EW_own_list += [V_EW]*interpolation_num
                self.V_SN_own_list += [V_SN]*interpolation_num
                self.Heading_Track_Angle_own_list += [Heading_Track_Angle2] * interpolation_num
            for item in self.lngandlat_own_list:
                self.lng_own_list.append(item[0])
                self.lat_own_list.append(item[1])
            print(self.voyage_distance_ownship_list)
            print(self.voyage_time_ownship_list)  #单位s
            print(self.Heading_Track_Angle_own_list)
            print(len(self.Heading_Track_Angle_own_list))
            print(len(self.V_EW_own_list))
            print(len(self.V_SN_own_list))
            print(len(self.lngandlat_own_list))
            print(len(self.lng_own_list))
        except:
            traceback.print_exc()

    # 目标机信息区域
    def import_info_target(self):
        current_targetship_index = self.ui.tabWidget.currentIndex()+1
        print(current_targetship_index)
        try:
            filename,_type = QFileDialog.getOpenFileName(self, '导入目标机信息', '','yaml(*.yaml)')
            with open(filename,'r',encoding='utf-8') as f:
                file_data = f.read()
                data_targetship = yaml.load(file_data)
            if data_targetship:
                self.findChild(QLineEdit,"txt_ICAO_target"+str(current_targetship_index)).setText(data_targetship['basic']['ICAO'])
                self.findChild(QLineEdit, "txt_FlightID_target" + str(current_targetship_index)).setText(data_targetship['basic']['Flight_ID'])
                self.findChild(QLineEdit, "txt_Altitude_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Altitude']))
                self.findChild(QLineEdit, "txt_V_SN_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['North_South_Velocity']))
                self.findChild(QLineEdit, "txt_V_EW_target"+ str(current_targetship_index)).setText(str(data_targetship['basic']['East_West_Velocity']))
                self.findChild(QLineEdit, "txt_Latitude_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Way_Point']['point1'][2]))
                self.findChild(QLineEdit, "txt_Longitude_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Way_Point']['point1'][1]))
                self.findChild(QLineEdit, "txt_Heading_Track_Angle_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Way_Point']['point1'][3]))
                self.findChild(QLineEdit, "txt_GroundSpeed_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Ground_Speed']))
                self.findChild(QLineEdit, "txt_Track_ID_target" + str(current_targetship_index)).setText(str(data_targetship['basic']['Track_ID']))
                self.findChild(QLineEdit, "txt_Tcas_Altitude_target" + str(current_targetship_index)).setText(
                    str(data_targetship['basic']['Altitude_TCAS']))
                self.findChild(QLineEdit, "txt_Relative_Direction_target" + str(current_targetship_index)).setText(
                    str(data_targetship['basic']['Bearing']))
                self.findChild(QLineEdit, "txt_Relative_Distance_target" + str(current_targetship_index)).setText(
                    str(data_targetship['basic']['Range']))

        except:
            traceback.print_exc()

    def add_new_tab(self):
        try:
            target_plane_index = self.ui.tabWidget.count()+1
            frame_copy = QFrame()
            btn_import_info_target = QPushButton(frame_copy)
            #btn_import_info_target.setObjectName('btn_import_info_target'+str(target_plane_index))
            btn_import_info_target.setText('导入飞机信息')
            btn_import_info_target.setGeometry(QRect(10, 15, 241, 28))
            btn_import_info_target.clicked.connect(self.import_info_target)

            # ADS-B布局
            groupBox_adsb = QGroupBox(frame_copy)
            groupBox_adsb.setTitle('ADS-B')
            groupBox_adsb.setGeometry(QRect(10, 50, 281, 361))

            layout_adsb = QWidget(groupBox_adsb)
            layout_adsb.setGeometry(QRect(0, 30, 271, 331))
            gridLayout_adsb = QGridLayout(layout_adsb)
            gridLayout_adsb.setContentsMargins(0, 0, 0, 0)
            # ICAO码
            label_ICAO = QLabel('ICAO码：',layout_adsb)
            label_ICAO.setMaximumSize(QSize(90, 16777215))
            label_ICAO.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_ICAO, 0, 1, 1, 1)
            lineEdit_ICAO = QLineEdit(layout_adsb)
            lineEdit_ICAO.setMaximumSize(QSize(150, 16777215))
            lineEdit_ICAO.setObjectName("txt_ICAO_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_ICAO, 0, 2, 1, 1)
            # 航班号
            label_Flight_No = QLabel('航班号：',layout_adsb)
            label_Flight_No.setMaximumSize(QSize(90, 16777215))
            label_Flight_No.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Flight_No, 1, 1, 1, 1)
            lineEdit_Flight_No = QLineEdit(layout_adsb)
            lineEdit_Flight_No.setMaximumSize(QSize(150, 16777215))
            lineEdit_Flight_No.setObjectName("txt_FlightID_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Flight_No, 1, 2, 1, 1)
            #压强高度
            label_Press_Height = QLabel('压强高度：',layout_adsb)
            label_Press_Height.setMaximumSize(QSize(90, 16777215))
            label_Press_Height.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Press_Height, 2, 1, 1, 1)
            lineEdit_Press_Height = QLineEdit(layout_adsb)
            lineEdit_Press_Height.setMaximumSize(QSize(150, 16777215))
            lineEdit_Press_Height.setObjectName("txt_Altitude_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Press_Height, 2, 2, 1, 1)
            #南北速度
            label_V_SN= QLabel('南北速度：',layout_adsb)
            label_V_SN.setMaximumSize(QSize(90, 16777215))
            label_V_SN.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_V_SN, 3, 1, 1, 1)
            lineEdit_V_SN = QLineEdit(layout_adsb)
            lineEdit_V_SN.setMaximumSize(QSize(150, 16777215))
            lineEdit_V_SN.setObjectName("txt_V_SN_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_V_SN, 3, 2, 1, 1)
            #东西速度
            label_V_EW= QLabel('东西速度：',layout_adsb)
            label_V_EW.setMaximumSize(QSize(90, 16777215))
            label_V_EW.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_V_EW, 4, 1, 1, 1)
            lineEdit_V_EW = QLineEdit(layout_adsb)
            lineEdit_V_EW.setMaximumSize(QSize(150, 16777215))
            lineEdit_V_EW.setObjectName("txt_V_EW_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_V_EW, 4, 2, 1, 1)
            #纬度
            label_Latitude= QLabel('纬度：',layout_adsb)
            label_Latitude.setMaximumSize(QSize(90, 16777215))
            label_Latitude.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Latitude, 5, 1, 1, 1)
            lineEdit_Latitude = QLineEdit(layout_adsb)
            lineEdit_Latitude.setMaximumSize(QSize(150, 16777215))
            lineEdit_Latitude.setObjectName("txt_Latitude_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Latitude, 5, 2, 1, 1)
            #经度
            label_Longitude= QLabel('纬度：',layout_adsb)
            label_Longitude.setMaximumSize(QSize(90, 16777215))
            label_Longitude.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Longitude, 6, 1, 1, 1)
            lineEdit_Longitude = QLineEdit(layout_adsb)
            lineEdit_Longitude.setMaximumSize(QSize(150, 16777215))
            lineEdit_Longitude.setObjectName("txt_Longitude_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Longitude, 6, 2, 1, 1)
            #航向角
            label_Heading_Track_Angle= QLabel('航向角：',layout_adsb)
            label_Heading_Track_Angle.setMaximumSize(QSize(90, 16777215))
            label_Heading_Track_Angle.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Heading_Track_Angle, 7, 1, 1, 1)
            lineEdit_Heading_Track_Angle = QLineEdit(layout_adsb)
            lineEdit_Heading_Track_Angle.setMaximumSize(QSize(150, 16777215))
            lineEdit_Heading_Track_Angle.setObjectName("txt_Heading_Track_Angle_target"+str(target_plane_index))
            gridLayout_adsb.addWidget(lineEdit_Heading_Track_Angle, 7, 2, 1, 1)
            #地速
            label_Ground_Speed= QLabel('地速：',layout_adsb)
            label_Ground_Speed.setMaximumSize(QSize(90, 16777215))
            label_Ground_Speed.setAlignment(Qt.AlignLeading |Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout_adsb.addWidget(label_Ground_Speed, 8, 1, 1, 1)
            lineEdit_Ground_Speed = QLineEdit(layout_adsb)
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
            groupBox_tcas.setGeometry(QRect(300, 50, 271, 361))
            layout_tcas = QWidget(groupBox_tcas)
            layout_tcas.setGeometry(QRect(10, 30, 251, 301))
            gridLayout_tcas = QGridLayout(layout_tcas)
            gridLayout_tcas.setContentsMargins(0, 0, 0, 0)
            #Track_ID
            label_Track_ID= QLabel('Track_ID：',layout_tcas)
            gridLayout_tcas.addWidget(label_Track_ID, 0, 1, 1, 1)
            lineEdit_Track_ID = QLineEdit(layout_tcas)
            lineEdit_Track_ID.setObjectName("txt_Track_ID_target"+str(target_plane_index))
            gridLayout_tcas.addWidget(lineEdit_Track_ID, 0, 2, 1, 1)
            #压强高度
            label_Press_Height_TCAS = QLabel('压强高度：',layout_tcas)
            gridLayout_tcas.addWidget(label_Press_Height_TCAS, 1, 1, 1, 1)
            lineEdit_Press_Height_TCAS = QLineEdit(layout_tcas)
            lineEdit_Press_Height_TCAS.setObjectName("txt_Tcas_Altitude_target"+str(target_plane_index))
            gridLayout_tcas.addWidget(lineEdit_Press_Height_TCAS, 1, 2, 1, 1)
            #相对本机方位
            label_Relative_Direction = QLabel('相对本机方位：',layout_tcas)
            gridLayout_tcas.addWidget(label_Relative_Direction, 2, 1, 1, 1)
            lineEdit_Relative_Direction = QLineEdit(layout_tcas)
            lineEdit_Relative_Direction.setObjectName("txt_Relative_Direction_target"+str(target_plane_index))
            gridLayout_tcas.addWidget(lineEdit_Relative_Direction, 2, 2, 1, 1)
            #相对本机距离
            label_Relative_Distance = QLabel('相对本机距离：',layout_tcas)
            gridLayout_tcas.addWidget(label_Relative_Distance, 3, 1, 1, 1)
            lineEdit_Relative_Distance = QLineEdit(layout_tcas)
            lineEdit_Relative_Distance.setObjectName("txt_Relative_Distance_target"+str(target_plane_index))
            gridLayout_tcas.addWidget(lineEdit_Relative_Distance, 3, 2, 1, 1)
            #"停止发送TCAS数据"button
            btn_stop_sending_tcas = QPushButton('停止发送TCAS数据', groupBox_tcas)



            btn_stop_sending_tcas.setGeometry(QRect(8, 329, 249, 28))
            btn_stop_sending_tcas.setObjectName("btn_stopsend_tcas_target"+str(target_plane_index))

            i = self.ui.tabWidget.addTab(frame_copy,  str(target_plane_index)+'号目标机')
            self.ui.tabWidget.setCurrentIndex(i)
        except:
            traceback.print_exc()

    def close_current_tab(self,int):
        # 如果当前标签页只剩下一个则不关闭
        if self.ui.tabWidget.count() < 2:
            QMessageBox.information(self,'提示','请保留至少一个目标机!',QMessageBox.Ok)
            return
        self.ui.tabWidget.removeTab(int)

    # 控制台区域
    def start_takeoff(self):
        #TODO:定时更新地图、经纬度等参数
        self.timer_transmit = QTimer(self)
        self.timer_transmit.timeout.connect(self.operate)
        # self.timer_transmit.singleShot(12000,self.end_operate)
        self.timer_transmit.start(1000)
        #TODO:打包数据，调用C接口


    def operate(self):
        try:
            self.ui.txt_Heading_Track_Angle_own.setText(str(self.Heading_Track_Angle_own_list[self.count]))
            self.ui.txt_Longitude_own.setText(str(self.lng_own_list[self.count]))
            self.ui.txt_Latitude_own.setText(str(self.lat_own_list[self.count]))
            self.ui.txt_V_EW_own.setText(str(self.V_EW_own_list[self.count]))
            self.ui.txt_V_SN_own.setText(str(self.V_SN_own_list[self.count]))
            self.count+=1
        except:
            traceback.print_exc()

    def end_operate(self):
        self.timer_transmit.stop()


    def update_time(self):
        current_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time_label.setText(current_Time)

    def geodistance(self,lng1,lat1,lng2,lat2):
        '''
        根据两点的经纬度计算地理距离
        :param lng1: 1号点经度
        :param lat1: 1号点纬度
        :param lng2: 2号点经度
        :param lat2: 2号点纬度
        :return: 两点的地理距离
        '''
        lng1,lat1,lng2,lat2 = map(radians,[float(lng1), float(lat1), float(lng2), float(lat2)])# 经纬度转换成弧度
        dlon = lng2-lng1
        dlat = lat2-lat1
        a = sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
        c = 2*asin(sqrt(a))*6371 # 地球平均半径，6371km
        distance = round(c , 3)
        return distance



if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
