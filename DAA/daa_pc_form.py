# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'daa_pc_form.py'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import os
import daa_ui1
import binascii
import socket
import json
import time
import traceback
from check_sum import *
from data_parser import *
from daa_frame import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from MyQGraphicsItem import *

server_ip1 = "192.168.1.2"  #xhx lxg
server_ip2 = "192.168.1.3" #xct
request_port1 = 10101  #lxg
request_port2 = 10001  #xhx
request_port3 = 9998   #xct

class Communication_Server1_Thread(QThread):
    signal_a = pyqtSignal(str,list)
    def __init__(self):
        super(Communication_Server1_Thread, self).__init__()
        self.socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.transmit_port = 0 #new port
        self.socket_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        '''
        step1：首次握手：UI向Server发送分辨率数据，发起连接, Server端响应连接，返回新的通信端口
        '''
        frame = DAAFrame() #模拟一个发起连接的数据帧
        frame.header = 0x4f3c  #UI to Server
        frame.type = 0xa1
        #屏幕长1024宽768 0102：长426宽362 0103：长426宽302  0201：长598宽756 0204长408宽324
        # frame.body = 0x0400030001AA016A01AA012E025602F401980144.to_bytes(length=20, byteorder='little',signed=False)
        frame.body = 0x040003000000000000F800A000000000012000D4.to_bytes(length=20, byteorder='little',signed=False)
        frame.length = 29
        frame.checksum = checksum(list(frame.pack()[:-2]))
        self.socket_1.sendto(frame.pack(), (server_ip1, request_port1))
        print("UI向Server1发送第一帧数据!")
        while True:
            data, address = self.socket_1.recvfrom(2048)
            frame = DAAFrame()
            frame.unpack(data)
            if frame.header == 0x3c4f and frame.type == 0xa2: #Server响应连接，返回数据通信端口
                temp_port = frame.body.hex()
                low_2 = temp_port[-2:]
                high_2 = temp_port[0:2]
                temp_port = low_2+high_2      #16进制高两位和低两位互换
                self.transmit_port = int(temp_port, 16)
                break
        if self.transmit_port:
            '''
             step2：二次握手 UI发送新的连接确认至新的监听端口，Server端返回界面数据
             '''
            self.socket_2.bind((server_ip1, 10010))
            frame = DAAFrame()  # 模拟一个连接确认的数据帧
            frame.header = 0x4f3c  # UI to Server
            frame.type = 0xa3  # 连接确认
            frame.body = b''
            frame.length = 9
            frame.checksum = checksum(list(frame.pack()[:-2]))
            self.socket_2.sendto(frame.pack(), (server_ip1, self.transmit_port))
            print("UI向Server1发送第二帧数据!")
            while True:
                time.sleep(1)
                data, address = self.socket_2.recvfrom(4096)
                frame = DAAFrame()
                frame.unpack(data)
                if frame.header == 0x3c4f and frame.type == 0xa4:  # Server响应连接,返回数据
                    datas = json.loads(frame.body.decode("utf-8"))
                    self.signal_a.emit("server1",datas)

class Communication_Server2_Thread(QThread):
    signal_a = pyqtSignal(str,list)
    '''
    step1：首次握手：UI向Server发送分辨率数据，发起连接, Server端响应连接，返回新的通信端口
    '''
    def __init__(self):
        super(Communication_Server2_Thread, self).__init__()
        self.socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.transmit_port = 0  # new port
        self.socket_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        frame = DAAFrame() #模拟一个发起连接的数据帧
        frame.header = 0x4f3c  #UI to Server
        frame.type = 0xa1
        # frame.body = 0x0400030001AA016A01AA012E025602F401980144.to_bytes(length=20, byteorder='little',signed=False) #屏幕长1024宽768
        frame.body = 0x040003000000000000F800A000000000012000D4.to_bytes(length=20, byteorder='little',signed=False)  # 屏幕长1024宽768 A高度层 248*160 B高度层288*212
        frame.length = 29
        frame.checksum = checksum(list(frame.pack()[:-2]))
        self.socket_1.sendto(frame.pack(), (server_ip1, request_port2))
        print("UI向Server2发送第一帧数据!")
        while True:
            data, address = self.socket_1.recvfrom(2048)
            frame = DAAFrame()
            frame.unpack(data)
            if frame.header == 0x3c4f and frame.type == 0xa2: #Server响应连接，返回数据通信端口
                temp_port = frame.body.hex()
                low_2 = temp_port[-2:]
                high_2 = temp_port[0:2]
                temp_port = low_2+high_2      #16进制高两位和低两位互换
                self.transmit_port = int(temp_port, 16)
                break
        if self.transmit_port:
            '''
             step2：二次握手 UI发送新的连接确认至新的监听端口，Server端返回界面数据
             '''
            self.socket_2.bind((server_ip1, 10011))
            self.data_parser = DataParser()
            frame = DAAFrame() #模拟一个连接确认的数据帧
            frame.header = 0x4f3c  #UI to Server
            frame.type = 0xa3    #连接确认
            frame.body = b''
            frame.length = 9
            frame.checksum = checksum(list(frame.pack()[:-2]))
            self.socket_2.sendto(frame.pack(), (server_ip1, self.transmit_port))
            print("UI向Server2发送第二帧数据!")
            while True:
                data, address = self.socket_2.recvfrom(4096)
                parsed = self.data_parser.accept(data)
                if not parsed:
                    continue
                frame_type, frame_body = parsed
                if frame_type == 0xa4:  # Server响应连接,返回数据
                    datas = json.loads(frame_body.decode("utf-8"))
                    self.signal_a.emit("server2",datas)

