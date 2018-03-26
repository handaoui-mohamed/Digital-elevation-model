import matplotlib.path as mplPath
import numpy as np

BOUNDS_FILE = 'bounds.txt'
XYZ_PATCH1 = 'N35W002.xyz'
XYZ_PATCH2 = 'N35W001.xyz'
OUTPUT_FILE = 'output.csv'


def readBounds(file_name):
    bounds = []
    with open(file_name, 'r') as f:
        for line in f:
            coordinates = line.strip().split(' ')
            bounds.append([float(coordinates[0]), float(coordinates[1])])

    return mplPath.Path(np.array(bounds))


def readXYZ(polygon, file_name, mode):
    index = 0
    with open(file_name, 'r') as input:
        with open(OUTPUT_FILE, mode) as output:
            for line in input:
                coordinates = line.strip().split(' ')
                coordinates = (float(coordinates[0]), float(coordinates[1]))
                index = index + 1
                print(index)
                if(polygon.contains_point(coordinates)):
                    print(','.join(map(str, line.strip().split(' '))),
                          file=output, end='\n')


def extractLinesEvery(lineNumber):
    index = 0
    with open(OUTPUT_FILE, 'r') as input:
        points = []
        with open(str(lineNumber)+'%_'+OUTPUT_FILE, 'w') as output:
            for line in input:
                index = index + 1
                print(index)
                if(index % lineNumber == 0):
                    print(line, file=output, end='')


if __name__ == '__main__':
    # polygon = readBounds(BOUNDS_FILE)
    # readXYZ(polygon, file_name=XYZ_PATCH1, mode='w')
    # readXYZ(polygon, file_name=XYZ_PATCH2, mode='a')
    extractLinesEvery(10)
