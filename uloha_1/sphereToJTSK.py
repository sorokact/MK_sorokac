from math import *
from uvtosd import*

def sphereToJTSK(u, v):
    #Shift to Feerro
    v = v + (17 + (2/3))*pi/180;
    
    #Cartographic pole
    uk = (59+(42/60)+(42.6969/3600))*(pi/180)
    vk = (42+(31/60)+(31.41725/3600))*(pi/180)
    
    #Conversion (u, v) -> (s, d)
    s, d = uvTosd(u, v, uk, vk)
    
    #LCC
    R = 6380703.6105
    s0 = 78.5 * pi/180
    c = sin(s0)
    rho0 = 0.9999 * R * 1/tan(s0)

    #Coordinates in LCC
    rho_n = (tan(s0/2 + pi/4))**c
    rho_d = (tan(s/2 + pi/4))**c
    rho = rho0 * rho_n / rho_d
    eps = c * d
    
    # (rho, eps) -> (y, x)
    y_jtsk = rho*sin(eps)
    x_jtsk = rho*cos(eps)
    
    #linear distortion
    m_scale = (c * rho) / (R * cos(s))
    dist = m_scale - 1
    
    #Meridian convergence
    ksi = asin(cos(uk) * sin(pi - d) / cos(u))
    c1 = eps - ksi
    
    return x_jtsk, y_jtsk, dist, c1

# Input points
u1 = 49.8344456
v1 = 14.8306903
u2 = 49.8709389
v2 = 14.8963158

# Convert to radians
u1_rad = u1 * pi / 180
v1_rad = v1 * pi / 180
u2_rad = u2 * pi / 180
v2_rad = v2 * pi / 180

#Calculate JTSK coordinates
y1_jtsk, x1_jtsk, dist1, c1 = sphereToJTSK(u1_rad, v1_rad) 
y2_jtsk, x2_jtsk, dist2, c2 = sphereToJTSK(u2_rad, v2_rad)

print(f"Bod 1: Y_JTSK = {y1_jtsk:.3f} m, X_JTSK = {x1_jtsk:.3f} m")
print(f"linear distortion = {dist1:.8f}")
print(f"meridian convergence = {c1:.8f} rad")

print(f"\nBod 2: Y_JTSK = {y2_jtsk:.3f} m, X_JTSK = {x2_jtsk:.3f} m")
print(f"linear distortion = {dist2:.8f}")
print(f"meridian convergence = {c2:.8f} rad")

#Distance between input points
d_sphere = sqrt((x2_jtsk - x1_jtsk)**2 + (y2_jtsk - y1_jtsk)**2)
print(f"distance: {d_sphere:.4f} m")