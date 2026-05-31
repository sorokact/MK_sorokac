from math import *
import matplotlib.pyplot as plot
from projection import *
from uvTosd import uv_sd
from graticule import graticule

proj = lambert

R = 1

#Pole
uk = -17.451351 * pi/180
vk = 15.163149 * pi/180

#Northernmost point
u1 = -19.762483 * pi/180
v1 = 33.05273 * pi/180

#Southernmost point
u2 = -17.856686 * pi/180
v2 = 25.236593 * pi/180

#Transformation to the oblique aspect
s1 = asin(sin(u1) * sin(uk) + cos(u1) * cos(uk) * cos(vk-v1))
s2 = asin(sin(u2) * sin(uk) + cos(u2) * cos(uk) * cos(vk-v2))

#Constant c of the conic projection
cn = log10(cos(s1)) - log10(cos(s2))
cd = log10(tan(s2/2+pi/4))-log10(tan(s1/2+pi/4))
c = cn / cd

#Compute s0
s0 = asin(c)

#Compute rho0: radius of the parallel (u = u0)
rho0_n = 2*R*cos(s0)*cos(s1)*(tan(s1/2+pi/4))**c
rho0_d = c*(cos(s0)*(tan(s0/2+pi/4))**c+cos(s1)*(tan(s1/2+pi/4))**c)
rho0 = rho0_n/rho0_d

#Compute rho1: radius of the north parallel (u = u1)
rho1 = rho0*((tan(s0/2+pi/4))/(tan(s1/2+pi/4)))**c

#Compute rho2: radius of the south parallel (u = u2)
rho2 = rho0*((tan(s0/2+pi/4))/(tan(s2/2+pi/4)))**c

#Scales
m1 = (c * rho1)/(R * cos(s1))
m2 = (c * rho2)/(R * cos(s2))
m0 = (c * rho0)/(R * cos(s0))

#Distortions
ny1 = (m1 -1) * 1000
ny2 = (m2 -1) * 1000
ny0 = (m0 - 1) * 1000

print(ny1, ny2, ny0)

#Graph settings
plot.figure(figsize=(8, 8))
plot.gca().set_aspect('equal', adjustable='box')

#Open file with borders of the country (AI 63 - 81 with own)
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
        x, y = lambert(R, s, d, s0, rho0)
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
du = 0.1* pi/180
dv = 0.1* pi/180

#Compute and draw graticule points
XM, YM, XP, YP = graticule(umin, umax, vmin, vmax, Du, Dv, du, dv, R, uk, vk, s0, rho0, proj)

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
        xg, yg = lambert(R, sg, dg, s0, rho0)
        
        #distortions
        rho = rho0 * ((tan(s0/2 + pi/4) / tan(sg/2 + pi/4))**c)
        m = c * rho / (R * cos(sg))
        mju_km = (m - 1) * 1000
        
        row_x.append(xg)
        row_y.append(yg)
        row_mju.append(mju_km)
        
    XG.append(row_x)
    YG.append(row_y)
    MJU_KM.append(row_mju)

#Draw contours of distortion
plot.contour(XG, YG, MJU_KM, levels=30, colors='r', linewidths=0.5)
cp = plot.contour(XG, YG, MJU_KM, levels=10, colors='r', linewidths=1.8)

input_points = [(u1, v1), (u2, v2)]
for u_p, v_p in input_points:
    s_p, d_p = uv_sd(u_p, v_p, uk, vk)
    xp, yp = proj(R, s_p, d_p, s0, rho0)
    plot.plot(xp, yp, 'r.', markersize=8, markeredgewidth=1.5)
    
#Set limits for better visualization
plot.xlim(min(xn_list) - 0.02, max(xn_list) + 0.02)
plot.ylim(min(yn_list) - 0.02, max(yn_list) + 0.02)

plot.show()