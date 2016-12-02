import sys

def read_txt(filename, header=False):
    '''import txt file as list of line (each line is a list
    of components separated by white spaces)

    parameters
    ---------------------
    filename: a str
    header: a boolean (default False)

    return a tuple (names, data rows)
    
    '''

    result = []
    names = []
    with open(filename, encoding='utf-8', mode='r') as f:
        if header:
            names = f.readline()
        while line:
            line = f.readline()
            data = line.strip().split()
            result.append(data)
    return (names,result)

    
