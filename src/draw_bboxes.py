#!/usr/bin/python3

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
import shapefile
from mpl_toolkits.basemap import Basemap

from bbox import get_bbox, get_center_dim, draw_screen_bbox

sf = shapefile.Reader("./../data/Parcel_Map/parcels")

shapes = sf.shapes()

bboxes = get_bbox(shapes)

m = Basemap(llcrnrlon=-83.304482,llcrnrlat=42.220958,
            urcrnrlon=-82.879274,urcrnrlat=42.469421,
#m = Basemap(llcrnrlon=-83.0865,llcrnrlat=42.3245,
#            urcrnrlon=-83.029,urcrnrlat=42.3855,
            resolution='h', epsg='4326',
            lat_0 = 42.3314, lon_0 = -83.0458)
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='#99d8c9', lake_color='aqua')

#for box in bboxes[:2000]:
for box in bboxes:
    draw_screen_bbox(box, m)

plt.savefig('../data/buildings.pdf')


