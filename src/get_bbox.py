#!/usr/bin/python3

import shapefile
import numpy as np
import pandas as pd

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
    df['id'] = np.arange(df.shape[0])

    return df
    

if __name__ == "__main__":
    print("function get_bbox(shapes)")
