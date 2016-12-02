#!/usr/bin/python3

import shapefile

def get_bbox(shapes):
    '''get a list of 'bbox' attributes from shapes got from
    a shapefile.Reader('path/to/shapes')'''

    bboxes = []
    for s in shapes:
        boundaries = s.bbox
        bboxes.append(boundaries)
    
    return bboxes

if __name__ == "__main__":
    print("function get_bbox(shapes)")
