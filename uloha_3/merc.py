from math import *

#Optimal Mercator projection

#Poin ts on the quator
u1 = 28.739286806*pi/180
v1 = 82.872763919*pi/180
u2 = 27.864137915*pi/180
v2 = 85.383052540*pi/180

#Northernmost point
u3 = 30.206883143*pi/180
v3 = 82.568450663*pi/180

#Southernmost point
u4 = 26.961881964*pi/180
v4 = 84.244878001*pi/180
 
#Pole
vk = atan2(tan(u1)*cos(v2)-tan(u2)*cos(v1), tan(u2)*sin(v1)-tan(u1)*sin(v2))
uk = atan(-1/tan(u2)*cos(vk-v2))

#Transformation to the oblique aspect
s1 = asin(sin(u1) * sin(uk) + cos(u1) * cos(uk) * cos(vk-v1))
s2 = asin(sin(u2) * sin(uk) + cos(u2) * cos(uk) * cos(vk-v2))
s3 = asin(sin(u3) * sin(uk) + cos(u3) * cos(uk) * cos(vk-v3))
s4 = asin(sin(u4) * sin(uk) + cos(u4) * cos(uk) * cos(vk-v4))

#True parallel
s0 = acos (2*cos(s3)/(1+cos(s3)))

#Scales
m1 = cos(s0)/cos(s1)
m2 = cos(s0)/cos(s2)
m3 = cos(s0)/cos(s3)
m4 = cos(s0)/cos(s4)

#Distortions
ny1 = (m1 -1) *1000
ny2 = (m2 -1) *1000
ny3 = (m3 -1) *1000
ny4 = (m4 -1) *1000

print(ny1, ny2, ny3, ny4)
