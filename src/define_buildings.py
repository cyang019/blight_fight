#!/usr/bin/python3

import numpy as np
import pandas as pd
import shapefile
from bbox import get_bbox, bbox_list_to_df

sf = shapefile.Reader("./../data/Parcel_Map/parcels")

shapes = sf.shapes()

bboxes = get_bbox(shapes)

df_bboxes = bbox_list_to_df(bboxes)

df_bboxes.to_csv('../data/buildings.csv', header=True, index=False)

