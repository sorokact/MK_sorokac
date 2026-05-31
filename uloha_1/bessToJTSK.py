from math import *
from uvtosd import*

def BesselToJTSK(phi_Bes, la_Bes):
    
    #Bessel parameters
    a_Bes = 6377397.155
    b_Bes = 6356078.963
    e2_Bes = (a_Bes*a_Bes - b_Bes*b_Bes)/(a_Bes*a_Bes)
    
    #Shift to Feerro
    la_Ferro = la_Bes + (17 + 2/3) * pi / 180
    
    #Gauss conformal projection, parameters
    phi0 = 49.5 * pi / 180
    alpha = sqrt (1 + e2_Bes * (cos(phi0))**4 / (1 - e2_Bes))
    u0 = asin(sin(phi0)/alpha)
    
    kn = (tan(phi0/2+pi/4)**alpha*((1-sqrt(e2_Bes)*sin(phi0))/(1+sqrt(e2_Bes)*sin(phi0)))**(alpha*sqrt(e2_Bes)/2))
    kd = tan(u0/2+pi/4)
    k = kn / kd
    
    R = (a_Bes*sqrt(1-e2_Bes))/(1-e2_Bes*(sin(phi0)**2))
    
    #Gauss conformal projection
    u = 2 * atan(1/k * (tan(phi_Bes/2 + pi/4) * ((1 - sqrt(e2_Bes)*sin(phi_Bes)) / (1 + sqrt(e2_Bes)*sin(phi_Bes)))**(sqrt(e2_Bes)/2))**alpha) - pi/2
    v = alpha * la_Ferro
    
    #Cartographic pole
    uk = (59+(42/60)+(42.6969/3600))*(pi/180)
    vk = (42+(31/60)+(31.41725/3600))*(pi/180)
    
    #Conversion (u, v) -> (s, d)
    s, d = uvTosd(u, v, uk, vk)
    
    #LCC
    s0 = 78.5 * pi/180
    rho0 = R*1/tan(s0)*0.9999
    c = sin(s0)
    
    rho = rho0*((tan(s0/2+pi/4))/(tan(s/2+pi/4)))**c
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
    
    return y_jtsk, x_jtsk, dist, c1

#Input coordinates
phi1_bes = 49.8344456
la1_bes = 14.8306903
phi2_bes = 49.8709389
la2_bes = 14.8963158

#Convert to radians
phi1_bes_rad = phi1_bes * pi / 180
la1_bes_rad = la1_bes * pi / 180
phi2_bes_rad = phi2_bes * pi / 180
la2_bes_rad = la2_bes * pi / 180

#Calculate JTSK coordinates
y1_jtsk, x1_jtsk, dist1, c1 = BesselToJTSK(phi1_bes_rad, la1_bes_rad)
y2_jtsk, x2_jtsk, dist2, c2 = BesselToJTSK(phi2_bes_rad, la2_bes_rad)

print(f"Bod 1: Y_JTSK = {y1_jtsk:.3f} m, X_JTSK = {x1_jtsk:.3f} m")
print(f"linear distortion = {dist1:.8f}")
print(f"meridian convergence = {c1:.8f} rad")

print(f"\nBod 2: Y_JTSK = {y2_jtsk:.3f} m, X_JTSK = {x2_jtsk:.3f} m")
print(f"linear distortion = {dist2:.8f}")
print(f"meridian convergence = {c2:.8f} rad")

#Distance between input points
d_bessel = sqrt((x2_jtsk - x1_jtsk)**2 + (y2_jtsk - y1_jtsk)**2)
print(f"distance: {d_bessel:.4f} m")