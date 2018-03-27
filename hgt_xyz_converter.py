"""Convert HGT data to XYZ points."""

import sys
from functools import partial


INPUT_FILE = 'N35W002.hgt'
OUTPUT_FILE = 'N35W002_.xyz'


def main(inputname, outputname):
    """Entry point of the program."""
    alts = []
    with open(inputname, 'rb') as f:
        for p, chunk in enumerate(iter(partial(f.read, 2), '')):
            if len(chunk) == 0:
                break
            alt = chunk[0]
            alt <<= 8
            alt |= chunk[1]
            x, y = divmod(p, 3601)
            x *= 30
            y *= 30
            alts.append((x, y, alt))
    with open(outputname, 'w') as f:
        for entry in alts:
            print("{} {} {}".format(*entry), file=f)


if __name__ == '__main__':
    main(INPUT_FILE, OUTPUT_FILE)
