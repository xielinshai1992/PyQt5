from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from math import *
import traceback
class MyCompass1_Item(QGraphicsItem):

    def __init__(self):
        super(MyCompass1_Item, self).__init__()
        self.Shape = ["Line", "Rectangle", 'Rounded Rectangle', "Ellipse", "Pie", 'Chord',
                      "Path", "Polygon", "Polyline", "Arc", "Points", "Text", "Pixmap"]
        self.pen = QPen(QColor(255, 255, 255))  #默认白色画笔
        self.brush = QBrush()
        self.update_angle_flag = 0  #更新角度标志位
        self.set_angle = 0  #设置的角度（顺时针）
        self.radius = 150  #罗盘圆半径

    def boundingRect(self):
        return QRectF(0, 0, 300, 300)

    def paint(self, painter, option, widget):
        painter.setPen(self.pen) #白色画笔
        painter.setRenderHints(QPainter.Antialiasing |     #抗锯齿
                               QPainter.TextAntialiasing |  # 高品质抗锯齿
                               QPainter.HighQualityAntialiasing | # 文字抗锯齿
                               QPainter.SmoothPixmapTransform)  # 使图元变换更加平滑
        #绘制罗盘
        painter.drawEllipse(0, 0, 300, 300)  # 绘制外圆
        painter.translate(150,150)           # 将painter坐标系原点移至画布中央

        if self.update_angle_flag == 0:  # 初始化
            #绘制分钟刻度线和小时刻度线
            for i in range(0, 240):
                if (i % 10) != 0:
                    painter.drawLine(150, 0, 145, 0)  # 绘制分钟刻度线
                else:
                    painter.drawLine(150, 0, 140, 0)  # 绘制小时刻度线
                painter.rotate(360 / 240)
            font = painter.font()
            font.setBold(True)
            painter.setFont(font)
            pointSize = font.pointSize()
            #绘制数字
            for i in range(0, 12):
                nhour = i + 3  # 按QT-Qpainter的坐标系换算，3小时的刻度线对应坐标轴0度
                if nhour >= 12:
                    nhour = nhour - 12
                x = 150 *0.85 * cos(i * 30 * pi / 180.0) - pointSize
                y = 150 *0.85 * sin(i * 30 * pi / 180.0) - pointSize
                width = pointSize * 3
                height = pointSize * 3
                painter.drawText(QRectF(x, y, width, height), Qt.AlignCenter, str(nhour*30))

        if self.update_angle_flag == 1: #开始设置角度
            # 绘制分钟刻度线和小时刻度线
            for i in range(0, 240):
                if ((i+int(self.set_angle/1.5)) % 10) != 0:
                    painter.drawLine(150, 0, 145, 0)  # 绘制分钟刻度线
                else:
                    painter.drawLine(150, 0, 140, 0)  # 绘制小时刻度线
                painter.rotate(360 / 240)
            font = painter.font()
            font.setBold(True)
            painter.setFont(font)
            pointSize = font.pointSize()
            #绘制数字
            for i in range(0, 12):
                nhour = i + 3  # 按QT-Qpainter的坐标系换算，3小时的刻度线对应坐标轴0度
                if nhour >= 12:
                    nhour = nhour - 12
                x = self.radius *0.85 * cos(i * 30 * pi / 180.0 + self.set_angle * pi / 180.0) - pointSize
                y = self.radius *0.85 * sin(i * 30 * pi / 180.0 + self.set_angle * pi / 180.0) - pointSize
                width = pointSize * 3
                height = pointSize * 3
                painter.drawText(QRectF(x, y, width, height), Qt.AlignCenter, str(nhour*30))
            pass

    def setShape(self, s):
        self.shape = s
        self.update()

    def setPen(self, p):
        self.pen = p
        self.update()

    def setBrush(self, b):
        self.brush = b
        self.update()

    def setAngle(self,angle):
        self.update_angle_flag = 1 #设置罗盘角度
        self.set_angle = angle
        self.update()

