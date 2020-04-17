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
        self.count = 0
        self.map_widgetItem = 0
        self.surf_compass_Item = 0
        self.airb_compass_Item = 0
        self.vsa_compass_Item = 0
        self.targetAir1_Item = 0
        self.air1_text_Item = 0
        self.initUI()
        #设置定时器 每50ms旋转一次
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.slotTimeout)
        self.timer.start(1000)


    def slotTimeout(self):
        self.rotateAngle = (self.rotateAngle+5)%360
        self.count +=5
        self.map_widgetItem.setRotation(self.rotateAngle)
        self.airb_compass_Item.setRotation(self.rotateAngle)
        self.vsa_compass_Item.setRotation(self.rotateAngle)
        self.targetAir1_Item.setPos(0+self.count,0+self.count)
        self.air1_text_Item.setPos(0+self.count,20+self.count)
        #self.surf_compass_Item.setRotation(self.rotateAngle+45)

    def initUI(self):
        self.ui = cdti_mainform.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_zoom_in_surf.clicked.connect(self.map_zoom_in)
        self.ui.btn_zoom_out_surf.clicked.connect(self.map_zoom_out)
        #通用图片初始化
        pixmap_ownship =  QPixmap("pic/ownship.png")
        pixmap_border = QPixmap("pic/b.png") #外轮廓
        scaledPixmap_border = pixmap_border.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatioByExpanding)
        pixmap_compass_transparent = QPixmap("pic/罗盘-透明背景.png") #透明罗盘
        scaledPixmap_compass_transparent = pixmap_compass_transparent.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatio)
        pixmap_compass_black = QPixmap("pic/罗盘-黑色背景.png")    #背景色为黑色罗盘
        scaledPixmap_compass_black = pixmap_compass_black.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatio)
        pixmap_targetship1 = QPixmap("pic/air1.png")   #目标机

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
        self.ui.graphicsView_surf.setStyleSheet("padding: 0px; border: 0px;")
        self.ui.horizontalLayout.addWidget(self.ui.graphicsView_surf)
        url = os.getcwd() + '/map_surf.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.browser.resize(640,640)
        surf_scene = QGraphicsScene(self)
        label_air_heading = QLabel("54.7")
        label_air_heading.setStyleSheet("color:white;background-color:transparent")
        #scene场景依次加入6个item
        self.map_widgetItem = surf_scene.addWidget(self.browser) # 1
        self.surf_border_Item = surf_scene.addPixmap(scaledPixmap_border) #2
        self.surf_compass_Item = surf_scene.addPixmap(scaledPixmap_compass_transparent) #3
        self.surf_ownship_item = surf_scene.addPixmap(pixmap_ownship)    #4
        self.targetAir1_Item = surf_scene.addPixmap(pixmap_targetship1) #5
        self.surf_air_heading = surf_scene.addWidget(label_air_heading)

        #初始化一架目标飞机（文本信息部分）        #6
        frame_targetAir1 = QFrame()
        frame_targetAir1.setStyleSheet("background-color:transparent")
        frame_targetAir1.setLayout(self.ui.formLayout_targetair)
        self.air1_text_Item = surf_scene.addWidget(frame_targetAir1)
        self.air1_text_Item.setOpacity(0.9)

        #设置Item位置
        self.surf_ownship_item.setPos(320-15,320+17.5)
        self.map_widgetItem.setPos(0,45)
        self.surf_compass_Item.setPos(0,45)
        self.surf_air_heading.setPos(315,20)
        #self.targetAir1_Item.setPos(270,270)
        #self.air1_text_Item.setPos(270,290)
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
        self.targetAir1_Item.stackBefore(self.surf_ownship_item)
        self.air1_text_Item.stackBefore(self.surf_ownship_item)
        self.targetAir1_Item.stackBefore(self.surf_border_Item)
        self.air1_text_Item.stackBefore(self.surf_border_Item)
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
        self.ui.pic_air_itp500.setVisible(False)
        self.ui.pic_air_itp501.setVisible(False)
        self.ui.pic_air_itp502.setVisible(False)
        self.ui.pic_air_itp503.setVisible(False)
        self.ui.pic_air_itp504.setVisible(False)
        self.ui.pic_air_itp505.setVisible(False)
        self.ui.pic_air_itp506.setVisible(False)
        self.ui.pic_air_itp507.setVisible(False)
        self.ui.pic_air_itp508.setVisible(False)
        self.ui.pic_air_itp509.setVisible(False)
        self.ui.pic_air_itp511.setVisible(False)
        self.ui.pic_air_itp512.setVisible(False)
        self.ui.pic_air_itp513.setVisible(False)
        self.ui.pic_air_itp514.setVisible(False)
        self.ui.pic_air_itp515.setVisible(False)
        self.ui.pic_air_itp516.setVisible(False)
        self.ui.pic_air_itp517.setVisible(False)
        self.ui.pic_air_itp518.setVisible(False)
        self.ui.pic_air_itp519.setVisible(False)

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

    def setPos_targetAir(self,appl_type,air_id,x,y):
        '''
        设置目标机位置
        :param appl_type: 应用名称
        :param air_id: 目标机id
        :param x: x轴方向坐标
        :param y: y轴方向坐标
        :return:
        '''
        pass

    def map_zoom_in(self):
        # 放大一级视图
        js_string_map_zoom_in = 'map.zoomIn();'
        self.browser.page().runJavaScript(js_string_map_zoom_in)  # 初始化本机位置、标注、航线、移动


    def map_zoom_out(self):
        # 缩小一级视图
        # 放大一级视图
        js_string_map_zoom_in = 'map.zoomOut();'
        self.browser.page().runJavaScript(js_string_map_zoom_in)  # 初始化本机位置、标注、航线、移动


    def set_targetAir_Info(self,air_id,is_visible,air_coordinate,air_rotation_angle,air_type_id,flight_number,speed,differ_attitude,air_ground_status,appl_status):
        '''
        设置单架目标机信息
        :param air_id:飞机id Airb：100-109 surf：200-209 vsa：300-309 itp：400-409
        :param is_visible:  true or false飞机是否可见
        :param air_coordinate: 序列 飞机容器坐标
        :param air_rotation_angle: 飞机旋转角度
        :param air_type_id: 飞机样式id
        :param flight_number: 航班号
        :param speed: 地速
        :param differ_attitude: 高度差
        :param air_ground_status:地空状态  地面/空中
        :param appl_status:应用状态 有效/无效
        :return:
        '''
        pass

    def set_OwnShip_Info(self,air_id,flight_number,longitude,latitude,attitude_range,p_attitude,course_angle,appl_status):


        pass

    def set_other_Info(self,):
        pass




if __name__=='__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())