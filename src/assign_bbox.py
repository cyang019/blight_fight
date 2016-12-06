#!/usr/bin/python3

def is_in_bbox(coord, bbox):
    '''given a coordinate, determine if it's in bbox, return a boolean

    parameters
    ---------------------
    coord: (lon,lat)
    bbox: (llcrnrlon, llcrnrlat, urcrnrlon, urcrnrlat)
    '''
    lon, lat = tuple(coord)
    llcrnrlon, llcrnrlat, urcrnrlon, urcrnrlat = tuple(bbox)

    if (lon < llcrnrlon) or (lon > urcrnrlon):
        return False
    if (lat < llcrnrlat) or (lat > urcrnrlat):
        return False
    
    return True