class MyArc1_Item(QGraphicsItem):

    def __init__(self):
        super(MyArc1_Item, self).__init__()
        self.Shape = ["Line", "Rectangle", 'Rounded Rectangle', "Ellipse", "Pie", 'Chord',
                      "Path", "Polygon", "Polyline", "Arc", "Points", "Text", "Pixmap"]
        self.pen_red = QPen(QColor(255, 0, 0))       # 红色画笔
        self.pen_red.setWidth(3)
        self.pen_yellow = QPen(QColor(255, 255, 0))  # 黄色画笔
        self.pen_yellow.setWidth(3)
        self.update_arc_flag = 0  #更新圆弧标志位
        self.update_arc_infos = [] #更新圆弧信息

    def boundingRect(self):
        return QRectF(0, 0, 300, 300)

    def paint(self, painter, option, widget):
        try:
            painter.setPen(self.pen_red) #红色画笔
            painter.setRenderHints(QPainter.Antialiasing |     #抗锯齿
                                   QPainter.TextAntialiasing |  # 高品质抗锯齿
                                   QPainter.HighQualityAntialiasing | # 文字抗锯齿
                                   QPainter.SmoothPixmapTransform)  # 使图元变换更加平滑
            if self.update_arc_flag == 0:
                painter.drawArc(0, 0, 300, 300, 0 * 16, 60 * 16)   #绘制圆弧
                painter.drawArc(0, 0, 300, 300, 120 * 16, 60 * 16) #绘制圆弧
                painter.setPen(self.pen_yellow)
                painter.drawArc(0, 0, 300, 300, 60 * 16, 60 * 16)
            if self.update_arc_flag == 1:
                for item in self.update_arc_infos:
                    color_rbg_Value = item['color']
                    differ = item['upperBound'] - item['lowerBound']
                    pen = QPen(QColor(color_rbg_Value))
                    pen.setWidth(3)
                    painter.setPen(pen)
                    painter.drawArc(0, 0, 300, 300, (175 - item['upperBound']) * 16, differ * 16)
        except:
            traceback.print_exc()

    def update_arc(self,info):
        self.update_arc_flag = 1 #更新圆弧
        self.update_arc_infos = info
        self.update()

    def setShape(self, s):
        self.shape = s
        self.update()

    def setPen(self, p):
        self.pen = p
        self.update()

class MyCompass2_Item(QGraphicsItem):

    def __init__(self):
        super(MyCompass2_Item, self).__init__()
        self.Shape = ["Line", "Rectangle", 'Rounded Rectangle', "Ellipse", "Pie", 'Chord',
                      "Path", "Polygon", "Polyline", "Arc", "Points", "Text", "Pixmap"]
        self.pen = QPen(QColor(255, 255, 255))  #默认白色画笔
        self.brush = QBrush()
        self.update_angle_flag = 0  #更新角度标志位
        self.set_angle = 0  #设置的角度（顺时针）
        self.radius = 240  #罗盘圆半径

    def boundingRect(self):
        return QRectF(0, 0, self.radius*2 , self.radius*2)

    def paint(self, painter, option, widget):
        painter.setPen(self.pen)                            #白色画笔
        painter.setRenderHints(QPainter.Antialiasing |      #抗锯齿
                               QPainter.TextAntialiasing |  # 高品质抗锯齿
                               QPainter.HighQualityAntialiasing | #文字抗锯齿
                               QPainter.SmoothPixmapTransform)  #使图元变换更加平滑
        #绘制罗盘
        painter.drawEllipse(0, 0, self.radius*2, self.radius*2)  # 绘制外圆
        painter.translate(self.radius,self.radius)           # 将painter坐标系原点移至画布中央

        if self.update_angle_flag == 0: #初始化
            # 绘制分钟刻度线和小时刻度线
            for i in range(0, 240):
                if (i % 10) != 0:
                    painter.drawLine(240, 0, 235, 0)  # 绘制分钟刻度线
                else:
                    painter.drawLine(240, 0, 230, 0)  # 绘制小时刻度线
                painter.rotate(360 / 240)
            font = painter.font()
            font.setBold(True)
            painter.setFont(font)
            pointSize = font.pointSize()
            #绘制数字
            for i in range(0, 12):
                nhour = i + 3  # 按QT-Qpainter的坐标系换算，3小时的刻度线对应坐标轴0度
                if nhour >= 12:
                    nhour = nhour - 12
                x = self.radius  *0.9 * cos(i * 30 * pi / 180.0) - pointSize
                y = self.radius  *0.9 * sin(i * 30 * pi / 180.0) - pointSize
                width = pointSize * 3
                height = pointSize * 3
                painter.drawText(QRectF(x, y, width, height), Qt.AlignCenter, str(nhour*30))
        if self.update_angle_flag == 1: #开始设置角度
            # 绘制分钟刻度线和小时刻度线
            for i in range(0, 240):
                if ((i+int(self.set_angle/1.5)) % 10) != 0:
                    painter.drawLine(240, 0, 235, 0)  # 绘制分钟刻度线
                else:
                    painter.drawLine(240, 0, 230, 0)  # 绘制小时刻度线
                painter.rotate(360 / 240)
            font = painter.font()
            font.setBold(True)
            painter.setFont(font)
            pointSize = font.pointSize()
            #绘制数字
            for i in range(0, 12):
                nhour = i + 3  # 按QT-Qpainter的坐标系换算，3小时的刻度线对应坐标轴0度
                if nhour >= 12:
                    nhour = nhour - 12
                x = 240 *0.9 * cos(i * 30 * pi / 180.0 + self.set_angle * pi / 180.0) - pointSize
                y = 240 *0.9 * sin(i * 30 * pi / 180.0 + self.set_angle * pi / 180.0) - pointSize
                width = pointSize * 3
                height = pointSize * 3
                painter.drawText(QRectF(x, y, width, height), Qt.AlignCenter, str(nhour*30))
            pass


    def setShape(self, s):
        self.shape = s
        self.update()

    def setPen(self, p):
        self.pen = p
        self.update()

    def setBrush(self, b):
        self.brush = b
        self.update()
    def setAngle(self,angle):
        self.update_angle_flag = 1 #设置罗盘角度
        self.set_angle = angle
        self.update()

