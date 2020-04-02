import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import cdti_mainform
class MainWindow(QMainWindow):


    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.rotateAngle = 0  # 每次旋转角度
        self.map_widgetItem = 0
        self.surf_compass_Item = 0
        self.initUI()
        #设置定时器 每50ms旋转一次
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.slotTimeout)
        self.timer.start(1000)

    def slotTimeout(self):
        self.rotateAngle = (self.rotateAngle+5)%360
        self.map_widgetItem.setRotation(self.rotateAngle)
        #self.surf_compass_Item.setRotation(self.rotateAngle+45)

    def initUI(self):
        self.ui = cdti_mainform.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.horizontalLayoutWidget.setGeometry(QRect(0, 0, 720, 720))
        self.ui.graphicsView = QGraphicsView(self.ui.centralwidget)
        self.ui.graphicsView.setObjectName("graphicsView")
        self.ui.graphicsView.setStyleSheet("background: transparent")
        self.ui.horizontalLayout.addWidget(self.ui.graphicsView)

        url = os.getcwd() + '/map_surf.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.browser.resize(640,640)
        map_scene = QGraphicsScene(self)
        #场景绘制圆形
        #pen = QPen()
        #pen.setColor(Qt.black)
        #brush = QBrush()
        #brush.setColor(Qt.red)
        #qGraphicsellipseItem = map_scene.addEllipse(50,50,380,380,pen,brush)
        #scene场景依次加入3个item
        self.map_widgetItem = map_scene.addWidget(self.browser) # 1
        pixmap_border = QPixmap("pic/b.png")
        scaledPixmap_border = pixmap_border.scaled(640, 700, aspectRatioMode=Qt.KeepAspectRatioByExpanding)
        self.border_Item = map_scene.addPixmap(scaledPixmap_border) #2
        pixmap_compass = QPixmap("pic/c.png")
        scaledPixmap_compass = pixmap_compass.scaled(640, 640, aspectRatioMode=Qt.KeepAspectRatio)
        self.surf_compass_Item = map_scene.addPixmap(scaledPixmap_compass) #3

        self.border_Item.setPos(0,0)
        self.map_widgetItem.setPos(0,45)
        self.surf_compass_Item.setPos(0,45)

        #获取旋转中心 得到一个QPointF对象
        centerPos_A = self.map_widgetItem.boundingRect().center()
        centerPos_B = self.surf_compass_Item.boundingRect().center()
        print(centerPos_A,centerPos_B)
        #设置旋转中心
        self.map_widgetItem.setTransformOriginPoint(centerPos_A)
        self.surf_compass_Item.setTransformOriginPoint(centerPos_B)
        # self.map_widgetItem.setRotation(10)
        # self.surf_compass_Item.setRotation(10)
        #设置item图层位置
        self.map_widgetItem.stackBefore(self.border_Item)
        self.ui.graphicsView.setScene(map_scene)
        self.ui.graphicsView.setSceneRect(1, 1, 715, 715)



if __name__=='__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())