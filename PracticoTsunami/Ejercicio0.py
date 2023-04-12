import numpy as np
import os
from matplotlib import pyplot as plt
from fun import read_xyz
from fun import ncgebco_read
from fun import plot_topobat
from fun import interp_malla
from fun import xyz_2_grid
from fun import extract_grid

#  -------------- Ejercicio 0-A: revisaremos los archivos de las batimetrias originales
#  -- INPUT --
dir_batoriginales = r'C:\Users\joanh\PycharmProjects\PracticoTsunami' # ruta donde esta el archivo, nunca terminar con /
filename = 'chimbote.xyz'  # nombre del archivo, junto con su extension
#  -- FIN INPUT --
dir_filename = os.path.join(dir_batoriginales, filename)  # estamos generando el path completo del archivo
vx, vy, vz = read_xyz(dir_filename)
vz=vz*-1
vxok = vx - 360
#  graficamos con scatter. Los colores indican la elevacion
plt.figure()
#plt.plot(vx, vy)
plt.scatter(vxok, vy, c=vz)
plt.xlabel('Lon (Deg.)')
plt.ylabel('Lat (Deg.)')
plt.title('Datos originales')
plt.grid(True)
plt.colorbar()
plt.show()

#  -------------- Ejercicio 0B: Restamos 360 a la longitud, para poder graficar con software GIS y otro
#  -- INPUT --
nombre_salida = 'Ilo_corr.xyz'
#  -- FIN INPUT --
vxok = vx - 360  # restamos 360 para obtener longitudes entre -180 y 180 para revisr con QGIS
bat = np.transpose([vxok, vy, vz])  # Pasamos de vectores filas a vectores columnas
np.savetxt(os.path.join(dir_batoriginales, nombre_salida), bat, delimiter=" ", fmt="%4.10f %4.10f %4.3f")  # guardamos en formato ascii

#  -------------- Ejercicio 0-C: Graficaremos la topobatimetria Gebco descargada en formato .nc
#  -- INPUT --
file_gebco = r'C:\Users\joanh\PycharmProjects\PracticoTsunami\prueba.nc'
# -- FIN INPUT --
lon, lat, z = ncgebco_read(file_gebco)  # leyenfo el archivo .nc descargado de la pagina de gebco.net

xlabel = 'Lon'  #  etiqueta del eje x
ylabel = 'Lat'  #  etiqueta del eje y
zlabel = 'Elevation (m)'  #  etiqueta de la barra de colores
plot_topobat(lon, lat, z, xlabel, ylabel, zlabel) # graficamos la malla topo-batimetrica
#  podemos graficar encima la ubicacion aproximada de un lugar de interes
plt.plot(-78.5698, -9.3089, 'or')  #  Chimbote
plt.plot(-77.13070, -12.09373, 'or')  #  Callao
plt.plot(-71.36013, -17.70081, 'or')  #  Ilo
style = dict(size=9, color='red')
ax = plt.gca()
ax.text(-78.5698, -9.3089, "Chimbote", ha='left', **style)
ax.text(-77.13070, -12.09373, "Callao", ha='left', **style)
ax.text(-71.36013, -17.70081, "Ilo", ha='left', **style)


#  -------------- Ejercicio 0-D: Interpolamos la malla GEBCO a una resolucion deseada
#  En este caso GEBCO 2022 tiene un espaciamiento de 15 segundos de arco, y generaremos una mas gruesa y obtener una malla mas liviana
#  -- INPUT --
res_arcsec = 30  # en segundos de arco. 1 miuto de arco = 60 segundos de arco. 1 segundo de arco es aprox. 30 metros.
dir_mallas = r'C:\Users\joanh\PycharmProjects\PracticoTsunami'
nombre_malla = 'callao.xyz'
#  -- FIN INPUT --

