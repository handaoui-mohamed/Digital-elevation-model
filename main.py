import matplotlib.path as mplPath
import numpy as np

BOUNDS_FILE = 'bounds.xy'
XYZ_FILE = 'N35W002.xyz'
OUTPUT_FILE = 'output.xyz'


def readBounds(file_name):
    bounds = []
    with open(file_name, 'r') as f:
        for line in f:
            coordinates = line.strip().split(' ')
            bounds.append([float(coordinates[0]), float(coordinates[1])])

    return mplPath.Path(np.array(bounds))


def readXYZ(polygon):
    index = 0
    with open(XYZ_FILE, 'r') as input:
        points = []
        with open(OUTPUT_FILE, 'w') as output:
            for line in input:
                coordinates = line.strip().split(' ')
                coordinates = (float(coordinates[0]), float(coordinates[1]))
                index = index + 1
                print(index)
                if(polygon.contains_point(coordinates)):
                    print(line, file=output, end='')


if __name__ == '__main__':
    polygon = readBounds(BOUNDS_FILE)
    readXYZ(polygon)
