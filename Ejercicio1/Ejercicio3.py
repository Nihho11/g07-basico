#  recordar sumarle 360 a la longitud y multiplicar por menos -1 la coordenada z
import numpy as np
import os
from matplotlib import pyplot as plt
from fun import read_xyz
from fun import plot_topobat
from fun import xyz_2_grid
from fun_output import read_out1d
from fun_output import read_out2d
from fun_output import read_tslocation
from fun_output import plot_tslocation
from fun_output import plot_out2d
from fun_output import read_tsrecord
from fun_output import plot_tsrecord
# ------------------ REVISION DE INPUTS ----------------------------------------
#  -------------- Ejercicio 3-A: revisaremos los archivos de las batimetrias
#  -- INPUT --
dir_mallas = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio 6\Ejercicio6_input' # ruta donde esta el archivo, nunca te
filename = 'callao.xyz'  # nombre del archivo, junto con su extension
#  -- FIN INPUT --
dir_filename = os.path.join(dir_mallas, filename)  # estamos generando el path completo del archivo
vx, vy, vz = read_xyz(dir_filename) # acá las coordenadas x,y,y z son vectores columnas, no podemos plotear elevación de la topo batimetría de forma bonita.
ulon, ulat, zmalla = xyz_2_grid(vx, vy, vz)  # hacemos esto para poder plotear la malla

xlabel = 'Lon'  #  etiqueta del eje x
ylabel = 'Lat'  #  etiqueta del eje y
zlabel = 'Elevation (m)'  #  etiqueta de la barra de colores
plot_topobat(ulon, ulat, zmalla*-1, xlabel, ylabel, zlabel) # graficamos la malla topo-batimetrica, multiplicamos el z pr -1 porque recordemos que guardmaos el mar (+) y tierra (-)

plt.plot(281.4312, -9.1162, 'or')  #  Chimbote
#plt.plot(282.8200, -12.09373, 'ok')  #  Callao
#plt.plot(284.842, -15.3467, 'om')  #  Marcona


#  -------------- Ejercicio 3-B: Generamos el archivo ts_location.dat
#  -- INPUT --
POI_lon = [281.4312, 282.8200, 284.842]
POI_lat = [-9.1162, -12.09373, -15.3467]
dir_savePOI = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio 6\Ejercicio6_input' # ruta donde queremos guardar el archivo ts_location.dat
#  -- FIN INPUT --

POI_lon = np.array(POI_lon, dtype=float) + 0   # Ahora sumamos 0, porque ya las longitudes las tenemos entre 0 y 360
POI_lat = np.array(POI_lat, dtype=float)
plt.plot(POI_lon, POI_lat, 'or')
plt.show()
POI = np.transpose([POI_lon, POI_lat])
np.savetxt(os.path.join(dir_savePOI, 'ts_location.dat'), POI, delimiter=" ", fmt="%4.10f %4.10f")


# ------------------ REVISION DE OUTPUS ----------------------------------------
#  -------------- Ejercicio 3-C: revisaremos la deformacion inicial
#  -- INPUT --
dir_output = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio 6\Ejercicio6_input'  # ruta de la carpeta donde se corrio el modelo
layerID = '01'  # debe ir entre '' ya que debe ser string
filename = 'ini_surface.dat'  # aca puedes escoger otro archivo y graficar
#  -- FIN INPUT -

ux = read_out1d(os.path.join(dir_output, 'layer' + layerID + '_x.dat'))  # estamos cargando la coordenada x (longitud), es un vector
uy = read_out1d(os.path.join(dir_output, 'layer' + layerID + '_y.dat'))  # estamos cargando la coordenada y (latitud), es un vector
vzbat = read_out2d(os.path.join(dir_output, 'layer' + layerID + '.dat'))  # estamos cargando la coordenada z (elevacion terreno) pero como vector
vzdef = read_out2d(os.path.join(dir_output, filename))  # estamos cargando la coordenada z (deformacion vertical superficie libre del mar) pero como vector

# debemos hacer un reshape a la vzbat de vector a matriz para poder graficar y revisar.
# Debemos revisar pr ejemplo que no haya valores extraños como NaN o ceros en los bordes por una interpolacion erronea.
zbat = vzbat.reshape(len(uy), len(ux))
zdef = vzdef.reshape(len(uy), len(ux))
xlabel = 'Lon'  #  etiqueta del eje x
ylabel = 'Lat'  #  etiqueta del eje y
zlabel = 'Initial Vert. Displ. (m)'  #  etiqueta de la barra de colores
vmin = zdef.min()  # Limite inferior del colorbar
vmax = zdef.max()  # Limite superior del colorbar
plot_out2d(ux, uy, zdef, zbat, xlabel, ylabel, zlabel, vmin, vmax)


#  -------------- Ejercicio 3-D: Graficaremos las series de tiempo (ts_record.dat)
#  -- INPUT --S
dir_output = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio 6\Ejercicio6_input' # ruta donde esta el archivo, nunca te
FP = [1, 2, 3]  # el ID de las ts_recordxxxx.dat que queremos graficar
#  -- FIN INPUT --
time = read_out1d(os.path.join(dir_output, 'time.dat')) # cargamos el vector tiempo

for i in FP:  # vamos a iterar para generar una figura para cada ts_recordxxx.dat deseado
    dummy = f'{i:04d}'
    dir_filename = os.path.join(dir_output, 'ts_record' + dummy + '.dat') # estamos generando el path completo del archivo
    eta, vx, vy = read_tsrecord(dir_filename)
    xlabel = 'Tiempo (min)'
    ylabel = 'eta (m)'
    title = 'FP ' + str(i)  # El nombre del gráfico es FP + ID del ts_record
    color = 'blue'
    plot_tsrecord(time/60, eta, xlabel, ylabel, title, color)

#  -------------- Ejercicio 3-E: revisaremos Maximum Water Surface Elevation and Depression  (zmax/zmin)
#  -- INPUT --
dir_output = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio 6\Ejercicio6_input'  # ruta de la carpeta donde se corrio el modelo
layerID = '01'  # debe ir entre '' ya que debe ser string
filename = 'zmax_layer' + layerID + '.dat'  # aca puedes escoger otro archivo y graficar
zlabel = 'Max. Surf. Elev. (m)'  #  etiqueta de la barra de colores
#  -- FIN INPUT -

ux = read_out1d(os.path.join(dir_output, 'layer' + layerID + '_x.dat'))  # estamos cargando la coordenada x (longitud), es un vector
uy = read_out1d(os.path.join(dir_output, 'layer' + layerID + '_y.dat'))  # estamos cargando la coordenada y (latitud), es un vector
vzbat = read_out2d(os.path.join(dir_output, 'layer' + layerID + '.dat'))  # estamos cargando la coordenada z (elevacion terreno) pero como vector
vzmax = read_out2d(os.path.join(dir_output, filename))  # estamos cargando la coordenada z (deformacion vertical superficie libre del mar) pero como vector

# debemos hacer un reshape a la vzbat de vector a matriz para poder graficar y revisar.
# Debemos revisar pr ejemplo que no haya valores extraños como NaN o ceros en los bordes por una interpolacion erronea.
zbat = vzbat.reshape(len(uy), len(ux))
zmax = vzmax.reshape(len(uy), len(ux))
xlabel = 'Lon'  #  etiqueta del eje x
ylabel = 'Lat'  #  etiqueta del eje y
vmin = zmax.min()  # Limite inferior del colorbar
vmax = zmax.max()  # Limite superior del colorbar
plot_out2d(ux, uy, zmax, zbat, xlabel, ylabel, zlabel, vmin, vmax)
