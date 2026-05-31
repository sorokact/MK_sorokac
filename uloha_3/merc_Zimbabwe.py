from math import *
import matplotlib.pyplot as plot
from uvTosd import uv_sd
from graticule import graticule
from projection import mercator

proj = mercator

R = 1

#Points on the equator
u1 = -20.462362 * pi/180
v1 = 29.202199 * pi/180

u2 = -19.830599 * pi/180
v2 = 33.143508 * pi/180

#Northernmost point
u3 = -17.868284 * pi/180
v3 = 25.216847 * pi/180

#Southernmost point
u4 = -16.865006 * pi/180
v4 = 29.176271 * pi/180

#Pole
vk = atan2(tan(u1)*cos(v2)-tan(u2)*cos(v1), tan(u2)*sin(v1)-tan(u1)*sin(v2))
uk = atan(-1/tan(u2)*cos(vk-v2))

#Transformation to the oblique aspect
s1 = asin(sin(u1) * sin(uk) + cos(u1) * cos(uk) * cos(vk-v1))
s2 = asin(sin(u2) * sin(uk) + cos(u2) * cos(uk) * cos(vk-v2))
s3 = asin(sin(u3) * sin(uk) + cos(u3) * cos(uk) * cos(vk-v3))
s4 = asin(sin(u4) * sin(uk) + cos(u4) * cos(uk) * cos(vk-v4))

#True parallel
s0 = acos(2*cos(s3)/(1+cos(s3)))

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

#Graph settings
plot.figure(figsize=(10, 6))
plot.gca().set_aspect('equal', adjustable='box')

#Open file with borders of the country (AI 58 - 77 with own)
file_path = r"uloha_3\data\Zimbabwe.txt"

xn_list = []
yn_list = []

f = open(file_path, "r")
for row in f:
    data = row.split()
    if len(data) >= 2:
        u = float(data[0]) * pi / 180
        v = float(data[1]) * pi / 180
        
        s, d = uv_sd(u, v, uk, vk)
        x, y = mercator(R, s, d, s0, 0)
        
        xn_list.append(x)
        yn_list.append(y)
f.close()

plot.plot(xn_list, yn_list, 'b', linewidth=2)


#Graticule
umin = -30 * pi/180
umax = -10 * pi/180
vmin = 20 * pi/180
vmax = 40 * pi/180
Du = 1 * pi/180
Dv = 1 * pi/180
du = 0.1 * pi/180
dv = 0.1 * pi/180

#Compute and draw graticule points
XM, YM, XP, YP = graticule(umin, umax, vmin, vmax, Du, Dv, du, dv, R, uk, vk, s0, 0, proj)

for i in range(len(XM)): plot.plot(XM[i], YM[i], 'k', alpha=0.3)
for i in range(len(XP)): plot.plot(XP[i], YP[i], 'k', alpha=0.3)


#Create grid
XG, YG, MJU_KM = [], [], []

#Steps for grid points
u_step = [umin + i * du for i in range(int((umax - umin) / du) + 1)]
v_step = [vmin + i * dv for i in range(int((vmax - vmin) / dv) + 1)]

#for cycle to compute grid points and distortions
for v_g in v_step:
    row_x, row_y, row_mju = [], [], []
    for u_g in u_step:
        sg, dg = uv_sd(u_g, v_g, uk, vk)
        xg, yg = proj(R, sg, dg, s0, 0)
        
        #distortions
        m = cos(s0) / cos(sg)
        mju_km = (m - 1) * 1000
        
        row_x.append(xg)
        row_y.append(yg)
        row_mju.append(mju_km)
        
    XG.append(row_x)
    YG.append(row_y)
    MJU_KM.append(row_mju)

#Draw contours of distortion
plot.contour(XG, YG, MJU_KM, levels=30, colors='r', linewidths=0.5)
cp = plot.contour(XG, YG, MJU_KM, levels=[0], colors='r', linewidths=1.8)

input_points = [(u1, v1), (u2, v2), (u3, v3), (u4, v4)]
for u_p, v_p in input_points:
    s_p, d_p = uv_sd(u_p, v_p, uk, vk)
    xp, yp = proj(R, s_p, d_p, s0, 0)
    plot.plot(xp, yp, 'r.', markersize=8, markeredgewidth=1.5)

#Set limits for better visualization
plot.xlim(min(xn_list) - 0.02, max(xn_list) + 0.02)
plot.ylim(min(yn_list) - 0.02, max(yn_list) + 0.02)

plot.show()