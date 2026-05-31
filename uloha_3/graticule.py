from math import *
from uvTosd import uv_sd

def graticule(umin, umax, vmin, vmax, Du, Dv, du, dv, R, uk, vk, s0, rho0, proj):
    #Create list of meridians
    XM, YM = [], []
    
    v = vmin
    while v <= vmax:
        #Create meridian points
        xm_line, ym_line = [], []
        u = umin
        while u <= umax:
            #Convert to oblique aspect
            s, d = uv_sd(u, v, uk, vk)
            
            #Compute xm, ym using the passed projection function
            xm, ym = proj(R, s, d, s0, rho0)
            
            xm_line.append(xm)
            ym_line.append(ym)
            u += du
        
        #record the meridian    
        XM.append(xm_line)
        YM.append(ym_line)
        v += Dv

    #Create list of parallels
    XP, YP = [], []
    
    u = umin
    while u <= umax:
        # Create parallel points
        xp_line, yp_line = [], []
        v = vmin
        while v <= vmax:
            #Convert to oblique aspect
            s, d = uv_sd(u, v, uk, vk)
            
            #Compute xp, yp using the passed projection function
            xp, yp = proj(R, s, d, s0, rho0)
            
            xp_line.append(xp)
            yp_line.append(yp)
            v += dv
            
        #record the parallel    
        XP.append(xp_line)
        YP.append(yp_line)
        u += Du

    return XM, YM, XP, YP