from a661_api import UA_TO_CDTI_DATA,A661_CMD_SET_PARAMATER_12BYTE,A661_CMD_SET_PARAMATER_16BYTE,CDTI_TO_UA_WIDGET_EVENT_DATA
import socket
import threading

class MyThread(threading.Thread):
    def __init__(self):
        # 注意：一定要显式的调用父类的初始化函数。
        super(MyThread, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(("127.0.0.1", 8002))  # 绑定服务器的ip和端口
        print("开始监听CDTI端发送的数据...")

    def run(self):
        while True:
            buffer = self.s.recv(4096)  # 一次接收最大字节长度
            receive_Data = CDTI_TO_UA_WIDGET_EVENT_DATA()
            receive_Data.decode(buffer)
            print(receive_Data.A661_BEGIN_BLOCK)
            print(receive_Data.LayerIdent)
            print(receive_Data.ContextNumber)
            print(receive_Data.BlockSize)
            print(receive_Data.Compass_InOut_Click_Envent.A661_NOTIFY_WIDGET_EVENT)
            print(receive_Data.Compass_InOut_Click_Envent.CommandSize)
            print(receive_Data.Compass_InOut_Click_Envent.WidgetIdent)
            print(receive_Data.Compass_InOut_Click_Envent.EventOrigin)
            print(receive_Data.Compass_InOut_Click_Envent.EventID)
            print(receive_Data.Compass_InOut_Click_Envent.UnusedPad)
            print(receive_Data.A661_END_BLOCK)
            print(receive_Data.Unused1)

#构造测试数据
global ua_to_cdti_data
ua_to_cdti_data = UA_TO_CDTI_DATA()
compass_rotate_angle = '35' #罗盘旋转角
compass_step = '51' #罗盘步长
ownship_id =  'AC9733'  #本机航班号
ownship_alt = '28000'   #本机飞行高度
ownship_lon = '36.1'   #本机经度
ownship_lat = '37.4'  #本机纬度
ownship_alt_range = '30000'     #本机高度范围
ownship_angle = '42.8'     #本机航向角
ownship_appstatus = 2   #本机应用状态
airport_map_rotate_angle = '35' #机场地图旋转角

target1_visible = 1
target1_pic = 1
target1_rotate_angle = '0'
target1_x = '150'
target1_y = '400'
target1_flightId = '1KKU3C'
target1_Speed = '890'
target1_Alt_dif = '100'
target1_Status = 'AIR'
target1_AppStatus = 1

target2_visible = 1
target2_pic = 4
target2_rotate_angle = '0'
target2_x = '250'
target2_y = '420'
target2_flightId = '2IJQ6M'
target2_Speed = '900'
target2_Alt_dif = '50'
target2_Status = 'AIR'
target2_AppStatus = 2

target3_visible = 1
target3_pic = 3
target3_rotate_angle = '0'
target3_x = '350'
target3_y = '440'
target3_flightId = '3YBJ6M'
target3_Speed = '900'
target3_Alt_dif = '80'
target3_Status = 'AIR'
target3_AppStatus = 1

target4_visible = 1
target4_pic = 2
target4_rotate_angle = '0'
target4_x = '450'
target4_y = '460'
target4_flightId = '4MS761'
target4_Speed = '750'
target4_Alt_dif = '100'
target4_Status = 'AIR'
target4_AppStatus = 2

target5_visible = 1
target5_pic = 1
target5_rotate_angle = '0'
target5_x = '550'
target5_y = '380'
target5_flightId = '5SAQW'
target5_Speed = '800'
target5_Alt_dif = '100'
target5_Status = 'AIR'
target5_AppStatus = 1

def pack():

    ua_to_cdti_data.A661_BEGIN_BLOCK = int('B0',16)
    ua_to_cdti_data.LayerIdent = 1
    ua_to_cdti_data.ContextNumber = 1
    ua_to_cdti_data.BlockSize = 908
    # #罗盘旋转角度
    compass_Bitmap_SET_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    compass_Bitmap_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    compass_Bitmap_SET_PARAMATER.CommandSize = 16
    compass_Bitmap_SET_PARAMATER.WidgetIdent = 0
    compass_Bitmap_SET_PARAMATER.UnusedPad = 0
    compass_Bitmap_SET_PARAMATER.ParameterIdent = int('B2C0',16)  #设置旋转角
    compass_Bitmap_SET_PARAMATER.ParameterValueBuffer = compass_rotate_angle.encode()
    #罗盘步长
    compass_Step_SET_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    compass_Step_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    compass_Step_SET_PARAMATER.CommandSize = 16
    compass_Step_SET_PARAMATER.WidgetIdent = 1
    compass_Step_SET_PARAMATER.UnusedPad = 0
    compass_Step_SET_PARAMATER.ParameterIdent = int('B490',16)
    compass_Step_SET_PARAMATER.ParameterValueBuffer = compass_step.encode()
    #本机航班号
    ownship_FlightId_SET_PARAMATER =  A661_CMD_SET_PARAMATER_16BYTE()
    ownship_FlightId_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_FlightId_SET_PARAMATER.CommandSize = 16
    ownship_FlightId_SET_PARAMATER.WidgetIdent = 2
    ownship_FlightId_SET_PARAMATER.UnusedPad = 0
    ownship_FlightId_SET_PARAMATER.ParameterIdent = int('B490',16)
    ownship_FlightId_SET_PARAMATER.ParameterValueBuffer = ownship_id.encode()
    #本机飞行高度
    ownship_Alt_SET_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    ownship_Alt_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Alt_SET_PARAMATER.CommandSize = 16
    ownship_Alt_SET_PARAMATER.WidgetIdent = 3
    ownship_Alt_SET_PARAMATER.UnusedPad = 0
    ownship_Alt_SET_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Alt_SET_PARAMATER.ParameterValueBuffer = ownship_alt.encode()
    #本机经度
    ownship_Lon_SET_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    ownship_Lon_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Lon_SET_PARAMATER.CommandSize = 16
    ownship_Lon_SET_PARAMATER.WidgetIdent = 4
    ownship_Lon_SET_PARAMATER.UnusedPad = 0
    ownship_Lon_SET_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Lon_SET_PARAMATER.ParameterValueBuffer = ownship_lon.encode()
    #本机纬度
    ownship_Lat_SET_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    ownship_Lat_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Lat_SET_PARAMATER.CommandSize = 16
    ownship_Lat_SET_PARAMATER.WidgetIdent = 5
    ownship_Lat_SET_PARAMATER.UnusedPad = 0
    ownship_Lat_SET_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Lat_SET_PARAMATER.ParameterValueBuffer = ownship_lat.encode()
    #本机高度范围
    ownship_Alt_Range_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    ownship_Alt_Range_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Alt_Range_PARAMATER.CommandSize = 16
    ownship_Alt_Range_PARAMATER.WidgetIdent = 6
    ownship_Alt_Range_PARAMATER.UnusedPad = 0
    ownship_Alt_Range_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Alt_Range_PARAMATER.ParameterValueBuffer = ownship_alt_range.encode()
    #本机航向角
    ownship_Course_Angle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    ownship_Course_Angle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Course_Angle_PARAMATER.CommandSize = 16
    ownship_Course_Angle_PARAMATER.WidgetIdent = 7
    ownship_Course_Angle_PARAMATER.UnusedPad = 0
    ownship_Course_Angle_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Course_Angle_PARAMATER.ParameterValueBuffer = ownship_angle.encode()
    #本机应用状态
    ownship_App_Status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    ownship_App_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_App_Status_PARAMATER.CommandSize = 12
    ownship_App_Status_PARAMATER.WidgetIdent = 8
    ownship_App_Status_PARAMATER.UnusedPad = 0
    ownship_App_Status_PARAMATER.ParameterIdent = int('B2F0',16)
    ownship_App_Status_PARAMATER.ParameterValueBuffer = ownship_appstatus
    #机场地图
    airport_Map_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    airport_Map_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    airport_Map_PARAMATER.CommandSize = 16
    airport_Map_PARAMATER.WidgetIdent = 9
    airport_Map_PARAMATER.UnusedPad = 0
    airport_Map_PARAMATER.ParameterIdent = int('B2C0',16)  #设置旋转角
    airport_Map_PARAMATER.ParameterValueBuffer = airport_map_rotate_angle.encode()
    #1号目标机设置显示、隐藏
    target1_Visible_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target1_Visible_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Visible_PARAMATER.CommandSize = 12
    target1_Visible_PARAMATER.WidgetIdent = 11
    target1_Visible_PARAMATER.UnusedPad = 0
    target1_Visible_PARAMATER.ParameterIdent = int('0xB530',16)  #设置显示/隐藏
    target1_Visible_PARAMATER.ParameterValueBuffer = target1_visible #1显示 0隐藏
    #1号目标机设置图片源
    target1_Pic_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target1_Pic_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Pic_PARAMATER.CommandSize = 12
    target1_Pic_PARAMATER.WidgetIdent = 11
    target1_Pic_PARAMATER.UnusedPad = 0
    target1_Pic_PARAMATER.ParameterIdent = int('0xB4C0',16)
    target1_Pic_PARAMATER.ParameterValueBuffer = target1_pic #图片类型ID
    #1号目标机设置旋转角
    target1_RotateAngle_PARAMATER= A661_CMD_SET_PARAMATER_16BYTE()
    target1_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_RotateAngle_PARAMATER.CommandSize = 16
    target1_RotateAngle_PARAMATER.WidgetIdent = 11
    target1_RotateAngle_PARAMATER.UnusedPad = 0
    target1_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target1_RotateAngle_PARAMATER.ParameterValueBuffer = target1_rotate_angle.encode()
    #1号目标机设置X轴坐标
    target1_X_PARAMATER= A661_CMD_SET_PARAMATER_16BYTE()
    target1_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_X_PARAMATER.CommandSize = 16
    target1_X_PARAMATER.WidgetIdent = 11
    target1_X_PARAMATER.UnusedPad = 0
    target1_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target1_X_PARAMATER.ParameterValueBuffer = target1_x.encode()
    #1号目标机设置Y轴坐标
    target1_Y_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target1_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Y_PARAMATER.CommandSize = 16
    target1_Y_PARAMATER.WidgetIdent = 11
    target1_Y_PARAMATER.UnusedPad = 0
    target1_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target1_Y_PARAMATER.ParameterValueBuffer = target1_y.encode() #图片类型ID
    #1号目标机航班号
    target1_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target1_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_FlightId_PARAMATER.CommandSize = 16
    target1_FlightId_PARAMATER.WidgetIdent = 12
    target1_FlightId_PARAMATER.UnusedPad = 0
    target1_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target1_FlightId_PARAMATER.ParameterValueBuffer = target1_flightId.encode()
    #1号目标机地速
    target1_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target1_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Speed_PARAMATER.CommandSize = 16
    target1_Speed_PARAMATER.WidgetIdent = 13
    target1_Speed_PARAMATER.UnusedPad = 0
    target1_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target1_Speed_PARAMATER.ParameterValueBuffer = target1_Speed.encode()
    #1号目标机高度差
    target1_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target1_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Alt_dif_PARAMATER.CommandSize = 16
    target1_Alt_dif_PARAMATER.WidgetIdent = 14
    target1_Alt_dif_PARAMATER.UnusedPad = 0
    target1_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target1_Alt_dif_PARAMATER.ParameterValueBuffer = target1_Alt_dif.encode()
    #1号目标机飞行状态
    target1_Status_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target1_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Status_PARAMATER.CommandSize = 16
    target1_Status_PARAMATER.WidgetIdent = 15
    target1_Status_PARAMATER.UnusedPad = 0
    target1_Status_PARAMATER.ParameterIdent = int('B490',16)
    target1_Status_PARAMATER.ParameterValueBuffer = target1_Status.encode()
    #1号目标机应用状态
    target1_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target1_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_AppStatus_PARAMATER.CommandSize = 12
    target1_AppStatus_PARAMATER.WidgetIdent = 16
    target1_AppStatus_PARAMATER.UnusedPad = 0
    target1_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target1_AppStatus_PARAMATER.ParameterValueBuffer = target1_AppStatus
    #2号目标机设置显示、隐藏
    target2_Visible_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_Visible_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Visible_PARAMATER.CommandSize = 12
    target2_Visible_PARAMATER.WidgetIdent = 21
    target2_Visible_PARAMATER.UnusedPad = 0
    target2_Visible_PARAMATER.ParameterIdent = int('0xB530',16)  #设置显示/隐藏
    target2_Visible_PARAMATER.ParameterValueBuffer = target2_visible #1显示 0隐藏
    #2号目标机设置图片源
    target2_Pic_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_Pic_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Pic_PARAMATER.CommandSize = 12
    target2_Pic_PARAMATER.WidgetIdent = 21
    target2_Pic_PARAMATER.UnusedPad = 0
    target2_Pic_PARAMATER.ParameterIdent = int('0xB4C0',16)
    target2_Pic_PARAMATER.ParameterValueBuffer = target2_pic #图片类型ID
    #2号目标机设置旋转角
    target2_RotateAngle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target2_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_RotateAngle_PARAMATER.CommandSize = 16
    target2_RotateAngle_PARAMATER.WidgetIdent = 21
    target2_RotateAngle_PARAMATER.UnusedPad = 0
    target2_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target2_RotateAngle_PARAMATER.ParameterValueBuffer = target2_rotate_angle.encode()
    #2号目标机设置X轴坐标
    target2_X_PARAMATER= A661_CMD_SET_PARAMATER_16BYTE()
    target2_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_X_PARAMATER.CommandSize = 16
    target2_X_PARAMATER.WidgetIdent = 21
    target2_X_PARAMATER.UnusedPad = 0
    target2_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target2_X_PARAMATER.ParameterValueBuffer = target2_x.encode()
    #1号目标机设置Y轴坐标
    target2_Y_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target2_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Y_PARAMATER.CommandSize = 16
    target2_Y_PARAMATER.WidgetIdent = 21
    target2_Y_PARAMATER.UnusedPad = 0
    target2_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target2_Y_PARAMATER.ParameterValueBuffer = target2_y.encode() #图片类型ID
    #2号目标机航班号
    target2_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target2_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_FlightId_PARAMATER.CommandSize = 16
    target2_FlightId_PARAMATER.WidgetIdent = 22
    target2_FlightId_PARAMATER.UnusedPad = 0
    target2_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target2_FlightId_PARAMATER.ParameterValueBuffer = target2_flightId.encode()
    #2号目标机地速
    target2_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target2_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Speed_PARAMATER.CommandSize = 16
    target2_Speed_PARAMATER.WidgetIdent = 23
    target2_Speed_PARAMATER.UnusedPad = 0
    target2_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target2_Speed_PARAMATER.ParameterValueBuffer = target2_Speed.encode()
    #2号目标机高度差
    target2_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target2_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Alt_dif_PARAMATER.CommandSize = 16
    target2_Alt_dif_PARAMATER.WidgetIdent = 24
    target2_Alt_dif_PARAMATER.UnusedPad = 0
    target2_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target2_Alt_dif_PARAMATER.ParameterValueBuffer = target2_Alt_dif.encode()
    #2号目标机飞行状态
    target2_Status_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target2_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Status_PARAMATER.CommandSize = 16
    target2_Status_PARAMATER.WidgetIdent = 25
    target2_Status_PARAMATER.UnusedPad = 0
    target2_Status_PARAMATER.ParameterIdent = int('B490',16)
    target2_Status_PARAMATER.ParameterValueBuffer = target2_Status.encode()
    #2号目标机应用状态
    target2_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_AppStatus_PARAMATER.CommandSize = 12
    target2_AppStatus_PARAMATER.WidgetIdent = 26
    target2_AppStatus_PARAMATER.UnusedPad = 0
    target2_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target2_AppStatus_PARAMATER.ParameterValueBuffer = target2_AppStatus

    #3号目标机设置显示、隐藏
    target3_Visible_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_Visible_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Visible_PARAMATER.CommandSize = 12
    target3_Visible_PARAMATER.WidgetIdent = 31
    target3_Visible_PARAMATER.UnusedPad = 0
    target3_Visible_PARAMATER.ParameterIdent = int('0xB530',16)  #设置显示/隐藏
    target3_Visible_PARAMATER.ParameterValueBuffer = target3_visible #1显示 0隐藏
    #3号目标机设置图片源
    target3_Pic_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_Pic_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Pic_PARAMATER.CommandSize = 12
    target3_Pic_PARAMATER.WidgetIdent = 31
    target3_Pic_PARAMATER.UnusedPad = 0
    target3_Pic_PARAMATER.ParameterIdent = int('0xB4C0',16)
    target3_Pic_PARAMATER.ParameterValueBuffer = target3_pic #图片类型ID
    #3号目标机设置旋转角
    target3_RotateAngle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target3_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_RotateAngle_PARAMATER.CommandSize = 16
    target3_RotateAngle_PARAMATER.WidgetIdent = 31
    target3_RotateAngle_PARAMATER.UnusedPad = 0
    target3_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target3_RotateAngle_PARAMATER.ParameterValueBuffer = target3_rotate_angle.encode()
    #3号目标机设置X轴坐标
    target3_X_PARAMATER= A661_CMD_SET_PARAMATER_16BYTE()
    target3_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_X_PARAMATER.CommandSize = 16
    target3_X_PARAMATER.WidgetIdent = 31
    target3_X_PARAMATER.UnusedPad = 0
    target3_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target3_X_PARAMATER.ParameterValueBuffer = target3_x.encode()
    #3号目标机设置Y轴坐标
    target3_Y_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target3_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Y_PARAMATER.CommandSize = 16
    target3_Y_PARAMATER.WidgetIdent = 31
    target3_Y_PARAMATER.UnusedPad = 0
    target3_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target3_Y_PARAMATER.ParameterValueBuffer = target3_y.encode() #图片类型ID
    #3号目标机航班号
    target3_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target3_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_FlightId_PARAMATER.CommandSize = 16
    target3_FlightId_PARAMATER.WidgetIdent = 32
    target3_FlightId_PARAMATER.UnusedPad = 0
    target3_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target3_FlightId_PARAMATER.ParameterValueBuffer = target3_flightId.encode()
    #3号目标机地速
    target3_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target3_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Speed_PARAMATER.CommandSize = 16
    target3_Speed_PARAMATER.WidgetIdent = 33
    target3_Speed_PARAMATER.UnusedPad = 0
    target3_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target3_Speed_PARAMATER.ParameterValueBuffer = target3_Speed.encode()
    #3号目标机高度差
    target3_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target3_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Alt_dif_PARAMATER.CommandSize = 16
    target3_Alt_dif_PARAMATER.WidgetIdent = 34
    target3_Alt_dif_PARAMATER.UnusedPad = 0
    target3_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target3_Alt_dif_PARAMATER.ParameterValueBuffer = target3_Alt_dif.encode()
    #3号目标机飞行状态
    target3_Status_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target3_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Status_PARAMATER.CommandSize = 16
    target3_Status_PARAMATER.WidgetIdent = 35
    target3_Status_PARAMATER.UnusedPad = 0
    target3_Status_PARAMATER.ParameterIdent = int('B490',16)
    target3_Status_PARAMATER.ParameterValueBuffer = target3_Status.encode()
    #3号目标机应用状态
    target3_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_AppStatus_PARAMATER.CommandSize = 12
    target3_AppStatus_PARAMATER.WidgetIdent = 36
    target3_AppStatus_PARAMATER.UnusedPad = 0
    target3_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target3_AppStatus_PARAMATER.ParameterValueBuffer = target3_AppStatus

    #4号目标机设置显示、隐藏
    target4_Visible_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_Visible_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Visible_PARAMATER.CommandSize = 12
    target4_Visible_PARAMATER.WidgetIdent = 41
    target4_Visible_PARAMATER.UnusedPad = 0
    target4_Visible_PARAMATER.ParameterIdent = int('0xB530',16)  #设置显示/隐藏
    target4_Visible_PARAMATER.ParameterValueBuffer = target4_visible #1显示 0隐藏
    #4号目标机设置图片源
    target4_Pic_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_Pic_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Pic_PARAMATER.CommandSize = 12
    target4_Pic_PARAMATER.WidgetIdent = 41
    target4_Pic_PARAMATER.UnusedPad = 0
    target4_Pic_PARAMATER.ParameterIdent = int('0xB4C0',16)
    target4_Pic_PARAMATER.ParameterValueBuffer = target4_pic #图片类型ID
    #4号目标机设置旋转角
    target4_RotateAngle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target4_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_RotateAngle_PARAMATER.CommandSize = 16
    target4_RotateAngle_PARAMATER.WidgetIdent = 41
    target4_RotateAngle_PARAMATER.UnusedPad = 0
    target4_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target4_RotateAngle_PARAMATER.ParameterValueBuffer = target4_rotate_angle.encode()
    #4号目标机设置X轴坐标
    target4_X_PARAMATER= A661_CMD_SET_PARAMATER_16BYTE()
    target4_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_X_PARAMATER.CommandSize = 16
    target4_X_PARAMATER.WidgetIdent = 41
    target4_X_PARAMATER.UnusedPad = 0
    target4_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target4_X_PARAMATER.ParameterValueBuffer = target4_x.encode()
    #4号目标机设置Y轴坐标
    target4_Y_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target4_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Y_PARAMATER.CommandSize = 16
    target4_Y_PARAMATER.WidgetIdent = 41
    target4_Y_PARAMATER.UnusedPad = 0
    target4_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target4_Y_PARAMATER.ParameterValueBuffer = target4_y.encode() #图片类型ID
    #4号目标机航班号
    target4_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target4_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_FlightId_PARAMATER.CommandSize = 16
    target4_FlightId_PARAMATER.WidgetIdent = 42
    target4_FlightId_PARAMATER.UnusedPad = 0
    target4_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target4_FlightId_PARAMATER.ParameterValueBuffer = target4_flightId.encode()
    #4号目标机地速
    target4_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target4_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Speed_PARAMATER.CommandSize = 16
    target4_Speed_PARAMATER.WidgetIdent = 43
    target4_Speed_PARAMATER.UnusedPad = 0
    target4_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target4_Speed_PARAMATER.ParameterValueBuffer = target4_Speed.encode()
    #4号目标机高度差
    target4_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target4_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Alt_dif_PARAMATER.CommandSize = 16
    target4_Alt_dif_PARAMATER.WidgetIdent = 44
    target4_Alt_dif_PARAMATER.UnusedPad = 0
    target4_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target4_Alt_dif_PARAMATER.ParameterValueBuffer = target4_Alt_dif.encode()
    #4号目标机飞行状态
    target4_Status_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target4_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Status_PARAMATER.CommandSize = 16
    target4_Status_PARAMATER.WidgetIdent = 45
    target4_Status_PARAMATER.UnusedPad = 0
    target4_Status_PARAMATER.ParameterIdent = int('B490',16)
    target4_Status_PARAMATER.ParameterValueBuffer = target4_Status.encode()
    #4号目标机应用状态
    target4_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_AppStatus_PARAMATER.CommandSize = 12
    target4_AppStatus_PARAMATER.WidgetIdent = 46
    target4_AppStatus_PARAMATER.UnusedPad = 0
    target4_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target4_AppStatus_PARAMATER.ParameterValueBuffer = target4_AppStatus

    #5号目标机设置显示、隐藏
    target5_Visible_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_Visible_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Visible_PARAMATER.CommandSize = 12
    target5_Visible_PARAMATER.WidgetIdent = 51
    target5_Visible_PARAMATER.UnusedPad = 0
    target5_Visible_PARAMATER.ParameterIdent = int('0xB530',16)  #设置显示/隐藏
    target5_Visible_PARAMATER.ParameterValueBuffer = target5_visible #1显示 0隐藏
    #5号目标机设置图片源
    target5_Pic_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_Pic_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Pic_PARAMATER.CommandSize = 12
    target5_Pic_PARAMATER.WidgetIdent = 51
    target5_Pic_PARAMATER.UnusedPad = 0
    target5_Pic_PARAMATER.ParameterIdent = int('0xB4C0',16)
    target5_Pic_PARAMATER.ParameterValueBuffer = target5_pic #图片类型ID
    #5号目标机设置旋转角
    target5_RotateAngle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target5_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_RotateAngle_PARAMATER.CommandSize = 16
    target5_RotateAngle_PARAMATER.WidgetIdent = 51
    target5_RotateAngle_PARAMATER.UnusedPad = 0
    target5_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target5_RotateAngle_PARAMATER.ParameterValueBuffer = target5_rotate_angle.encode()
    #5号目标机设置X轴坐标
    target5_X_PARAMATER= A661_CMD_SET_PARAMATER_16BYTE()
    target5_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_X_PARAMATER.CommandSize = 16
    target5_X_PARAMATER.WidgetIdent = 51
    target5_X_PARAMATER.UnusedPad = 0
    target5_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target5_X_PARAMATER.ParameterValueBuffer = target5_x.encode()
    #5号目标机设置Y轴坐标
    target5_Y_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target5_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Y_PARAMATER.CommandSize = 16
    target5_Y_PARAMATER.WidgetIdent = 51
    target5_Y_PARAMATER.UnusedPad = 0
    target5_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target5_Y_PARAMATER.ParameterValueBuffer = target5_y.encode() #图片类型ID
    #5号目标机航班号
    target5_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target5_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_FlightId_PARAMATER.CommandSize = 16
    target5_FlightId_PARAMATER.WidgetIdent = 52
    target5_FlightId_PARAMATER.UnusedPad = 0
    target5_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target5_FlightId_PARAMATER.ParameterValueBuffer = target5_flightId.encode()
    #5号目标机地速
    target5_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target5_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Speed_PARAMATER.CommandSize = 16
    target5_Speed_PARAMATER.WidgetIdent = 53
    target5_Speed_PARAMATER.UnusedPad = 0
    target5_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target5_Speed_PARAMATER.ParameterValueBuffer = target5_Speed.encode()
    #5号目标机高度差
    target5_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target5_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Alt_dif_PARAMATER.CommandSize = 16
    target5_Alt_dif_PARAMATER.WidgetIdent = 54
    target5_Alt_dif_PARAMATER.UnusedPad = 0
    target5_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target5_Alt_dif_PARAMATER.ParameterValueBuffer = target5_Alt_dif.encode()
    #5号目标机飞行状态
    target5_Status_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target5_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Status_PARAMATER.CommandSize = 16
    target5_Status_PARAMATER.WidgetIdent = 55
    target5_Status_PARAMATER.UnusedPad = 0
    target5_Status_PARAMATER.ParameterIdent = int('B490',16)
    target5_Status_PARAMATER.ParameterValueBuffer = target5_Status.encode()
    #5号目标机应用状态
    target5_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_AppStatus_PARAMATER.CommandSize = 12
    target5_AppStatus_PARAMATER.WidgetIdent = 56
    target5_AppStatus_PARAMATER.UnusedPad = 0
    target5_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target5_AppStatus_PARAMATER.ParameterValueBuffer = target5_AppStatus

    ua_to_cdti_data.Compass_Bitmap_SET_PARAMATER = compass_Bitmap_SET_PARAMATER
    ua_to_cdti_data.Compass_Step_SET_PARAMATER = compass_Step_SET_PARAMATER
    ua_to_cdti_data.Ownship_FlightId_SET_PARAMATER = ownship_FlightId_SET_PARAMATER
    ua_to_cdti_data.Ownship_Alt_SET_PARAMATER = ownship_Alt_SET_PARAMATER
    ua_to_cdti_data.Ownship_Lon_SET_PARAMATER = ownship_Lon_SET_PARAMATER
    ua_to_cdti_data.Ownship_Lat_SET_PARAMATER = ownship_Lat_SET_PARAMATER
    ua_to_cdti_data.Ownship_Alt_Range_PARAMATER = ownship_Alt_Range_PARAMATER
    ua_to_cdti_data.Ownship_Course_Angle_PARAMATER = ownship_Course_Angle_PARAMATER
    ua_to_cdti_data.Ownship_App_Status_PARAMATER = ownship_App_Status_PARAMATER
    ua_to_cdti_data.Airport_Map_PARAMATER = airport_Map_PARAMATER

    ua_to_cdti_data.Target1_Visible_PARAMATER = target1_Visible_PARAMATER
    ua_to_cdti_data.Target1_Pic_PARAMATER = target1_Pic_PARAMATER
    ua_to_cdti_data.Target1_RotateAngle_PARAMATER = target1_RotateAngle_PARAMATER
    ua_to_cdti_data.Target1_X_PARAMATER = target1_X_PARAMATER
    ua_to_cdti_data.Target1_Y_PARAMATER = target1_Y_PARAMATER
    ua_to_cdti_data.Target1_FlightId_PARAMATER = target1_FlightId_PARAMATER
    ua_to_cdti_data.Target1_Speed_PARAMATER = target1_Speed_PARAMATER
    ua_to_cdti_data.Target1_Alt_dif_PARAMATER = target1_Alt_dif_PARAMATER
    ua_to_cdti_data.Target1_Status_PARAMATER = target1_Status_PARAMATER
    ua_to_cdti_data.Target1_AppStatus_PARAMATER = target1_AppStatus_PARAMATER

    ua_to_cdti_data.Target2_Visible_PARAMATER = target2_Visible_PARAMATER
    ua_to_cdti_data.Target2_Pic_PARAMATER = target2_Pic_PARAMATER
    ua_to_cdti_data.Target2_RotateAngle_PARAMATER = target2_RotateAngle_PARAMATER
    ua_to_cdti_data.Target2_X_PARAMATER = target2_X_PARAMATER
    ua_to_cdti_data.Target2_Y_PARAMATER = target2_Y_PARAMATER
    ua_to_cdti_data.Target2_FlightId_PARAMATER = target2_FlightId_PARAMATER
    ua_to_cdti_data.Target2_Speed_PARAMATER = target2_Speed_PARAMATER
    ua_to_cdti_data.Target2_Alt_dif_PARAMATER = target2_Alt_dif_PARAMATER
    ua_to_cdti_data.Target2_Status_PARAMATER = target2_Status_PARAMATER
    ua_to_cdti_data.Target2_AppStatus_PARAMATER = target2_AppStatus_PARAMATER

    ua_to_cdti_data.Target3_Visible_PARAMATER = target3_Visible_PARAMATER
    ua_to_cdti_data.Target3_Pic_PARAMATER = target3_Pic_PARAMATER
    ua_to_cdti_data.Target3_RotateAngle_PARAMATER = target3_RotateAngle_PARAMATER
    ua_to_cdti_data.Target3_X_PARAMATER = target3_X_PARAMATER
    ua_to_cdti_data.Target3_Y_PARAMATER = target3_Y_PARAMATER
    ua_to_cdti_data.Target3_FlightId_PARAMATER = target3_FlightId_PARAMATER
    ua_to_cdti_data.Target3_Speed_PARAMATER = target3_Speed_PARAMATER
    ua_to_cdti_data.Target3_Alt_dif_PARAMATER = target3_Alt_dif_PARAMATER
    ua_to_cdti_data.Target3_Status_PARAMATER = target3_Status_PARAMATER
    ua_to_cdti_data.Target3_AppStatus_PARAMATER = target3_AppStatus_PARAMATER

    ua_to_cdti_data.Target4_Visible_PARAMATER = target4_Visible_PARAMATER
    ua_to_cdti_data.Target4_Pic_PARAMATER = target4_Pic_PARAMATER
    ua_to_cdti_data.Target4_RotateAngle_PARAMATER = target4_RotateAngle_PARAMATER
    ua_to_cdti_data.Target4_X_PARAMATER = target4_X_PARAMATER
    ua_to_cdti_data.Target4_Y_PARAMATER = target4_Y_PARAMATER
    ua_to_cdti_data.Target4_FlightId_PARAMATER = target4_FlightId_PARAMATER
    ua_to_cdti_data.Target4_Speed_PARAMATER = target4_Speed_PARAMATER
    ua_to_cdti_data.Target4_Alt_dif_PARAMATER = target4_Alt_dif_PARAMATER
    ua_to_cdti_data.Target4_Status_PARAMATER = target4_Status_PARAMATER
    ua_to_cdti_data.Target4_AppStatus_PARAMATER = target4_AppStatus_PARAMATER

    ua_to_cdti_data.Target5_Visible_PARAMATER = target5_Visible_PARAMATER
    ua_to_cdti_data.Target5_Pic_PARAMATER = target5_Pic_PARAMATER
    ua_to_cdti_data.Target5_RotateAngle_PARAMATER = target5_RotateAngle_PARAMATER
    ua_to_cdti_data.Target5_X_PARAMATER = target5_X_PARAMATER
    ua_to_cdti_data.Target5_Y_PARAMATER = target5_Y_PARAMATER
    ua_to_cdti_data.Target5_FlightId_PARAMATER = target5_FlightId_PARAMATER
    ua_to_cdti_data.Target5_Speed_PARAMATER = target5_Speed_PARAMATER
    ua_to_cdti_data.Target5_Alt_dif_PARAMATER = target5_Alt_dif_PARAMATER
    ua_to_cdti_data.Target5_Status_PARAMATER = target5_Status_PARAMATER
    ua_to_cdti_data.Target5_AppStatus_PARAMATER = target5_AppStatus_PARAMATER
    ua_to_cdti_data.A661_END_BLOCK = int('D0',16)
    ua_to_cdti_data.Unused1 = '000'.encode()




if __name__ == '__main__':
    work_a = MyThread()
    work_a.start()
    pack()
    buf = ua_to_cdti_data.encode()
    print("待发送的字节:" + str(ua_to_cdti_data.encode()))
    IP_PORT = ('127.0.0.1', 8001)
    socket_661 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    socket_661.sendto(buf, IP_PORT)