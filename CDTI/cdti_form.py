import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import*
import cdti_mainform
class MainWindow(QMainWindow):


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.rotateAngle = 0  # 每次旋转角度
        self.map_widgetItem = 0
        self.surf_compass_Item = 0
        self.airb_compass_Item = 0
        self.vsa_compass_Item = 0
        self.initUI()
        #设置定时器 每50ms旋转一次
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.slotTimeout)
        self.timer.start(1000)

    def slotTimeout(self):
        self.rotateAngle = (self.rotateAngle+5)%360
        self.map_widgetItem.setRotation(self.rotateAngle)
        self.airb_compass_Item.setRotation(self.rotateAngle)
        self.vsa_compass_Item.setRotation(self.rotateAngle)
        #self.surf_compass_Item.setRotation(self.rotateAngle+45)

    def initUI(self):
        self.ui = cdti_mainform.Ui_MainWindow()
        self.ui.setupUi(self)

        #通用图片初始化
        pixmap_ownship =  QPixmap("pic/ownship.png")
        pixmap_border = QPixmap("pic/b.png") #外轮廓
        scaledPixmap_border = pixmap_border.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatioByExpanding)
        pixmap_compass_transparent = QPixmap("pic/罗盘-透明背景.png") #透明罗盘
        scaledPixmap_compass_transparent = pixmap_compass_transparent.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatio)
        pixmap_compass_black = QPixmap("pic/罗盘-黑色背景.png")    #背景色为黑色罗盘
        scaledPixmap_compass_black = pixmap_compass_black.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatio)


        #airb
        self.ui.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_airb = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_airb.setStyleSheet("background: transparent")
        self.ui.horizontalLayout_2.addWidget(self.ui.graphicsView_airb)
        airb_scene = QGraphicsScene(self)
        #scene场景依次加入3个item
        self.airb_border_Item = airb_scene.addPixmap(scaledPixmap_border) #1
        self.airb_compass_Item = airb_scene.addPixmap(scaledPixmap_compass_black) #2
        self.airb_ownship_item = airb_scene.addPixmap(pixmap_ownship)#3
        #设置Item位置
        self.airb_compass_Item.setPos(0,45)
        self.airb_ownship_item.setPos(320-15,320+17.5)
        self.ui.graphicsView_airb.setScene(airb_scene)
        self.ui.graphicsView_airb.setSceneRect(1, 1, 715, 715)
        #设置罗盘旋转
        centerPos = self.airb_compass_Item.boundingRect().center()
        #设置旋转中心
        self.airb_compass_Item.setTransformOriginPoint(centerPos)
        # self.airb_compass_Item.setRotation(10)

        #surf
        self.ui.horizontalLayoutWidget.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_surf = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_surf.setStyleSheet("background: transparent")
        self.ui.horizontalLayout.addWidget(self.ui.graphicsView_surf)
        url = os.getcwd() + '/map_surf.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.browser.resize(640,640)
        surf_scene = QGraphicsScene(self)
        #scene场景依次加入4个item
        self.map_widgetItem = surf_scene.addWidget(self.browser) # 1
        self.surf_border_Item = surf_scene.addPixmap(scaledPixmap_border) #2
        self.surf_compass_Item = surf_scene.addPixmap(scaledPixmap_compass_transparent) #3
        self.surf_ownship_item = surf_scene.addPixmap(pixmap_ownship)    #4
        #设置Item位置
        self.surf_ownship_item.setPos(320-15,320+17.5)
        #self.surf_border_Item.setPos(0, 0)
        self.map_widgetItem.setPos(0,45)
        self.surf_compass_Item.setPos(0,45)
        #获取旋转中心 得到一个QPointF对象
        centerPos_A = self.map_widgetItem.boundingRect().center()
        centerPos_B = self.surf_compass_Item.boundingRect().center()
        #设置旋转中心
        self.map_widgetItem.setTransformOriginPoint(centerPos_A)
        self.surf_compass_Item.setTransformOriginPoint(centerPos_B)
        # self.map_widgetItem.setRotation(10)
        # self.surf_compass_Item.setRotation(10)
        #设置item图层位置
        self.map_widgetItem.stackBefore(self.surf_border_Item)
        self.ui.graphicsView_surf.setScene(surf_scene)
        self.ui.graphicsView_surf.setSceneRect(1, 1, 715, 715)

        #vsa
        self.ui.horizontalLayoutWidget_3.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_vsa = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_vsa.setStyleSheet("background: transparent")
        self.ui.horizontalLayout_3.addWidget(self.ui.graphicsView_vsa)
        vsa_scene = QGraphicsScene(self)
        # scene场景依次加入3个item
        self.vsa_border_Item = vsa_scene.addPixmap(scaledPixmap_border)  # 1
        self.vsa_compass_Item = vsa_scene.addPixmap(scaledPixmap_compass_black)  # 2
        self.vsa_ownship_item = vsa_scene.addPixmap(pixmap_ownship)  # 3
        # 设置Item位置
        self.vsa_compass_Item.setPos(0, 45)
        self.vsa_ownship_item.setPos(320 - 15, 320 + 17.5)
        self.ui.graphicsView_vsa.setScene(vsa_scene)
        self.ui.graphicsView_vsa.setSceneRect(1, 1, 715, 715)
        # 设置罗盘旋转
        centerPos = self.vsa_compass_Item.boundingRect().center()
        # 设置旋转中心
        self.vsa_compass_Item.setTransformOriginPoint(centerPos)
        # self.vsa_compass_Item.setRotation(10)

        #itp
        self.ui.horizontalLayoutWidget_4.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView_itp = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView_itp.setStyleSheet("background: transparent")
        self.ui.horizontalLayout_4.addWidget(self.ui.graphicsView_itp)
        itp_scene = QGraphicsScene(self)
        # scene场景依次加入3个item
        self.itp_border_Item = itp_scene.addPixmap(scaledPixmap_border)  # 1
        self.itp_compass_Item = itp_scene.addPixmap(scaledPixmap_compass_black)  # 2
        self.itp_ownship_item = itp_scene.addPixmap(pixmap_ownship)  # 3
        # 设置Item位置
        self.itp_compass_Item.setPos(0, 45)
        self.itp_ownship_item.setPos(320 - 15, 320 + 17.5)
        self.ui.graphicsView_itp.setScene(itp_scene)
        self.ui.graphicsView_itp.setSceneRect(1, 1, 715, 715)
        # 设置罗盘旋转
        centerPos = self.itp_compass_Item.boundingRect().center()
        # 设置旋转中心
        self.itp_compass_Item.setTransformOriginPoint(centerPos)
        # self.vsa_compass_Item.setRotation(10)



if __name__=='__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())