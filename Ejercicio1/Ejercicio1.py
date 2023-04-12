#  recordar sumarle 360 a la longitud y multiplicar por menos -1 la coordenada z
import numpy as np
import os
from matplotlib import pyplot as plt
from fun import read_xyz
from fun import xyz_2_grid
from fun import plot_topobat
from fun import interp_malla
from fun import extract_grid
from fun_output import read_out1d
from fun_output import read_out2d
from fun_output import read_tslocation
from fun_output import plot_tslocation
from fun_output import plot_out2d

# ------------------ REVISION DE INPUTS ----------------------------------------
#  -------------- Ejercicio 1-A: revisaremos los archivos de las batimetrias
#  -- INPUT --
dir_mallas = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio2\Ejercicio2_input\falla puntual 2_outputs' # ruta donde esta el archivo, nunca te
filename = 'malla_d.xyz'  # nombre del archivo, junto con su extension
#  -- FIN INPUT --
dir_filename = os.path.join(dir_mallas, filename)  # estamos generando el path completo del archivo
vx, vy, vz = read_xyz(dir_filename) # acá las coordenadas x,y,y z son vectores columnas, no podemos plotear elevación de la topo batimetría de forma bonita.
ulon, ulat, zmalla = xyz_2_grid(vx, vy, vz)  # hacemos esto para poder plotear la malla

xlabel = 'Lon'  #  etiqueta del eje x
ylabel = 'Lat'  #  etiqueta del eje y
zlabel = 'Elevation (m)'  #  etiqueta de la barra de colores
plot_topobat(ulon, ulat, zmalla*-1, xlabel, ylabel, zlabel) # graficamos la malla topo-batimetrica, multiplicamos el z pr -1 porque recordemos que guardmaos el mar (+) y tierra (-)

#  Graficamos encima las ubicaciones de los mareografos obtenidos de la pagina del IOC sea level monitoring.
plt.plot(-78.5698+360, -9.3089, 'or')  #  Chimbote
#plt.plot(-77.23070+360, -12.09373, 'ok')  #  Callao
#plt.plot(-71.36013+360, -17.70081, 'om')  #  Ilo

# Hacemos zoom a cada sitio de interes, y revisamos si estas ubicaciones estan en tierra o en agua.


#  -------------- Ejercicio 1-B: Generamos el archivo ts_location.dat
#  -- INPUT --
POI_lon = [281.3, 282.8, 288.61]  #  Chimbote, Callo, Ilo
POI_lat = [-9.15, -12.150, -17.74] #  Chimbote, Callo, Ilo
dir_POI = r'C:\Users\joanh\PycharmProjects\Ejercicio1' # ruta donde queremos guardar el archivo ts_location.dat
#  -- FIN INPUT --

POI_lon = np.array(POI_lon, dtype=float) + 0   # Ahora sumamos 0, porque ya las longitudes las tenemos entre 0 y 360
POI_lat = np.array(POI_lat, dtype=float)
POI = np.transpose([POI_lon, POI_lat])
np.savetxt(os.path.join(dir_POI, 'ts_location.dat'), POI, delimiter=" ", fmt="%4.10f %4.10f")

# ------------------ REVISION DE OUTPUS -------------------------------------
#  -------------- Ejercicio 1-C: Revisamos el layer01 (malla topobatimetrica)
#  -- INPUT --
dir_output = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio2\Ejercicio2_input\falla puntual 2_outputs'  # ruta de la carpeta donde se corrio el modelo
layerID = '03'  # debe ir entre '' ya que debe ser string
#  -- FIN INPUT -
ux = read_out1d(os.path.join(dir_output, 'layer' + layerID + '_x.dat'))  # estamos cargando la coordenada x (longitud), es un vector
uy = read_out1d(os.path.join(dir_output, 'layer' + layerID + '_y.dat'))  # estamos cargando la coordenada y (latitud), es un vector
vzbat = read_out2d(os.path.join(dir_output, 'layer' + layerID + '.dat'))  # estamos cargando la coordenada z (elevacion terreno) pero como vector

# debemos hacer un reshape a la vzbat de vector a matriz para poder graficar y revisar.
# Debemos revisar pr ejemplo que no haya valores extraños como NaN o ceros en los bordes por una interpolacion erronea.
zbat = vzbat.reshape(len(uy), len(ux))

# Ahora graficamos el layer01
xlabel = 'Lon'  #  etiqueta del eje x
ylabel = 'Lat'  #  etiqueta del eje y
zlabel = 'Elevation (m)'  #  etiqueta de la barra de colores
plot_topobat(ux, uy, zbat*-1, xlabel, ylabel, zlabel)  # multiplicamos el z pr -1 porque tierra (-) y mar (+)
# no cerrar la figura
# cargamos las ubicaciones de los puntos de pronostico de ts_location.dat y verificamos que estén en mar haciendo zoom
plot_tslocation(dir_output)  # esta funcion plotea los FP encima de alguna figura ya existente.

#  -------------- Ejercicio 1-D: revisaremos la deformacion inicial
#  -- INPUT --
dir_output = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio2\Ejercicio2_input\falla puntual 2_outputs'  # ruta de la carpeta donde se corrio el modelo
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


#  -------------- Ejercicio 1-E: revisaremos Maximum Water Surface Elevation and Depression  (zmax/zmin)
#  -- INPUT --
dir_output = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio2\Ejercicio2_input\falla puntual 2_outputs'  # ruta de la carpeta donde se corrio el modelo
layerID = '01'  # debe ir entre '' ya que debe ser string
filename = 'zmax_layer' + layerID + '.dat'  # aca puedes escoger otro archivo y graficar
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
zlabel = 'Max. Surf. Elev. (m)'  #  etiqueta de la barra de colores
vmin = zmax.min()  # Limite inferior del colorbar
vmax = 20 #zmax.max()  # Limite superior del colorbar
plot_out2d(ux, uy, zmax, zbat, xlabel, ylabel, zlabel, vmin, vmax)

#  ax.legend() agregar leyenda a las series de tiempo
# calcular el valor maximo y minimo de la serie de tiempo.

