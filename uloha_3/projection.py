from math import *

def lambert(R, s, d, s0, rho0):
    c = sin(s0)
    rho = rho0 * ((tan(s0/2 + pi/4))**c / (tan(s/2 + pi/4))**c)
    eps = c * d
    return rho * sin(eps), rho0 - rho * cos(eps)

def mercator(R, s, d, s0, rho0):
    x = R * d
    y = R * log(tan(s/2 + pi/4))
    return x, y

def stereographic(R, s, d, s0, rho0):
    rho = 2 * R * tan(pi/4 - s/2)
    return rho * sin(d), -rho * cos(d)