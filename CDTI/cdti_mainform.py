# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cdti_mainform.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 950)
        MainWindow.setMinimumSize(QtCore.QSize(1380, 950))
        MainWindow.setMaximumSize(QtCore.QSize(1380, 950))
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1351, 901))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_AIRB = QtWidgets.QWidget()
        self.tab_AIRB.setObjectName("tab_AIRB")
        self.frame_2 = QtWidgets.QFrame(self.tab_AIRB)
        self.frame_2.setGeometry(QtCore.QRect(680, 20, 641, 831))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_20 = QtWidgets.QLabel(self.frame_2)
        self.label_20.setGeometry(QtCore.QRect(40, 40, 121, 16))
        self.label_20.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(40, 70, 161, 16))
        self.label_21.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_2)
        self.label_22.setGeometry(QtCore.QRect(40, 100, 161, 16))
        self.label_22.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(70, 130, 211, 16))
        self.label_23.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_23.setObjectName("label_23")
        self.frame_airb = QtWidgets.QFrame(self.tab_AIRB)
        self.frame_airb.setGeometry(QtCore.QRect(10, 20, 641, 821))
        self.frame_airb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_airb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_airb.setObjectName("frame_airb")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_airb)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 591, 541))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.frame_airb)
        self.frame_9.setGeometry(QtCore.QRect(0, 710, 641, 111))
        self.frame_9.setStyleSheet("color:rgb(255, 255, 255)")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setLineWidth(1)
        self.frame_9.setObjectName("frame_9")
        self.label_37 = QtWidgets.QLabel(self.frame_9)
        self.label_37.setGeometry(QtCore.QRect(30, 20, 121, 16))
        self.label_37.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame_9)
        self.label_38.setGeometry(QtCore.QRect(30, 50, 121, 16))
        self.label_38.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.frame_9)
        self.label_39.setGeometry(QtCore.QRect(380, 70, 51, 16))
        self.label_39.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.frame_9)
        self.label_40.setGeometry(QtCore.QRect(380, 20, 131, 16))
        self.label_40.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_40.setObjectName("label_40")
        self.btn_zoom_add_5 = QtWidgets.QPushButton(self.frame_9)
        self.btn_zoom_add_5.setGeometry(QtCore.QRect(420, 60, 31, 31))
        self.btn_zoom_add_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/+.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_add_5.setIcon(icon)
        self.btn_zoom_add_5.setObjectName("btn_zoom_add_5")
        self.btn_zoom_reduce_5 = QtWidgets.QPushButton(self.frame_9)
        self.btn_zoom_reduce_5.setGeometry(QtCore.QRect(450, 60, 31, 31))
        self.btn_zoom_reduce_5.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/-.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_reduce_5.setIcon(icon1)
        self.btn_zoom_reduce_5.setObjectName("btn_zoom_reduce_5")
        self.label_41 = QtWidgets.QLabel(self.frame_9)
        self.label_41.setGeometry(QtCore.QRect(30, 80, 121, 16))
        self.label_41.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_41.setObjectName("label_41")
        self.tabWidget.addTab(self.tab_AIRB, "")
        self.tab_SURF = QtWidgets.QWidget()
        self.tab_SURF.setObjectName("tab_SURF")
        self.frame_surf = QtWidgets.QFrame(self.tab_SURF)
        self.frame_surf.setGeometry(QtCore.QRect(10, 20, 641, 821))
        self.frame_surf.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_surf.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_surf.setObjectName("frame_surf")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_surf)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_8 = QtWidgets.QFrame(self.frame_surf)
        self.frame_8.setGeometry(QtCore.QRect(0, 710, 641, 111))
        self.frame_8.setStyleSheet("color:rgb(255, 255, 255)")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setLineWidth(1)
        self.frame_8.setObjectName("frame_8")
        self.label_32 = QtWidgets.QLabel(self.frame_8)
        self.label_32.setGeometry(QtCore.QRect(30, 20, 121, 16))
        self.label_32.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_8)
        self.label_33.setGeometry(QtCore.QRect(30, 50, 121, 16))
        self.label_33.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_8)
        self.label_34.setGeometry(QtCore.QRect(380, 70, 51, 16))
        self.label_34.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_8)
        self.label_35.setGeometry(QtCore.QRect(380, 20, 131, 16))
        self.label_35.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_35.setObjectName("label_35")
        self.btn_zoom_in_surf = QtWidgets.QPushButton(self.frame_8)
        self.btn_zoom_in_surf.setGeometry(QtCore.QRect(420, 60, 31, 31))
        self.btn_zoom_in_surf.setText("")
        self.btn_zoom_in_surf.setIcon(icon)
        self.btn_zoom_in_surf.setObjectName("btn_zoom_in_surf")
        self.btn_zoom_out_surf = QtWidgets.QPushButton(self.frame_8)
        self.btn_zoom_out_surf.setGeometry(QtCore.QRect(450, 60, 31, 31))
        self.btn_zoom_out_surf.setText("")
        self.btn_zoom_out_surf.setIcon(icon1)
        self.btn_zoom_out_surf.setObjectName("btn_zoom_out_surf")
        self.label_36 = QtWidgets.QLabel(self.frame_8)
        self.label_36.setGeometry(QtCore.QRect(30, 80, 121, 16))
        self.label_36.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_36.setObjectName("label_36")
        self.frame_3 = QtWidgets.QFrame(self.tab_SURF)
        self.frame_3.setGeometry(QtCore.QRect(680, 20, 641, 831))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(40, 40, 121, 16))
        self.label_24.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_3)
        self.label_25.setGeometry(QtCore.QRect(40, 70, 161, 16))
        self.label_25.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_3)
        self.label_26.setGeometry(QtCore.QRect(40, 100, 161, 16))
        self.label_26.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        self.label_27.setGeometry(QtCore.QRect(70, 130, 211, 16))
        self.label_27.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_27.setObjectName("label_27")
        self.tabWidget.addTab(self.tab_SURF, "")
        self.tab_VSA = QtWidgets.QWidget()
        self.tab_VSA.setObjectName("tab_VSA")
        self.frame_vsa = QtWidgets.QFrame(self.tab_VSA)
        self.frame_vsa.setGeometry(QtCore.QRect(10, 20, 641, 821))
        self.frame_vsa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vsa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vsa.setObjectName("frame_vsa")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_vsa)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 591, 541))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(self.frame_vsa)
        self.frame_10.setGeometry(QtCore.QRect(0, 710, 641, 111))
        self.frame_10.setStyleSheet("color:rgb(255, 255, 255)")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_10.setLineWidth(1)
        self.frame_10.setObjectName("frame_10")
        self.label_42 = QtWidgets.QLabel(self.frame_10)
        self.label_42.setGeometry(QtCore.QRect(30, 20, 121, 16))
        self.label_42.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.frame_10)
        self.label_43.setGeometry(QtCore.QRect(30, 50, 121, 16))
        self.label_43.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame_10)
        self.label_44.setGeometry(QtCore.QRect(380, 70, 51, 16))
        self.label_44.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.frame_10)
        self.label_45.setGeometry(QtCore.QRect(380, 20, 131, 16))
        self.label_45.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_45.setObjectName("label_45")
        self.btn_zoom_add_6 = QtWidgets.QPushButton(self.frame_10)
        self.btn_zoom_add_6.setGeometry(QtCore.QRect(420, 60, 31, 31))
        self.btn_zoom_add_6.setText("")
        self.btn_zoom_add_6.setIcon(icon)
        self.btn_zoom_add_6.setObjectName("btn_zoom_add_6")
        self.btn_zoom_reduce_6 = QtWidgets.QPushButton(self.frame_10)
        self.btn_zoom_reduce_6.setGeometry(QtCore.QRect(450, 60, 31, 31))
        self.btn_zoom_reduce_6.setText("")
        self.btn_zoom_reduce_6.setIcon(icon1)
        self.btn_zoom_reduce_6.setObjectName("btn_zoom_reduce_6")
        self.label_46 = QtWidgets.QLabel(self.frame_10)
        self.label_46.setGeometry(QtCore.QRect(30, 80, 121, 16))
        self.label_46.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_46.setObjectName("label_46")
        self.frame_4 = QtWidgets.QFrame(self.tab_VSA)
        self.frame_4.setGeometry(QtCore.QRect(680, 20, 641, 831))
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_28 = QtWidgets.QLabel(self.frame_4)
        self.label_28.setGeometry(QtCore.QRect(40, 40, 121, 16))
        self.label_28.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame_4)
        self.label_29.setGeometry(QtCore.QRect(40, 70, 161, 16))
        self.label_29.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_4)
        self.label_30.setGeometry(QtCore.QRect(40, 100, 161, 16))
        self.label_30.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_4)
        self.label_31.setGeometry(QtCore.QRect(70, 130, 211, 16))
        self.label_31.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_31.setObjectName("label_31")
        self.tabWidget.addTab(self.tab_VSA, "")
        self.tab_ITP = QtWidgets.QWidget()
        self.tab_ITP.setObjectName("tab_ITP")
        self.frame_itp = QtWidgets.QFrame(self.tab_ITP)
        self.frame_itp.setGeometry(QtCore.QRect(10, 20, 641, 821))
        self.frame_itp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_itp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_itp.setObjectName("frame_itp")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_itp)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 591, 541))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_11 = QtWidgets.QFrame(self.frame_itp)
        self.frame_11.setGeometry(QtCore.QRect(0, 710, 641, 111))
        self.frame_11.setStyleSheet("color:rgb(255, 255, 255)")
        self.frame_11.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_11.setLineWidth(1)
        self.frame_11.setObjectName("frame_11")
        self.label_47 = QtWidgets.QLabel(self.frame_11)
        self.label_47.setGeometry(QtCore.QRect(30, 20, 121, 16))
        self.label_47.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.frame_11)
        self.label_48.setGeometry(QtCore.QRect(30, 50, 121, 16))
        self.label_48.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.frame_11)
        self.label_49.setGeometry(QtCore.QRect(380, 70, 51, 16))
        self.label_49.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.frame_11)
        self.label_50.setGeometry(QtCore.QRect(380, 20, 131, 16))
        self.label_50.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_50.setObjectName("label_50")
        self.btn_zoom_add_7 = QtWidgets.QPushButton(self.frame_11)
        self.btn_zoom_add_7.setGeometry(QtCore.QRect(420, 60, 31, 31))
        self.btn_zoom_add_7.setText("")
        self.btn_zoom_add_7.setIcon(icon)
        self.btn_zoom_add_7.setObjectName("btn_zoom_add_7")
        self.btn_zoom_reduce_7 = QtWidgets.QPushButton(self.frame_11)
        self.btn_zoom_reduce_7.setGeometry(QtCore.QRect(450, 60, 31, 31))
        self.btn_zoom_reduce_7.setText("")
        self.btn_zoom_reduce_7.setIcon(icon1)
        self.btn_zoom_reduce_7.setObjectName("btn_zoom_reduce_7")
        self.label_51 = QtWidgets.QLabel(self.frame_11)
        self.label_51.setGeometry(QtCore.QRect(30, 80, 121, 16))
        self.label_51.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_51.setObjectName("label_51")
        self.frame_5 = QtWidgets.QFrame(self.tab_ITP)
        self.frame_5.setGeometry(QtCore.QRect(680, 20, 641, 831))
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_52 = QtWidgets.QLabel(self.frame_5)
        self.label_52.setGeometry(QtCore.QRect(40, 40, 121, 16))
        self.label_52.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.frame_5)
        self.label_53.setGeometry(QtCore.QRect(40, 70, 161, 16))
        self.label_53.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_53.setObjectName("label_53")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(20, 160, 601, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pic/ITP.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_zoom_add_8 = QtWidgets.QPushButton(self.frame_5)
        self.btn_zoom_add_8.setGeometry(QtCore.QRect(250, 650, 31, 31))
        self.btn_zoom_add_8.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("pic/triangle-l.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_add_8.setIcon(icon2)
        self.btn_zoom_add_8.setObjectName("btn_zoom_add_8")
        self.btn_zoom_reduce_8 = QtWidgets.QPushButton(self.frame_5)
        self.btn_zoom_reduce_8.setGeometry(QtCore.QRect(400, 650, 31, 31))
        self.btn_zoom_reduce_8.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pic/triangle-r.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_zoom_reduce_8.setIcon(icon3)
        self.btn_zoom_reduce_8.setObjectName("btn_zoom_reduce_8")
        self.tabWidget.addTab(self.tab_ITP, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1380, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_20.setText(_translate("MainWindow", "OWNSHIP POSITION:"))
        self.label_21.setText(_translate("MainWindow", "DISPLAY ALTITUDE RANGE:"))
        self.label_22.setText(_translate("MainWindow", "TARGETS:"))
        self.label_23.setText(_translate("MainWindow", "ID               GROUNDSPEED KT"))
        self.label_37.setText(_translate("MainWindow", "OwnShip Alt："))
        self.label_38.setText(_translate("MainWindow", "Time："))
        self.label_39.setText(_translate("MainWindow", "ZOOM:"))
        self.label_40.setText(_translate("MainWindow", "OwnShip FID："))
        self.label_41.setText(_translate("MainWindow", "APPL Status："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_AIRB), _translate("MainWindow", "AIRB"))
        self.label_32.setText(_translate("MainWindow", "OwnShip Alt："))
        self.label_33.setText(_translate("MainWindow", "Time："))
        self.label_34.setText(_translate("MainWindow", "ZOOM:"))
        self.label_35.setText(_translate("MainWindow", "OwnShip FID："))
        self.label_36.setText(_translate("MainWindow", "APPL Status："))
        self.label_24.setText(_translate("MainWindow", "OWNSHIP POSITION:"))
        self.label_25.setText(_translate("MainWindow", "DISPLAY ALTITUDE RANGE:"))
        self.label_26.setText(_translate("MainWindow", "TARGETS:"))
        self.label_27.setText(_translate("MainWindow", "ID               GROUNDSPEED KT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_SURF), _translate("MainWindow", "SURF"))
        self.label_42.setText(_translate("MainWindow", "OwnShip Alt："))
        self.label_43.setText(_translate("MainWindow", "Time："))
        self.label_44.setText(_translate("MainWindow", "ZOOM:"))
        self.label_45.setText(_translate("MainWindow", "OwnShip FID："))
        self.label_46.setText(_translate("MainWindow", "APPL Status："))
        self.label_28.setText(_translate("MainWindow", "OWNSHIP POSITION:"))
        self.label_29.setText(_translate("MainWindow", "DISPLAY ALTITUDE RANGE:"))
        self.label_30.setText(_translate("MainWindow", "TARGETS:"))
        self.label_31.setText(_translate("MainWindow", "ID               GROUNDSPEED KT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_VSA), _translate("MainWindow", "VSA"))
        self.label_47.setText(_translate("MainWindow", "OwnShip Alt："))
        self.label_48.setText(_translate("MainWindow", "Time："))
        self.label_49.setText(_translate("MainWindow", "ZOOM:"))
        self.label_50.setText(_translate("MainWindow", "OwnShip FID："))
        self.label_51.setText(_translate("MainWindow", "APPL Status："))
        self.label_52.setText(_translate("MainWindow", "OWNSHIP POSITION:"))
        self.label_53.setText(_translate("MainWindow", "DISPLAY ALTITUDE RANGE:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ITP), _translate("MainWindow", "ITP"))

