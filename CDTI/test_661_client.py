from a661_api import *
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

compass_rotate_angle = 0    #罗盘旋转角
compass_step = 32            #罗盘步长
ownship_toa_time = 64965.176  #toa时间
ownship_id =  'AC9733'       #本机航班号
ownship_alt =  31999
#本机飞行高度
ownship_lon = 103.956214      #本机经度
ownship_lat = 30.567821     #本机纬度
ownship_alt_range = 30000    #本机高度范围
ownship_angle = 34.612     #本机航向角
ownship_appstatus = 15 # '0b0111' airb有效、surf有效、vsa有效、itp有效#本机应用状态

target1_visible = 1
target1_pic = 302
target1_rotate_angle = 0
target1_x = 150
target1_y = 400
target1_flightId = '1KKU3C'
target1_Speed = 890
target1_Alt_dif = 1000
target1_Status = 1   #1=AIR 2=GROUND
target1_AppStatus = 11 # '0b1011' airb有效、surf有效、vsa无效、itp有效

target1_lon = 103.958082
target1_lat = 30.572672
target1_vsa_distance = 20.75
target1_vsa_velocity1 = 976.1
target1_vsa_velocity2 = 730.45
target1_itp_distance = 32
target1_itp_distance_rate = 20.0
target1_itp_forward = 1
target1_itp_geometry_status = 1


target2_visible = 1
target2_pic = 302
target2_rotate_angle = 13
target2_x = 250
target2_y = 420
target2_flightId = '2IJQ6M'
target2_Speed = 900
target2_Alt_dif = 2000
target2_Status = 1   # 1=AIR 2=GROUND
target2_AppStatus = 9 # '0b1001' airb有效、surf无效、vsa无效、itp有效
target2_lon = 103.960526
target2_lat = 32.687632
target2_vsa_horizontal_distance = 14.5
target2_vsa_velocity1 = 376.1
target2_vsa_velocity2 = 130.667
target2_itp_distance = 64    #16bytes
target2_itp_distance_rate = 7.8   #16byte
target2_itp_forward = 1    #12bytes
target2_itp_geometry_status = 0  #12bytes

target3_visible = 1
target3_pic = 302
target3_rotate_angle = 12
target3_x = 350
target3_y = 440
target3_flightId = '3YBJ6M'
target3_Speed = 895
target3_Alt_dif = 3000
target3_Status = 2   # 1=AIR 2=GROUND
target3_AppStatus =  13 # '0b1101' airb有效、surf无效、vsa无效、itp有效
target3_lon = 103.960526
target3_lat = 30.579263
target3_vsa_horizontal_distance = 10
target3_vsa_velocity1 = 476.1
target3_vsa_velocity2 = 230
target3_itp_distance = 16  #16bytes
target3_itp_distance_rate = 5.8    #16byte
target3_itp_forward = 1      #12bytes
target3_itp_geometry_status = 0  #12bytes

target4_visible = 1
target4_pic = 302
target4_rotate_angle = 15
target4_x = 450
target4_y = 460
target4_flightId = '4MS761'
target4_Speed = 750
target4_Alt_dif = -1000
target4_Status =  2   # 1=AIR 2=GROUND
target4_AppStatus = 0 # '0b0000' airb无效、surf无效、vsa无效、itp无效
target4_lon = 103.950896
target4_lat = 30.570433
target4_vsa_horizontal_distance = 24.12
target4_vsa_velocity1 = 446.1
target4_vsa_velocity2 = 240
target4_itp_distance = 32   #16bytes
target4_itp_distance_rate = 9.8  #16byte
target4_itp_forward = 2      #12bytes
target4_itp_geometry_status = 1  #12bytes

target5_visible = 1
target5_pic = 362
target5_rotate_angle = 6
target5_x = 550
target5_y = 380
target5_flightId = '5SAQW'
target5_Speed = 800
target5_Alt_dif = -2000
target5_Status =  1   # 1=AIR 2=GROUND
target5_AppStatus = 11 # '0b1011' airb有效、surf有效、vsa无效、itp有效
target5_lon = 103.955926
target5_lat = 30.581129
target5_vsa_horizontal_distance = 31.9
target5_vsa_velocity1 = 345.6
target5_vsa_velocity2 = 287.887
target5_itp_distance = 64     #16bytes
target5_itp_distance_rate = 4.8  #16byte
target5_itp_forward = 2     #12bytes
target5_itp_geometry_status = 1  #12bytes

# target2_visible = 0
# target2_pic = 0
# target2_rotate_angle = 0
# target2_x = 0
# target2_y = 0
# target2_flightId = ''
# target2_Speed = 0
# target2_Alt_dif = 0
# target2_Status = 0   # 1=AIR 2=GROUND
# target2_AppStatus = 0 # '0b1001' airb有效、surf无效、vsa无效、itp有效
# target2_lon = 0
# target2_lat = 0
# target2_vsa_horizontal_distance = 0
# target2_vsa_velocity1 =0
# target2_vsa_velocity2 = 0
# target2_itp_distance =0  #16bytes
# target2_itp_distance_rate =0 #16byte
# target2_itp_forward = 0    #12bytes
# target2_itp_geometry_status = 0  #12bytes
#
# target3_visible = 0
# target3_pic = 0
# target3_rotate_angle = 0
# target3_x = 0
# target3_y = 0
# target3_flightId = ''
# target3_Speed = 0
# target3_Alt_dif =0
# target3_Status = 0  # 1=AIR 2=GROUND
# target3_AppStatus =  0 # '0b1101' airb有效、surf无效、vsa无效、itp有效
# target3_lon = 0
# target3_lat = 0
# target3_vsa_horizontal_distance =0
# target3_vsa_velocity1 = 0
# target3_vsa_velocity2 = 0
# target3_itp_distance = 0 #16bytes
# target3_itp_distance_rate = 0   #16byte
# target3_itp_forward = 0    #12bytes
# target3_itp_geometry_status = 0  #12bytes
#
# target4_visible =0
# target4_pic = 0
# target4_rotate_angle = 0
# target4_x = 0
# target4_y = 0
# target4_flightId = ''
# target4_Speed = 0
# target4_Alt_dif =0
# target4_Status =  0   # 1=AIR 2=GROUND
# target4_AppStatus = 0 # '0b0000' airb无效、surf无效、vsa无效、itp无效
# target4_lon = 0
# target4_lat = 0
# target4_vsa_horizontal_distance =0
# target4_vsa_velocity1 = 0
# target4_vsa_velocity2 = 0
# target4_itp_distance = 0   #16bytes
# target4_itp_distance_rate =0  #16byte
# target4_itp_forward =0    #12bytes
# target4_itp_geometry_status =0  #12bytes
#
# target5_visible = 0
# target5_pic = 0
# target5_rotate_angle = 0
# target5_x = 0
# target5_y = 0
# target5_flightId = ''
# target5_Speed = 0
# target5_Alt_dif = 0
# target5_Status =  0   # 1=AIR 2=GROUND
# target5_AppStatus = 0
# target5_lon = 0
# target5_lat = 0
# target5_vsa_horizontal_distance = 0
# target5_vsa_velocity1 = 0
# target5_vsa_velocity2 = 0
# target5_itp_distance = 0     #16bytes
# target5_itp_distance_rate = 0  #16byte
# target5_itp_forward = 0   #12bytes
# target5_itp_geometry_status = 0  #12bytes

