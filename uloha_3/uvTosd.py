from math import *

def uv_sd(u, v, uk, vk):
    s = asin(sin(u) * sin(uk) + cos(u) * cos(uk) * cos(v - vk))
    d = atan2(cos(u) * sin(v - vk), sin(u) * cos(uk) - cos(u) * sin(uk) * cos(v - vk))
    return s, d