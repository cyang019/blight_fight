#!/usr/bin/python
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon=-83.304482,llcrnrlat=42.220958,
              urcrnrlon=-82.879274,urcrnrlat=42.469421,
              resolution='h', epsg='4326', 
              lat_0 = 42.3314, lon_0 = -83.0458)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#99d8c9',lake_color='aqua')
#map.drawcoastlines()

#map.drawcounties()
map.readshapefile('./Detroit_City_Boundaries/zipcode', 'zipcode')
map.readshapefile('../data/Parcel_Map/parcels', 'parcels')

plt.show()
