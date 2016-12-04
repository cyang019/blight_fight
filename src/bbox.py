#!/usr/bin/python3

import shapefile
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

def get_bbox(shapes):
    '''return a list of 'bbox' attributes from shapes got from
    a shapefile.Reader('path/to/shapes')'''

    bboxes = []
    for s in shapes:
        boundaries = s.bbox
        bboxes.append(boundaries)
    
    return bboxes

def bbox_list_to_df(bboxes):
    ''' convert a list of (llcrnrlon,llcrnrlat,urcrnrlon,urcrnrlat)'s
    into a dataframe with each bbox associated with an ID'''

    np_bboxes = np.array(bboxes)
    columns = ['llcrnrlon','llcrnrlat','urcrnrlon','urcrnrlat']
    df = pd.DataFrame(bboxes,columns=columns,copy=True)
    df['building_id'] = np.arange(df.shape[0])
    df = df[['building_id', 'llcrnrlon', 'llcrnrlat', 'urcrnrlon', 'urcrnrlat']]

    return df
    
def get_center_dim(bbox_tuple):
    '''given a bbox represented as (llcrnrlon, llcrnrlat, urcrnrlon,
    urcrnrlat), return a rectangle as ((centerX,centerY),length,height)
    '''
    llcrnrlon, llcrnrlat, urcrnrlon, urcrnrlat = tuple(bbox_tuple)
    centerX = (urcrnrlon + llcrnrlon)/2.0
    centerY = (urcrnrlat + llcrnrlat)/2.0
    length = urcrnrlon - llcrnrlon
    height = urcrnrlat - llcrnrlat

    return ((centerX, centerY), length, height)

def draw_screen_bbox(bbox_tuple, m):
    '''draw a rectangle bbox on a Basemap instance m'''
    recParam = get_center_dim(bbox_tuple)
    rec = Rectangle(*recParam, alpha=0.3, facecolor='red')
    plt.gca().add_patch(rec)


if __name__ == "__main__":
    print("functions related to bbox attribute of a shapefile")