res_grados = res_arcsec / 3600   # la unidad es grados de longitud
lonq = np.arange(lon.min(), lon.max(), res_grados)  #  generamos nuevo vector longitud
latq = np.arange(lat.min(), lat.max(), res_grados)  #  generamos nuevo vector latitud
zq = interp_malla(lon, lat, z, lonq, latq)  #  interpolamos z para nuevos vectores longitud y latitud
xx, yy = np.meshgrid(lonq, latq)  # generamos matriz longitud latitud
#  le sumaremos 360 a la longitud porque para ingresar a gebco los valores van de 0 a 360.
#  multiplicaremos z *-1 porque para ingresar a gebco el mar (+) y tierra (-)
bat_xyz = np.transpose([xx.flatten()+360, yy.flatten(), zq.flatten()*-1])
np.savetxt(os.path.join(dir_mallas, nombre_malla), bat_xyz, delimiter=" ", fmt="%4.10f %4.10f %4.3f")

#  -------------- Ejercicio 0-E: Visualizamos la malla en formato .xyz para revisar si quedo correcta.
#  -- INPUT --
dir_mallas = r'C:\Users\joanh\PycharmProjects\PracticoTsunami'
nombre_malla = 'callao.xyz'
#  -- FIN INPUT --
dir_filename2 = os.path.join(dir_mallas, nombre_malla)  # estamos generando el path completo del archivo
vx, vy, vz = read_xyz(dir_filename2)
ulon, ulat, zbat = xyz_2_grid(vx, vy, vz)  # hacemos esto para poder plotear la malla

xlabel = 'Lon'  #  etiqueta del eje x
ylabel = 'Lat'  #  etiqueta del eje y
zlabel = 'Elevation (m)'  #  etiqueta de la barra de colores
plot_topobat(ulon, ulat, zbat*-1, xlabel, ylabel, zlabel)  # multiplicamos z*-1 porque Comcot mar(+) tierra(-)

#  -------------- Ejercicio 0-F: Extraeremos solamente un area de una malla topo-batimetrica (En este caso recortaremos gebco)
#  Escogemos un sector cerca de Chimbote
#  -- INPUT --
xlim = [-79, -78.1]  # anotamos los limites en el eje x (longitud)
ylim = [-8.6, -9.9]  # anotamos los limites en el eje y (latitud)
file_gebco = r'C:\Users\joanh\PycharmProjects\PracticoTsunami\gebco_2022_n-7.5_s-10.5_w-80.0_e-77.5.nc'
dir_mallas = r'C:\Users\joanh\PycharmProjects\PracticoTsunami' # ruta donde quiero guardar el archivo .xyz
nombre_malla2 = 'chimbote.xyz'
# -- FIN INPUT --
xlabel = 'Lon'  #  etiqueta del eje x
ylabel = 'Lat'  #  etiqueta del eje y
zlabel = 'Elevation (m)'  #  etiqueta de la barra de colores
lon, lat, z = ncgebco_read(file_gebco)  # leyendo el archivo .nc descargado de la pagina de gebco.net
plot_topobat(lon, lat, z, xlabel, ylabel, zlabel)

lon_rec, lat_rec, zrec = extract_grid(lon, lat, z, xlim, ylim)
plot_topobat(lon_rec, lat_rec, zrec, xlabel, ylabel, zlabel)
xx2, yy2 = np.meshgrid(lon_rec, lat_rec)  # generamos matriz longitud latitud
bat_xyz2 = np.transpose([xx2.flatten()+360, yy2.flatten(), zrec.flatten()*-1])
np.savetxt(os.path.join(dir_mallas, nombre_malla2), bat_xyz2, delimiter=" ", fmt="%4.10f %4.10f %4.3f")

#  -------------- Ejercicio 0-G: Generamos el archivo ts_location.dat
#  -- INPUT --
POI_lon = [-78.6125, -78.606449, -78.586714, -78.623985]
POI_lat = [-9.0761, -9.083945,  -9.087867, -9.127094]
dir_POI = r'C:\Users\noteh\Dropbox\2022-PeruTsutraining\Ejercicio0' # ruta donde queremos guardar el archivo ts_location.dat
#  -- FIN INPUT --

POI_lon = np.array(POI_lon, dtype=float) + 360  # sumamos 360, porque estamos dejando todas las longitudes entre 0 y 360
POI_lat = np.array(POI_lat, dtype=float)
POI = np.transpose([POI_lon, POI_lat])
np.savetxt(os.path.join(dir_POI, 'ts_location.dat'), POI, delimiter=" ", fmt="%4.10f %4.10f")
