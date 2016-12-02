#!/usr/bin/python3

import shapefile

def invalid_index(shapes):
    '''give invalid entry number based on the number of fields
    presented in a shape. (should contain 'bbox', 'parts', 'points',
    and 'shapeType)
    
    parameters
    ---------------------
    shapes: <shapefilereader.shapes()>
    
    return a list of invalid numbers.
    '''

    positions = []
    pos = 0
    for s in shapes:
        n = 0
        for name in dir(s):
            if not name.startswith("__"):
                n = n + 1
        if n != 4:
            positions.append(pos)
        pos = pos + 1
    return positions

if __name__ == "__main__":
    print ("function invalid_index(shapes)")
                
