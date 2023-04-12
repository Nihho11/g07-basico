import numpy as np
import os
import netCDF4 as nc
import matplotlib.colors as colors
from matplotlib import cm
import matplotlib.pyplot as plt
from scipy.interpolate import griddata


# def reshape_out2D(ux, uy, z):
    #zre = z.reshape(len(uy), len(ux))
    #return zre

def read_out2d(filename):
    #  newlist = [line.rstrip() for line in fh.readlines()]
    #  newlist = [line.split() for line in fh.readlines()]
    list = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            list.extend(line.split())
    arr = np.array(list, dtype=float)
    return arr

def read_out1d(filename):
    out = np.loadtxt(filename)
    return out

def read_tslocation(filename):
    tsloc = np.loadtxt(filename)
    poix = tsloc[:, 0]
    poiy = tsloc[:, 1]
    return poix, poiy

def read_tsrecord(filename):
    ts = np.loadtxt(filename)
    eta = ts[:, 0]
    vx = ts[:, 1]
    vy = ts[:, 2]
    return eta, vx, vy

def plot_out2d(ux, uy, zdef, zbat, xlabel, ylabel, zlabel, vmin, vmax):
    x,  y = np.meshgrid(ux, uy)
    fig, ax = plt.subplots(constrained_layout=True)
    pcm = ax.pcolormesh(x, y, zdef, rasterized=True, cmap='jet', vmin=vmin, vmax=vmax)  # , norm=divnorm, cmap=terrain_map, shading='auto')
    levels = 0  #  nos interesa solo la cota cero o linea de costa
    cm = ax.contour(x, y, zbat, levels, colors='k')
    ax.set_xlabel(xlabel)  #'Lon $[^o E]$')
    ax.set_ylabel(ylabel)  #'Lat $[^o N]$')
    #  ax.axis('equal')
    ax.set_aspect('equal', 'box')
    fig.colorbar(pcm, shrink=0.6, extend='both', label=zlabel) #'Elevation [m]')
    plt.grid(True)
    plt.show()
    #  plt.savefig("figura.pdf", format='png, dpi=300)

def plot_tslocation(path):
    FPx, FPy = read_tslocation(os.path.join(path, 'ts_location.dat'))
    # ax = plt.gca()
    style = dict(size=10, color='black')
    #ax.plot(FPx, FPy, 'ok')  # Graficams los FP
    plt.plot(FPx, FPy, 'ok')
    for i in range(0, len(FPx), 1):
        ax = plt.gca()
        ax.text(FPx[i], FPy[i], str(i+1), ha='left', **style)

def plot_tsrecord(t, ts, xlabel, ylabel, title, color):
    fig, ax = plt.subplots(constrained_layout=True)
    ax.plot(t, ts, color=color)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.title(title)
    plt.xlim([t.min(), t.max()])
    plt.grid(True)
    plt.show()

def plotsave_out2d(ux, uy, zdef, zbat, xlabel, ylabel, zlabel, vmin, vmax, title, cmap, fpath):
    x,  y = np.meshgrid(ux, uy)
    fig, ax = plt.subplots(constrained_layout=True)
    pcm = ax.pcolormesh(x, y, zdef, rasterized=True, cmap=cmap, vmin=vmin, vmax=vmax)  # , norm=divnorm, cmap=terrain_map, shading='auto')
    levels = 0  #  nos interesa solo la cota cero o linea de costa
    cm = ax.contour(x, y, zbat, levels, colors='k')
    ax.set_xlabel(xlabel)  #'Lon $[^o E]$')
    ax.set_ylabel(ylabel)  #'Lat $[^o N]$')
    #  ax.axis('equal')
    ax.set_aspect('equal', 'box')
    fig.colorbar(pcm, shrink=0.6, extend='both', label=zlabel) #'Elevation [m]')
    plt.title(title)
    plt.grid(True)
    plt.show()
    plt.savefig(fpath, format='png')  #, dpi=300)