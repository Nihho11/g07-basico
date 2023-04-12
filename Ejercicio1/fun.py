import numpy as np
import netCDF4 as nc
import matplotlib.colors as colors
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def read_xyz(filename):
    x, y, z = [], [], []
    with open(filename, 'r') as f:
        for line in f.readlines():
            xval, yval, zval = map(float, line.split())
            x.append(xval)
            y.append(yval)
            z.append(zval)
    return np.asarray(x), np.asarray(y), np.asarray(z)

def ncgebco_read(fpath):
    # path_nc = os.path.join(path_input, name_nc)  #
    #file = r'C:\Users\noteh\PycharmProjects\sipat_NRT\send_to_modelate\mallas\gebco.nc'
    f = nc.Dataset(fpath)
    VARS = f.variables.keys()

    if len(VARS) == 3:
        x = np.array(f.variables['lon'][:], dtype=float)  # cargando la variable
        y = np.array(f.variables['lat'][:], dtype=float)  # cargando la variable
        z = np.array(f.variables['elevation'][:], dtype=float)  # cargando la variable originalmente viene en formato integer, lo convertimos a formato float

    return x, y, z

def read_asc(fpath):

    # Load .asc (ascii file)
    z = np.loadtxt(fpath, skiprows=6)

    # Load header
    with open(fpath, 'r') as fp:
        ncols = int(fp.readline().split()[1])
        nrows = int(fp.readline().split()[1])
        xmin = float(fp.readline().split()[1])
        ymin = float(fp.readline().split()[1])
        cellsize = float(fp.readline().split()[1])
        nodata = float(fp.readline().split()[1])

    xmax = xmin + cellsize * (ncols - 1)
    ymax = ymin + cellsize * (nrows - 1)

    extent = [xmin, xmax, ymin, ymax]
    x = np.arange(xmin,xmax+0.5*cellsize,cellsize)
    y = np.flip(np.arange(ymin,ymax+0.5*cellsize,cellsize))

    return x, y, z, extent

def plot_topobat(x,y,z,xlabel,ylabel,zlabel):
    # modificado de esta página
    # https://matplotlib.org/3.2.2/gallery/userdemo/colormap_normalizations_diverging.html

    # make a colormap that has land and ocean clearly delineated and of the
    # same length (256 + 256)
    colors_undersea = plt.cm.terrain(np.linspace(0, 0.17, 256))
    colors_land = plt.cm.terrain(np.linspace(0.25, 1, 256))
    all_colors = np.vstack((colors_undersea, colors_land))
    terrain_map = colors.LinearSegmentedColormap.from_list('terrain_map', all_colors)

    # make the norm:  Note the center is offset so that the land has more
    # dynamic range:
    divnorm = colors.TwoSlopeNorm(vmin=z.min(), vcenter=0, vmax=z.max())
    fig, ax = plt.subplots(constrained_layout=True)
    pcm = ax.pcolormesh(x, y, z, rasterized=True, norm=divnorm, cmap=terrain_map, shading='auto')
    ax.set_xlabel(xlabel) #'Lon $[^o E]$')
    ax.set_ylabel(ylabel) #'Lat $[^o N]$')
    #ax.axis('equal')
    ax.set_aspect('equal', 'box')
    fig.colorbar(pcm, shrink=0.6, extend='both', label=zlabel) #'Elevation [m]')
    plt.grid(True)
    plt.show()
    #  plt.savefig("figura.pdf", dpi=300)

def interp_malla(x, y, z, xq, yq):
    # Inputs
    #  x: vector con las coordenadas x, dimension (nx,)
    #  y: vector con las coordenadas x, dimension (ny,)
    #  z: matriz con la elevacion z, demsion (ny,nx)
    #  xq: vector con las nuevas coordenadas x, dimension (nx2,)
    #  yq: vector con las nuevas coordenadas y, dimension (ny2,)
    # Output:
    #  zq: matriz con la elevacion z interpolada, demsion (ny2,nx2)
    xx, yy = np.meshgrid(x, y)
    vx = xx.flatten()
    vy = yy.flatten()
    values = np.array(z.flatten(), dtype=float)
    xxq, yyq = np.meshgrid(xq, yq)
    zq = griddata((vx, vy), values, (xxq, yyq), method='linear', fill_value=0)

    return zq

def xyz_2_grid(vx, vy, vz):
    # no importa el orden en que esten xyz.
    # lo importante es que para hysea x e y tienen que estar ordenados de menor a mayor.
    #  xmalla e ymalla siempre estaran en el orden de menor a mayor)

    ux = np.unique(vx)
    uy = np.unique(vy)
    ncols = len(ux)
    nrows = len(uy)
    if vx[0] == vx[1]:
        xx = np.transpose(np.reshape(vx, (-1, nrows)))
        yy = np.transpose(np.reshape(vy, (-1, nrows)))
        z = np.transpose(np.reshape(vz, (-1, nrows)))

    elif vy[0] == vy[1]:
        xx = np.reshape(vx, (-1, ncols))
        yy = np.reshape(vy, (-1, ncols))
        z = np.reshape(vz, (-1, ncols))

    x = xx[0, :]
    y = yy[:, 0]

    return x, y, z


def interp_xyz_2_grid(xyz, xgrid, ygrid):
    # no importa el orden en que esten xyz.
    # lo importante es que para hysea x e y tienen que estar ordenados de menor a mayor.
    #  xmalla e ymalla siempre estaran en el orden de menor a mayor)

    lon = xyz[:, 0]
    lat = xyz[:, 1]
    values = xyz[:, 2]
    # las mallas siempre estan con la longitud de 0 a 360,
     # dado que no estan grillados, haremos una interpolacion 2D para poder llenar con ceros y
    # tener una matriz rectangular
    xx, yy = np.meshgrid(xgrid, ygrid)
    z = griddata((lon, lat), values, (xx, yy), method='linear', fill_value=0)
    x = xx[0, :]
    y = yy[:, 0]
    return x, y, z

def extract_grid(x, y, z, xlim, ylim):
    # Inputs
    #  x: vector con las coordenadas x, dimension (nx,)
    #  y: vector con las coordenadas x, dimension (ny,)
    #  z: matriz con la elevacion z, demsion (ny,nx)
    #  xlim: lista con limites de longitud
    #  ylim: lista con limites de latitud
    # Output:
    #  xq: vector con las nuevas coordenadas x, dimension (nx2,)
    #  yq: vector con las nuevas coordenadas y, dimension (ny2,)
    #  zq: matriz con la elevacion z recortad, dimesion (ny2,nx2)

    XLIM = np.array(xlim)
    YLIM = np.array(ylim)

    cols = np.where((x >= XLIM.min()) & (x <= XLIM.max()))
    rows = np.where((y >= YLIM.min()) & (y <= YLIM.max()))
    xq = x[np.ix_(cols[0])]
    yq = y[np.ix_(rows[0])]
    zq = z[np.ix_(rows[0], cols[0])]

    return xq, yq, zq