class MyArc2_Item(QGraphicsItem):

    def __init__(self):
        super(MyArc2_Item, self).__init__()
        self.Shape = ["Line", "Rectangle", 'Rounded Rectangle', "Ellipse", "Pie", 'Chord',
                      "Path", "Polygon", "Polyline", "Arc", "Points", "Text", "Pixmap"]
        self.pen_red = QPen(QColor(255, 0, 0))       # 红色画笔
        self.pen_red.setWidth(3)
        self.pen_yellow = QPen(QColor(255, 255, 0))  # 黄色画笔
        self.pen_yellow.setWidth(3)
        self.update_arc_flag = 0  #更新圆弧标志位
        self.update_arc_infos = [] #更新圆弧信息

    def boundingRect(self):
        return QRectF(0, 0, 480, 480)

    def paint(self, painter, option, widget):
        painter.setPen(self.pen_red) #红色画笔
        painter.setRenderHints(QPainter.Antialiasing |     #抗锯齿
                               QPainter.TextAntialiasing |  # 高品质抗锯齿
                               QPainter.HighQualityAntialiasing | # 文字抗锯齿
                               QPainter.SmoothPixmapTransform)  # 使图元变换更加平滑
        if self.update_arc_flag == 0:
            painter.drawArc(0, 0, 480, 480, 0 * 16, 60 * 16)   #绘制圆弧
            painter.drawArc(0, 0, 480, 480, 120 * 16, 60 * 16) #绘制圆弧
            painter.setPen(self.pen_yellow)
            painter.drawArc(0, 0, 480, 480, 60 * 16, 60 * 16)
        if self.update_arc_flag == 1:
            for item in self.update_arc_infos:
                color_rbg_Value = item['color']
                differ = item['upperBound'] - item['lowerBound']
                pen = QPen(QColor(color_rbg_Value))
                pen.setWidth(3)
                painter.setPen(pen)
                painter.drawArc(0, 0, 480, 480, (175 - item['upperBound']) * 16, differ * 16)

    def update_arc(self,info):
        self.update_arc_flag = 1 #更新圆弧
        self.update_arc_infos = info
        self.update()

    def setShape(self, s):
        self.shape = s
        self.update()

    def setPen(self, p):
        self.pen = p
        self.update()