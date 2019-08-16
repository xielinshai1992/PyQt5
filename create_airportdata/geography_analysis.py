#-*- coding: utf-8 -*-
from math import *
class Geography_Analysis():

    R_earth = 6371            #地球平均半径 单位km
    Long_R_earth = 6378.137   #长半径 单位km
    Short_R_earth = 6356.752  #短半径 单位km
    f = 1/298.2572236         #扁率

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
        c = 2* asin(sqrt(a))* self.R_earth # 地球平均半径，6371km
        distance = round(c , 3)
        return distance

    def get_lngAndlat(self,lng1,lat1,angle,distance):
        '''
        根据一点的经纬度、方位角、距离计算另一点的经纬度
        :param lng1:经度
        :param lat1:纬度
        :param angle:方位角  #deg
        :param distance:距离
        :return:
        '''
        alpha1 = self.degTorad(angle);
        sinAlpha1 = sin(alpha1);
        cosAlpha1 = cos(alpha1);
        tanU1 = (1 - self.f) * tan(self.degTorad(lat1));
        cosU1 = 1 / sqrt((1 + tanU1 * tanU1));
        sinU1 = tanU1 * cosU1;
        sigma1 = atan2(tanU1, cosAlpha1);
        sinAlpha = cosU1 * sinAlpha1;
        cosSqAlpha = 1 - sinAlpha * sinAlpha;
        uSq = cosSqAlpha * (self.Long_R_earth * self.Long_R_earth - self.Short_R_earth * self.Short_R_earth) / (self.Short_R_earth * self.Short_R_earth);
        A = 1 + uSq / 16384 * (4096 + uSq * (-768 + uSq * (320 - 175 * uSq)));
        B = uSq / 1024 * (256 + uSq * (-128 + uSq * (74 - 47 * uSq)));
        cos2SigmaM = 0;
        sinSigma = 0;
        cosSigma = 0;
        sigma =  distance / (self.Short_R_earth * A)
        sigmaP = 2 * pi;
        while abs(sigma - sigmaP) > 1e-12:
            cos2SigmaM = cos(2 * sigma1 + sigma);
            sinSigma = sin(sigma);
            cosSigma = cos(sigma);
            deltaSigma = B * sinSigma * (cos2SigmaM + B / 4 * (cosSigma * (-1 + 2 * cos2SigmaM * cos2SigmaM)- B / 6 * cos2SigmaM * (-3 + 4 * sinSigma * sinSigma) * (-3 + 4 * cos2SigmaM * cos2SigmaM)));
            sigmaP = sigma;
            sigma = distance / (self.Short_R_earth * A) + deltaSigma;

        tmp = sinU1 * sinSigma - cosU1 * cosSigma * cosAlpha1;

        lat2 = atan2(sinU1 * cosSigma + cosU1 * sinSigma * cosAlpha1,(1 - self.f) * sqrt(sinAlpha * sinAlpha + tmp * tmp));

        x = atan2(sinSigma * sinAlpha1, cosU1 *cosSigma - sinU1 * sinSigma * cosAlpha1);

        C = self.f / 16 * cosSqAlpha * (4 + self.f * (4 - 3 * cosSqAlpha));

        L = x - (1 - C) * self.f * sinAlpha * (sigma + C * sinSigma * (cos2SigmaM + C * cosSigma * (-1 + 2 * cos2SigmaM * cos2SigmaM)));

        revAz = atan2(sinAlpha, -tmp) #final bearing
        return round(lng1+self.radTodeg(L),5) , round(self.radTodeg(lat2),5)

    def degTorad(self, deg):
        '''
        角度转弧度
        :param deg:
        :return:
        '''
        return deg * pi /180.0

    def radTodeg(self, x):
        '''
        弧度换角度
        :return:
        '''
        return  x * 180 / pi

# ga = Geography_Analysis()
# print(ga.get_lngAndlat(106.063333, 31.358, 29, 123.954))