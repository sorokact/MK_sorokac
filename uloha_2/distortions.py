import pyproj
import math

crs_geo = pyproj.CRS.from_epsg(4326)

# gnómonická projekce s pólem v (90°, 0°)
crs_gnom = pyproj.CRS.from_proj4('+proj=gnom +lat_0=90 +lon_0=0 +datum=WGS84')

p = pyproj.Proj(crs_gnom)

gnom_f = p.get_factors(72, 58.282526, False, True)

print(f"Měřítko v poledníku: {gnom_f.meridional_scale}")
print(f"Měřítko v rovnoběžce: {gnom_f.parallel_scale}")
print(f"Tissotova indikatrix - poloosa a: {gnom_f.tissot_semimajor}")
print(f"Tissotova indikatrix - poloosa b: {gnom_f.tissot_semiminor}")
print(f"Úhel mezi poledníkem a rovnoběžkou: {gnom_f.meridian_parallel_angle}°")
print(f"Úhlové zkreslení: {gnom_f.angular_distortion}°")
print(f"Plošné měřítko: {gnom_f.areal_scale}")
print(f"Meridiánová konvergence: {gnom_f.meridian_convergence}°")