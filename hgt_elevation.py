import numpy as np

SAMPLES = 1201
FILES = ['coordinates/N35W002.xyz', 'coordinates/N35W001.xyz']


def read_elevation_from_file(hgt_file, lon, lat):
    with open(hgt_file, 'rb') as hgt_data:
        # Each data is 16bit signed integer(i2) - big endian(>)
        elevations = np.fromfile(
            hgt_data,  # binary data
            np.dtype('>i2'),  # data type
            SAMPLES * SAMPLES  # length
        ).reshape((SAMPLES, SAMPLES))

        lat_row = int(round((lat - int(lat)) * (SAMPLES - 1), 0))
        lon_row = int(round((lon - int(lon)) * (SAMPLES - 1), 0))

        return elevations[SAMPLES - 1 - lat_row, lon_row].astype(int)


# example
print(read_elevation_from_file(FILES[0], -1.58, 35.64))
