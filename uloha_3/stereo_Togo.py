from math import *
import matplotlib.pyplot as plot
from projection import *
from uvTosd import uv_sd
from graticule import graticule

proj = stereographic

R = 1

#Pole
uk = 8.681021 * pi/180
vk = 0.764245 * pi/180

#Southern-most point
u2 = 6.094000 * pi/180
v2 = 1.198633 * pi/180

# Transformation to the oblique aspect
s2 = asin(sin(u2) * sin(uk) + cos(u2) * cos(uk) * cos(vk-v2))

#Constant c of the stereographic projection
psi2 = pi/2 - s2
c = (2 * cos(psi2/2)**2) / (1 + cos(psi2/2)**2)

#Compute s0
psi0 = 2 * acos(sqrt(c))
s0 = pi/2 - psi0

#Scales
m2 = c / (cos(psi2/2)**2)
m0 = c / (cos(psi0/2)**2)

#Distortions
ny2 = (m2 - 1) * 1000
ny0 = (m0 - 1) * 1000

print(ny2, ny0)

#Graph settings
plot.figure(figsize=(8, 8))
plot.gca().set_aspect('equal', adjustable='box')

#Open file with borders of the country (AI 45 - 64 with own)
file_path = r"uloha_3\data\Togo.txt"

xn_list = []
yn_list = []

f = open(file_path, "r")
for row in f:
    data = row.split()
    if len(data) >= 2:
        u = float(data[0]) * pi / 180
        v = float(data[1]) * pi / 180
        
        s, d = uv_sd(u, v, uk, vk)
        x, y = stereographic(R, s, d, s0, 0)
        
        xn_list.append(x)
        yn_list.append(y)
f.close()

plot.plot(xn_list, yn_list, 'b', linewidth=2)

#Graticule
umin = 0 * pi/180
umax = 20 * pi/180
vmin = -5 * pi/180
vmax = 15 * pi/180
Du = 1 * pi/180
Dv = 1 * pi/180
du = 0.1* pi/180
dv = 0.1* pi/180

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
        xg, yg = stereographic(R, sg, dg, s0, 0)
        
        #distortions
        psig = pi/2 - sg
        psi0_g = pi/2 - s0
        
        m = (cos(psi0_g/2)**2) / (cos(psig/2)**2)
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

input_points = [(u2, v2)]
for u_p, v_p in input_points:
    s_p, d_p = uv_sd(u_p, v_p, uk, vk)
    xp, yp = stereographic(R, s_p, d_p, s0, 0)
    plot.plot(xp, yp, 'rx', markersize=8, markeredgewidth=1.5)
    
#Set limits for better visualization
plot.xlim(min(xn_list) - 0.1, max(xn_list) + 0.1)
plot.ylim(min(yn_list) - 0.1, max(yn_list) + 0.1)

plot.show()