"""Convert HGT data to XYZ points."""
import re
import numpy as np
from os.path import basename
from time import time
from progress import printDate, printProgressBar, printTiming

SAMPLES = 1201
FILES = ['patches/N35W002.hgt', 'patches/N35W001.hgt']

TOTAL_LINES = (SAMPLES * SAMPLES) * len(FILES)


def hgtToXyz(hgt_file):
    """
    this is not a generique function, it only woks with NxxWxxx.hgt files
    """
    TOTAL_LINES = SAMPLES * SAMPLES
    baseLat, baseLon = map(int, re.findall('\d+', basename(hgt_file)))
    hgt_data = open(hgt_file, 'rb')
    xyz_file = open(hgt_file + '.xyz', 'w')
    # Each data is 16bit signed integer(i2) - big endian(>)
    elevations = np.fromfile(
        hgt_data,  # binary data
        np.dtype('>i2'),  # data type
        TOTAL_LINES  # length
    ).reshape((SAMPLES, SAMPLES))

    sample = SAMPLES - 1
    currentIndex = 0
    for row_index, row in enumerate(elevations):
        lat = str(baseLat + (sample - row_index) / sample)
        for index, elevation in enumerate(row):
            currentIndex += 1
            printProgressBar(currentIndex, TOTAL_LINES)
            lon = str(-baseLon + ((index + sample) - sample) / sample)
            print(lon+' '+lat+' ' + str(elevation), file=xyz_file, end='\n')

    hgt_data.close()
    xyz_file.close()


if __name__ == '__main__':
    start = time()
    printDate('Extraction START TIME: ')
    for patch in FILES:
        print('\nExtraction of file = '+basename(patch), end='\n')
        hgtToXyz(patch)
    printDate('\nExtraction END TIME: ')
    printTiming(start)
