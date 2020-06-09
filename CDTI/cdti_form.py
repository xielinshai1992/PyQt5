import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import*
import cdti_mainform
import socket
import datetime
from a661_api import *

class Receive_661_DataThread(QThread):
    signal_a = pyqtSignal(list)
    def __init__(self):
        super(Receive_661_DataThread, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("127.0.0.1", 8001))  # 绑定服务器的ip和端口

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
            receive_Info.append(
                [receive_Data.Airport_Map_PARAMATER.WidgetIdent, receive_Data.Airport_Map_PARAMATER.ParameterIdent,
                 receive_Data.Airport_Map_PARAMATER.ParameterValueBuffer])
            # air1
            receive_Info.append(
                [receive_Data.Target1_Visible_PARAMATER.WidgetIdent, receive_Data.Target1_Visible_PARAMATER.ParameterIdent,
                 receive_Data.Target1_Visible_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target1_Pic_PARAMATER.WidgetIdent, receive_Data.Target1_Pic_PARAMATER.ParameterIdent,
                 receive_Data.Target1_Pic_PARAMATER.ParameterValueBuffer])

            receive_Info.append([receive_Data.Target1_RotateAngle_PARAMATER.WidgetIdent,
                                 receive_Data.Target1_RotateAngle_PARAMATER.ParameterIdent,
                                 receive_Data.Target1_RotateAngle_PARAMATER.ParameterValueBuffer
                                 ])
            receive_Info.append(
                [receive_Data.Target1_X_PARAMATER.WidgetIdent, receive_Data.Target1_X_PARAMATER.ParameterIdent,
                 receive_Data.Target1_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target1_Y_PARAMATER.WidgetIdent, receive_Data.Target1_Y_PARAMATER.ParameterIdent,
                 receive_Data.Target1_Y_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target1_FlightId_PARAMATER.WidgetIdent,
                                 receive_Data.Target1_FlightId_PARAMATER.ParameterIdent,
                                 receive_Data.Target1_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target1_Speed_PARAMATER.WidgetIdent, receive_Data.Target1_Speed_PARAMATER.ParameterIdent,
                 receive_Data.Target1_Speed_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target1_Alt_dif_PARAMATER.WidgetIdent, receive_Data.Target1_Alt_dif_PARAMATER.ParameterIdent,
                 receive_Data.Target1_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target1_Status_PARAMATER.WidgetIdent, receive_Data.Target1_Status_PARAMATER.ParameterIdent,
                 receive_Data.Target1_Status_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target1_AppStatus_PARAMATER.WidgetIdent,
                                 receive_Data.Target1_AppStatus_PARAMATER.ParameterIdent,
                                 receive_Data.Target1_AppStatus_PARAMATER.ParameterValueBuffer])

            # air2
            receive_Info.append(
                [receive_Data.Target2_Visible_PARAMATER.WidgetIdent, receive_Data.Target2_Visible_PARAMATER.ParameterIdent,
                 receive_Data.Target2_Visible_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target2_Pic_PARAMATER.WidgetIdent, receive_Data.Target2_Pic_PARAMATER.ParameterIdent,
                 receive_Data.Target2_Pic_PARAMATER.ParameterValueBuffer])

            receive_Info.append([receive_Data.Target2_RotateAngle_PARAMATER.WidgetIdent,
                                 receive_Data.Target2_RotateAngle_PARAMATER.ParameterIdent,
                                 receive_Data.Target2_RotateAngle_PARAMATER.ParameterValueBuffer
                                 ])
            receive_Info.append(
                [receive_Data.Target2_X_PARAMATER.WidgetIdent, receive_Data.Target2_X_PARAMATER.ParameterIdent,
                 receive_Data.Target2_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target2_Y_PARAMATER.WidgetIdent, receive_Data.Target2_Y_PARAMATER.ParameterIdent,
                 receive_Data.Target2_Y_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target2_FlightId_PARAMATER.WidgetIdent,
                                 receive_Data.Target2_FlightId_PARAMATER.ParameterIdent,
                                 receive_Data.Target2_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target2_Speed_PARAMATER.WidgetIdent, receive_Data.Target2_Speed_PARAMATER.ParameterIdent,
                 receive_Data.Target2_Speed_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target2_Alt_dif_PARAMATER.WidgetIdent, receive_Data.Target2_Alt_dif_PARAMATER.ParameterIdent,
                 receive_Data.Target2_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target2_Status_PARAMATER.WidgetIdent, receive_Data.Target2_Status_PARAMATER.ParameterIdent,
                 receive_Data.Target2_Status_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target2_AppStatus_PARAMATER.WidgetIdent,
                                 receive_Data.Target2_AppStatus_PARAMATER.ParameterIdent,
                                 receive_Data.Target2_AppStatus_PARAMATER.ParameterValueBuffer])

            # air3
            receive_Info.append(
                [receive_Data.Target3_Visible_PARAMATER.WidgetIdent, receive_Data.Target3_Visible_PARAMATER.ParameterIdent,
                 receive_Data.Target3_Visible_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target3_Pic_PARAMATER.WidgetIdent, receive_Data.Target3_Pic_PARAMATER.ParameterIdent,
                 receive_Data.Target3_Pic_PARAMATER.ParameterValueBuffer])

            receive_Info.append([receive_Data.Target3_RotateAngle_PARAMATER.WidgetIdent,
                                 receive_Data.Target3_RotateAngle_PARAMATER.ParameterIdent,
                                 receive_Data.Target3_RotateAngle_PARAMATER.ParameterValueBuffer
                                 ])
            receive_Info.append(
                [receive_Data.Target3_X_PARAMATER.WidgetIdent, receive_Data.Target3_X_PARAMATER.ParameterIdent,
                 receive_Data.Target3_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target3_Y_PARAMATER.WidgetIdent, receive_Data.Target3_Y_PARAMATER.ParameterIdent,
                 receive_Data.Target3_Y_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target3_FlightId_PARAMATER.WidgetIdent,
                                 receive_Data.Target3_FlightId_PARAMATER.ParameterIdent,
                                 receive_Data.Target3_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target3_Speed_PARAMATER.WidgetIdent, receive_Data.Target3_Speed_PARAMATER.ParameterIdent,
                 receive_Data.Target3_Speed_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target3_Alt_dif_PARAMATER.WidgetIdent, receive_Data.Target3_Alt_dif_PARAMATER.ParameterIdent,
                 receive_Data.Target3_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target3_Status_PARAMATER.WidgetIdent, receive_Data.Target3_Status_PARAMATER.ParameterIdent,
                 receive_Data.Target3_Status_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target3_AppStatus_PARAMATER.WidgetIdent,
                                 receive_Data.Target3_AppStatus_PARAMATER.ParameterIdent,
                                 receive_Data.Target3_AppStatus_PARAMATER.ParameterValueBuffer])

            # air4
            receive_Info.append(
                [receive_Data.Target4_Visible_PARAMATER.WidgetIdent, receive_Data.Target4_Visible_PARAMATER.ParameterIdent,
                 receive_Data.Target4_Visible_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target4_Pic_PARAMATER.WidgetIdent, receive_Data.Target4_Pic_PARAMATER.ParameterIdent,
                 receive_Data.Target4_Pic_PARAMATER.ParameterValueBuffer])

            receive_Info.append([receive_Data.Target4_RotateAngle_PARAMATER.WidgetIdent,
                                 receive_Data.Target4_RotateAngle_PARAMATER.ParameterIdent,
                                 receive_Data.Target4_RotateAngle_PARAMATER.ParameterValueBuffer
                                 ])
            receive_Info.append(
                [receive_Data.Target4_X_PARAMATER.WidgetIdent, receive_Data.Target4_X_PARAMATER.ParameterIdent,
                 receive_Data.Target4_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target4_Y_PARAMATER.WidgetIdent, receive_Data.Target4_Y_PARAMATER.ParameterIdent,
                 receive_Data.Target4_Y_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target4_FlightId_PARAMATER.WidgetIdent,
                                 receive_Data.Target4_FlightId_PARAMATER.ParameterIdent,
                                 receive_Data.Target4_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target4_Speed_PARAMATER.WidgetIdent, receive_Data.Target4_Speed_PARAMATER.ParameterIdent,
                 receive_Data.Target4_Speed_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target4_Alt_dif_PARAMATER.WidgetIdent, receive_Data.Target4_Alt_dif_PARAMATER.ParameterIdent,
                 receive_Data.Target4_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target4_Status_PARAMATER.WidgetIdent, receive_Data.Target4_Status_PARAMATER.ParameterIdent,
                 receive_Data.Target4_Status_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target4_AppStatus_PARAMATER.WidgetIdent,
                                 receive_Data.Target4_AppStatus_PARAMATER.ParameterIdent,
                                 receive_Data.Target4_AppStatus_PARAMATER.ParameterValueBuffer])

            # air5
            receive_Info.append(
                [receive_Data.Target5_Visible_PARAMATER.WidgetIdent, receive_Data.Target5_Visible_PARAMATER.ParameterIdent,
                 receive_Data.Target5_Visible_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target5_Pic_PARAMATER.WidgetIdent, receive_Data.Target5_Pic_PARAMATER.ParameterIdent,
                 receive_Data.Target5_Pic_PARAMATER.ParameterValueBuffer])

            receive_Info.append([receive_Data.Target5_RotateAngle_PARAMATER.WidgetIdent,
                                 receive_Data.Target5_RotateAngle_PARAMATER.ParameterIdent,
                                 receive_Data.Target5_RotateAngle_PARAMATER.ParameterValueBuffer
                                 ])
            receive_Info.append(
                [receive_Data.Target5_X_PARAMATER.WidgetIdent, receive_Data.Target5_X_PARAMATER.ParameterIdent,
                 receive_Data.Target5_X_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target5_Y_PARAMATER.WidgetIdent, receive_Data.Target5_Y_PARAMATER.ParameterIdent,
                 receive_Data.Target5_Y_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target5_FlightId_PARAMATER.WidgetIdent,
                                 receive_Data.Target5_FlightId_PARAMATER.ParameterIdent,
                                 receive_Data.Target5_FlightId_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target5_Speed_PARAMATER.WidgetIdent, receive_Data.Target5_Speed_PARAMATER.ParameterIdent,
                 receive_Data.Target5_Speed_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append(
                [receive_Data.Target5_Alt_dif_PARAMATER.WidgetIdent, receive_Data.Target5_Alt_dif_PARAMATER.ParameterIdent,
                 receive_Data.Target5_Alt_dif_PARAMATER.ParameterValueBuffer])
            receive_Info.append(
                [receive_Data.Target5_Status_PARAMATER.WidgetIdent, receive_Data.Target5_Status_PARAMATER.ParameterIdent,
                 receive_Data.Target5_Status_PARAMATER.ParameterValueBuffer
                 ])
            receive_Info.append([receive_Data.Target5_AppStatus_PARAMATER.WidgetIdent,
                                 receive_Data.Target5_AppStatus_PARAMATER.ParameterIdent,
                                 receive_Data.Target5_AppStatus_PARAMATER.ParameterValueBuffer])
            self.signal_a.emit(receive_Info)



class MainWindow(QMainWindow):

    map_wigdetId = {0: 'surf_compass_bitmap', 1: 'surf_compass_step', 2: 'surf_ownship_id_txt', 3: 'surf_ownship_alt_txt', 4: 'surf_ownship_lon_txt', 5: 'surf_ownship_lat_txt', 6: 'surf_ownship_altrange_txt', 7: 'surf_ownship_angle_txt', 8: 'surf_ownship_applstatus_txt', 9: 'surf_airport_map', 11: 'surf_targetshow_bitmap1', 12: 'surf_target1_id_txt', 13: 'surf_target1_speed_txt', 14: 'surf_target1_altdif_txt', 15: 'surf_target1_airstatus_txt', 16: 'surf_target1_applstatus_bitmap', 21: 'surf_targetshow_bitmap2', 22: 'surf_target2_id_txt', 23: 'surf_target2_speed_txt', 24: 'surf_target2_altdif_txt', 25: 'surf_target2_airstatus_txt', 26: 'surf_target2_applstatus_bitmap', 31: 'surf_targetshow_bitmap3', 32: 'surf_target3_id_txt', 33: 'surf_target3_speed_txt', 34: 'surf_target3_altdif_txt', 35: 'surf_target3_airstatus_txt', 36: 'surf_target3_applstatus_bitmap', 41: 'surf_targetshow_bitmap4', 42: 'surf_target4_id_txt', 43: 'surf_target4_speed_txt', 44: 'surf_target4_altdif_txt', 45: 'surf_target4_airstatus_txt', 46: 'surf_target4_applstatus_bitmap', 51: 'surf_targetshow_bitmap5', 52: 'surf_target5_id_txt', 53: 'surf_target5_speed_txt', 54: 'surf_target5_altdif_txt', 55: 'surf_target5_airstatus_txt', 56: 'surf_target5_applstatus_bitmap'}

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
        self.initUI()
        #设置定时器 每50ms旋转一次
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.slotTimeout)
        #self.timer.start(1000)
        timer_a = QTimer(self)
        timer_a.timeout.connect(self.update_time)
        timer_a.start()
        self.myWorker = Receive_661_DataThread()
        self.myWorker.signal_a.connect(self.update_cdti_ui)
        self.myWorker.start()
        print("打开UDP通信端口，开始接收UA发送数据...")

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


    def slotTimeout(self):
        self.rotateAngle = (self.rotateAngle+5)%360
        self.count +=5
        self.map_widgetItem.setRotation(self.rotateAngle)
        self.airb_compass_Item.setRotation(self.rotateAngle)
        self.vsa_compass_Item.setRotation(self.rotateAngle)
        self.targetAir1_Item.setPos(0+self.count,0+self.count)
        self.surf_air1_text_Item.setPos(0 + self.count, 20 + self.count)
        #self.surf_compass_Item.setRotation(self.rotateAngle+45)


    def setQLabelVisible(self,widget_id,is_Visible):
        '''
        设置Qlabel控件是否可见
        :param widget_id: Qlabel控件id
        :param is_Visible:bool类型，true可见 false不可见
        :return:
        '''
        mywidget = self.findChild(QLabel,widget_id)
        if mywidget:
            mywidget.setVisible(is_Visible)
        pass


    def setQLabelText(self,widget_id,text_string):
        '''
        设置Qlabel控件文本
        :param widget_id:Qlabel控件id
        :param text_string:文本内容
        :return:
        '''
        mywidget = self.findChild(QLabel,widget_id)
        if mywidget:
            mywidget.setText(text_string)
        pass


    def setQLabelPicSource(self,widget_id,status_flag):
        '''
        设置QLabel图片源,代表本机应用可用状态
        :param widget_id:Qlabel控件id
        :return:status_flag:状态标识 1对应有效，0对应无效
        '''
        mywidget = self.findChild(QLabel,widget_id)
        if mywidget:
            if status_flag == 1:
                mywidget.setPixmap(QPixmap("pic/appstatus1.png"))
            else:
                mywidget.setPixmap(QPixmap("pic/appstatus2.png"))
        pass

    def initUI(self):
        self.ui = cdti_mainform.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_zoom_in_surf.clicked.connect(self.map_zoom_in)
        self.ui.btn_zoom_out_surf.clicked.connect(self.map_zoom_out)
        self.ui.widget_itp.setVisible(False)
        self.ui.widget_airb.setVisible(False)
        self.ui.widget_surf.setVisible(False)
        self.ui.widget_vsa.setVisible(False)
        #self.ui.pushButton_test.clicked.connect(self.mytest)

        #通用图片初始化
        pixmap_ownship =  QPixmap("pic/ownship.png") #本机图标
        pixmap_border = QPixmap("pic/b.png") #罗盘外轮廓
        scaledPixmap_border = pixmap_border.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatioByExpanding)
        pixmap_compass_transparent = QPixmap("pic/罗盘-透明背景.png") #透明罗盘
        scaledPixmap_compass_transparent = pixmap_compass_transparent.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatio)
        pixmap_compass_black = QPixmap("pic/罗盘-黑色背景.png")    #背景色为黑色罗盘
        scaledPixmap_compass_black = pixmap_compass_black.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatio)
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

        #surf
        #通用部分开始
        self.ui.horizontalLayoutWidget.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_surf = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_surf.setStyleSheet("padding: 0px; border: 0px;")
        self.ui.horizontalLayout.addWidget(self.ui.graphicsView_surf)
        url = os.getcwd() + '/map_surf.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.browser.resize(640,640)
        self.surf_scene = QGraphicsScene(self)

        #scene场景增加条目并设置位置
        self.map_widgetItem = self.surf_scene.addWidget(self.browser) # 地图条目
        self.map_widgetItem.setPos(0, 45)
        self.surf_border_Item = self.surf_scene.addPixmap(scaledPixmap_border) #罗盘边框条目
        self.surf_compass_Item = self.surf_scene.addPixmap(scaledPixmap_compass_transparent) #罗盘条目
        self.surf_compass_Item.setPos(0,45)
        self.surf_ownship_item = self.surf_scene.addPixmap(pixmap_ownship)    #本机图标
        self.surf_ownship_item.setPos(320-15,320+17.5)

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
        #初始化五架目标机不可见
        self.surf_targetair1_PixItem.setVisible(False)
        self.surf_air1_text_Item.setVisible(False)
        self.surf_targetair2_PixItem.setVisible(False)
        self.surf_air2_text_Item.setVisible(False)
        self.surf_targetair3_PixItem.setVisible(False)
        self.surf_air3_text_Item.setVisible(False)
        self.surf_targetair4_PixItem.setVisible(False)
        self.surf_air4_text_Item.setVisible(False)
        self.surf_targetair5_PixItem.setVisible(False)
        self.surf_air5_text_Item.setVisible(False)

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
        self.airb_compass_Item.setPos(0, 45)
        self.airb_ownship_item = self.airb_scene.addPixmap(pixmap_ownship)  # 本机图标
        self.airb_ownship_item.setPos(320 - 15, 320 + 17.5)

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
        # 初始化五架目标机不可见
        self.airb_targetair1_PixItem.setVisible(False)
        self.airb_air1_text_Item.setVisible(False)
        self.airb_targetair2_PixItem.setVisible(False)
        self.airb_air2_text_Item.setVisible(False)
        self.airb_targetair3_PixItem.setVisible(False)
        self.airb_air3_text_Item.setVisible(False)
        self.airb_targetair4_PixItem.setVisible(False)
        self.airb_air4_text_Item.setVisible(False)
        self.airb_targetair5_PixItem.setVisible(False)
        self.airb_air5_text_Item.setVisible(False)
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
        self.vsa_compass_Item.setPos(0, 45)
        self.vsa_ownship_item = self.vsa_scene.addPixmap(pixmap_ownship)  # 本机图标
        self.vsa_ownship_item.setPos(320 - 15, 320 + 17.5)

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
        self.vsa_targetair1_PixItem.setVisible(False)
        self.vsa_air1_text_Item.setVisible(False)
        self.vsa_targetair2_PixItem.setVisible(False)
        self.vsa_air2_text_Item.setVisible(False)
        self.vsa_targetair3_PixItem.setVisible(False)
        self.vsa_air3_text_Item.setVisible(False)
        self.vsa_targetair4_PixItem.setVisible(False)
        self.vsa_air4_text_Item.setVisible(False)
        self.vsa_targetair5_PixItem.setVisible(False)
        self.vsa_air5_text_Item.setVisible(False)
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
        self.itp_compass_Item.setPos(0, 45)
        self.itp_ownship_item = self.itp_scene.addPixmap(pixmap_ownship)  # 本机图标
        self.itp_ownship_item.setPos(320 - 15, 320 + 17.5)

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

        self.itp_targetair1_PixItem.setVisible(False)
        self.itp_air1_text_Item.setVisible(False)
        self.itp_targetair2_PixItem.setVisible(False)
        self.itp_air2_text_Item.setVisible(False)
        self.itp_targetair3_PixItem.setVisible(False)
        self.itp_air3_text_Item.setVisible(False)
        self.itp_targetair4_PixItem.setVisible(False)
        self.itp_air4_text_Item.setVisible(False)
        self.itp_targetair5_PixItem.setVisible(False)
        self.itp_air5_text_Item.setVisible(False)

    def map_zoom_in(self):
            # 放大一级视图
            js_string_map_zoom_in = 'map.zoomIn();'
            self.browser.page().runJavaScript(js_string_map_zoom_in)  # 初始化本机位置、标注、航线、移动

    def map_zoom_out(self):
        # 缩小一级视图
        # 放大一级视图
        js_string_map_zoom_in = 'map.zoomOut();'
        self.browser.page().runJavaScript(js_string_map_zoom_in)  # 初始化本机位置、标注、航线、移动


    def update_cdti_ui(self,info):
        '''

        :param info:
        :return:
        '''
        target_x_list = []  # 目标机x轴坐标序列
        target_y_list = []  # 目标机y轴坐标序列
        if info:
           print("接收到UA发送数据，开始解析")
           print(info)
           #清空所有UI
           for item in info:
               try:
                   if item[1] == 46384:  # 设置控件显示or隐藏
                       if 'surf_targetshow_bitmap1' == self.map_wigdetId[item[0]]:
                           self.surf_targetair1_PixItem.setVisible(item[2])
                           self.surf_air1_text_Item.setVisible(item[2])
                           self.airb_targetair1_PixItem.setVisible(item[2])
                           self.airb_air1_text_Item.setVisible(item[2])
                           self.vsa_targetair1_PixItem.setVisible(item[2])
                           self.vsa_air1_text_Item.setVisible(item[2])
                           self.itp_targetair1_PixItem.setVisible(item[2])
                           self.itp_air1_text_Item.setVisible(item[2])
                       if 'surf_targetshow_bitmap2' == self.map_wigdetId[item[0]]:
                           self.surf_targetair2_PixItem.setVisible(item[2])
                           self.surf_air2_text_Item.setVisible(item[2])
                           self.airb_targetair2_PixItem.setVisible(item[2])
                           self.airb_air2_text_Item.setVisible(item[2])
                           self.vsa_targetair2_PixItem.setVisible(item[2])
                           self.vsa_air2_text_Item.setVisible(item[2])
                           self.itp_targetair2_PixItem.setVisible(item[2])
                           self.itp_air2_text_Item.setVisible(item[2])
                       if 'surf_targetshow_bitmap3' == self.map_wigdetId[item[0]]:
                           self.surf_targetair3_PixItem.setVisible(item[2])
                           self.surf_air3_text_Item.setVisible(item[2])
                           self.airb_targetair3_PixItem.setVisible(item[2])
                           self.airb_air3_text_Item.setVisible(item[2])
                           self.vsa_targetair3_PixItem.setVisible(item[2])
                           self.vsa_air3_text_Item.setVisible(item[2])
                           self.itp_targetair3_PixItem.setVisible(item[2])
                           self.itp_air3_text_Item.setVisible(item[2])
                       if 'surf_targetshow_bitmap4' == self.map_wigdetId[item[0]]:
                           self.surf_targetair4_PixItem.setVisible(item[2])
                           self.surf_air4_text_Item.setVisible(item[2])
                           self.airb_targetair4_PixItem.setVisible(item[2])
                           self.airb_air4_text_Item.setVisible(item[2])
                           self.vsa_targetair4_PixItem.setVisible(item[2])
                           self.vsa_air4_text_Item.setVisible(item[2])
                           self.itp_targetair4_PixItem.setVisible(item[2])
                           self.itp_air4_text_Item.setVisible(item[2])
                       if 'surf_targetshow_bitmap5' == self.map_wigdetId[item[0]]:
                           self.surf_targetair5_PixItem.setVisible(item[2])
                           self.surf_air5_text_Item.setVisible(item[2])
                           self.airb_targetair5_PixItem.setVisible(item[2])
                           self.airb_air5_text_Item.setVisible(item[2])
                           self.vsa_targetair5_PixItem.setVisible(item[2])
                           self.vsa_air5_text_Item.setVisible(item[2])
                           self.itp_targetair5_PixItem.setVisible(item[2])
                           self.itp_air5_text_Item.setVisible(item[2])
                   if item[1] == 46224:  # 设置文本
                       if self.map_wigdetId[item[0]] == 'surf_ownship_angle_txt':#设置本机航向角
                           surf_air_heading_txt = QLabel(str(item[2].decode()))
                           airb_air_heading_txt = QLabel(str(item[2].decode()))
                           vsa_air_heading_txt = QLabel(str(item[2].decode()))
                           itp_air_heading_txt = QLabel(str(item[2].decode()))
                           surf_air_heading_txt.setStyleSheet("color:white;background-color:transparent")
                           airb_air_heading_txt.setStyleSheet("color:white;background-color:transparent")
                           vsa_air_heading_txt.setStyleSheet("color:white;background-color:transparent")
                           itp_air_heading_txt.setStyleSheet("color:white;background-color:transparent")
                           surf_air_heading = self.surf_scene.addWidget(surf_air_heading_txt)  # 本机航向角
                           airb_air_heading = self.airb_scene.addWidget(airb_air_heading_txt)  # 本机航向角
                           vsa_air_heading = self.vsa_scene.addWidget(vsa_air_heading_txt)  # 本机航向角
                           itp_air_heading = self.itp_scene.addWidget(itp_air_heading_txt)  # 本机航向角
                           surf_air_heading.setPos(315, 20)
                           airb_air_heading.setPos(315, 20)
                           vsa_air_heading.setPos(315, 20)
                           itp_air_heading.setPos(315, 20)
                       if 'surf_target1_id_txt' == self.map_wigdetId[item[0]]:#设置1号目标机id
                           surf_mywidget = self.surf_frametxt_targetAir1.findChild(QLabel,self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           airb_mywidget = self.airb_frametxt_targetAir1.findChild(QLabel, "airb_target1_id_txt")
                           airb_mywidget.setText(str(item[2].decode()))
                           vsa_mywidget = self.vsa_frametxt_targetAir1.findChild(QLabel, "vsa_target1_id_txt")
                           vsa_mywidget.setText(str(item[2].decode()))
                           itp_mywidget = self.itp_frametxt_targetAir1.findChild(QLabel, "itp_target1_id_txt")
                           itp_mywidget.setText(str(item[2].decode()))
                           self.ui.surf_targetair1_id_info.setText(str(item[2].decode()))
                           self.ui.airb_targetair1_id_info.setText(str(item[2].decode()))
                           self.ui.vsa_targetair1_id_info.setText(str(item[2].decode()))
                       if 'surf_target2_id_txt' == self.map_wigdetId[item[0]]:#设置2号目标机id
                           surf_mywidget = self.surf_frametxt_targetAir2.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           airb_mywidget = self.airb_frametxt_targetAir2.findChild(QLabel, "airb_target2_id_txt")
                           airb_mywidget.setText(str(item[2].decode()))
                           vsa_mywidget = self.vsa_frametxt_targetAir2.findChild(QLabel, "vsa_target2_id_txt")
                           vsa_mywidget.setText(str(item[2].decode()))
                           itp_mywidget = self.itp_frametxt_targetAir2.findChild(QLabel, "itp_target2_id_txt")
                           itp_mywidget.setText(str(item[2].decode()))
                           self.ui.surf_targetair2_id_info.setText(str(item[2].decode()))
                           self.ui.airb_targetair2_id_info.setText(str(item[2].decode()))
                           self.ui.vsa_targetair2_id_info.setText(str(item[2].decode()))
                       if 'surf_target3_id_txt' == self.map_wigdetId[item[0]]:#设置3号目标机id
                           surf_mywidget = self.surf_frametxt_targetAir3.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           airb_mywidget = self.airb_frametxt_targetAir3.findChild(QLabel, "airb_target3_id_txt")
                           airb_mywidget.setText(str(item[2].decode()))
                           vsa_mywidget = self.vsa_frametxt_targetAir3.findChild(QLabel, "vsa_target3_id_txt")
                           vsa_mywidget.setText(str(item[2].decode()))
                           itp_mywidget = self.itp_frametxt_targetAir3.findChild(QLabel, "itp_target3_id_txt")
                           itp_mywidget.setText(str(item[2].decode()))
                           self.ui.surf_targetair3_id_info.setText(str(item[2].decode()))
                           self.ui.airb_targetair3_id_info.setText(str(item[2].decode()))
                           self.ui.vsa_targetair3_id_info.setText(str(item[2].decode()))
                       if 'surf_target4_id_txt' == self.map_wigdetId[item[0]]:#设置4号目标机id
                           surf_mywidget = self.surf_frametxt_targetAir4.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           airb_mywidget = self.airb_frametxt_targetAir4.findChild(QLabel, "airb_target4_id_txt")
                           airb_mywidget.setText(str(item[2].decode()))
                           vsa_mywidget = self.vsa_frametxt_targetAir4.findChild(QLabel, "vsa_target4_id_txt")
                           vsa_mywidget.setText(str(item[2].decode()))
                           itp_mywidget = self.itp_frametxt_targetAir4.findChild(QLabel, "itp_target4_id_txt")
                           itp_mywidget.setText(str(item[2].decode()))
                           self.ui.surf_targetair4_id_info.setText(str(item[2].decode()))
                           self.ui.airb_targetair4_id_info.setText(str(item[2].decode()))
                           self.ui.vsa_targetair4_id_info.setText(str(item[2].decode()))
                       if 'surf_target5_id_txt' == self.map_wigdetId[item[0]]:#设置5号目标机id
                           surf_mywidget = self.surf_frametxt_targetAir5.findChild(QLabel,self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           airb_mywidget = self.airb_frametxt_targetAir5.findChild(QLabel, "airb_target5_id_txt")
                           airb_mywidget.setText(str(item[2].decode()))
                           vsa_mywidget = self.vsa_frametxt_targetAir5.findChild(QLabel, "vsa_target5_id_txt")
                           vsa_mywidget.setText(str(item[2].decode()))
                           itp_mywidget = self.itp_frametxt_targetAir5.findChild(QLabel, "itp_target5_id_txt")
                           itp_mywidget.setText(str(item[2].decode()))
                           self.ui.surf_targetair5_id_info.setText(str(item[2].decode()))
                           self.ui.airb_targetair5_id_info.setText(str(item[2].decode()))
                           self.ui.vsa_targetair5_id_info.setText(str(item[2].decode()))
                       if 'surf_ownship_lon_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           airb_mywidget = self.findChild(QLabel,"airb_ownship_lon_txt")
                           airb_mywidget.setText(str(item[2].decode()))
                           vsa_mywidget = self.findChild(QLabel,"vsa_ownship_lon_txt")
                           vsa_mywidget.setText(str(item[2].decode()))
                           itp_mywidget = self.findChild(QLabel,"itp_ownship_lon_txt")
                           itp_mywidget.setText(str(item[2].decode()))
                       if 'surf_ownship_lat_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           airb_mywidget = self.findChild(QLabel,"airb_ownship_lat_txt")
                           airb_mywidget.setText(str(item[2].decode()))
                           vsa_mywidget = self.findChild(QLabel,"vsa_ownship_lat_txt")
                           vsa_mywidget.setText(str(item[2].decode()))
                           itp_mywidget = self.findChild(QLabel,"itp_ownship_lat_txt")
                           itp_mywidget.setText(str(item[2].decode()))
                       if 'surf_ownship_altrange_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           airb_mywidget = self.findChild(QLabel, "airb_ownship_altrange_txt")
                           airb_mywidget.setText(str(item[2].decode()))
                           vsa_mywidget = self.findChild(QLabel, "vsa_ownship_altrange_txt")
                           vsa_mywidget.setText(str(item[2].decode()))
                           itp_mywidget = self.findChild(QLabel, "itp_ownship_altrange_txt")
                           itp_mywidget.setText(str(item[2].decode()))
                       if 'surf_ownship_alt_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           self.ui.airb_ownship_alt_txt.setText(str(item[2].decode()))
                           self.ui.vsa_ownship_alt_txt.setText(str(item[2].decode()))
                           self.ui.itp_ownship_alt_txt.setText(str(item[2].decode()))
                       if 'surf_ownship_id_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           self.ui.airb_ownship_id_txt.setText(str(item[2].decode()))
                           self.ui.vsa_ownship_id_txt.setText(str(item[2].decode()))
                           self.ui.itp_ownship_id_txt.setText(str(item[2].decode()))
                       if 'surf_target1_speed_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           self.ui.airb_target1_speed_txt.setText(str(item[2].decode()))
                           self.ui.vsa_target1_speed_txt.setText(str(item[2].decode()))
                       if 'surf_target2_speed_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           self.ui.airb_target2_speed_txt.setText(str(item[2].decode()))
                           self.ui.vsa_target2_speed_txt.setText(str(item[2].decode()))
                       if 'surf_target3_speed_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           self.ui.airb_target3_speed_txt.setText(str(item[2].decode()))
                           self.ui.vsa_target3_speed_txt.setText(str(item[2].decode()))
                       if 'surf_target4_speed_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           self.ui.airb_target4_speed_txt.setText(str(item[2].decode()))
                           self.ui.vsa_target4_speed_txt.setText(str(item[2].decode()))
                       if 'surf_target5_speed_txt' == self.map_wigdetId[item[0]]:
                           surf_mywidget = self.findChild(QLabel, self.map_wigdetId[item[0]])
                           surf_mywidget.setText(str(item[2].decode()))
                           self.ui.airb_target5_speed_txt.setText(str(item[2].decode()))
                           self.ui.vsa_target5_speed_txt.setText(str(item[2].decode()))
                       if 'surf_compass_step' == self.map_wigdetId[item[0]]:
                           compass_step = int(item[2])
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
                       if 'surf_ownship_applstatus_txt' == self.map_wigdetId[item[0]]:
                           self.ui.airb_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           self.ui.surf_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           self.ui.vsa_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           self.ui.itp_ownship_applstatus_bitmap.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                       if 'surf_target1_applstatus_bitmap' == self.map_wigdetId[item[0]]:
                           surf_pic_widget = self.surf_frametxt_targetAir1.findChild(QLabel, self.map_wigdetId[item[0]])
                           airb_pic_widget = self.airb_frametxt_targetAir1.findChild(QLabel, "airb_target1_applstatus_bitmap")
                           vsa_pic_widget = self.vsa_frametxt_targetAir1.findChild(QLabel, "vsa_target1_applstatus_bitmap")
                           itp_pic_widget = self.itp_frametxt_targetAir1.findChild(QLabel, "itp_target1_applstatus_bitmap")
                           surf_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           airb_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           vsa_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           itp_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                       if 'surf_target2_applstatus_bitmap' == self.map_wigdetId[item[0]]:
                           surf_pic_widget = self.surf_frametxt_targetAir2.findChild(QLabel, self.map_wigdetId[item[0]])
                           airb_pic_widget = self.airb_frametxt_targetAir2.findChild(QLabel, "airb_target2_applstatus_bitmap")
                           vsa_pic_widget = self.vsa_frametxt_targetAir2.findChild(QLabel, "vsa_target2_applstatus_bitmap")
                           itp_pic_widget = self.itp_frametxt_targetAir2.findChild(QLabel, "itp_target2_applstatus_bitmap")
                           surf_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           airb_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           vsa_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           itp_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                       if 'surf_target3_applstatus_bitmap' == self.map_wigdetId[item[0]]:
                           surf_pic_widget = self.surf_frametxt_targetAir3.findChild(QLabel,self.map_wigdetId[item[0]])
                           airb_pic_widget = self.airb_frametxt_targetAir3.findChild(QLabel,"airb_target3_applstatus_bitmap")
                           vsa_pic_widget = self.vsa_frametxt_targetAir3.findChild(QLabel, "vsa_target3_applstatus_bitmap")
                           itp_pic_widget = self.itp_frametxt_targetAir3.findChild(QLabel,"itp_target3_applstatus_bitmap")
                           surf_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           airb_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           vsa_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           itp_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                       if 'surf_target4_applstatus_bitmap' == self.map_wigdetId[item[0]]:
                           surf_pic_widget = self.surf_frametxt_targetAir4.findChild(QLabel,
                                                                                     self.map_wigdetId[item[0]])
                           airb_pic_widget = self.airb_frametxt_targetAir4.findChild(QLabel,
                                                                                     "airb_target4_applstatus_bitmap")
                           vsa_pic_widget = self.vsa_frametxt_targetAir4.findChild(QLabel,
                                                                                   "vsa_target4_applstatus_bitmap")
                           itp_pic_widget = self.itp_frametxt_targetAir4.findChild(QLabel,
                                                                                   "itp_target4_applstatus_bitmap")
                           surf_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           airb_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           vsa_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           itp_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                       if 'surf_target5_applstatus_bitmap' == self.map_wigdetId[item[0]]:
                           surf_pic_widget = self.surf_frametxt_targetAir5.findChild(QLabel,
                                                                                     self.map_wigdetId[item[0]])
                           airb_pic_widget = self.airb_frametxt_targetAir5.findChild(QLabel,
                                                                                     "airb_target5_applstatus_bitmap")
                           vsa_pic_widget = self.vsa_frametxt_targetAir5.findChild(QLabel,
                                                                                   "vsa_target5_applstatus_bitmap")
                           itp_pic_widget = self.itp_frametxt_targetAir5.findChild(QLabel,
                                                                                   "itp_target5_applstatus_bitmap")
                           surf_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           airb_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           vsa_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                           itp_pic_widget.setPixmap(QPixmap("pic/appstatus" + str(item[2]) + ".png"))
                   if item[1] == 46272: #设置目标机图标
                       if 'surf_targetshow_bitmap1' == self.map_wigdetId[item[0]]:
                           pixmap_targetship = QPixmap("pic/air" + str(item[2]) + ".png")  # 1号类型目标机图标
                           self.surf_targetair1_PixItem.setPixmap(pixmap_targetship)
                           self.airb_targetair1_PixItem.setPixmap(pixmap_targetship)
                           self.vsa_targetair1_PixItem.setPixmap(pixmap_targetship)
                           self.itp_targetair1_PixItem.setPixmap(pixmap_targetship)
                       if 'surf_targetshow_bitmap2' == self.map_wigdetId[item[0]]:
                           pixmap_targetship = QPixmap("pic/air" + str(item[2]) + ".png")  # 2号类型目标机图标
                           self.surf_targetair2_PixItem.setPixmap(pixmap_targetship)
                           self.airb_targetair2_PixItem.setPixmap(pixmap_targetship)
                           self.vsa_targetair2_PixItem.setPixmap(pixmap_targetship)
                           self.itp_targetair2_PixItem.setPixmap(pixmap_targetship)
                       if 'surf_targetshow_bitmap3' == self.map_wigdetId[item[0]]:
                           pixmap_targetship = QPixmap("pic/air" + str(item[2]) + ".png")  # 3号类型目标机图标
                           self.surf_targetair3_PixItem.setPixmap(pixmap_targetship)
                           self.airb_targetair3_PixItem.setPixmap(pixmap_targetship)
                           self.vsa_targetair3_PixItem.setPixmap(pixmap_targetship)
                           self.itp_targetair3_PixItem.setPixmap(pixmap_targetship)
                       if 'surf_targetshow_bitmap4' == self.map_wigdetId[item[0]]:
                           pixmap_targetship = QPixmap("pic/air" + str(item[2]) + ".png")  # 4号类型目标机图标
                           self.surf_targetair4_PixItem.setPixmap(pixmap_targetship)
                           self.airb_targetair4_PixItem.setPixmap(pixmap_targetship)
                           self.vsa_targetair4_PixItem.setPixmap(pixmap_targetship)
                           self.itp_targetair4_PixItem.setPixmap(pixmap_targetship)
                       if 'surf_targetshow_bitmap5' == self.map_wigdetId[item[0]]:
                           pixmap_targetship = QPixmap("pic/air" + str(item[2]) + ".png")  # 5号类型目标机图标
                           self.surf_targetair5_PixItem.setPixmap(pixmap_targetship)
                           self.airb_targetair5_PixItem.setPixmap(pixmap_targetship)
                           self.vsa_targetair5_PixItem.setPixmap(pixmap_targetship)
                           self.itp_targetair5_PixItem.setPixmap(pixmap_targetship)
                   if item[1] ==  45760: # 设置旋转角
                       if 'surf_targetshow_bitmap1' == self.map_wigdetId[item[0]]:
                           self.surf_targetair1_PixItem.setRotation(int(item[2].decode()))
                           self.airb_targetair1_PixItem.setRotation(int(item[2].decode()))
                           self.vsa_targetair1_PixItem.setRotation(int(item[2].decode()))
                           self.itp_targetair1_PixItem.setRotation(int(item[2].decode()))
                       if 'surf_targetshow_bitmap2' == self.map_wigdetId[item[0]]:
                           self.surf_targetair2_PixItem.setRotation(int(item[2].decode()))
                           self.airb_targetair2_PixItem.setRotation(int(item[2].decode()))
                           self.vsa_targetair2_PixItem.setRotation(int(item[2].decode()))
                           self.itp_targetair2_PixItem.setRotation(int(item[2].decode()))
                       if 'surf_targetshow_bitmap3' == self.map_wigdetId[item[0]]:
                           self.surf_targetair3_PixItem.setRotation(int(item[2].decode()))
                           self.airb_targetair3_PixItem.setRotation(int(item[2].decode()))
                           self.vsa_targetair3_PixItem.setRotation(int(item[2].decode()))
                           self.itp_targetair3_PixItem.setRotation(int(item[2].decode()))
                       if 'surf_targetshow_bitmap4' == self.map_wigdetId[item[0]]:
                           self.surf_targetair4_PixItem.setRotation(int(item[2].decode()))
                           self.airb_targetair4_PixItem.setRotation(int(item[2].decode()))
                           self.vsa_targetair4_PixItem.setRotation(int(item[2].decode()))
                           self.itp_targetair4_PixItem.setRotation(int(item[2].decode()))
                       if 'surf_targetshow_bitmap5' == self.map_wigdetId[item[0]]:
                           self.surf_targetair5_PixItem.setRotation(int(item[2].decode()))
                           self.airb_targetair5_PixItem.setRotation(int(item[2].decode()))
                           self.vsa_targetair5_PixItem.setRotation(int(item[2].decode()))
                           self.itp_targetair5_PixItem.setRotation(int(item[2].decode()))
                   if item[1] == 45824: # 设置目标机X轴坐标
                       if 'surf_targetshow_bitmap1' == self.map_wigdetId[item[0]]:
                           target_x_list.append(int(item[2].decode()))
                       if 'surf_targetshow_bitmap2' == self.map_wigdetId[item[0]]:
                           target_x_list.append(int(item[2].decode()))
                       if 'surf_targetshow_bitmap3' == self.map_wigdetId[item[0]]:
                           target_x_list.append(int(item[2].decode()))
                       if 'surf_targetshow_bitmap4' == self.map_wigdetId[item[0]]:
                           target_x_list.append(int(item[2].decode()))
                       if 'surf_targetshow_bitmap5' == self.map_wigdetId[item[0]]:
                           target_x_list.append(int(item[2].decode()))
                   if item[1] == 45840: # 设置目标机Y轴坐标
                       if 'surf_targetshow_bitmap1' == self.map_wigdetId[item[0]]:
                           target_y_list.append(int(item[2].decode()))
                       if 'surf_targetshow_bitmap2' == self.map_wigdetId[item[0]]:
                           target_y_list.append(int(item[2].decode()))
                       if 'surf_targetshow_bitmap3' == self.map_wigdetId[item[0]]:
                           target_y_list.append(int(item[2].decode()))
                       if 'surf_targetshow_bitmap4' == self.map_wigdetId[item[0]]:
                           target_y_list.append(int(item[2].decode()))
                       if 'surf_targetshow_bitmap5' == self.map_wigdetId[item[0]]:
                           target_y_list.append(int(item[2].decode()))
                   self.surf_targetair1_PixItem.setPos(target_x_list[0],target_y_list[0])
                   self.surf_air1_text_Item.setPos(target_x_list[0], target_y_list[0]+20)
                   self.surf_targetair2_PixItem.setPos(target_x_list[1],target_y_list[1])
                   self.surf_air2_text_Item.setPos(target_x_list[1], target_y_list[1]+20)
                   self.surf_targetair3_PixItem.setPos(target_x_list[2],target_y_list[2])
                   self.surf_air3_text_Item.setPos(target_x_list[2], target_y_list[2]+20)
                   self.surf_targetair4_PixItem.setPos(target_x_list[3],target_y_list[3])
                   self.surf_air4_text_Item.setPos(target_x_list[3], target_y_list[3]+20)
                   self.surf_targetair5_PixItem.setPos(target_x_list[4],target_y_list[4])
                   self.surf_air5_text_Item.setPos(target_x_list[4], target_y_list[4]+20)

                   self.airb_targetair1_PixItem.setPos(target_x_list[0],target_y_list[0])
                   self.airb_air1_text_Item.setPos(target_x_list[0], target_y_list[0]+20)
                   self.airb_targetair2_PixItem.setPos(target_x_list[1],target_y_list[1])
                   self.airb_air2_text_Item.setPos(target_x_list[1], target_y_list[1]+20)
                   self.airb_targetair3_PixItem.setPos(target_x_list[2],target_y_list[2])
                   self.airb_air3_text_Item.setPos(target_x_list[2], target_y_list[2]+20)
                   self.airb_targetair4_PixItem.setPos(target_x_list[3],target_y_list[3])
                   self.airb_air4_text_Item.setPos(target_x_list[3], target_y_list[3]+20)
                   self.airb_targetair5_PixItem.setPos(target_x_list[4],target_y_list[4])
                   self.airb_air5_text_Item.setPos(target_x_list[4], target_y_list[4]+20)

                   self.vsa_targetair1_PixItem.setPos(target_x_list[0],target_y_list[0])
                   self.vsa_air1_text_Item.setPos(target_x_list[0], target_y_list[0]+20)
                   self.vsa_targetair2_PixItem.setPos(target_x_list[1],target_y_list[1])
                   self.vsa_air2_text_Item.setPos(target_x_list[1], target_y_list[1]+20)
                   self.vsa_targetair3_PixItem.setPos(target_x_list[2],target_y_list[2])
                   self.vsa_air3_text_Item.setPos(target_x_list[2], target_y_list[2]+20)
                   self.vsa_targetair4_PixItem.setPos(target_x_list[3],target_y_list[3])
                   self.vsa_air4_text_Item.setPos(target_x_list[3], target_y_list[3]+20)
                   self.vsa_targetair5_PixItem.setPos(target_x_list[4],target_y_list[4])
                   self.vsa_air5_text_Item.setPos(target_x_list[4], target_y_list[4]+20)

                   self.itp_targetair1_PixItem.setPos(target_x_list[0],target_y_list[0])
                   self.itp_air1_text_Item.setPos(target_x_list[0], target_y_list[0]+20)
                   self.itp_targetair2_PixItem.setPos(target_x_list[1],target_y_list[1])
                   self.itp_air2_text_Item.setPos(target_x_list[1], target_y_list[1]+20)
                   self.itp_targetair3_PixItem.setPos(target_x_list[2],target_y_list[2])
                   self.itp_air3_text_Item.setPos(target_x_list[2], target_y_list[2]+20)
                   self.itp_targetair4_PixItem.setPos(target_x_list[3],target_y_list[3])
                   self.itp_air4_text_Item.setPos(target_x_list[3], target_y_list[3]+20)
                   self.itp_targetair5_PixItem.setPos(target_x_list[4],target_y_list[4])
                   self.itp_air5_text_Item.setPos(target_x_list[4], target_y_list[4]+20)
               except:
                   print("更新界面UI有错误，请检查~")
                   continue



if __name__=='__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())