from numpy import *
from pyproj import *
from matplotlib.pyplot import *

def project(proj_name, R_z, lat, lon, lat0, lon0):
    # Create new projection given by proj_name (Added lon_0 to center the map)
    my_proj =  Proj(proj=proj_name, R=R_z, lat_1 = lat0, lon_0 = lon0)

    # Project point calculation
    [X,Y] = my_proj(lon, lat)

    #Distortions
    dist = my_proj.get_factors(lon, lat)
    a = dist.tissot_semimajor
    b = dist.tissot_semiminor

    return X, Y, a, b 

def graticule(lat_min, lon_min, lat_max, lon_max, Dlat, Dlon, dlat, dlon, R, lat0, lon0, proj_name):
    #Create graticule of the given map projection
    #Create meridians
    lat_mer = arange(lat_min, lat_max + dlat/2, dlat)
    lon_mer = arange(lon_min, lon_max + Dlon/2, Dlon)
    
    #Create parallels
    lat_par = arange(lat_min, lat_max + Dlat/2, Dlat)
    lon_par = arange(lon_min, lon_max + dlon/2, dlon)

    #Create meshgrid
    lat_merg, lon_merg = meshgrid(lat_mer, lon_mer)
    lon_parg, lat_parg = meshgrid(lon_par, lat_par)
    
    #Project meridians (Added lon0 parameter)
    mer_proj = project(proj_name, R, lat_merg, lon_merg, lat0, lon0)

    #Project parallels (Added lon0 parameter)
    par_proj = project(proj_name, R, lat_parg, lon_parg, lat0, lon0)
    
    return mer_proj, par_proj   

#Define projection
proj_name = "sinu"
#proj_name = "bonne"
#proj_name = "eck5"
#proj_name = "wintri"
#proj_name = "aitoff"

R = 6380000
lat0 = 70.0
lon0 = -20.0

#Define projection grid
lat_min = 50
lat_max = 85
lon_min = -80
lon_max = 40
Dlat = 5
Dlon = 10
dlat = 0.1 * Dlat
dlon = 0.1 * Dlon
nlat = 100
nlon = 100

#Create intervals
lat = linspace(lat_min, lat_max, nlat)
lon = linspace(lon_min, lon_max, nlon)

#Create  meshgrid
latg, long = meshgrid(lat, lon)

#Project meshgrid
X, Y, a, b = project(proj_name, R, latg, long, lat0, lon0)

#Airy local
h2_a = 0.5*((a-1)**2+(b-1)**2)

#Complex local
h2_c = 0.5*(abs(a-1)+abs(b-1)) + a/b - 1

#Airy global
H2_a = mean(h2_a)

#Complex global
H2_c = mean(h2_c)

#Airy weighted global
w = cos(latg * pi /180)
H2_aw = sum(w*h2_a)/sum(w)

#Complex weighted global
H2_cw = sum(w*h2_c)/sum(w) 

print(H2_aw, H2_cw)

#Percentage of area with angular distortion < 50%
#Angular distortion in radians
omega = 2 * arcsin(abs(a - b) / (a + b))
#Convert to degrees
omega_deg = omega * 180 / pi
#Count points with angular distortion < 50 degrees
points_low_angle_distortion = sum(omega_deg < 50)
total_points = latg.size
pct_angle_ok = (points_low_angle_distortion / total_points) * 100

#Percentage of area with scale variation M < 50%
points_low_scale_distortion = sum((a >= 0.5) & (a <= 1.5))
pct_scale_ok = (points_low_scale_distortion / total_points) * 100

print(f"Angular distortion < 50%: {pct_angle_ok:.2f}%")
print(f"Scale variation < 50%: {pct_scale_ok:.2f}%")

#Set window size
figure(figsize=(15, 10))
    
#Draw continents
continent_files = ["data/denmark.txt", "data/denmark2.txt", "data/greenland.txt", "data/norway.txt", "data/sweden.txt", "data/finland.txt"]

for file_name in continent_files:
    continents = loadtxt(file_name)

    #Extract coordinates
    latc = continents[:, 0]
    lonc = continents[:, 1]

    #Project points (Added lon0 parameter)
    Xc, Yc, ac, bc = project(proj_name, R, latc, lonc, lat0, lon0)

    #Draw points
    plot(Xc, Yc, linewidth = 0.5, color = 'green')

#Create meridians and parallels
mer_proj, par_proj = graticule(lat_min, lon_min, lat_max, lon_max, Dlat, Dlon, dlat, dlon, R, lat0, lon0, proj_name)

#Extract coordinates
Xm = mer_proj[0]
Ym = mer_proj[1]

Xp = par_proj[0]
Yp = par_proj[1]

#PLot meridians and parallels
plot(transpose(Xm), transpose(Ym), color = 'black', linewidth = 0.5)
plot(transpose(Xp), transpose(Yp), color = 'black', linewidth = 0.5)

#Variable map scale
S = 100000000
Sv = S/a

#Create contour lines
dS = arange(20 000 000, 120 000 000, 5 000 000)
contours = contour(X, Y, Sv, levels = dS, colors = 'red', linewidths = 0.6)

#Create contour labels
clabel(contours, inline = True, fontsize = 6)

show()


