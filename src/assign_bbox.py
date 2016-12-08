#!/usr/bin/python3
import numpy as np
import pandas as pd

def nearest_pos(q, np_listX, np_listY, length=0.000411, width= 0.000204):
    '''find the possible neighbour index of the q in a set of 2D points
    x, and y of the points are in two separate numpy arrays'''
    x, y = q
    posX = np.argwhere(np.abs(np_listX - x) < length).ravel()
    posY = np.argwhere(np.abs(np_listY - y) < width).ravel()
    poses = np.intersect1d(posX,posY)
    return poses

def raw_dist(pt1, pt2):
    '''smallest 'distance' defined as: dist = 2*abs(x-x0) + abs(y-y0)
    The ratio 2 is used here because of the rectangle size for each
    building have the dimensions of ratio roughly equal to 2
    '''
    return np.abs(pt1[0] - pt2[0]) + 2*np.abs(pt1[1] - pt2[1])


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