def pack():

    ua_to_cdti_data.A661_BEGIN_BLOCK = int('B0',16)
    ua_to_cdti_data.LayerIdent = 1
    ua_to_cdti_data.ContextNumber = 1
    ua_to_cdti_data.BlockSize = 1376
    # TOA时间
    ownship_Toa_TIME_PARAMATER =  A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    ownship_Toa_TIME_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    ownship_Toa_TIME_PARAMATER.CommandSize = 16
    ownship_Toa_TIME_PARAMATER.WidgetIdent = 9
    ownship_Toa_TIME_PARAMATER.UnusedPad1 = 0
    ownship_Toa_TIME_PARAMATER.ParameterIdent = int('B490', 16)
    ownship_Toa_TIME_PARAMATER.ParameterValueBuffer = ownship_toa_time
    ownship_Toa_TIME_PARAMATER.UnusedPad2 = 0
    # 罗盘旋转角度
    compass_Bitmap_SET_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    compass_Bitmap_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    compass_Bitmap_SET_PARAMATER.CommandSize = 12
    compass_Bitmap_SET_PARAMATER.WidgetIdent = 0
    compass_Bitmap_SET_PARAMATER.UnusedPad = 0
    compass_Bitmap_SET_PARAMATER.ParameterIdent = int('B2C0',16)  #设置旋转角
    compass_Bitmap_SET_PARAMATER.ParameterValueBuffer = compass_rotate_angle
    #罗盘步长
    compass_Step_SET_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    compass_Step_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    compass_Step_SET_PARAMATER.CommandSize = 12
    compass_Step_SET_PARAMATER.WidgetIdent = 1
    compass_Step_SET_PARAMATER.UnusedPad = 0
    compass_Step_SET_PARAMATER.ParameterIdent = int('B490',16)
    compass_Step_SET_PARAMATER.ParameterValueBuffer = compass_step
    #本机航班号
    ownship_FlightId_SET_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    ownship_FlightId_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_FlightId_SET_PARAMATER.CommandSize = 16
    ownship_FlightId_SET_PARAMATER.WidgetIdent = 2
    ownship_FlightId_SET_PARAMATER.UnusedPad1 = 0
    ownship_FlightId_SET_PARAMATER.ParameterIdent = int('B490',16)
    ownship_FlightId_SET_PARAMATER.ParameterValueBuffer = ownship_id.encode()
    ownship_FlightId_SET_PARAMATER.UnusedPad2 = 0

    #本机飞行高度
    ownship_Alt_SET_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    ownship_Alt_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Alt_SET_PARAMATER.CommandSize = 12
    ownship_Alt_SET_PARAMATER.WidgetIdent = 3
    ownship_Alt_SET_PARAMATER.UnusedPad = 0
    ownship_Alt_SET_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Alt_SET_PARAMATER.ParameterValueBuffer = ownship_alt
    #本机经度
    ownship_Lon_SET_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    ownship_Lon_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Lon_SET_PARAMATER.CommandSize = 16
    ownship_Lon_SET_PARAMATER.WidgetIdent = 4
    ownship_Lon_SET_PARAMATER.UnusedPad = 0
    ownship_Lon_SET_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Lon_SET_PARAMATER.ParameterValueBuffer = ownship_lon
    #本机纬度
    ownship_Lat_SET_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    ownship_Lat_SET_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Lat_SET_PARAMATER.CommandSize = 16
    ownship_Lat_SET_PARAMATER.WidgetIdent = 5
    ownship_Lat_SET_PARAMATER.UnusedPad = 0
    ownship_Lat_SET_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Lat_SET_PARAMATER.ParameterValueBuffer = ownship_lat
    #本机高度范围
    ownship_Alt_Range_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    ownship_Alt_Range_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Alt_Range_PARAMATER.CommandSize = 12
    ownship_Alt_Range_PARAMATER.WidgetIdent = 6
    ownship_Alt_Range_PARAMATER.UnusedPad = 0
    ownship_Alt_Range_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Alt_Range_PARAMATER.ParameterValueBuffer = ownship_alt_range
    #本机航向角
    ownship_Course_Angle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    ownship_Course_Angle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_Course_Angle_PARAMATER.CommandSize = 16
    ownship_Course_Angle_PARAMATER.WidgetIdent = 7
    ownship_Course_Angle_PARAMATER.UnusedPad = 0
    ownship_Course_Angle_PARAMATER.ParameterIdent = int('B490',16)
    ownship_Course_Angle_PARAMATER.ParameterValueBuffer = ownship_angle
    #本机应用状态
    ownship_App_Status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    ownship_App_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    ownship_App_Status_PARAMATER.CommandSize = 12
    ownship_App_Status_PARAMATER.WidgetIdent = 8
    ownship_App_Status_PARAMATER.UnusedPad = 0
    ownship_App_Status_PARAMATER.ParameterIdent = int('B2F0',16)
    ownship_App_Status_PARAMATER.ParameterValueBuffer = ownship_appstatus
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
    target1_RotateAngle_PARAMATER= A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target1_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_RotateAngle_PARAMATER.CommandSize = 16
    target1_RotateAngle_PARAMATER.WidgetIdent = 11
    target1_RotateAngle_PARAMATER.UnusedPad1 = 0
    target1_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target1_RotateAngle_PARAMATER.ParameterValueBuffer = target1_rotate_angle
    target1_RotateAngle_PARAMATER.UnusedPad2 = 0
    #1号目标机设置X轴坐标
    target1_X_PARAMATER= A661_CMD_SET_PARAMATER_12BYTE()
    target1_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_X_PARAMATER.CommandSize = 12
    target1_X_PARAMATER.WidgetIdent = 11
    target1_X_PARAMATER.UnusedPad = 0
    target1_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target1_X_PARAMATER.ParameterValueBuffer = target1_x
    #1号目标机设置Y轴坐标
    target1_Y_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target1_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Y_PARAMATER.CommandSize = 12
    target1_Y_PARAMATER.WidgetIdent = 11
    target1_Y_PARAMATER.UnusedPad = 0
    target1_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target1_Y_PARAMATER.ParameterValueBuffer = target1_y #图片类型ID
    #1号目标机航班号
    target1_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target1_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_FlightId_PARAMATER.CommandSize = 16
    target1_FlightId_PARAMATER.WidgetIdent = 12
    target1_FlightId_PARAMATER.UnusedPad = 0
    target1_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target1_FlightId_PARAMATER.ParameterValueBuffer = target1_flightId.encode()
    #1号目标机地速
    target1_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target1_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Speed_PARAMATER.CommandSize = 16
    target1_Speed_PARAMATER.WidgetIdent = 13
    target1_Speed_PARAMATER.UnusedPad = 0
    target1_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target1_Speed_PARAMATER.ParameterValueBuffer = target1_Speed
    #1号目标机高度差
    target1_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_INT()
    target1_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Alt_dif_PARAMATER.CommandSize = 16
    target1_Alt_dif_PARAMATER.WidgetIdent = 14
    target1_Alt_dif_PARAMATER.UnusedPad = 0
    target1_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target1_Alt_dif_PARAMATER.ParameterValueBuffer = target1_Alt_dif
    #1号目标机飞行状态
    target1_Status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target1_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_Status_PARAMATER.CommandSize = 12
    target1_Status_PARAMATER.WidgetIdent = 15
    target1_Status_PARAMATER.UnusedPad = 0
    target1_Status_PARAMATER.ParameterIdent = int('B490',16)
    target1_Status_PARAMATER.ParameterValueBuffer = target1_Status
    #1号目标机应用状态
    target1_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target1_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_AppStatus_PARAMATER.CommandSize = 12
    target1_AppStatus_PARAMATER.WidgetIdent = 16
    target1_AppStatus_PARAMATER.UnusedPad = 0
    target1_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target1_AppStatus_PARAMATER.ParameterValueBuffer = target1_AppStatus
    #1号目标机经度
    target1_lon_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target1_lon_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_lon_PARAMATER.CommandSize = 16
    target1_lon_PARAMATER.WidgetIdent = 17
    target1_lon_PARAMATER.UnusedPad1 = 0
    target1_lon_PARAMATER.ParameterIdent = int('B490',16)
    target1_lon_PARAMATER.ParameterValueBuffer = target1_lon
    target1_lon_PARAMATER.UnusedPad2 = 0
    #1号目标机纬度
    target1_lat_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target1_lat_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_lat_PARAMATER.CommandSize = 16
    target1_lat_PARAMATER.WidgetIdent = 18
    target1_lat_PARAMATER.UnusedPad1 = 0
    target1_lat_PARAMATER.ParameterIdent = int('B490',16)
    target1_lat_PARAMATER.ParameterValueBuffer = target1_lat
    target1_lat_PARAMATER.UnusedPad2 = 0
    #1号目标机vsa水平距离
    target1_vsa_horizontal_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target1_vsa_horizontal_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target1_vsa_horizontal_distance_PARAMATER.CommandSize = 16
    target1_vsa_horizontal_distance_PARAMATER.WidgetIdent = 19
    target1_vsa_horizontal_distance_PARAMATER.UnusedPad1 = 0
    target1_vsa_horizontal_distance_PARAMATER.ParameterIdent = int('B490',16)
    target1_vsa_horizontal_distance_PARAMATER.ParameterValueBuffer = target1_vsa_distance
    target1_vsa_horizontal_distance_PARAMATER.UnusedPad2 = 0
    #1号目标机vsa速度
    target1_vsa_velocity_PARAMATER = A661_CMD_SET_PARAMATER_20BYTE_2FLOAT()
    target1_vsa_velocity_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target1_vsa_velocity_PARAMATER.CommandSize = 20
    target1_vsa_velocity_PARAMATER.WidgetIdent = 20
    target1_vsa_velocity_PARAMATER.UnusedPad1 = 0
    target1_vsa_velocity_PARAMATER.ParameterIdent = int('B490', 16)
    target1_vsa_velocity_PARAMATER.ParameterValueBuffer = target1_vsa_velocity1
    target1_vsa_velocity_PARAMATER.ParameterValueBuffer2 = target1_vsa_velocity2
    target1_vsa_velocity_PARAMATER.UnusedPad2 = 0
    #1号目标机itp距离
    target1_itp_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target1_itp_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target1_itp_distance_PARAMATER.CommandSize = 16
    target1_itp_distance_PARAMATER.WidgetIdent = 21
    target1_itp_distance_PARAMATER.UnusedPad1 = 0
    target1_itp_distance_PARAMATER.ParameterIdent = int('B490', 16)
    target1_itp_distance_PARAMATER.ParameterValueBuffer = target1_itp_distance
    target1_itp_distance_PARAMATER.UnusedPad2 = 0
    #1号目标机itp距离变化率
    target1_itp_distance_rate_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target1_itp_distance_rate_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target1_itp_distance_rate_PARAMATER.CommandSize = 16
    target1_itp_distance_rate_PARAMATER.WidgetIdent = 22
    target1_itp_distance_rate_PARAMATER.UnusedPad1 = 0
    target1_itp_distance_rate_PARAMATER.ParameterIdent = int('B490', 16)
    target1_itp_distance_rate_PARAMATER.ParameterValueBuffer = target1_itp_distance_rate
    target1_itp_distance_rate_PARAMATER.UnusedPad2 = 0
    #1号目标机itp前后状态
    target1_itp_forward_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target1_itp_forward_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target1_itp_forward_PARAMATER.CommandSize = 12
    target1_itp_forward_PARAMATER.WidgetIdent = 23
    target1_itp_forward_PARAMATER.UnusedPad = 0
    target1_itp_forward_PARAMATER.ParameterIdent = int('B490', 16)
    target1_itp_forward_PARAMATER.ParameterValueBuffer = target1_itp_forward
    #1号目标机itp几何状态
    target1_itp_geometry_status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target1_itp_geometry_status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target1_itp_geometry_status_PARAMATER.CommandSize = 12
    target1_itp_geometry_status_PARAMATER.WidgetIdent = 24
    target1_itp_geometry_status_PARAMATER.UnusedPad = 0
    target1_itp_geometry_status_PARAMATER.ParameterIdent = int('B490', 16)
    target1_itp_geometry_status_PARAMATER.ParameterValueBuffer = target1_itp_geometry_status


    #2号目标机设置显示、隐藏
    target2_Visible_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_Visible_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Visible_PARAMATER.CommandSize = 12
    target2_Visible_PARAMATER.WidgetIdent = 31
    target2_Visible_PARAMATER.UnusedPad = 0
    target2_Visible_PARAMATER.ParameterIdent = int('0xB530',16)  #设置显示/隐藏
    target2_Visible_PARAMATER.ParameterValueBuffer = target2_visible #1显示 0隐藏
    #2号目标机设置图片源
    target2_Pic_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_Pic_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Pic_PARAMATER.CommandSize = 12
    target2_Pic_PARAMATER.WidgetIdent = 31
    target2_Pic_PARAMATER.UnusedPad = 0
    target2_Pic_PARAMATER.ParameterIdent = int('0xB4C0',16)
    target2_Pic_PARAMATER.ParameterValueBuffer = target2_pic #图片类型ID
    #2号目标机设置旋转角
    target2_RotateAngle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target2_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_RotateAngle_PARAMATER.CommandSize = 16
    target2_RotateAngle_PARAMATER.WidgetIdent = 31
    target2_RotateAngle_PARAMATER.UnusedPad1 = 0
    target2_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target2_RotateAngle_PARAMATER.ParameterValueBuffer = target2_rotate_angle
    target2_RotateAngle_PARAMATER.UnusedPad2 = 0
    #2号目标机设置X轴坐标
    target2_X_PARAMATER= A661_CMD_SET_PARAMATER_12BYTE()
    target2_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_X_PARAMATER.CommandSize = 12
    target2_X_PARAMATER.WidgetIdent = 31
    target2_X_PARAMATER.UnusedPad = 0
    target2_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target2_X_PARAMATER.ParameterValueBuffer = target2_x
    #1号目标机设置Y轴坐标
    target2_Y_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Y_PARAMATER.CommandSize = 12
    target2_Y_PARAMATER.WidgetIdent = 31
    target2_Y_PARAMATER.UnusedPad = 0
    target2_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target2_Y_PARAMATER.ParameterValueBuffer = target2_y #图片类型ID
    #2号目标机航班号
    target2_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target2_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_FlightId_PARAMATER.CommandSize = 16
    target2_FlightId_PARAMATER.WidgetIdent = 32
    target2_FlightId_PARAMATER.UnusedPad = 0
    target2_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target2_FlightId_PARAMATER.ParameterValueBuffer = target2_flightId.encode()
    #2号目标机地速
    target2_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target2_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Speed_PARAMATER.CommandSize = 16
    target2_Speed_PARAMATER.WidgetIdent = 33
    target2_Speed_PARAMATER.UnusedPad = 0
    target2_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target2_Speed_PARAMATER.ParameterValueBuffer = target2_Speed
    #2号目标机高度差
    target2_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_INT()
    target2_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Alt_dif_PARAMATER.CommandSize = 16
    target2_Alt_dif_PARAMATER.WidgetIdent = 34
    target2_Alt_dif_PARAMATER.UnusedPad = 0
    target2_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target2_Alt_dif_PARAMATER.ParameterValueBuffer = target2_Alt_dif
    #2号目标机飞行状态
    target2_Status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_Status_PARAMATER.CommandSize = 12
    target2_Status_PARAMATER.WidgetIdent = 35
    target2_Status_PARAMATER.UnusedPad = 0
    target2_Status_PARAMATER.ParameterIdent = int('B490',16)
    target2_Status_PARAMATER.ParameterValueBuffer = target2_Status
    #2号目标机应用状态
    target2_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target2_AppStatus_PARAMATER.CommandSize = 12
    target2_AppStatus_PARAMATER.WidgetIdent = 36
    target2_AppStatus_PARAMATER.UnusedPad = 0
    target2_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target2_AppStatus_PARAMATER.ParameterValueBuffer = target2_AppStatus

    # 2号目标机经度
    target2_lon_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target2_lon_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target2_lon_PARAMATER.CommandSize = 16
    target2_lon_PARAMATER.WidgetIdent = 37
    target2_lon_PARAMATER.UnusedPad1 = 0
    target2_lon_PARAMATER.ParameterIdent = int('B490', 16)
    target2_lon_PARAMATER.ParameterValueBuffer = target2_lon
    target2_lon_PARAMATER.UnusedPad2 = 0
    # 2号目标机纬度
    target2_lat_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target2_lat_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target2_lat_PARAMATER.CommandSize = 16
    target2_lat_PARAMATER.WidgetIdent = 38
    target2_lat_PARAMATER.UnusedPad1 = 0
    target2_lat_PARAMATER.ParameterIdent = int('B490', 16)
    target2_lat_PARAMATER.ParameterValueBuffer = target2_lat
    target2_lat_PARAMATER.UnusedPad2 = 0
    # 2号目标机vsa水平距离
    target2_vsa_horizontal_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target2_vsa_horizontal_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target2_vsa_horizontal_distance_PARAMATER.CommandSize = 16
    target2_vsa_horizontal_distance_PARAMATER.WidgetIdent =39
    target2_vsa_horizontal_distance_PARAMATER.UnusedPad1 = 0
    target2_vsa_horizontal_distance_PARAMATER.ParameterIdent = int('B490', 16)
    target2_vsa_horizontal_distance_PARAMATER.ParameterValueBuffer = target2_vsa_horizontal_distance
    target2_vsa_horizontal_distance_PARAMATER.UnusedPad2 = 0
    # 2号目标机vsa速度
    target2_vsa_velocity_PARAMATER = A661_CMD_SET_PARAMATER_20BYTE_2FLOAT()
    target2_vsa_velocity_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target2_vsa_velocity_PARAMATER.CommandSize = 16
    target2_vsa_velocity_PARAMATER.WidgetIdent = 40
    target2_vsa_velocity_PARAMATER.UnusedPad1 = 0
    target2_vsa_velocity_PARAMATER.ParameterIdent = int('B490', 16)
    target2_vsa_velocity_PARAMATER.ParameterValueBuffer = target2_vsa_velocity1
    target2_vsa_velocity_PARAMATER.ParameterValueBuffer2 = target2_vsa_velocity2
    target2_vsa_velocity_PARAMATER.UnusedPad2 = 0
    #2号目标机itp距离
    target2_itp_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target2_itp_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target2_itp_distance_PARAMATER.CommandSize = 16
    target2_itp_distance_PARAMATER.WidgetIdent =41
    target2_itp_distance_PARAMATER.UnusedPad1 = 0
    target2_itp_distance_PARAMATER.ParameterIdent = int('B490', 16)
    target2_itp_distance_PARAMATER.ParameterValueBuffer = target2_itp_distance
    target2_itp_distance_PARAMATER.UnusedPad2 = 0
    # 2号目标机itp距离变化率
    target2_itp_distance_rate_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target2_itp_distance_rate_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target2_itp_distance_rate_PARAMATER.CommandSize = 16
    target2_itp_distance_rate_PARAMATER.WidgetIdent = 42
    target2_itp_distance_rate_PARAMATER.UnusedPad1 = 0
    target2_itp_distance_rate_PARAMATER.ParameterIdent = int('B490', 16)
    target2_itp_distance_rate_PARAMATER.ParameterValueBuffer = target2_itp_distance_rate
    target2_itp_distance_rate_PARAMATER.UnusedPad2 = 0
    # 2号目标机itp前后状态
    target2_itp_forward_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_itp_forward_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target2_itp_forward_PARAMATER.CommandSize = 12
    target2_itp_forward_PARAMATER.WidgetIdent = 43
    target2_itp_forward_PARAMATER.UnusedPad = 0
    target2_itp_forward_PARAMATER.ParameterIdent = int('B490', 16)
    target2_itp_forward_PARAMATER.ParameterValueBuffer = target2_itp_forward
    # 2号目标机itp几何状态
    target2_itp_geometry_status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target2_itp_geometry_status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target2_itp_geometry_status_PARAMATER.CommandSize = 12
    target2_itp_geometry_status_PARAMATER.WidgetIdent = 44
    target2_itp_geometry_status_PARAMATER.UnusedPad = 0
    target2_itp_geometry_status_PARAMATER.ParameterIdent = int('B490', 16)
    target2_itp_geometry_status_PARAMATER.ParameterValueBuffer = target2_itp_geometry_status

    #3号目标机设置显示、隐藏
    target3_Visible_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_Visible_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Visible_PARAMATER.CommandSize = 12
    target3_Visible_PARAMATER.WidgetIdent = 51
    target3_Visible_PARAMATER.UnusedPad = 0
    target3_Visible_PARAMATER.ParameterIdent = int('0xB530',16)  #设置显示/隐藏
    target3_Visible_PARAMATER.ParameterValueBuffer = target3_visible #1显示 0隐藏
    #3号目标机设置图片源
    target3_Pic_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_Pic_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Pic_PARAMATER.CommandSize = 12
    target3_Pic_PARAMATER.WidgetIdent = 51
    target3_Pic_PARAMATER.UnusedPad = 0
    target3_Pic_PARAMATER.ParameterIdent = int('0xB4C0',16)
    target3_Pic_PARAMATER.ParameterValueBuffer = target3_pic #图片类型ID
    #3号目标机设置旋转角
    target3_RotateAngle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target3_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_RotateAngle_PARAMATER.CommandSize = 16
    target3_RotateAngle_PARAMATER.WidgetIdent = 51
    target3_RotateAngle_PARAMATER.UnusedPad1 = 0
    target3_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target3_RotateAngle_PARAMATER.ParameterValueBuffer = target3_rotate_angle
    target3_RotateAngle_PARAMATER.UnusedPad2 = 0
    #3号目标机设置X轴坐标
    target3_X_PARAMATER= A661_CMD_SET_PARAMATER_12BYTE()
    target3_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_X_PARAMATER.CommandSize = 12
    target3_X_PARAMATER.WidgetIdent = 51
    target3_X_PARAMATER.UnusedPad = 0
    target3_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target3_X_PARAMATER.ParameterValueBuffer = target3_x
    #3号目标机设置Y轴坐标
    target3_Y_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Y_PARAMATER.CommandSize = 12
    target3_Y_PARAMATER.WidgetIdent = 51
    target3_Y_PARAMATER.UnusedPad = 0
    target3_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target3_Y_PARAMATER.ParameterValueBuffer = target3_y #图片类型ID
    #3号目标机航班号
    target3_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target3_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_FlightId_PARAMATER.CommandSize = 16
    target3_FlightId_PARAMATER.WidgetIdent = 52
    target3_FlightId_PARAMATER.UnusedPad = 0
    target3_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target3_FlightId_PARAMATER.ParameterValueBuffer = target3_flightId.encode()
    #3号目标机地速
    target3_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target3_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Speed_PARAMATER.CommandSize = 16
    target3_Speed_PARAMATER.WidgetIdent = 53
    target3_Speed_PARAMATER.UnusedPad = 0
    target3_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target3_Speed_PARAMATER.ParameterValueBuffer = target3_Speed
    #3号目标机高度差
    target3_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_INT()
    target3_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Alt_dif_PARAMATER.CommandSize = 16
    target3_Alt_dif_PARAMATER.WidgetIdent = 54
    target3_Alt_dif_PARAMATER.UnusedPad = 0
    target3_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target3_Alt_dif_PARAMATER.ParameterValueBuffer = target3_Alt_dif
    #3号目标机飞行状态
    target3_Status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_Status_PARAMATER.CommandSize = 12
    target3_Status_PARAMATER.WidgetIdent = 55
    target3_Status_PARAMATER.UnusedPad = 0
    target3_Status_PARAMATER.ParameterIdent = int('B490',16)
    target3_Status_PARAMATER.ParameterValueBuffer = target3_Status
    #3号目标机应用状态
    target3_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target3_AppStatus_PARAMATER.CommandSize = 12
    target3_AppStatus_PARAMATER.WidgetIdent = 56
    target3_AppStatus_PARAMATER.UnusedPad = 0
    target3_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target3_AppStatus_PARAMATER.ParameterValueBuffer = target3_AppStatus

    # 3号目标机经度
    target3_lon_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target3_lon_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target3_lon_PARAMATER.CommandSize = 16
    target3_lon_PARAMATER.WidgetIdent = 57
    target3_lon_PARAMATER.UnusedPad1 = 0
    target3_lon_PARAMATER.ParameterIdent = int('B490', 16)
    target3_lon_PARAMATER.ParameterValueBuffer = target3_lon
    target3_lon_PARAMATER.UnusedPad2 = 0
    # 3号目标机纬度
    target3_lat_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target3_lat_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target3_lat_PARAMATER.CommandSize = 16
    target3_lat_PARAMATER.WidgetIdent = 58
    target3_lat_PARAMATER.UnusedPad1 = 0
    target3_lat_PARAMATER.ParameterIdent = int('B490', 16)
    target3_lat_PARAMATER.ParameterValueBuffer = target3_lat
    target3_lat_PARAMATER.UnusedPad2 = 0
    # 3号目标机vsa水平距离
    target3_vsa_horizontal_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target3_vsa_horizontal_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target3_vsa_horizontal_distance_PARAMATER.CommandSize = 16
    target3_vsa_horizontal_distance_PARAMATER.WidgetIdent = 59
    target3_vsa_horizontal_distance_PARAMATER.UnusedPad1 = 0
    target3_vsa_horizontal_distance_PARAMATER.ParameterIdent = int('B490', 16)
    target3_vsa_horizontal_distance_PARAMATER.ParameterValueBuffer = target3_vsa_horizontal_distance
    target3_vsa_horizontal_distance_PARAMATER.UnusedPad2 = 0
    # 3号目标机vsa速度
    target3_vsa_velocity_PARAMATER = A661_CMD_SET_PARAMATER_20BYTE_2FLOAT()
    target3_vsa_velocity_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target3_vsa_velocity_PARAMATER.CommandSize = 20
    target3_vsa_velocity_PARAMATER.WidgetIdent = 60
    target3_vsa_velocity_PARAMATER.UnusedPad1 = 0
    target3_vsa_velocity_PARAMATER.ParameterIdent = int('B490', 16)
    target3_vsa_velocity_PARAMATER.ParameterValueBuffer = target3_vsa_velocity1
    target3_vsa_velocity_PARAMATER.ParameterValueBuffer2 = target3_vsa_velocity2
    target3_vsa_velocity_PARAMATER.UnusedPad2 = 0
    # 3号目标机itp距离
    target3_itp_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target3_itp_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target3_itp_distance_PARAMATER.CommandSize = 16
    target3_itp_distance_PARAMATER.WidgetIdent = 61
    target3_itp_distance_PARAMATER.UnusedPad1= 0
    target3_itp_distance_PARAMATER.ParameterIdent = int('B490', 16)
    target3_itp_distance_PARAMATER.ParameterValueBuffer = target3_itp_distance
    target3_itp_distance_PARAMATER.UnusedPad2 = 0
    # 3号目标机itp距离变化率
    target3_itp_distance_rate_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target3_itp_distance_rate_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target3_itp_distance_rate_PARAMATER.CommandSize = 16
    target3_itp_distance_rate_PARAMATER.WidgetIdent = 62
    target3_itp_distance_rate_PARAMATER.UnusedPad1 = 0
    target3_itp_distance_rate_PARAMATER.ParameterIdent = int('B490', 16)
    target3_itp_distance_rate_PARAMATER.ParameterValueBuffer = target3_itp_distance_rate
    target3_itp_distance_rate_PARAMATER.UnusedPad2 = 0

    # 3号目标机itp前后状态
    target3_itp_forward_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_itp_forward_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target3_itp_forward_PARAMATER.CommandSize = 12
    target3_itp_forward_PARAMATER.WidgetIdent = 63
    target3_itp_forward_PARAMATER.UnusedPad = 0
    target3_itp_forward_PARAMATER.ParameterIdent = int('B490', 16)
    target3_itp_forward_PARAMATER.ParameterValueBuffer = target3_itp_forward
    # 3号目标机itp几何状态
    target3_itp_geometry_status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target3_itp_geometry_status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target3_itp_geometry_status_PARAMATER.CommandSize = 12
    target3_itp_geometry_status_PARAMATER.WidgetIdent = 64
    target3_itp_geometry_status_PARAMATER.UnusedPad = 0
    target3_itp_geometry_status_PARAMATER.ParameterIdent = int('B490', 16)
    target3_itp_geometry_status_PARAMATER.ParameterValueBuffer = target3_itp_geometry_status

    #4号目标机设置显示、隐藏
    target4_Visible_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_Visible_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Visible_PARAMATER.CommandSize = 12
    target4_Visible_PARAMATER.WidgetIdent = 71
    target4_Visible_PARAMATER.UnusedPad = 0
    target4_Visible_PARAMATER.ParameterIdent = int('0xB530',16)  #设置显示/隐藏
    target4_Visible_PARAMATER.ParameterValueBuffer = target4_visible #1显示 0隐藏
    #4号目标机设置图片源
    target4_Pic_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_Pic_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Pic_PARAMATER.CommandSize = 12
    target4_Pic_PARAMATER.WidgetIdent = 71
    target4_Pic_PARAMATER.UnusedPad = 0
    target4_Pic_PARAMATER.ParameterIdent = int('0xB4C0',16)
    target4_Pic_PARAMATER.ParameterValueBuffer = target4_pic #图片类型ID
    #4号目标机设置旋转角
    target4_RotateAngle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target4_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_RotateAngle_PARAMATER.CommandSize = 16
    target4_RotateAngle_PARAMATER.WidgetIdent = 71
    target4_RotateAngle_PARAMATER.UnusedPad1 = 0
    target4_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target4_RotateAngle_PARAMATER.ParameterValueBuffer = target4_rotate_angle
    target4_RotateAngle_PARAMATER.UnusedPad2 = 0
    #4号目标机设置X轴坐标
    target4_X_PARAMATER= A661_CMD_SET_PARAMATER_12BYTE()
    target4_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_X_PARAMATER.CommandSize = 12
    target4_X_PARAMATER.WidgetIdent = 71
    target4_X_PARAMATER.UnusedPad = 0
    target4_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target4_X_PARAMATER.ParameterValueBuffer = target4_x
    #4号目标机设置Y轴坐标
    target4_Y_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Y_PARAMATER.CommandSize = 12
    target4_Y_PARAMATER.WidgetIdent = 71
    target4_Y_PARAMATER.UnusedPad = 0
    target4_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target4_Y_PARAMATER.ParameterValueBuffer = target4_y#图片类型ID
    #4号目标机航班号
    target4_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target4_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_FlightId_PARAMATER.CommandSize = 16
    target4_FlightId_PARAMATER.WidgetIdent = 72
    target4_FlightId_PARAMATER.UnusedPad = 0
    target4_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target4_FlightId_PARAMATER.ParameterValueBuffer = target4_flightId.encode()
    #4号目标机地速
    target4_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target4_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Speed_PARAMATER.CommandSize = 16
    target4_Speed_PARAMATER.WidgetIdent = 73
    target4_Speed_PARAMATER.UnusedPad = 0
    target4_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target4_Speed_PARAMATER.ParameterValueBuffer = target4_Speed
    #4号目标机高度差
    target4_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_INT()
    target4_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Alt_dif_PARAMATER.CommandSize = 16
    target4_Alt_dif_PARAMATER.WidgetIdent = 74
    target4_Alt_dif_PARAMATER.UnusedPad = 0
    target4_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target4_Alt_dif_PARAMATER.ParameterValueBuffer = target4_Alt_dif
    #4号目标机飞行状态
    target4_Status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_Status_PARAMATER.CommandSize = 12
    target4_Status_PARAMATER.WidgetIdent = 75
    target4_Status_PARAMATER.UnusedPad = 0
    target4_Status_PARAMATER.ParameterIdent = int('B490',16)
    target4_Status_PARAMATER.ParameterValueBuffer = target4_Status
    #4号目标机应用状态
    target4_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target4_AppStatus_PARAMATER.CommandSize = 12
    target4_AppStatus_PARAMATER.WidgetIdent = 76
    target4_AppStatus_PARAMATER.UnusedPad = 0
    target4_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target4_AppStatus_PARAMATER.ParameterValueBuffer = target4_AppStatus

    # 4号目标机经度
    target4_lon_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target4_lon_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target4_lon_PARAMATER.CommandSize = 16
    target4_lon_PARAMATER.WidgetIdent = 77
    target4_lon_PARAMATER.UnusedPad1 = 0
    target4_lon_PARAMATER.ParameterIdent = int('B490', 16)
    target4_lon_PARAMATER.ParameterValueBuffer = target4_lon
    target4_lon_PARAMATER.UnusedPad2 = 0
    # 4号目标机纬度
    target4_lat_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target4_lat_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target4_lat_PARAMATER.CommandSize = 16
    target4_lat_PARAMATER.WidgetIdent = 78
    target4_lat_PARAMATER.UnusedPad1 = 0
    target4_lat_PARAMATER.ParameterIdent = int('B490', 16)
    target4_lat_PARAMATER.ParameterValueBuffer = target4_lat
    target4_lat_PARAMATER.UnusedPad2 = 0
    # 4号目标机vsa水平距离
    target4_vsa_horizontal_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target4_vsa_horizontal_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target4_vsa_horizontal_distance_PARAMATER.CommandSize = 16
    target4_vsa_horizontal_distance_PARAMATER.WidgetIdent = 79
    target4_vsa_horizontal_distance_PARAMATER.UnusedPad1 = 0
    target4_vsa_horizontal_distance_PARAMATER.ParameterIdent = int('B490', 16)
    target4_vsa_horizontal_distance_PARAMATER.ParameterValueBuffer = target4_vsa_horizontal_distance
    target4_vsa_horizontal_distance_PARAMATER.UnusedPad2 = 0
    # 4号目标机vsa速度
    target4_vsa_velocity_PARAMATER = A661_CMD_SET_PARAMATER_20BYTE_2FLOAT()
    target4_vsa_velocity_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target4_vsa_velocity_PARAMATER.CommandSize = 20
    target4_vsa_velocity_PARAMATER.WidgetIdent = 80
    target4_vsa_velocity_PARAMATER.UnusedPad1 = 0
    target4_vsa_velocity_PARAMATER.ParameterIdent = int('B490', 16)
    target4_vsa_velocity_PARAMATER.ParameterValueBuffer = target4_vsa_velocity1
    target4_vsa_velocity_PARAMATER.ParameterValueBuffer2 = target4_vsa_velocity2
    target4_vsa_velocity_PARAMATER.UnusedPad2 = 0
    # 4号目标机itp距离
    target4_itp_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target4_itp_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target4_itp_distance_PARAMATER.CommandSize = 16
    target4_itp_distance_PARAMATER.WidgetIdent = 81
    target4_itp_distance_PARAMATER.UnusedPad1 = 0
    target4_itp_distance_PARAMATER.ParameterIdent = int('B490', 16)
    target4_itp_distance_PARAMATER.ParameterValueBuffer = target4_itp_distance
    target4_itp_distance_PARAMATER.UnusedPad2 = 0
    # 4号目标机itp距离变化率
    target4_itp_distance_rate_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target4_itp_distance_rate_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target4_itp_distance_rate_PARAMATER.CommandSize = 16
    target4_itp_distance_rate_PARAMATER.WidgetIdent = 82
    target4_itp_distance_rate_PARAMATER.UnusedPad1 = 0
    target4_itp_distance_rate_PARAMATER.ParameterIdent = int('B490', 16)
    target4_itp_distance_rate_PARAMATER.ParameterValueBuffer = target4_itp_distance_rate
    target4_itp_distance_rate_PARAMATER.UnusedPad2 = 0
    # 4号目标机itp前后状态
    target4_itp_forward_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_itp_forward_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target4_itp_forward_PARAMATER.CommandSize = 12
    target4_itp_forward_PARAMATER.WidgetIdent = 83
    target4_itp_forward_PARAMATER.UnusedPad = 0
    target4_itp_forward_PARAMATER.ParameterIdent = int('B490', 16)
    target4_itp_forward_PARAMATER.ParameterValueBuffer = target4_itp_forward
    # 4号目标机itp几何状态
    target4_itp_geometry_status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target4_itp_geometry_status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target4_itp_geometry_status_PARAMATER.CommandSize = 12
    target4_itp_geometry_status_PARAMATER.WidgetIdent = 84
    target4_itp_geometry_status_PARAMATER.UnusedPad = 0
    target4_itp_geometry_status_PARAMATER.ParameterIdent = int('B490', 16)
    target4_itp_geometry_status_PARAMATER.ParameterValueBuffer = target4_itp_geometry_status

    #5号目标机设置显示、隐藏
    target5_Visible_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_Visible_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Visible_PARAMATER.CommandSize = 12
    target5_Visible_PARAMATER.WidgetIdent = 91
    target5_Visible_PARAMATER.UnusedPad = 0
    target5_Visible_PARAMATER.ParameterIdent = int('0xB530',16)  #设置显示/隐藏
    target5_Visible_PARAMATER.ParameterValueBuffer = target5_visible #1显示 0隐藏
    #5号目标机设置图片源
    target5_Pic_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_Pic_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Pic_PARAMATER.CommandSize = 12
    target5_Pic_PARAMATER.WidgetIdent = 91
    target5_Pic_PARAMATER.UnusedPad = 0
    target5_Pic_PARAMATER.ParameterIdent = int('0xB4C0',16)
    target5_Pic_PARAMATER.ParameterValueBuffer = target5_pic #图片类型ID
    #5号目标机设置旋转角
    target5_RotateAngle_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target5_RotateAngle_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_RotateAngle_PARAMATER.CommandSize = 16
    target5_RotateAngle_PARAMATER.WidgetIdent = 91
    target5_RotateAngle_PARAMATER.UnusedPad1 = 0
    target5_RotateAngle_PARAMATER.ParameterIdent = int('0xB2C0',16)
    target5_RotateAngle_PARAMATER.ParameterValueBuffer = target5_rotate_angle
    target5_RotateAngle_PARAMATER.UnusedPad2 = 0
    #5号目标机设置X轴坐标
    target5_X_PARAMATER= A661_CMD_SET_PARAMATER_12BYTE()
    target5_X_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_X_PARAMATER.CommandSize = 12
    target5_X_PARAMATER.WidgetIdent = 91
    target5_X_PARAMATER.UnusedPad = 0
    target5_X_PARAMATER.ParameterIdent = int('0xB300',16)
    target5_X_PARAMATER.ParameterValueBuffer = target5_x
    #5号目标机设置Y轴坐标
    target5_Y_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_Y_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Y_PARAMATER.CommandSize = 12
    target5_Y_PARAMATER.WidgetIdent = 91
    target5_Y_PARAMATER.UnusedPad = 0
    target5_Y_PARAMATER.ParameterIdent = int('0xB310',16)  #设置显示/隐藏
    target5_Y_PARAMATER.ParameterValueBuffer = target5_y #图片类型ID
    #5号目标机航班号
    target5_FlightId_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE()
    target5_FlightId_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_FlightId_PARAMATER.CommandSize = 16
    target5_FlightId_PARAMATER.WidgetIdent = 92
    target5_FlightId_PARAMATER.UnusedPad = 0
    target5_FlightId_PARAMATER.ParameterIdent = int('B490',16)
    target5_FlightId_PARAMATER.ParameterValueBuffer = target5_flightId.encode()
    #5号目标机地速
    target5_Speed_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target5_Speed_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Speed_PARAMATER.CommandSize = 16
    target5_Speed_PARAMATER.WidgetIdent = 93
    target5_Speed_PARAMATER.UnusedPad = 0
    target5_Speed_PARAMATER.ParameterIdent = int('B490',16)
    target5_Speed_PARAMATER.ParameterValueBuffer = target5_Speed
    #5号目标机高度差
    target5_Alt_dif_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_INT()
    target5_Alt_dif_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Alt_dif_PARAMATER.CommandSize = 16
    target5_Alt_dif_PARAMATER.WidgetIdent = 94
    target5_Alt_dif_PARAMATER.UnusedPad = 0
    target5_Alt_dif_PARAMATER.ParameterIdent = int('B490',16)
    target5_Alt_dif_PARAMATER.ParameterValueBuffer = target5_Alt_dif
    #5号目标机飞行状态
    target5_Status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_Status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_Status_PARAMATER.CommandSize = 12
    target5_Status_PARAMATER.WidgetIdent = 95
    target5_Status_PARAMATER.UnusedPad = 0
    target5_Status_PARAMATER.ParameterIdent = int('B490',16)
    target5_Status_PARAMATER.ParameterValueBuffer = target5_Status
    #5号目标机应用状态
    target5_AppStatus_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_AppStatus_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02',16)
    target5_AppStatus_PARAMATER.CommandSize = 12
    target5_AppStatus_PARAMATER.WidgetIdent = 96
    target5_AppStatus_PARAMATER.UnusedPad = 0
    target5_AppStatus_PARAMATER.ParameterIdent = int('B2F0',16)
    target5_AppStatus_PARAMATER.ParameterValueBuffer = target5_AppStatus
    # 5号目标机经度
    target5_lon_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target5_lon_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target5_lon_PARAMATER.CommandSize = 16
    target5_lon_PARAMATER.WidgetIdent = 97
    target5_lon_PARAMATER.UnusedPad1 = 0
    target5_lon_PARAMATER.ParameterIdent = int('B490', 16)
    target5_lon_PARAMATER.ParameterValueBuffer = target5_lon
    target5_lon_PARAMATER.UnusedPad2 = 0
    # 5号目标机纬度
    target5_lat_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target5_lat_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target5_lat_PARAMATER.CommandSize = 16
    target5_lat_PARAMATER.WidgetIdent = 98
    target5_lat_PARAMATER.UnusedPad1 = 0
    target5_lat_PARAMATER.ParameterIdent = int('B490', 16)
    target5_lat_PARAMATER.ParameterValueBuffer = target5_lat
    target5_lat_PARAMATER.UnusedPad2 = 0
    #5号目标机vsa水平距离
    target5_vsa_horizontal_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target5_vsa_horizontal_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target5_vsa_horizontal_distance_PARAMATER.CommandSize = 16
    target5_vsa_horizontal_distance_PARAMATER.WidgetIdent = 99
    target5_vsa_horizontal_distance_PARAMATER.UnusedPad1 = 0
    target5_vsa_horizontal_distance_PARAMATER.ParameterIdent = int('B490', 16)
    target5_vsa_horizontal_distance_PARAMATER.ParameterValueBuffer = target5_vsa_horizontal_distance
    target5_vsa_horizontal_distance_PARAMATER.UnusedPad2 = 0
    # 5号目标机vsa速度
    target5_vsa_velocity_PARAMATER = A661_CMD_SET_PARAMATER_20BYTE_2FLOAT()
    target5_vsa_velocity_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target5_vsa_velocity_PARAMATER.CommandSize = 16
    target5_vsa_velocity_PARAMATER.WidgetIdent = 100
    target5_vsa_velocity_PARAMATER.UnusedPad1= 0
    target5_vsa_velocity_PARAMATER.ParameterIdent = int('B490', 16)
    target5_vsa_velocity_PARAMATER.ParameterValueBuffer = target5_vsa_velocity1
    target5_vsa_velocity_PARAMATER.ParameterValueBuffer2 = target5_vsa_velocity2
    target5_vsa_velocity_PARAMATER.UnusedPad2 = 0
    # 5号目标机itp距离
    target5_itp_distance_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target5_itp_distance_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target5_itp_distance_PARAMATER.CommandSize = 16
    target5_itp_distance_PARAMATER.WidgetIdent = 101
    target5_itp_distance_PARAMATER.UnusedPad1 = 0
    target5_itp_distance_PARAMATER.ParameterIdent = int('B490', 16)
    target5_itp_distance_PARAMATER.ParameterValueBuffer = target5_itp_distance
    target5_itp_distance_PARAMATER.UnusedPad2 = 0
    # 5号目标机itp距离变化率
    target5_itp_distance_rate_PARAMATER = A661_CMD_SET_PARAMATER_16BYTE_FLOAT()
    target5_itp_distance_rate_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target5_itp_distance_rate_PARAMATER.CommandSize = 16
    target5_itp_distance_rate_PARAMATER.WidgetIdent = 102
    target5_itp_distance_rate_PARAMATER.UnusedPad1 = 0
    target5_itp_distance_rate_PARAMATER.ParameterIdent = int('B490', 16)
    target5_itp_distance_rate_PARAMATER.ParameterValueBuffer = target5_itp_distance_rate
    target5_itp_distance_rate_PARAMATER.UnusedPad2 = 0
    # 5号目标机itp前后状态
    target5_itp_forward_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_itp_forward_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target5_itp_forward_PARAMATER.CommandSize = 12
    target5_itp_forward_PARAMATER.WidgetIdent = 103
    target5_itp_forward_PARAMATER.UnusedPad = 0
    target5_itp_forward_PARAMATER.ParameterIdent = int('B490', 16)
    target5_itp_forward_PARAMATER.ParameterValueBuffer = target5_itp_forward
    # 5号目标机itp几何状态
    target5_itp_geometry_status_PARAMATER = A661_CMD_SET_PARAMATER_12BYTE()
    target5_itp_geometry_status_PARAMATER.A661_CMD_SET_PARAMETER = int('CA02', 16)
    target5_itp_geometry_status_PARAMATER.CommandSize = 12
    target5_itp_geometry_status_PARAMATER.WidgetIdent = 104
    target5_itp_geometry_status_PARAMATER.UnusedPad = 0
    target5_itp_geometry_status_PARAMATER.ParameterIdent = int('B490', 16)
    target5_itp_geometry_status_PARAMATER.ParameterValueBuffer = target5_itp_geometry_status


    ua_to_cdti_data.Compass_Bitmap_SET_PARAMATER = compass_Bitmap_SET_PARAMATER
    ua_to_cdti_data.Compass_Step_SET_PARAMATER = compass_Step_SET_PARAMATER
    ua_to_cdti_data.Ownship_TOA_TIME_PARAMATER = ownship_Toa_TIME_PARAMATER
    ua_to_cdti_data.Ownship_FlightId_SET_PARAMATER = ownship_FlightId_SET_PARAMATER
    ua_to_cdti_data.Ownship_Alt_SET_PARAMATER = ownship_Alt_SET_PARAMATER
    ua_to_cdti_data.Ownship_Lon_SET_PARAMATER = ownship_Lon_SET_PARAMATER
    ua_to_cdti_data.Ownship_Lat_SET_PARAMATER = ownship_Lat_SET_PARAMATER
    ua_to_cdti_data.Ownship_Alt_Range_PARAMATER = ownship_Alt_Range_PARAMATER
    ua_to_cdti_data.Ownship_Course_Angle_PARAMATER = ownship_Course_Angle_PARAMATER
    ua_to_cdti_data.Ownship_App_Status_PARAMATER = ownship_App_Status_PARAMATER

    target1_info = TARGET_INFO()
    target2_info = TARGET_INFO()
    target3_info = TARGET_INFO()
    target4_info = TARGET_INFO()
    target5_info = TARGET_INFO()
    Array_Target = TARGET_INFO*5
    array_target_infos = Array_Target()
    target1_info.Target_Visible_PARAMATER = target1_Visible_PARAMATER
    target1_info.Target_Pic_PARAMATER = target1_Pic_PARAMATER
    target1_info.Target_RotateAngle_PARAMATER = target1_RotateAngle_PARAMATER
    target1_info.Target_X_PARAMATER = target1_X_PARAMATER
    target1_info.Target_Y_PARAMATER = target1_Y_PARAMATER
    target1_info.Target_FlightId_PARAMATER = target1_FlightId_PARAMATER
    target1_info.Target_Speed_PARAMATER = target1_Speed_PARAMATER
    target1_info.Target_Alt_dif_PARAMATER = target1_Alt_dif_PARAMATER
    target1_info.Target_Status_PARAMATER = target1_Status_PARAMATER
    target1_info.Target_AppStatus_PARAMATER = target1_AppStatus_PARAMATER
    target1_info.Target_Lon_SET_PARAMATER = target1_lon_PARAMATER
    target1_info.Target_Lat_SET_PARAMATER = target1_lat_PARAMATER
    target1_info.Target_VSA_DIS_PARAMATER = target1_vsa_horizontal_distance_PARAMATER
    target1_info.Target_VSA_Velocity_PARAMATER = target1_vsa_velocity_PARAMATER
    target1_info.Target_ITP_DIS_PARAMATER= target1_itp_distance_PARAMATER
    target1_info.Target_ITP_DIS_RATE_PARAMATER = target1_itp_distance_rate_PARAMATER
    target1_info.Target_ITP_FORWARD_PARAMATER = target1_itp_forward_PARAMATER
    target1_info.Target_ITP_Geometry_Status_PARAMATER = target1_itp_geometry_status_PARAMATER

    target2_info.Target_Visible_PARAMATER = target2_Visible_PARAMATER
    target2_info.Target_Pic_PARAMATER = target2_Pic_PARAMATER
    target2_info.Target_RotateAngle_PARAMATER = target2_RotateAngle_PARAMATER
    target2_info.Target_X_PARAMATER = target2_X_PARAMATER
    target2_info.Target_Y_PARAMATER = target2_Y_PARAMATER
    target2_info.Target_FlightId_PARAMATER = target2_FlightId_PARAMATER
    target2_info.Target_Speed_PARAMATER = target2_Speed_PARAMATER
    target2_info.Target_Alt_dif_PARAMATER = target2_Alt_dif_PARAMATER
    target2_info.Target_Status_PARAMATER = target2_Status_PARAMATER
    target2_info.Target_AppStatus_PARAMATER = target2_AppStatus_PARAMATER
    target2_info.Target_Lon_SET_PARAMATER = target2_lon_PARAMATER
    target2_info.Target_Lat_SET_PARAMATER = target2_lat_PARAMATER
    target2_info.Target_VSA_DIS_PARAMATER = target2_vsa_horizontal_distance_PARAMATER
    target2_info.Target_VSA_Velocity_PARAMATER = target2_vsa_velocity_PARAMATER
    target2_info.Target_ITP_DIS_PARAMATER= target2_itp_distance_PARAMATER
    target2_info.Target_ITP_DIS_RATE_PARAMATER = target2_itp_distance_rate_PARAMATER
    target2_info.Target_ITP_FORWARD_PARAMATER = target2_itp_forward_PARAMATER
    target2_info.Target_ITP_Geometry_Status_PARAMATER = target2_itp_geometry_status_PARAMATER

    target3_info.Target_Visible_PARAMATER = target3_Visible_PARAMATER
    target3_info.Target_Pic_PARAMATER = target3_Pic_PARAMATER
    target3_info.Target_RotateAngle_PARAMATER = target3_RotateAngle_PARAMATER
    target3_info.Target_X_PARAMATER = target3_X_PARAMATER
    target3_info.Target_Y_PARAMATER = target3_Y_PARAMATER
    target3_info.Target_FlightId_PARAMATER = target3_FlightId_PARAMATER
    target3_info.Target_Speed_PARAMATER = target3_Speed_PARAMATER
    target3_info.Target_Alt_dif_PARAMATER = target3_Alt_dif_PARAMATER
    target3_info.Target_Status_PARAMATER = target3_Status_PARAMATER
    target3_info.Target_AppStatus_PARAMATER = target3_AppStatus_PARAMATER
    target3_info.Target_Lon_SET_PARAMATER = target3_lon_PARAMATER
    target3_info.Target_Lat_SET_PARAMATER = target3_lat_PARAMATER
    target3_info.Target_VSA_DIS_PARAMATER = target3_vsa_horizontal_distance_PARAMATER
    target3_info.Target_VSA_Velocity_PARAMATER = target3_vsa_velocity_PARAMATER
    target3_info.Target_ITP_DIS_PARAMATER= target3_itp_distance_PARAMATER
    target3_info.Target_ITP_DIS_RATE_PARAMATER = target3_itp_distance_rate_PARAMATER
    target3_info.Target_ITP_FORWARD_PARAMATER = target3_itp_forward_PARAMATER
    target3_info.Target_ITP_Geometry_Status_PARAMATER = target3_itp_geometry_status_PARAMATER

    target4_info.Target_Visible_PARAMATER = target4_Visible_PARAMATER
    target4_info.Target_Pic_PARAMATER = target4_Pic_PARAMATER
    target4_info.Target_RotateAngle_PARAMATER = target4_RotateAngle_PARAMATER
    target4_info.Target_X_PARAMATER = target4_X_PARAMATER
    target4_info.Target_Y_PARAMATER = target4_Y_PARAMATER
    target4_info.Target_FlightId_PARAMATER = target4_FlightId_PARAMATER
    target4_info.Target_Speed_PARAMATER = target4_Speed_PARAMATER
    target4_info.Target_Alt_dif_PARAMATER = target4_Alt_dif_PARAMATER
    target4_info.Target_Status_PARAMATER = target4_Status_PARAMATER
    target4_info.Target_AppStatus_PARAMATER = target4_AppStatus_PARAMATER
    target4_info.Target_Lon_SET_PARAMATER = target4_lon_PARAMATER
    target4_info.Target_Lat_SET_PARAMATER = target4_lat_PARAMATER
    target4_info.Target_VSA_DIS_PARAMATER = target4_vsa_horizontal_distance_PARAMATER
    target4_info.Target_VSA_Velocity_PARAMATER = target4_vsa_velocity_PARAMATER
    target4_info.Target_ITP_DIS_PARAMATER= target4_itp_distance_PARAMATER
    target4_info.Target_ITP_DIS_RATE_PARAMATER = target4_itp_distance_rate_PARAMATER
    target4_info.Target_ITP_FORWARD_PARAMATER = target4_itp_forward_PARAMATER
    target4_info.Target_ITP_Geometry_Status_PARAMATER = target4_itp_geometry_status_PARAMATER

    target5_info.Target_Visible_PARAMATER = target5_Visible_PARAMATER
    target5_info.Target_Pic_PARAMATER = target5_Pic_PARAMATER
    target5_info.Target_RotateAngle_PARAMATER = target5_RotateAngle_PARAMATER
    target5_info.Target_X_PARAMATER = target5_X_PARAMATER
    target5_info.Target_Y_PARAMATER = target5_Y_PARAMATER
    target5_info.Target_FlightId_PARAMATER = target5_FlightId_PARAMATER
    target5_info.Target_Speed_PARAMATER = target5_Speed_PARAMATER
    target5_info.Target_Alt_dif_PARAMATER = target5_Alt_dif_PARAMATER
    target5_info.Target_Status_PARAMATER = target5_Status_PARAMATER
    target5_info.Target_AppStatus_PARAMATER = target5_AppStatus_PARAMATER
    target5_info.Target_Lon_SET_PARAMATER = target5_lon_PARAMATER
    target5_info.Target_Lat_SET_PARAMATER = target5_lat_PARAMATER
    target5_info.Target_VSA_DIS_PARAMATER = target5_vsa_horizontal_distance_PARAMATER
    target5_info.Target_VSA_Velocity_PARAMATER = target5_vsa_velocity_PARAMATER
    target5_info.Target_ITP_DIS_PARAMATER= target5_itp_distance_PARAMATER
    target5_info.Target_ITP_DIS_RATE_PARAMATER = target5_itp_distance_rate_PARAMATER
    target5_info.Target_ITP_FORWARD_PARAMATER = target5_itp_forward_PARAMATER
    target5_info.Target_ITP_Geometry_Status_PARAMATER = target5_itp_geometry_status_PARAMATER
    array_target_infos[0] = target1_info
    array_target_infos[1] = target2_info
    array_target_infos[2] = target3_info
    array_target_infos[3] = target4_info
    array_target_infos[4] = target5_info
    ua_to_cdti_data.Target_Lists = array_target_infos
    ua_to_cdti_data.A661_END_BLOCK = int('D0',16)
    ua_to_cdti_data.Unused1 = '000'.encode()


if __name__ == '__main__':
   # work_a = MyThread()
   # work_a.start()
    pack()
    buf = ua_to_cdti_data.encode()
    print("待发送的字节:" + str(ua_to_cdti_data.encode()))
    IP_PORT = ('127.0.0.1', 8006)
    socket_661 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    socket_661.sendto(buf, IP_PORT)