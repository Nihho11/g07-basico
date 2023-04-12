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
from fun_output import read_tsrecord
from fun_output import plot_out2d
from fun_output import plot_tsrecord
from fun_output import plotsave_out2d
#

# ------------------ REVISION DE OUTPUS ----------------------------------------
#  -------------- Ejercicio 2-A: Graficaremos las series de tiempo (ts_record.dat)
#  -- INPUT --
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



# ------------------ REVISION DE OUTPUS ----------------------------------------
#  -------------- Ejercicio 2-B: Graficaremos z o h en el tiempo y se guardará la figura
#  -- INPUT --
dir_output = r'C:\Users\joanh\OneDrive\Escritorio\Modelamiento de Tsunamis\Ejercicio 6\Ejercicio6_input' # ruta donde esta el archivo, nunca te
layerID = '01'  # debe ir entre '' ya que debe ser string
varname = 'z'  # puede ser z, h, m o n
zlabel = 'Surf. Elev. (m)'  # etiqueta de la barra de colores, dependera de var name
tstart = 0  # time step inicio
tstop = 10400  # time step fin
tstep = 600  # time step
cmap = 'jet'  # colormap
xlabel = 'Lon'  # etiqueta del eje x
ylabel = 'Lat'  # etiqueta del eje y
#  -- FIN INPUT --
ux = read_out1d(os.path.join(dir_output, 'layer' + layerID + '_x.dat'))  # estamos cargando la coordenada x (longitud), es un vector
uy = read_out1d(os.path.join(dir_output, 'layer' + layerID + '_y.dat'))  # estamos cargando la coordenada y (latitud), es un vector
vzbat = read_out2d(os.path.join(dir_output,'layer' + layerID + '.dat'))  # estamos cargando la coordenada z (elevacion terreno) pero como vector
vzmax = read_out2d(os.path.join(dir_output,'zmax_layer' + layerID + '.dat'))
vzmin = read_out2d(os.path.join(dir_output,'zmin_layer' + layerID + '.dat'))
zbat = vzbat.reshape(len(uy), len(ux))
time = read_out1d(os.path.join(dir_output, 'time.dat')) # cargamos el vector tiempo
deltat = time[1]-time[0]  # en segundos, ya que es la unidad de comcot
timestep = range(tstart, tstop, tstep)
vmin = 0 #vzmin.min()  # para el limite inferior del colorbar
vmax = 0.5 #vzmax.max()  # para el limite superior del colorbar
for istep in timestep:
    time_seg = int(istep*deltat)
    dummy = f'{time_seg:06d}'
    filenamei = varname + '_' + layerID + '_' + dummy
    vz = read_out2d(os.path.join(dir_output, filenamei + '.dat'))  # estamos cargando la coordenada z (deformacion vertical superficie libre del mar) pero como vector
    z = vz.reshape(len(uy), len(ux))
    title = 'Layer ' + layerID + ', t=' + str(time_seg) + 'seg'
    fpath = os.path.join(dir_output, filenamei + '.png')
    plotsave_out2d(ux, uy, z, zbat, xlabel, ylabel, zlabel, vmin, vmax, title, cmap, fpath)