class Communication_Server3_Thread(QThread):
    signal_a = pyqtSignal(str,list)
    '''
    step1：首次握手：UI向Server发送分辨率数据，发起连接, Server端响应连接，返回新的通信端口
    '''
    def __init__(self):
        super(Communication_Server3_Thread, self).__init__()
        self.socket_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.transmit_port = 0  # new port
        self.socket_2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        frame = DAAFrame() #模拟一个发起连接的数据帧
        frame.header = 0x4f3c  #UI to Server
        frame.type = 0xa1
        frame.body = 0x040003000000000000F800A000000000012000D4.to_bytes(length=20, byteorder='little',signed=False)  # 屏幕长1024宽768 A高度层 248*160 B高度层288*212
        # frame.body = 0x0400030001AA016A01AA012E025602F401980144.to_bytes(length=20, byteorder='little',signed=False)

        frame.length = 29
        frame.checksum = checksum(list(frame.pack()[:-2]))
        self.socket_1.sendto(frame.pack(), (server_ip2, request_port3))
        print("UI向Server3发送第一帧数据!")
        while True:
            data, address = self.socket_1.recvfrom(2048)
            frame = DAAFrame()
            frame.unpack(data)
            if frame.header == 0x3c4f and frame.type == 0xa2: #Server响应连接，返回数据通信端口
                temp_port = frame.body.hex()
                low_2 = temp_port[-2:]
                high_2 = temp_port[0:2]
                temp_port = low_2+high_2      #16进制高两位和低两位互换
                self.transmit_port = int(temp_port, 16)
                break
        if self.transmit_port:
            '''
             step2：二次握手 UI发送新的连接确认至新的监听端口，Server端返回界面数据
             '''
            self.socket_2.bind((server_ip1, 10012))
            frame = DAAFrame() #模拟一个连接确认的数据帧
            frame.header = 0x4f3c  #UI to Server
            frame.type = 0xa3    #连接确认
            frame.body = b''
            frame.length = 10
            frame.checksum = checksum(list(frame.pack()[:-2]))
            print("UI向Server3发送第二帧数据!")
            self.socket_2.sendto(frame.pack(), (server_ip2, self.transmit_port))
            while True:
                data, address = self.socket_2.recvfrom(2048)
                frame = DAAFrame()
                frame.unpack(data)
                if frame.header == 0x3c4f and frame.type == 0xa4:  # Server响应连接,返回数据
                    datas = json.loads(frame.body.decode("utf-8"))
                    self.signal_a.emit("server3",datas)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = daa_ui1.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.frame.setStyleSheet("background:black")
        self.ui.tabWidget.tabBar().hide() #隐藏

        self.ui.btn_jump1.clicked.connect(self.update_tab1)
        self.ui.btn_jump2.clicked.connect(self.update_tab2)
        self.ui.btn_jump1.setStyleSheet("background:transparent")
        self.ui.btn_jump2.setStyleSheet("background:transparent")
        self.ui.frame_1.setStyleSheet("background:black")
        self.ui.frame_2.setStyleSheet("background:black")
        self.ui.frame_3.setStyleSheet("background:black")
        self.ui.frame_4.setStyleSheet("background:black")
        self.ui.frame_5.setStyleSheet("background:black")
        self.ui.frame_6.setStyleSheet("background:black")
        self.ui.frame_7.setStyleSheet("background:black")

        self.ui.listWidget_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  #禁用竖直滑动条
        self.ui.listWidget_1.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #禁用水平滑动条
        self.target_white_pix = QPixmap("pic/benji.png")
        self.target_yellow_pix = QPixmap("pic/qtfeiji1.png")  # 黄色
        self.target_red_pix = QPixmap("pic/qtfeiji2.png")  # 红色
        self.target_green_pix = QPixmap("pic/qtfeiji3.png")  # 绿色

        self.ui.tab1_own_pix.setVisible(False)
        self.ui.tab2_own_pix.setVisible(False)

        self.old_ownship_id = ""
        self.old_target_id = [""]*30
        self.old_tab1_target_id_list = []
        self.old_tab2_target_id_list = []

        self.tab1_dict_temp = {}  # key:flight_id value:target_index
        self.tab2_dict_temp = {}  # key:flight_id value:target_index
        self.tab1_new_num = 0
        self.tab2_new_num = 0
        for i in range(1,6):
            eval("self.ui.tab1_target" + str(i)+"_info.setVisible(False)")
            eval("self.ui.tab1_target" + str(i) + "_pix.setVisible(False)")
            eval("self.ui.tab2_target" + str(i) + "_info.setVisible(False)")
            eval("self.ui.tab2_target" + str(i) + "_pix.setVisible(False)")

            eval("self.ui.tab1_target" + str(i)+"_info").setStyleSheet("color:white;background-color:transparent;font-size:10px")
            eval("self.ui.tab2_target" + str(i) + "_info").setStyleSheet("color:white;background-color:transparent;font-size:10px")
            eval("self.ui.tab1_target" + str(i) + "_info").setGeometry(QRect(0, 0, 66, 60))
            eval("self.ui.tab2_target" + str(i) + "_info").setGeometry(QRect(0, 0, 66, 60))


        for i in range(0,500):#listWidget1创建500个刻度条 1个刻度条代表100m海拔高度
            if i % 10 == 0:
                label = QLabel("-"+str(50000 - i*100))
                label.setFont(QFont("宋体", 8))
                label.setStyleSheet("color:white;background-color:black")
                label.setFixedSize(35, 10)
                item = QListWidgetItem()  # 创建QListWidgetItem对象
                item.setSizeHint(QSize(45, 10))  # 设置QListWidgetItem大小
                self.ui.listWidget_1.addItem(item)  # 添加item
                self.ui.listWidget_1.setItemWidget(item, label)  # 为item设置widget
            else:
                label = QLabel("-")  # 头像显示
                label.setFont(QFont("宋体", 7))
                label.setStyleSheet("color:white;background-color:black")
                label.setFixedSize(10, 8)
                item = QListWidgetItem()  # 创建QListWidgetItem对象
                item.setSizeHint(QSize(45, 8))  # 设置QListWidgetItem大小
                self.ui.listWidget_1.addItem(item)  # 添加item
                self.ui.listWidget_1.setItemWidget(item, label)  # 为item设置widget
        self.ui.listWidget_1.setCurrentRow(500 - 390 + 16)  # 刻度标移到39000

        self.ui.listWidget_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  #禁用竖直滑动条
        self.ui.listWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) #禁用水平滑动条
        for i in range(0,700):#listWidget2创建700个刻度条 1刻度条1飞行速度
            if i % 10 == 0:
                label = QLabel("-"+str(700 - i))
                label.setFont(QFont("宋体", 8))
                label.setStyleSheet("color:white;background-color:black")
                label.setFixedSize(25, 10)
                item = QListWidgetItem()  # 创建QListWidgetItem对象
                item.setSizeHint(QSize(45, 10))  # 设置QListWidgetItem大小
                self.ui.listWidget_2.addItem(item)  # 添加item
                self.ui.listWidget_2.setItemWidget(item, label)  # 为item设置widget
            else:
                label = QLabel("-")  # 头像显示
                label.setFont(QFont("宋体", 7))
                label.setStyleSheet("color:white;background-color:black")
                label.setFixedSize(10, 8)
                item = QListWidgetItem()  # 创建QListWidgetItem对象
                item.setSizeHint(QSize(45, 8))  # 设置QListWidgetItem大小
                self.ui.listWidget_2.addItem(item)  # 添加item
                self.ui.listWidget_2.setItemWidget(item, label)  # 为item设置widget
        self.ui.listWidget_2.setCurrentRow(700 - 486 + 17)  # 刻度标移到486
        url = os.getcwd() + '/map/map_a.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        pen_white = QPen(Qt.white)
        pen_blue = QPen(Qt.blue)
        pen_blue.setStyle(Qt.DashLine)
        # tab1 地图模块及信息显示模块
        self.ui.horizontalLayout_1.addWidget(self.browser)
        self.ui.tabelWidget_1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tabelWidget_1.horizontalHeader().setStyleSheet("QHeaderView::section{background:black;color:white}")
        self.ui.tabelWidget_1.verticalHeader().setVisible(False)
        # tab1 罗盘区域 view2
        self.ui.horizontalLayoutWidget_3.setGeometry(QRect(40, 30, 302, 302))
        self.view_2 = QGraphicsView()  #创建视图窗口
        self.view_2.setRenderHint(QPainter.Antialiasing)
        self.view_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.horizontalLayout_2.addWidget(self.view_2)
        self.view_2.setStyleSheet("background:transparent;border:0px")
        self.view_2.setWindowFlags(Qt.FramelessWindowHint)
        self.view_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scene_2 = QGraphicsScene(self)  #绘制画布
        self.view_2.setScene(self.scene_2)
        self.view_2.setStyleSheet("border:0px")
        self.compass1_item = MyCompass1_Item() #罗盘
        self.scene_2.addItem(self.compass1_item)
        centerPos1 = self.compass1_item.boundingRect().center() #设置罗盘按中心点旋转
        self.compass1_item.setTransformOriginPoint(centerPos1)
        pixmap_ownship = QPixmap("pic/feiji1.png")  #本机图标
        self.ownship_item = self.scene_2.addPixmap(pixmap_ownship)
        self.ownship_item.setPos(130, 130)
        pixmap_chuizhixian = QPixmap("pic/chuizhixian1.png") #垂直条图标
        self.chuizhixian_item = self.scene_2.addPixmap(pixmap_chuizhixian)
        self.chuizhixian_item.setPos(140,0)
        pixmap_xiaoyuan = QPixmap("pic/xiaoyuan.png") #小圆图标
        self.xiaoyuan_item = self.scene_2.addPixmap(pixmap_xiaoyuan)
        self.xiaoyuan_item.setPos(0, 0)
        self.ARC_item = MyArc1_Item()
        self.scene_2.addItem(self.ARC_item)

        #tab2 UI
        self.ui.btn1.setStyleSheet("QPushButton{border-image:url(button2.png)}")
        self.ui.btn2.setStyleSheet("QPushButton{border-image:url(button2.png)}")
        self.ui.btn3.setStyleSheet("QPushButton{border-image:url(button2.png)}")


        #tab2 罗盘区域 view5
        self.ui.horizontalLayoutWidget_5.setGeometry(QRect(80, 130, 484, 484))
        self.view_5 = QGraphicsView()  #创建视图窗口
        self.view_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.view_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.horizontalLayout_5.addWidget(self.view_5)
        self.scene_5 = QGraphicsScene(self)
        self.view_5.setScene(self.scene_5)
        self.view_5.setStyleSheet("border:0px")
        self.compass2_item = MyCompass2_Item()
        self.scene_5.addItem(self.compass2_item)
        self.ARC2_item = MyArc2_Item()
        self.scene_5.addItem(self.ARC2_item)
        pixmap_ownship = QPixmap("pic/feiji1.png")  # 本机图标
        self.ownship_item = self.scene_5.addPixmap(pixmap_ownship)
        self.ownship_item.setPos(220, 220)
        pixmap_chuizhixian = QPixmap("pic/chuizhixian1.png")
        pixmap_chuizhixian1 = pixmap_chuizhixian.scaled(33, 483, aspectRatioMode=Qt.KeepAspectRatioByExpanding)
        self.chuizhixian_item = self.scene_5.addPixmap(pixmap_chuizhixian1)
        self.chuizhixian_item.setPos(223,-1)
        pixmap_xiaoyuan = QPixmap("pic/luopan2.png") #小圆图标
        self.xiaoyuan_item = self.scene_5.addPixmap(pixmap_xiaoyuan)
        self.xiaoyuan_item.setPos(0, 0)

        self.worker1 = Communication_Server1_Thread()
        self.worker1.signal_a.connect(self.update_UI)
        self.worker1.start()
        self.worker2 = Communication_Server2_Thread()
        self.worker2.signal_a.connect(self.update_UI)
        self.worker2.start()
        self.worker3 = Communication_Server3_Thread()
        self.worker3.signal_a.connect(self.update_UI)
        self.worker3.start()

    def update_tab1(self):
        self.ui.tabWidget.setCurrentIndex(1)
        # infos = [
        #     {'command_id': '04', 'id': '010304',
        #      'value': [{'color': '#FFFFFF', 'describe': '', 'isSelf': 1, 'step': 2, 'x': 0, 'y': 0},
        #                {'color': '#FFFF00', 'describe': 'in1\n0.0NM 0.0KT', 'isSelf': 0, 'step': 2, 'x': 100, 'y': 50},
        #                {'color': '#FF0000', 'describe': 'in2\n2.1NM 1.3KT', 'isSelf': 0, 'step': 2, 'x': 30, 'y': 30}]},
        #     {'command_id': '04', 'id': '020301',
        #      'value': [{'color': '#FFFFFF', 'describe': '', 'isSelf': 1, 'step': 2, 'x': 0, 'y': -0.672},
        #                {'color': '#FFFFFF', 'describe': '\n0.0NM 0.0KT', 'isSelf': 0, 'step': 2, 'x': 0,
        #                 'y': 83.318001},
        #                {'color': '#FFFFFF', 'describe': '\n0.0NM 0.0KT', 'isSelf': 0, 'step': 2, 'x': 0,
        #                 'y': 268.093994}]},
        #     {'command_id': '03', 'id': '010201', 'value': 84.37641143798828},
        #     {'command_id': '02', 'id': '010202',
        #      'value': [{'alt': 36325.4593175853, 'dir': 0.2454411871194467, 'flightID': 'in1', 'status': 3, 'x': -0.224,
        #                 'y': -0.072},
        #                {'alt': 36325.4593175853,
        #                 'dir': -1.3990138810797839,
        #                 'flightID': 'in2',
        #                 'status': 3, 'x': 0.012,
        #                 'y': 0.232},
        #                {'alt': 37047.24409448819,
        #                 'dir': -0.5399702255044248,
        #                 'flightID': 'in3',
        #                 'status': 0, 'x': -0.093,
        #                 'y': 0.025}]},
        #     {'command_id': '02', 'id': '010203',
        #      'value': [{'color': '#ff0000', 'lowerBound': 0.0, 'upperBound': 109.37641143798828},
        #                {'color': '#1fca36', 'lowerBound': 109.37641143798828, 'upperBound': 264.37640380859375},
        #                {'color': '#ff0000', 'lowerBound': 264.37640380859375, 'upperBound': 360.0}]},
        #     {'command_id': '02', 'id': '010204', 'value': 84.37641143798828},
        #     {'command_id': '01', 'id': '010205', 'value': 486.0},
        #     {'command_id': '01', 'id': '010206', 'value': [
        #         {'lowerBound': 10.0, 'status': 3.0, 'upperBound': 571.0},
        #         {'lowerBound': 571.0, 'status': 4.0, 'upperBound': 700.0}]},
        #     {'command_id': '03', 'id': '020101', 'value': 84.37641143798828}, {'command_id': '02', 'id': '020102',
        #                                                                        'value': [{'alt': '2700',
        #                                                                                   'dir': 0.2454411871194467,
        #                                                                                   'flightID': 'in1',
        #                                                                                   'status': 3, 'x': -0.224,
        #                                                                                   'y': -0.072}, {'alt': '2700',
        #                                                                                                  'dir': -1.3990138810797839,
        #                                                                                                  'flightID': 'in2',
        #                                                                                                  'status': 3,
        #                                                                                                  'x': 0.012,
        #                                                                                                  'y': 0.232},
        #                                                                                  {'alt': '2700',
        #                                                                                   'dir': -0.5399702255044248,
        #                                                                                   'flightID': 'in3',
        #                                                                                   'status': 0, 'x': -0.093,
        #                                                                                   'y': 0.025}]},
        #     {'command_id': '07', 'id': '020103', 'value': 2}, {'command_id': '02', 'id': '020104', 'value': {
        #         'description': 'ALT 35997m\nVS 0.00ft/m\nGS 486.00Kts', 'location': 'N 30.398553 E 104.076888'}},
        #     {'command_id': '07', 'id': '020105',
        #      'value': [{'color': '#ff0000', 'lowerBound': 0.0, 'upperBound': 109.37641143798828},
        #                {'color': '#1fca36', 'lowerBound': 109.37641143798828, 'upperBound': 264.37640380859375},
        #                {'color': '#ff0000', 'lowerBound': 264.37640380859375, 'upperBound': 360.0}]},
        #     {'command_id': '02', 'id': '010401', 'value': [
        #         {'alt': 35997.37532808399, 'dir': 84.37641143798828, 'flightID': 'self.own_ship.FlightID',
        #          'isSelf': True, 'lat': 30.398553253647684, 'lon': 104.07688842696501},
        #         {'alt': 36325.4593175853, 'dir': 98.43915557861328, 'flightID': 'in1', 'isSelf': False,
        #          'lat': 30.41293104282459, 'lon': 104.0696756263138, 'status': 3},
        #         {'alt': 36325.4593175853, 'dir': 4.218820571899414, 'flightID': 'in2', 'isSelf': False,
        #          'lat': 30.399294341593386, 'lon': 104.09482480434198, 'status': 3},
        #         {'alt': 37047.24409448819, 'dir': 53.43839645385742, 'flightID': 'in3', 'isSelf': False,
        #          'lat': 30.404850793610205, 'lon': 104.07809056040688, 'status': 0}]}
        # ]
        # self.ui.tab1_own_pix.setVisible(False)
        # self.ui.tab2_own_pix.setVisible(False)
        # for i in range(1,6):
        #     eval("self.ui.tab1_target" + str(i)+"_info.setVisible(False)")
        #     eval("self.ui.tab1_target" + str(i) + "_pix.setVisible(False)")
        #     eval("self.ui.tab2_target" + str(i) + "_info.setVisible(False)")
        #     eval("self.ui.tab2_target" + str(i) + "_pix.setVisible(False)")
        # try:
        #     for item in infos:
        #         if item['id'] == '010304':  # 本机及目标机高度层展示426*302
        #             target_index = 1  #目标机索引
        #             for air_info in item['value']:
        #                 air_type = air_info['isSelf']  # 1为本机，0为目标机
        #                 if air_type:  # 本机默认为白色
        #                     self.ui.tab1_own_pix.setVisible(True)
        #                     x = air_info['x']
        #                     y = air_info['y']
        #                     self.ui.tab1_own_pix.setGeometry(x+180,y+140,25,10)  #180,140为原点
        #                 else:
        #                     print("tab1 出现一架入侵机")
        #                     eval("self.ui.tab1_target" + str(target_index)+"_pix.setVisible(True)")
        #                     eval("self.ui.tab1_target" + str(target_index) + "_info.setVisible(True)")
        #                     air_color = air_info['color']
        #                     if air_color == '#FFFFFF':  # 白色
        #                         eval("self.ui.tab1_target" + str(target_index) + "_pix").setPixmap(QPixmap("pic/benji.png"))
        #                     if air_color == '#FFFF00':  # 黄色
        #                         eval("self.ui.tab1_target" + str(target_index) + "_pix").setPixmap(QPixmap("pic/qtfeiji1.png"))
        #                     if air_color == '#FF0000':  # 红色
        #                         eval("self.ui.tab1_target" + str(target_index) + "_pix").setPixmap(QPixmap("pic/qtfeiji2.png"))
        #                     if air_color == '#00FF00':  # 绿色
        #                         eval("self.ui.tab1_target" + str(target_index) + "_pix").setPixmap(QPixmap("pic/qtfeiji3.png"))
        #                     x = air_info['x']
        #                     y = air_info['y']
        #                     print(x,y)
        #                     eval("self.ui.tab1_target" + str(target_index) + "_pix").setGeometry(180+x, 140-y, 25, 10)
        #                     describe = air_info['describe']
        #                     eval("self.ui.tab1_target" + str(target_index) + "_info").setText("    "+describe)
        #                     eval("self.ui.tab1_target" + str(target_index) + "_info").setGeometry(160+x, 150-y, 66, 20)
        #                     target_index += 1
        #         if item['id'] == '020301':  # 本机及目标机高度层展示  408*324
        #             target_index = 1  # 目标机索引
        #             for air_info in item['value']:
        #                 air_type = air_info['isSelf']  # 1为本机，0为目标机
        #                 if air_type:  # 本机默认为白色
        #                     self.ui.tab2_own_pix.setVisible(True)
        #                     x = air_info['x']
        #                     y = air_info['y']
        #                     self.ui.tab2_own_pix.setGeometry(x + 205, y + 145, 25, 10)  # 205,145为原点
        #                 else:
        #                     print("tab2 出现一架入侵机")
        #                     eval("self.ui.tab2_target" + str(target_index) + "_pix.setVisible(True)")
        #                     eval("self.ui.tab2_target" + str(target_index) + "_info.setVisible(True)")
        #                     air_color = air_info['color']
        #                     if air_color == '#FFFFFF':  # 白色
        #                         eval("self.ui.tab2_target" + str(target_index) + "_pix").setPixmap(
        #                             QPixmap("pic/benji.png"))
        #                     if air_color == '#FFFF00':  # 黄色
        #                         eval("self.ui.tab2_target" + str(target_index) + "_pix").setPixmap(
        #                             QPixmap("pic/qtfeiji1.png"))
        #                     if air_color == '#FF0000':  # 红色
        #                         eval("self.ui.tab2_target" + str(target_index) + "_pix").setPixmap(
        #                             QPixmap("pic/qtfeiji2.png"))
        #                     if air_color == '#00FF00':  # 绿色
        #                         eval("self.ui.tab2_target" + str(target_index) + "_pix").setPixmap(
        #                             QPixmap("pic/qtfeiji3.png"))
        #                     x = air_info['x']
        #                     y = air_info['y']
        #                     print(x,y)
        #                     eval("self.ui.tab2_target" + str(target_index) + "_pix").setGeometry(205+x, 145-y, 25,10)
        #                     describe = air_info['describe']
        #                     eval("self.ui.tab2_target" + str(target_index) + "_info").setText("    " + describe)
        #                     eval("self.ui.tab2_target" + str(target_index) + "_info").setGeometry(185+x, 155-y, 66,20)
        #                     target_index += 1
        #
        #         if item['id'] == '010202':  # 入侵机列表 在罗盘中绘制入侵机
        #             for item_info in item['value']:
        #                 flight_id = item_info['flightID']
        #                 x = item_info['x']
        #                 y = item_info['y']
        #                 angle = item_info['dir']
        #                 status = item_info['status']
        #                 target_item = QGraphicsPixmapItem()
        #                 if status == 0:  # 999999 灰色
        #                     target_item = QGraphicsPixmapItem(QPixmap("pic/target-gray.png"))
        #                     self.scene_2.addItem(target_item)
        #                 if status == 1 or status == 2:  # ffff00  黄色
        #                     target_item = QGraphicsPixmapItem(QPixmap("pic/target-yellow.png"))
        #                     self.scene_2.addItem(target_item)
        #                 if status == 3:  # ff0000 红色
        #                     target_item = QGraphicsPixmapItem(QPixmap("pic/target-red.png"))
        #                     self.scene_2.addItem(target_item)
        #                 if status == 4:  # 00ff00 绿色
        #                     target_item = QGraphicsPixmapItem(QPixmap("pic/target-green.png"))
        #                     self.scene_2.addItem(target_item)
        #                 if target_item:
        #                     target_item.setPos(130+150*x, 130+150*y)
        #                     target_item.setRotation(angle)
        #
        #         if item['id'] == '020102':  # 入侵机列表 在罗盘中绘制入侵机
        #             for item_info in item['value']:
        #                 flight_id = item_info['flightID']
        #                 x = item_info['x']
        #                 y = item_info['y']
        #                 angle = item_info['dir']
        #                 status = item_info['status']
        #                 target_item = QGraphicsPixmapItem()
        #                 if status == 0:  # 999999 灰色
        #                     target_item = QGraphicsPixmapItem(QPixmap("pic/target-gray.png"))
        #                     self.scene_5.addItem(target_item)
        #                 if status == 1 or status == 2:  # ffff00  黄色
        #                     target_item = self.scene_5.addPixmap(QPixmap("pic/target-yellow.png"))
        #                 if status == 3:  # ff0000 红色
        #                     target_item = self.scene_5.addPixmap(QPixmap("pic/target-red.png"))
        #                 if status == 4:  # 00ff00 绿色
        #                     target_item = self.scene_5.addPixmap(QPixmap("pic/target-green.png"))
        #                 if target_item:
        #                     target_item.setPos(220+240*x, 220+240*y)
        #                     target_item.setRotation(angle)
        #
        # except:
        #     traceback.print_exc()

    def update_tab2(self):
        self.ui.tabWidget.setCurrentIndex(0)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        try:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except:
            traceback.print_exc()

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def update_UI(self,server,infos):
        # print("receive from: "+server)
        # print("Infos: "+ str(infos))
        # self.ui.tabelWidget_1.setRowCount(0)  # tabelWidget_1初始化
        # self.ui.tabelWidget_1.clearContents()
        try:
            for item in infos:
                # server3
                if item['id'] == '010304':  # 本机及目标机高度层展示426*302
                    target_index = 1  #目标机索引
                    for air_info in item['value']:
                        air_type = air_info['isSelf']  # 1为本机，0为目标机
                        if air_type:  # 本机默认为白色
                            self.ui.tab1_own_pix.setVisible(True)
                            x = air_info['x']
                            y = air_info['y']
                            self.ui.tab1_own_pix.setGeometry(x+180,y+140,25,10)  #180,140为原点
                        else:
                            x = air_info['x']
                            y = air_info['y']
                            x_geo = 180 + int(1.5*x)
                            if y >= 0:
                                y_geo = 130 - int(y/(160*2)*100)
                            else:
                                y_geo = 130 + int(y/(160*2)*100)
                            if y_geo >= 45 and y_geo <= 245 and x_geo >= 40 and x_geo <= 350:
                                eval("self.ui.tab1_target" + str(target_index)+"_pix.setVisible(True)")
                                eval("self.ui.tab1_target" + str(target_index) + "_info.setVisible(True)")
                                air_color = air_info['color']
                                if air_color == '#FFFFFF':  # 白色
                                    eval("self.ui.tab1_target" + str(target_index) + "_pix").setPixmap(QPixmap("pic/qtfeiji0.png"))
                                    eval("self.ui.tab1_target" + str(target_index) + "_info").setStyleSheet(
                                        "color:white;background-color:transparent;font-size:10px")
                                if air_color == '#FFFF00':  # 黄色
                                    eval("self.ui.tab1_target" + str(target_index) + "_pix").setPixmap(QPixmap("pic/qtfeiji1.png"))
                                    eval("self.ui.tab1_target" + str(target_index) + "_info").setStyleSheet("color:yellow;background-color:transparent;font-size:10px")
                                if air_color == '#FF0000':  # 红色
                                    eval("self.ui.tab1_target" + str(target_index) + "_pix").setPixmap(QPixmap("pic/qtfeiji2.png"))
                                    eval("self.ui.tab1_target" + str(target_index) + "_info").setStyleSheet(
                                        "color:red;background-color:transparent;font-size:10px")
                                if air_color == '#00FF00':  # 绿色
                                    eval("self.ui.tab1_target" + str(target_index) + "_pix").setPixmap(QPixmap("pic/qtfeiji3.png"))
                                    eval("self.ui.tab1_target" + str(target_index) + "_info").setStyleSheet(
                                        "color:green;background-color:transparent;font-size:10px")
                                eval("self.ui.tab1_target" + str(target_index) + "_pix").setGeometry(x_geo, y_geo, 25, 10)
                                describe = air_info['describe']
                                eval("self.ui.tab1_target" + str(target_index) + "_info").setText("    "+describe)
                                eval("self.ui.tab1_target" + str(target_index) + "_info").setGeometry(x_geo-20,y_geo+10, 66, 20)
                                target_index += 1
                if item['id'] == '020301':  # 本机及目标机高度层展示  408*324
                    target_index = 1  # 目标机索引
                    for air_info in item['value']:
                        air_type = air_info['isSelf']  # 1为本机，0为目标机
                        if air_type:  # 本机默认为白色
                            self.ui.tab2_own_pix.setVisible(True)
                            x = air_info['x']
                            y = air_info['y']
                            self.ui.tab2_own_pix.setGeometry(x + 205, y + 145, 25, 10)  # 205,145为原点
                        else:
                            x = air_info['x']
                            y = air_info['y']
                            x_geo = 205 + int(x*145/380)
                            if y>=0:
                                y_geo = 145 - int(y*60/268)
                            else:
                                y_geo = 145 + int(y*60/268)
                            if y_geo>=30 and y_geo<=275 and x_geo>=45 and x_geo<=355:
                                eval("self.ui.tab2_target" + str(target_index) + "_pix.setVisible(True)")
                                eval("self.ui.tab2_target" + str(target_index) + "_info.setVisible(True)")
                                air_color = air_info['color']
                                if air_color == '#FFFFFF':  # 白色
                                    eval("self.ui.tab2_target" + str(target_index) + "_pix").setPixmap(
                                        QPixmap("pic/qtfeiji0.png"))
                                    eval("self.ui.tab2_target" + str(target_index) + "_info").setStyleSheet(
                                        "color:white;background-color:transparent;font-size:10px")
                                if air_color == '#FFFF00':  # 黄色
                                    eval("self.ui.tab2_target" + str(target_index) + "_pix").setPixmap(
                                        QPixmap("pic/qtfeiji1.png"))
                                    eval("self.ui.tab2_target" + str(target_index) + "_info").setStyleSheet(
                                        "color:yellow;background-color:transparent;font-size:10px")
                                if air_color == '#FF0000':  # 红色
                                    eval("self.ui.tab2_target" + str(target_index) + "_pix").setPixmap(
                                        QPixmap("pic/qtfeiji2.png"))
                                    eval("self.ui.tab2_target" + str(target_index) + "_info").setStyleSheet(
                                        "color:red;background-color:transparent;font-size:10px")
                                if air_color == '#00FF00':  # 绿色
                                    eval("self.ui.tab2_target" + str(target_index) + "_pix").setPixmap(
                                        QPixmap("pic/qtfeiji3.png"))
                                    eval("self.ui.tab2_target" + str(target_index) + "_info").setStyleSheet(
                                        "color:green;background-color:transparent;font-size:10px")
                                eval("self.ui.tab2_target" + str(target_index) + "_pix").setGeometry(x_geo, y_geo, 25,10)
                                describe = air_info['describe']
                                eval("self.ui.tab2_target" + str(target_index) + "_info").setText("    " + describe)
                                eval("self.ui.tab2_target" + str(target_index) + "_info").setGeometry(x_geo-20, y_geo+10, 66,20)
                                target_index += 1
                # server1
                if item['id'] == '010101':  # 界面1目标机列表 done
                    target_num = len(item['value']['content'])  # 目标机数量
                    self.ui.tabelWidget_1.setRowCount(target_num + 1)  # 设置tabelWidget_1行数
                    ownship_id = item['value']['header'][0]
                    ownship_alt = item['value']['header'][1]
                    ownship_lon = item['value']['header'][2]
                    ownship_lat = item['value']['header'][3]
                    if self.old_ownship_id!= ownship_id:
                        self.browser.page().runJavaScript("remove_overlay();")
                        js_string_own_init = '''init_ownship(%f,%f,'%s');''' % (
                            float(ownship_lon), float(ownship_lat), ownship_id)
                        self.browser.page().runJavaScript(js_string_own_init)
                        self.old_ownship_id = ownship_id
                    ownship_speed = item['value']['header'][4]
                    ownship_v_speed = item['value']['header'][5]
                    ownship_angle = item['value']['header'][6]
                    ownship_id_item = QTableWidgetItem(ownship_id)
                    ownship_id_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 居中显示
                    ownship_id_item.setForeground(QColor(255, 255, 255))  # 白色背景
                    ownship_alt_item = QTableWidgetItem(ownship_alt)
                    ownship_alt_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    ownship_alt_item.setForeground(QColor(255, 255, 255))
                    ownship_lon_item = QTableWidgetItem(ownship_lon)
                    ownship_lon_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    ownship_lon_item.setForeground(QColor(255, 255, 255))
                    ownship_lat_item = QTableWidgetItem(ownship_lat)
                    ownship_lat_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    ownship_lat_item.setForeground(QColor(255, 255, 255))
                    ownship_speed_item = QTableWidgetItem(ownship_speed)
                    ownship_speed_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    ownship_speed_item.setForeground(QColor(255, 255, 255))
                    ownship_v_speed_item = QTableWidgetItem(ownship_v_speed)
                    ownship_v_speed_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    ownship_v_speed_item.setForeground(QColor(255, 255, 255))
                    ownship_angle_item = QTableWidgetItem(ownship_angle)
                    ownship_angle_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                    ownship_angle_item.setForeground(QColor(255, 255, 255))
                    self.ui.tabelWidget_1.setItem(0, 0, ownship_id_item)
                    self.ui.tabelWidget_1.setItem(0, 1, ownship_alt_item)
                    self.ui.tabelWidget_1.setItem(0, 2, ownship_lon_item)
                    self.ui.tabelWidget_1.setItem(0, 3, ownship_lat_item)
                    self.ui.tabelWidget_1.setItem(0, 4, ownship_speed_item)
                    self.ui.tabelWidget_1.setItem(0, 5, ownship_v_speed_item)
                    self.ui.tabelWidget_1.setItem(0, 6, ownship_angle_item)
                    # 目标机
                    for index in range(0, target_num):
                        target_id = item['value']['content'][index][0]
                        target_alt = item['value']['content'][index][1]
                        target_lon = item['value']['content'][index][2]
                        target_lat = item['value']['content'][index][3]
                        if self.old_target_id[index] != target_id:
                            # self.browser.page().runJavaScript("remove_overlay();")
                            js_string_target_init = '''init_target(%d,%f,%f,'%s');''' % (
                                index + 1, float(target_lon), float(target_lat), target_id)
                            print(js_string_target_init)
                            self.browser.page().runJavaScript(js_string_target_init)
                            self.old_target_id[index] = target_id
                        target_speed = item['value']['content'][index][4]
                        target_v_speed = item['value']['content'][index][5]
                        target_angle = item['value']['content'][index][6]
                        target_id_item = QTableWidgetItem(target_id)
                        target_id_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)  # 居中显示
                        target_id_item.setForeground(QColor(255, 255, 255))  # 白色背景
                        target_alt_item = QTableWidgetItem(target_alt)
                        target_alt_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                        target_alt_item.setForeground(QColor(255, 255, 255))
                        target_lon_item = QTableWidgetItem(target_lon)
                        target_lon_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                        target_lon_item.setForeground(QColor(255, 255, 255))
                        target_lat_item = QTableWidgetItem(target_lat)
                        target_lat_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                        target_lat_item.setForeground(QColor(255, 255, 255))
                        target_speed_item = QTableWidgetItem(target_speed)
                        target_speed_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                        target_speed_item.setForeground(QColor(255, 255, 255))
                        target_v_speed_item = QTableWidgetItem(target_v_speed)
                        target_v_speed_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                        target_v_speed_item.setForeground(QColor(255, 255, 255))
                        target_angle_item = QTableWidgetItem(target_angle)
                        target_angle_item.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                        target_angle_item.setForeground(QColor(255, 255, 255))
                        self.ui.tabelWidget_1.setItem(index + 1, 0, target_id_item)
                        self.ui.tabelWidget_1.setItem(index + 1, 1, target_alt_item)
                        self.ui.tabelWidget_1.setItem(index + 1, 2, target_lon_item)
                        self.ui.tabelWidget_1.setItem(index + 1, 3, target_lat_item)
                        self.ui.tabelWidget_1.setItem(index + 1, 4, target_speed_item)
                        self.ui.tabelWidget_1.setItem(index + 1, 5, target_v_speed_item)
                        self.ui.tabelWidget_1.setItem(index + 1, 6, target_angle_item)
                if item['id'] == '010501':  # 避撞信息提示 done
                    self.ui.label_9.setText(item['value'])
                if item['id'] == '010301':  # 刻度尺的高度值 done
                    self.ui.angle_kedu_txt.setText(str(int(item['value'])))
                    self.ui.listWidget_1.setCurrentRow(516 - int(item['value'] / 100))
                if item['id'] == '010305':  # 3个高度层文本 done
                    self.ui.alt_label1.setText(item['value'][2])
                    self.ui.alt_label2.setText(item['value'][1])
                    self.ui.alt_label3.setText(item['value'][0])
                if item['id'] == '010306':  # 警戒范围及颜色
                    for item_info in item['value']:
                        lowerBound = int(item_info['lowerBound'])
                        upperBound = int(item_info['upperBound'])
                        status = item_info['status']
                        if lowerBound < 0:
                            lowerBound = 0
                        if upperBound < 0:
                            upperBound = 0
                        # print(status, lowerBound, upperBound)
                        lower_index = int((50000 - lowerBound) / 100)
                        upper_index = int((50000 - upperBound) / 100)
                        if status == 0:  # 999999 灰色
                            for i in range(upper_index, lower_index):
                                self.ui.listWidget_1.itemWidget(self.ui.listWidget_1.item(i)).setStyleSheet(
                                    "color:white;background-color:gray")
                        if status == 1 or status == 2:  # ffff00  黄色
                            for i in range(upper_index, lower_index):
                                self.ui.listWidget_1.itemWidget(self.ui.listWidget_1.item(i)).setStyleSheet(
                                    "color:white;background-color:#cccc33")
                        if status == 3:  # ff0000 红色
                            for i in range(upper_index, lower_index):
                                self.ui.listWidget_1.itemWidget(self.ui.listWidget_1.item(i)).setStyleSheet(
                                    "color:white;background-color:#ff0000")
                        if status == 4:  # 00ff00 绿色
                            for i in range(upper_index, lower_index):
                                self.ui.listWidget_1.itemWidget(self.ui.listWidget_1.item(i)).setStyleSheet(
                                    "color:white;background-color:lightgreen")
                if item['id'] == '020201':  # RA/TA/CLC文本 done
                    self.ui.textBrowser.setText(item['value']['ra']['location1'])
                    self.ui.textBrowser_2.setText(item['value']['ra']['location2'])
                    self.ui.textBrowser_3.setText(item['value']['ra']['speed'])
                if item['id'] == '020302':  # 5个高度层文本 done
                    self.ui.alt_label1_2.setText(item['value'][4])
                    self.ui.alt_label2_2.setText(item['value'][3])
                    self.ui.alt_label3_2.setText(item['value'][2]) 
                    self.ui.alt_label4.setText(item['value'][1])
                    self.ui.alt_label5.setText(item['value'][0])
                # server2
                if item['id'] == '010201':  # 旋转角度 文本 done
                    self.ui.txt_angle.setText(str(int(item['value'])))
                if item['id'] == '010202':  # 入侵机列表 在罗盘中绘制入侵机
                    for flight_id in self.tab1_dict_temp: #visible false
                        eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setVisible(False)")
                    for item_info in item['value']:
                        flight_id = item_info['flightID']
                        if flight_id not in self.old_tab1_target_id_list:
                            self.old_tab1_target_id_list.append(flight_id)
                            # create
                            # self.tab1_target1_item = QGraphicsPixmapItem()
                            # self.tab1_target1_item.setVisible()
                            exec("self.tab1_target" + str(self.tab1_new_num + 1) + "_item = QGraphicsPixmapItem()")
                            exec("self.scene_2.addItem(self.tab1_target"+str(self.tab1_new_num+1)+"_item)")
                            self.tab1_dict_temp[flight_id] =self.tab1_new_num+1
                            self.tab1_new_num+=1
                        else:
                            x = item_info['x']
                            y = item_info['y']
                            angle = item_info['dir']
                            status = item_info['status']
                            x_view = 130 + 150 * x
                            y_view = 130 + 150 * y
                            y_view = 300 - y_view
                            #先判断入侵机坐标范围 300*300
                            if x_view < 15 or y_view < 20 or x_view > 285 or y_view > 280:
                                pass
                            else:
                                eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setVisible(True)")
                                if status == 0:  # 999999 灰色
                                    gray_pix = QPixmap("pic/target-gray.png")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setPixmap(gray_pix)")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setPos(x_view, y_view)")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setRotation(angle*180/3.14)")
                                if status == 1 or status == 2:  # ffff00  黄色
                                    yellow_pix = QPixmap("pic/target-yellow.png")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setPixmap(yellow_pix)")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setPos(x_view, y_view)")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setRotation(angle*180/3.14)")
                                if status == 3:  # ff0000 红色
                                    red_pix = QPixmap("pic/target-red.png")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setPixmap(red_pix)")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setPos(x_view, y_view)")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setRotation(angle*180/3.14)")
                                if status == 4:  # 00ff00 绿色
                                    green_pix = QPixmap("pic/target-green.png")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setPixmap(green_pix)")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setPos(x_view, y_view)")
                                    eval("self.tab1_target" + str(self.tab1_dict_temp[flight_id]) + "_item.setRotation(angle*180/3.14)")
                if item['id'] == '010203':  # 罗盘弧度绘制 done
                    self.ARC_item.update_arc(item['value'])
                if item['id'] == '010204':  # 罗盘旋转角度 done
                    self.compass1_item.setAngle(360 - int(item['value']))
                if item['id'] == '010205':  # 本机地速 done
                    self.ui.label_6.setText(str(int(item['value'])))
                    self.ui.listWidget_2.setCurrentRow(700+17 - int(item['value']))  # 刻度标移动
                if item['id'] == '010206':  # 地速警戒范围及颜色
                    for item_info in item['value']:
                        lowerBound = int(item_info['lowerBound'])
                        upperBound = int(item_info['upperBound'])
                        status = item_info['status']
                        # print("lowerBound:"+str(lowerBound))
                        # print("upperBound:" + str(upperBound))
                        # print("status:" + str(status))
                        lower_index = int(700 - lowerBound)
                        upper_index = int(700 - upperBound)
                        # print(lower_index)
                        # print(upper_index)
                        if status == 0:  # 999999 灰色
                            for i in range(upper_index, lower_index + 1):
                                self.ui.listWidget_2.itemWidget(self.ui.listWidget_2.item(i)).setStyleSheet(
                                    "color:white;background-color:gray")
                        if status == 1 or status == 2:  # ffff00  黄色
                            for i in range(upper_index, lower_index + 1):
                                self.ui.listWidget_2.itemWidget(self.ui.listWidget_2.item(i)).setStyleSheet(
                                    "color:white;background-color:#cccc33")
                        if status == 3:  # ff0000 红色
                            for i in range(upper_index, lower_index + 1):
                                self.ui.listWidget_2.itemWidget(self.ui.listWidget_2.item(i)).setStyleSheet(
                                    "color:white;background-color:#ff0000")
                        if status == 4:  # 00ff00 绿色
                            for i in range(upper_index, lower_index + 1):
                                self.ui.listWidget_2.itemWidget(self.ui.listWidget_2.item(i)).setStyleSheet(
                                    "color:white;background-color:lightgreen")
                if item['id'] == '020103':  # 罗盘步长 done
                    self.ui.label_step1.setText(str(item['value'] * 2))
                    self.ui.label_step2.setText(str(item['value']))
                    self.ui.label_step3.setText(str(item['value'] * -1))
                    self.ui.label_step4.setText(str(item['value'] * -2))
                    self.ui.label_step4_2.setText(str(item['value'] * 2))
                    self.ui.label_step4_3.setText(str(item['value']))
                    self.ui.label_step4_5.setText(str(item['value'] * -1))
                    self.ui.label_step4_6.setText(str(item['value'] * -2))
                    self.ui.label_step4_1.setText(str(item['value'] * 2))
                    self.ui.label_step4_7.setText(str(item['value']))
                    self.ui.label_step4_8.setText(str(item['value'] * -1))
                    self.ui.label_step4_10.setText(str(item['value'] * -2))
                if item['id'] == '020104':  # 飞机信息列表 done
                    self.ui.label_11.setText(str(item['value']['location']))
                    self.ui.label_12.setText(str(item['value']['description']))
                if item['id'] == '020105':  # 罗盘弧度绘制 done
                    self.ARC2_item.update_arc(item['value'])
                if item['id'] == '020101':  # 旋转角度 done
                    self.ui.angle_txt.setText(str(int(item['value'])))
                    self.compass2_item.setAngle(360 - int(item['value']))
                if item['id'] == '020102':  # 入侵机列表 在罗盘中绘制入侵机
                    for flight_id in self.tab2_dict_temp:#visible false
                        eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setVisible(False)")
                    for item_info in item['value']:
                        flight_id = item_info['flightID']
                        if flight_id not in self.old_tab2_target_id_list:
                            self.old_tab2_target_id_list.append(flight_id)
                            # create
                            exec("self.tab2_target" + str(self.tab2_new_num + 1) + "_item = QGraphicsPixmapItem()")
                            exec("self.scene_5.addItem(self.tab2_target" + str(self.tab2_new_num + 1) + "_item)")
                            self.tab2_dict_temp[flight_id] = self.tab2_new_num + 1
                            self.tab2_new_num += 1
                        else:
                            x = item_info['x']
                            y = item_info['y']
                            angle = item_info['dir']
                            status = item_info['status']
                            x_view = 220 + 240 * x
                            y_view = 220 + 240 * y
                            y_view = 480 - y_view
                            # 先判断入侵机坐标范围 480*480
                            if x_view < 15 or y_view < 15 or x_view > 465 or y_view > 465:
                                # eval("self.scene_5.removeItem(self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item)")
                                # print("delete tab2 target index: " + str(self.tab2_dict_temp[flight_id]))
                                pass
                            else:
                                eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setVisible(True)")
                                if status == 0:  # 999999 灰色
                                    gray_pix = QPixmap("pic/target-gray.png")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setPixmap(gray_pix)")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setPos(x_view, y_view)")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setRotation(angle*180/3.14)")
                                if status == 1 or status == 2:  # ffff00  黄色
                                    yellow_pix = QPixmap("pic/target-yellow.png")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setPixmap(yellow_pix)")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setPos(x_view, y_view)")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setRotation(angle*180/3.14)")
                                if status == 3:  # ff0000 红色
                                    red_pix = QPixmap("pic/target-red.png")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setPixmap(red_pix)")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setPos(x_view, y_view)")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setRotation(angle*180/3.14)")
                                if status == 4:  # 00ff00 绿色
                                    green_pix = QPixmap("pic/target-green.png")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setPixmap(green_pix)")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setPos(x_view, y_view)")
                                    eval("self.tab2_target" + str(self.tab2_dict_temp[flight_id]) + "_item.setRotation(angle*180/3.14)")
                if item['id'] == '010401':  # 地图绘制飞机
                    temp = 0
                    for item in item['value']:
                        angle = item['dir']
                        id = item['flightID']
                        isself = item['isSelf']
                        if isself == True:  # 绘制本机
                            js_string_own_update = '''update_own_position(%f,%f,%d);''' % (
                                item['lon'], item['lat'], angle)
                            # print(js_string_own_update)
                            self.browser.page().runJavaScript(js_string_own_update)
                        else:  # 绘制入侵机
                            js_string_target_update = '''update_target_position(%d,%f,%f,%d);''' % (
                                temp + 1, item['lon'], item['lat'], angle)
                            # print(js_string_target_update)
                            self.browser.page().runJavaScript(js_string_target_update)
                            temp += 1
        except:
            traceback.print_exc()




if __name__=='__main__':
    import sys
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    form1 = MainWindow()
    form1.show()
    sys.exit(app.exec_())
